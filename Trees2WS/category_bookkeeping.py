#!/usr/bin/env python3
"""Read Trees2WS inputs/workspaces and write category bookkeeping as Markdown.

Example:
  python3 -B category_bookkeeping.py --category ttH_had_1 --inputDir inputs_27June
  python3 -B category_bookkeeping.py --allCategories --inputDir inputs_27June

Requires PyROOT in the CMSSW environment. Each ROOT file is read in a fresh
process. Input files are opened READ-only; only the requested report is written.
"""
import argparse
import json
import math
from pathlib import Path
import re
import subprocess
import sys

# Same normalization convention and values as Trees2WS/calc_yields.py.
# These factors assume input `weight` needs multiplication by lumi * XS * BR.
LUMI = {'2022preEE': 7.98, '2022postEE': 26.68,
        '2023preBPix': 17.96, '2023postBPix': 9.68}
XS_BR = {'GluGluH': 52.23e3 * 0.00227, 'VBFH': 4.078e3 * 0.00227,
         'VH': 2.4009e3 * 0.00227, 'ttH': 570.0 * 0.00227,
         'tHqLep': 83.26 * 0.3258 * 0.00227,
         'tHqHad': 83.26 * (1 - 0.3258) * 0.00227,
         'tHW': 17.2 * 0.00227, 'bbH': 526.9 * 0.00227}
PREFIX = {'GluGluH': 'ggh', 'VBFH': 'vbf', 'VH': 'vh', 'ttH': 'tth',
          'tHqLep': 'tHqLep', 'tHqHad': 'tHqHad', 'tHW': 'tHW', 'bbH': 'bbh'}
VERSIONS = ['input', 'incl', 'in', 'out']
LABELS = {'input': 'Input ROOT tree', 'incl': 'Inclusive workspace',
          'in': 'In workspace', 'out': 'Out workspace'}
REGIONS = [('below', 'Below range', 'm < 100'),
           ('lower', 'Lower sideband', '100 ≤ m < 120'),
           ('blind', 'Blinded region', '120 ≤ m ≤ 130'),
           ('upper', 'Upper sideband', '130 < m ≤ 180'),
           ('above', 'Above range', 'm > 180'),
           ('invalid', 'Invalid mass', 'Nonfinite')]


def mass_region(mass):
    if not math.isfinite(mass):
        return 'invalid'
    if mass < 100:
        return 'below'
    if mass > 180:
        return 'above'
    if mass < 120:
        return 'lower'
    if mass <= 130:
        return 'blind'
    return 'upper'


def read_root(request, root_file=None):
    """Worker: return plain numbers, releasing ROOT memory on process exit."""
    import ROOT
    ROOT.gROOT.SetBatch(True)
    owns_file = root_file is None
    if owns_file:
        root_file = ROOT.TFile.Open(request['path'], 'READ')
    if not root_file or root_file.IsZombie():
        raise RuntimeError('Cannot open ROOT file: ' + request['path'])
    try:
        if request['kind'] == 'discover':
            directory = root_file.Get('DiphotonTree')
            if not directory:
                raise RuntimeError('Missing DiphotonTree directory')
            return categories_from_names(key.GetName() for key in directory.GetListOfKeys())
        if request['kind'] == 'batch':
            return {category: read_root(child, root_file)
                    for category, child in request['requests'].items()}
        if request['kind'] == 'tree':
            tree = None
            for name in request['names']:
                tree = root_file.Get(name)
                if tree:
                    break
            if not tree or not tree.InheritsFrom('TTree'):
                raise RuntimeError('Missing tree: ' + ', '.join(request['names']))
            if not tree.GetBranch('weight'):
                raise RuntimeError('Missing weight branch in ' + tree.GetName())
            tree.SetBranchStatus('*', 0)
            tree.SetBranchStatus('weight', 1)
            if request['data']:
                if not tree.GetBranch('CMS_hgg_mass'):
                    raise RuntimeError('Missing CMS_hgg_mass branch')
                tree.SetBranchStatus('CMS_hgg_mass', 1)
            regions = {key: [0, 0.0] for key, _, _ in REGIONS}
            nonunit = 0
            weights = []
            for event in tree:
                weight = float(event.weight)
                if not math.isfinite(weight):
                    raise RuntimeError('Nonfinite event weight in ' + tree.GetName())
                weights.append(weight)
                if request['data']:
                    key = mass_region(float(event.CMS_hgg_mass))
                    regions[key][0] += 1
                    regions[key][1] += weight
                    nonunit += int(weight != 1.0)
            result = {'events': int(tree.GetEntries()), 'weight': math.fsum(weights),
                      'object': tree.GetName()}
            if request['data']:
                result.update(regions=regions, nonunit=nonunit)
        else:
            workspace = root_file.Get('tagsDumper/cms_hgg_13TeV')
            if not workspace:
                raise RuntimeError('Missing tagsDumper/cms_hgg_13TeV')
            dataset = workspace.data(request['name'])
            if not dataset or dataset.ClassName() != 'RooDataSet':
                raise RuntimeError('Missing RooDataSet: ' + request['name'])
            result = {'events': int(dataset.numEntries()),
                      'weight': float(dataset.sumEntries()), 'object': dataset.GetName()}
            if request['data']:
                regions = {key: [0, 0.0] for key, _, _ in REGIONS}
                nonunit = 0
                for index in range(dataset.numEntries()):
                    row = dataset.get(index)
                    key = mass_region(float(row.getRealValue('CMS_hgg_mass')))
                    weight = float(dataset.weight())
                    regions[key][0] += 1
                    regions[key][1] += weight
                    nonunit += int(weight != 1.0)
                result.update(regions=regions, nonunit=nonunit)
        return result
    finally:
        if owns_file:
            root_file.Close()


def make_request(path, category, version, process=None):
    is_data = process is None
    prefix = 'Data' if is_data else PREFIX[process]
    stem = prefix + ('_13TeV_' if is_data else '_125_13TeV_') + category
    names = ['DiphotonTree/' + stem]
    if process == 'ttH':
        names.append(names[0].replace('/tth_', '/ttH_', 1))
    request = {'path': str(path), 'kind': 'tree' if version == 'input' else 'workspace',
               'names': names, 'data': is_data,
               'name': stem if is_data else prefix + '_' + version + '_125_13TeV_' + category}
    return request


def run_worker(request):
    path = request['path']
    completed = subprocess.run(
        [sys.executable, '-B', str(Path(__file__).resolve()), '--worker', json.dumps(request)],
        capture_output=True, text=True)
    if completed.returncode:
        raise RuntimeError(f'{path}: worker failed ({completed.returncode})\n{completed.stderr.strip()}')
    for line in completed.stdout.splitlines():
        if line.startswith('BOOKKEEPING_JSON '):
            return json.loads(line[len('BOOKKEEPING_JSON '):])
    raise RuntimeError('No worker result for ' + str(path))


def read_isolated(path, category, version, process=None):
    if isinstance(category, list):
        request = {'path': str(path), 'kind': 'batch', 'requests': {
            name: make_request(path, name, version, process) for name in category}}
    else:
        request = make_request(path, category, version, process)
    return run_worker(request)


def categories_from_names(names):
    categories = sorted({name[len('Data_13TeV_'):] for name in names
                         if name.startswith('Data_13TeV_') and 'sigma' not in name})
    if not categories:
        raise RuntimeError('No nominal Data_13TeV_<category> trees found')
    for category in categories:
        if not re.fullmatch(r'[A-Za-z0-9_]+', category):
            raise RuntimeError('Unsupported category name: ' + category)
    return categories


def unique_file(pattern, directory):
    files = sorted(directory.glob(pattern))
    if len(files) != 1:
        raise RuntimeError(f'Expected one file matching {directory}/{pattern}; found {len(files)}')
    return files[0]


def table(headers, rows):
    lines = ['| ' + ' | '.join(headers) + ' |',
             '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    lines.extend('| ' + ' | '.join(str(value) for value in row) + ' |' for row in rows)
    return '\n'.join(lines)


def totals(records):
    return {version: {
        'events': sum(row['events'] for row in records if row['version'] == version),
        'weight': math.fsum(row['weight'] for row in records if row['version'] == version),
        'yield': math.fsum(row['yield'] for row in records if row['version'] == version)
    } for version in VERSIONS}


def agrees(left, right):
    return left['events'] == right['events'] and math.isclose(
        left['weight'], right['weight'], rel_tol=1e-9, abs_tol=1e-12)


def build_report(category, input_dir, records, data, sources, checks):
    lines = [f'# Category bookkeeping: {category}', '',
             f'Input directory: `{input_dir}`', '',
             'MC uses nominal datasets only. Events are unweighted entry counts; '
             'Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.', '',
             'Normalization values follow `Trees2WS/calc_yields.py`; the upstream '
             'normalization of `weight` must be verified separately. Mass regions are in GeV.', '',
             '## MC: totals across selected eras', '']
    rows = []
    for process in dict.fromkeys(row['process'] for row in records):
        combined = totals([row for row in records if row['process'] == process])
        for version in VERSIONS:
            result = combined[version]
            rows.append([process, LABELS[version], f"{result['events']:,}",
                         f"{result['weight']:.12f}", f'{XS_BR[process]:.6f}', f"{result['yield']:.9f}"])
    lines += [table(['Process', 'Version', 'Events', 'Σ weight', 'XS × BR (fb)', 'Yield'], rows), '',
              '## MC: total category yield across processes and eras', '']
    combined = totals(records)
    lines += [table(['Version', 'Events', 'Σ weight', 'Yield'], [
        [LABELS[v], f"{combined[v]['events']:,}", f"{combined[v]['weight']:.12f}",
         f"{combined[v]['yield']:.9f}"] for v in VERSIONS]), '',
        'Yields are summed after each process and era receives its own normalization. '
        'The combined Σ weight is a bookkeeping sum, not a common-normalization yield.', '',
        '## MC: per-era bookkeeping', '']
    lines += [table(['Era', 'Process', 'Version', 'Events', 'Σ weight', 'Lumi (fb⁻¹)',
                     'XS × BR (fb)', 'Yield'], [
        [r['era'], r['process'], LABELS[r['version']], f"{r['events']:,}",
         f"{r['weight']:.12f}", f"{LUMI[r['era']]:.2f}",
         f"{XS_BR[r['process']]:.6f}", f"{r['yield']:.9f}"] for r in records]), '',
        '## Observed data: combined eras', '',
        'Data has no XS/luminosity multiplier or generator-level in/out split. '
        'Events in the designated blinded region are counted, without modifying the files.', '',
        table(['Version', 'Events', 'Σ weight', 'Nonunit-weight events'], [
            [label, f"{result['events']:,}", f"{result['weight']:.6f}", result['nonunit']]
            for label, result in data]), '', '### Data mass regions', '']
    region_rows = [(key, label, definition) for key, label, definition in REGIONS]
    region_rows += [('sidebands', 'Sidebands combined', '100 ≤ m < 120 or 130 < m ≤ 180'),
                    ('fit', 'Fit range total', '100 ≤ m ≤ 180'), ('total', 'Total', 'All entries')]
    rows = []
    for key, label, definition in region_rows:
        row = [label, definition]
        for _, result in data:
            selected = {'sidebands': ['lower', 'upper'], 'fit': ['lower', 'blind', 'upper'],
                        'total': [r[0] for r in REGIONS]}.get(key, [key])
            row += [f"{sum(result['regions'][k][0] for k in selected):,}",
                    f"{math.fsum(result['regions'][k][1] for k in selected):.6f}"]
        rows.append(row)
    headers = ['Mass region', 'Definition (GeV)']
    for label, _ in data:
        headers += [label + ': events', label + ': Σ weight']
    lines += [table(headers, rows), '', '## Consistency checks', '',
              table(['Sample', 'Check', 'Result'], checks), '',
              'Checks compare event counts and summed weights. Input versus inclusive differences '
              'may indicate conversion selections or a mismatch between input and workspace versions.', '',
              '## Source ROOT files', '', table(['Sample/version', 'File', 'ROOT object'], sources), '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--category', help='One analysis category')
    selection.add_argument('--allCategories', action='store_true',
                           help='Discover all nominal categories from the data input tree file')
    parser.add_argument('--inputDir', required=True, type=Path,
                        help='Directory containing <process>_<era>/ and Data/ (e.g. inputs_27June)')
    parser.add_argument('--output', type=Path, help='Single-category Markdown output')
    parser.add_argument('--outputDir', type=Path, default=Path('bookkeeping'),
                        help='All-category report directory; default bookkeeping/')
    parser.add_argument('--processes', nargs='+', choices=list(PREFIX), default=list(PREFIX))
    parser.add_argument('--eras', nargs='+', choices=list(LUMI), default=list(LUMI))
    parser.add_argument('--force', action='store_true', help='Allow replacing existing reports')
    args = parser.parse_args()
    if args.category and not re.fullmatch(r'[A-Za-z0-9_]+', args.category):
        parser.error('Category must contain only letters, digits and underscores')
    if args.allCategories and args.output:
        parser.error('Use --outputDir with --allCategories, rather than --output')
    input_dir = args.inputDir.resolve()
    if not input_dir.is_dir():
        parser.error('Input directory does not exist: ' + str(input_dir))
    data_paths = [('input', 'Input data', unique_file('*.root', input_dir / 'Data')),
                  ('incl', 'Data workspace', unique_file('*.root', input_dir / 'Data' / 'ws'))]
    categories = (run_worker({'path': str(data_paths[0][2]), 'kind': 'discover'})
                  if args.allCategories else [args.category])
    outputs = {category: (args.outputDir / ('bookkeeping_' + category + '.md')
                         if args.allCategories else
                         args.output or Path('bookkeeping_' + category + '.md'))
               for category in categories}
    index = args.outputDir / 'README.md' if args.allCategories else None
    targets = list(outputs.values()) + ([index] if index else [])
    for output in targets:
        if output.suffix.lower() != '.md':
            parser.error('Output must have the .md extension')
        if output.exists() and not args.force:
            parser.error('Report already exists: ' + str(output) + '; use --force to replace')
    if args.allCategories:
        if args.outputDir.exists() and not args.outputDir.is_dir():
            parser.error('Output directory path is not a directory')
    elif not next(iter(outputs.values())).parent.is_dir():
        parser.error('Output parent directory does not exist')
    records = {category: [] for category in categories}
    sources = {category: [] for category in categories}
    checks = {category: [] for category in categories}
    data = {category: [] for category in categories}
    print(f'Categories ({len(categories)}): ' + ', '.join(categories), flush=True)
    # Load each workspace once for all requested categories, in an isolated worker.
    for era in dict.fromkeys(args.eras):
        for process in dict.fromkeys(args.processes):
            directory = input_dir / (process + '_' + era)
            group = {}
            for version in VERSIONS:
                path = unique_file('*.root' if version == 'input' else 'ws_*_' + version + '/*.root', directory)
                print(f'Reading {process} / {era} / {LABELS[version]}', flush=True)
                results = read_isolated(path, categories, version, process)
                group[version] = results
                for category, result in results.items():
                    row = dict(result, process=process, era=era, version=version)
                    row['yield'] = result['weight'] * LUMI[era] * XS_BR[process]
                    records[category].append(row)
                    sources[category].append([process + ' / ' + era + ' / ' + version,
                                              str(path), result['object']])
            for category in categories:
                sample = {v: group[v][category] for v in VERSIONS}
                split = {'events': sample['in']['events'] + sample['out']['events'],
                         'weight': sample['in']['weight'] + sample['out']['weight']}
                checks[category] += [[process + ' / ' + era, 'Input = inclusive',
                                     'PASS' if agrees(sample['input'], sample['incl']) else 'DIFFERENCE'],
                                    [process + ' / ' + era, 'Inclusive = in + out',
                                     'PASS' if agrees(sample['incl'], split) else 'DIFFERENCE']]
    for version, label, path in data_paths:
        print('Reading ' + label, flush=True)
        results = read_isolated(path, categories, version)
        for category, result in results.items():
            data[category].append((label, result))
            sources[category].append([label, str(path), result['object']])
    reports = {}
    for category in categories:
        checks[category].append(['Data', 'Input = workspace',
                                'PASS' if agrees(data[category][0][1], data[category][1][1]) else 'DIFFERENCE'])
        reports[outputs[category]] = build_report(category, input_dir, records[category],
                                                 data[category], sources[category], checks[category])
    if index:
        summary = []
        for category in categories:
            combined = totals(records[category])
            summary.append([f'[{category}]({outputs[category].name})',
                            f"{combined['incl']['yield']:.9f}",
                            f"{combined['in']['yield']:.9f}",
                            f"{combined['out']['yield']:.9f}",
                            f"{data[category][1][1]['events']:,}"])
        reports[index] = ('# Category bookkeeping\n\n'
                          + f'Input directory: `{input_dir}`\n\n'
                          + 'MC yields sum the selected processes and eras. Data is combined.\n\n'
                          + table(['Category report', 'MC inclusive yield', 'MC in yield',
                                   'MC out yield', 'Data events'], summary) + '\n')
        args.outputDir.mkdir(parents=True, exist_ok=True)
    for output, report in reports.items():
        with output.open('w' if args.force else 'x', encoding='utf-8') as handle:
            handle.write(report)
        print('Report written: ' + str(output.resolve()))


if __name__ == '__main__':
    try:
        if len(sys.argv) == 3 and sys.argv[1] == '--worker':
            print('BOOKKEEPING_JSON ' + json.dumps(read_root(json.loads(sys.argv[2])), allow_nan=False))
        else:
            main()
    except (RuntimeError, OSError, ValueError) as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        sys.exit(1)
