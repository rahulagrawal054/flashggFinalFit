#!/usr/bin/env python3
"""Plot category_bookkeeping.py Markdown reports without reading ROOT files.

  python3 -B plot_bookkeeping.py --inputDir bookkeeping

Requires matplotlib and NumPy. Outputs PNG and PDF in <inputDir>/plots/.
"""
import argparse
from collections import defaultdict
from pathlib import Path
import math
import re

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

PROCESS_ORDER = ['ttH', 'tHqHad', 'tHqLep', 'tHW', 'GluGluH', 'VBFH', 'VH', 'bbH']
PROCESS_COLORS = ['#4477AA', '#228833', '#66CCEE', '#AA3377', '#EE6677', '#CCBB44', '#BBBBBB', '#000000']
ERA_ORDER = ['2022preEE', '2022postEE', '2023preBPix', '2023postBPix']
ERA_COLORS = ['#4477AA', '#66CCEE', '#EE6677', '#AA3377']


def number(value):
    result = float(value.replace(',', '').strip())
    if not math.isfinite(result):
        raise ValueError('Nonfinite report value: ' + value)
    return result


def markdown_tables(text):
    """Return table rows grouped by the most recent Markdown heading."""
    section, tables = '', {}
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if line.startswith('#'):
            section = line.lstrip('#').strip()
        if line.startswith('|') and index + 1 < len(lines):
            separator = lines[index + 1].strip().strip('|').split('|')
            if all(re.fullmatch(r'\s*:?-+:?\s*', cell) for cell in separator):
                headers = [cell.strip() for cell in line.strip('|').split('|')]
                rows = []
                index += 2
                while index < len(lines) and lines[index].strip().startswith('|'):
                    cells = [cell.strip() for cell in lines[index].strip().strip('|').split('|')]
                    if len(cells) != len(headers):
                        raise ValueError('Malformed table in section: ' + section)
                    rows.append(dict(zip(headers, cells)))
                    index += 1
                tables[section] = rows
                continue
        index += 1
    return tables


def read_report(path, data_source="input"):
    text = path.read_text(encoding='utf-8')
    title = re.search(r'^# Category bookkeeping: ([A-Za-z0-9_]+)$', text, re.MULTILINE)
    if not title:
        raise ValueError('Missing category heading in ' + str(path))
    tables = markdown_tables(text)
    required = ['MC: totals across selected eras', 'MC: total category yield across processes and eras',
                'MC: per-era bookkeeping', 'Data mass regions']
    for section in required:
        if section not in tables:
            raise ValueError(f'{path}: missing section {section}; wait for a complete report')
    processes = {}
    for row in tables[required[0]]:
        if row['Version'] == 'Inclusive workspace':
            if row['Process'] in processes:
                raise ValueError('Duplicate process in ' + str(path))
            processes[row['Process']] = number(row['Yield'])
    versions = {row['Version']: number(row['Yield']) for row in tables[required[1]]}
    if any(label not in versions for label in ['Inclusive workspace', 'In workspace', 'Out workspace']):
        raise ValueError('Missing MC version in ' + str(path))
    eras = defaultdict(float)
    for row in tables[required[2]]:
        if row['Version'] == 'Inclusive workspace':
            eras[row['Era']] += number(row['Yield'])
    regions = {}
    for row in tables[required[3]]:
        label = row['Mass region']
        # Input counts retain events excluded by the workspace mass range.
        column = 'Input data: events' if data_source == 'input' else 'Data workspace: events'
        regions[label] = number(row[column])
    for label in ['Below range', 'Lower sideband', 'Blinded region', 'Upper sideband', 'Above range']:
        if label not in regions:
            raise ValueError('Missing data region in ' + str(path))
    checks = tables.get('Consistency checks', [])
    differences = sum(row['Result'] != 'PASS' for row in checks)
    return {'category': title.group(1), 'processes': processes, 'versions': versions,
            'eras': dict(eras), 'regions': regions, 'differences': differences,
            'data_source': data_source,
            'negative_rows': [dict(row, category=title.group(1)) for row in tables[required[2]]
                              if row['Version'] != 'Input ROOT tree' and number(row['Yield']) < 0]}


def category_key(report):
    category = report['category']
    group_order = ['ttH_had', 'ttH_lep', 'tH_had', 'tH_lep', 'bkg_had', 'bkg_lep']
    match = re.fullmatch(r'(.+?)_(\d+)', category)
    group, index = (match.group(1), int(match.group(2))) if match else (category, 0)
    return (group_order.index(group) if group in group_order else len(group_order), group, index)


def axis(categories, ylabel, title):
    fig, ax = plt.subplots(figsize=(max(9, len(categories) * 0.72), 6))
    ax.set_xticks(np.arange(len(categories)))
    ax.set_xticklabels(categories, rotation=55, ha='right')
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(axis='y', alpha=0.25)
    ax.set_axisbelow(True)
    ax.axhline(0, color='black', linewidth=0.6)
    return fig, ax


def stacked(ax, series):
    """Keep positive and negative weighted yields on separate sides of zero."""
    n = len(series[0][1])
    positive, negative = np.zeros(n), np.zeros(n)
    for label, values, color in series:
        values = np.asarray(values, dtype=float)
        bottom = np.where(values >= 0, positive, negative)
        ax.bar(np.arange(n), values, bottom=bottom, label=label, color=color, width=0.72)
        positive += np.maximum(values, 0)
        negative += np.minimum(values, 0)
    ax.legend(fontsize=9, ncol=min(4, len(series)))


def set_scale(ax, requested):
    values = []
    for bar in ax.patches:
        values.extend([bar.get_height(), bar.get_y() + bar.get_height()])
    values = [v for v in values if math.isfinite(v) and v != 0]
    actual = requested
    if requested == 'log' and any(v < 0 for v in values):
        actual = 'symlog'
    if actual == 'symlog':
        threshold = min((abs(v) for v in values), default=1.0) / 10
        ax.set_yscale('symlog', linthresh=threshold)
    elif actual == 'log':
        positive = [v for v in values if v > 0]
        if positive:
            ax.set_ylim(min(positive) * 0.5, max(positive) * 3)
        else:
            ax.set_ylim(0.1, 10)
        # Clip zero baselines below the visible range so positive bars render.
        # Bar heights and the underlying yields are unchanged.
        ax.set_yscale('log', nonpositive='clip')
        # Nonpositive values have no position on a logarithmic axis.
        for text in ax.texts:
            if text.get_text() == 'undefined':
                text.set_y(ax.get_ylim()[0])
    if actual != 'linear':
        ax.set_ylabel(ax.get_ylabel() + ' [' + actual + ' scale]')
    ax.grid(axis='y', which='both', alpha=0.2)
    return actual


def save(fig, output_dir, name, force=False, yscale="log"):
    set_scale(fig.axes[0], yscale)
    for extension in ['png', 'pdf']:
        path = output_dir / (name + '.' + extension)
        if path.exists() and not force:
            raise FileExistsError('Plot already exists: ' + str(path) + '; use --force')
        fig.savefig(path, dpi=180, bbox_inches='tight')
    plt.close(fig)


def make_plots(reports, output_dir, force=False, yscale="log"):
    categories = [r['category'] for r in reports]
    processes = [p for p in PROCESS_ORDER if any(p in r['processes'] for r in reports)]
    processes += sorted(set().union(*(set(r['processes']) for r in reports)) - set(processes))
    fig, ax = axis(categories, 'Expected signal events', 'Inclusive MC contributions by category')
    stacked(ax, [(p, [r['processes'].get(p, 0) for r in reports], PROCESS_COLORS[i % len(PROCESS_COLORS)])
                 for i, p in enumerate(processes)])
    save(fig, output_dir, 'mc_process_yields', force, yscale)

    fig, ax = axis(categories, 'Expected signal events', 'Fiducial in/out MC yields by category')
    stacked(ax, [('In', [r['versions']['In workspace'] for r in reports], '#228833'),
                 ('Out', [r['versions']['Out workspace'] for r in reports], '#EE6677')])
    save(fig, output_dir, 'mc_fiducial_yields', force, yscale)

    fractions = [100 * r['versions']['In workspace'] / r['versions']['Inclusive workspace']
                 if r['versions']['Inclusive workspace'] != 0 else np.nan for r in reports]
    fig, ax = axis(categories, 'In / inclusive weighted yield (%)', 'Fiducial in fraction by category')
    ax.bar(np.arange(len(categories)), fractions, color='#228833', width=0.72)
    ax.axhline(100, color='gray', linewidth=0.8, linestyle='--')
    for i, value in enumerate(fractions):
        if not np.isfinite(value):
            ax.text(i, 0, 'undefined', rotation=90, ha='center', va='bottom', fontsize=8)
    save(fig, output_dir, 'mc_fiducial_fraction', force, yscale)

    eras = [e for e in ERA_ORDER if any(e in r['eras'] for r in reports)]
    fig, ax = axis(categories, 'Expected signal events', 'Inclusive MC yields by era (era luminosities applied)')
    width = 0.8 / len(eras)
    for i, era in enumerate(eras):
        positions = np.arange(len(categories)) + (i - (len(eras) - 1) / 2) * width
        ax.bar(positions, [r['eras'].get(era, 0) for r in reports], width,
               label=era, color=ERA_COLORS[i % len(ERA_COLORS)])
    ax.legend(ncol=min(4, len(eras)), fontsize=9)
    save(fig, output_dir, 'mc_era_yields', force, yscale)

    source_label = 'input ROOT trees' if reports[0].get('data_source', 'input') == 'input' else 'data workspaces'
    fig, ax = axis(categories, 'Observed data events', 'Data counts by mass region — ' + source_label)
    stacked(ax, [(label, [r['regions'][{'Below 100 GeV': 'Below range', 'Above 180 GeV': 'Above range'}.get(label, label)] for r in reports], color) for label, color in
                 [('Below 100 GeV', '#AA3377'), ('Lower sideband', '#4477AA'),
                  ('Blinded region', '#CCBB44'), ('Upper sideband', '#66CCEE'),
                  ('Above 180 GeV', '#EE6677')]])
    ax.set_title('Data counts by mass region — ' + source_label, pad=35)
    ax.text(0.0, 1.02, 'Below 100 GeV: ' + str(int(sum(r['regions']['Below range'] for r in reports)))
            + ' events; above 180 GeV: ' + str(int(sum(r['regions']['Above range'] for r in reports)))
            + ' events', transform=ax.transAxes, va='bottom', fontsize=9)
    save(fig, output_dir, 'data_mass_regions', force, yscale)


def negative_plot_names(reports):
    eras = sorted(set().union(*(set(r['eras']) for r in reports)),
                  key=lambda e: (ERA_ORDER.index(e) if e in ERA_ORDER else len(ERA_ORDER), e))
    return ['negative_yields_' + era for era in eras]


def make_negative_plots(reports, output_dir, force=False):
    rows = [row for report in reports for row in report['negative_rows']]
    versions = [('Inclusive workspace', 'Inclusive'), ('In workspace', 'In'), ('Out workspace', 'Out')]
    names = negative_plot_names(reports)
    for name in names:
        era = name[len('negative_yields_'):]
        groups = [[row for row in rows if row['Era'] == era and row['Version'] == version]
                  for version, _ in versions]
        for group in groups:
            group.sort(key=lambda row: number(row['Yield']))
        height = max(4, 0.38 * max((len(group) for group in groups), default=0) + 2)
        fig, axes = plt.subplots(1, 3, figsize=(22, height), constrained_layout=True)
        fig.suptitle('Negative MC yields — ' + era + ' (signed values, symlog axes)')
        for ax, group, (_, label) in zip(axes, groups, versions):
            ax.set_title(label + f' ({len(group)} negative contributions)')
            if not group:
                ax.text(0.5, 0.5, 'No negative yields', transform=ax.transAxes, ha='center')
                ax.set_axis_off()
                continue
            values = [number(row['Yield']) for row in group]
            colors = [PROCESS_COLORS[PROCESS_ORDER.index(row['Process'])]
                      if row['Process'] in PROCESS_ORDER else '#AA3377' for row in group]
            ax.barh(np.arange(len(group)), values, color=colors)
            ax.set_yticks(np.arange(len(group)))
            ax.set_yticklabels([row['category'] + ' / ' + row['Process'] for row in group], fontsize=8)
            ax.invert_yaxis()
            ax.set_xscale('symlog', linthresh=min(abs(v) for v in values) / 10)
            ax.axvline(0, color='black', linewidth=0.8)
            ax.set_xlabel('Expected signal events (negative weighted yield)')
            ax.grid(axis='x', which='both', alpha=0.2)
            ax.set_axisbelow(True)
            for index, value in enumerate(values):
                ax.annotate(f'{value:.6g}', (value, index), xytext=(-4, 0),
                            textcoords='offset points', ha='right', va='center', fontsize=8)
            ax.set_xlim(min(values) * 5, 0)
        # Dedicated plots use signed horizontal axes; bypass the vertical-axis helper.
        for extension in ['png', 'pdf']:
            path = output_dir / (name + '.' + extension)
            if path.exists() and not force:
                raise FileExistsError('Plot already exists: ' + str(path))
            fig.savefig(path, dpi=180, bbox_inches='tight')
        plt.close(fig)
    headers = ['Category', 'Process', 'Era', 'Version', 'Events', 'Σ weight', 'Lumi (fb⁻¹)', 'XS × BR (fb)', 'Yield']
    lines = ['# Negative MC yield tracking', '',
             f'**{len(rows)} negative process/era/version contributions** in the selected reports.', '',
             'Input-tree rows are excluded to avoid duplicating inclusive contributions. '
             'Every plot separates inclusive, in, and out. Values are signed expected yields; '
             'the horizontal axes use symlog to display their different magnitudes.', '',
             '## Exact values', '',
             '| ' + ' | '.join(headers) + ' |',
             '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    for row in rows:
        lines.append('| ' + ' | '.join(row['category'] if h == 'Category' else row[h] for h in headers) + ' |')
    if not rows:
        lines += ['', 'No negative contributions found.']
    for name in names:
        lines += ['', f'![{name}]({name}.png)', '', f'[PDF]({name}.pdf)']
    with (output_dir / 'negative_yields.md').open('w' if force else 'x', encoding='utf-8') as handle:
        handle.write('\n'.join(lines) + '\n')
    return len(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--inputDir', type=Path, default=Path('bookkeeping'))
    parser.add_argument('--outputDir', type=Path, help='Default: <inputDir>/plots')
    parser.add_argument('--categories', nargs='+', help='Optional category subset')
    parser.add_argument('--yscale', choices=['log', 'linear', 'symlog'], default='log',
                        help='Default log; switches to symlog when negative yields occur')
    parser.add_argument('--dataSource', choices=['input', 'workspace'], default='input',
                        help='Data counts from input trees (default) or converted workspaces')
    parser.add_argument('--negativeOnly', action='store_true',
                        help='Generate only dedicated negative-yield plots and tracking table')
    parser.add_argument('--force', action='store_true', help='Replace existing plot files')
    args = parser.parse_args()
    files = sorted(args.inputDir.glob('bookkeeping_*.md'))
    if not files:
        parser.error('No bookkeeping_*.md reports found in ' + str(args.inputDir))
    reports = [read_report(path, args.dataSource) for path in files]
    if args.categories:
        missing = set(args.categories) - {r['category'] for r in reports}
        if missing:
            parser.error('Missing category reports: ' + ', '.join(sorted(missing)))
        reports = [r for r in reports if r['category'] in args.categories]
    reports.sort(key=category_key)
    if len({r['category'] for r in reports}) != len(reports):
        parser.error('Duplicate category reports')
    # Consistent era/process selections are required for comparable category plots.
    if len({tuple(sorted(r['eras'])) for r in reports}) > 1 or len({tuple(sorted(r['processes'])) for r in reports}) > 1:
        parser.error('Reports use different process or era selections; select matching reports')
    output_dir = args.outputDir or args.inputDir / 'plots'
    names = [] if args.negativeOnly else ['mc_process_yields', 'mc_fiducial_yields',
             'mc_fiducial_fraction', 'mc_era_yields', 'data_mass_regions']
    names += negative_plot_names(reports)
    targets = [output_dir / (name + '.' + ext) for name in names for ext in ['png', 'pdf']]
    targets.append(output_dir / 'negative_yields.md')
    if not args.negativeOnly:
        targets.append(output_dir / 'README.md')
    if not args.force and any(p.exists() for p in targets):
        parser.error('Output files already exist; choose --outputDir or use --force')
    output_dir.mkdir(parents=True, exist_ok=True)
    negative_count = make_negative_plots(reports, output_dir, args.force)
    if args.negativeOnly:
        print(f'Saved negative-yield plots and negative_yields.md ({negative_count} entries) in {output_dir.resolve()}')
        return
    make_plots(reports, output_dir, args.force, args.yscale)
    lines = ['# Bookkeeping plots', '', f'Reports read from `{args.inputDir.resolve()}`.', '',
             f'Requested y-axis scale: **{args.yscale}**. Log plots use symlog when negative values occur. '
             'Zero counts do not form visible bars on logarithmic axes. Data underflow/overflow totals '
             'are annotated even when zero. Data source: **' + args.dataSource + '**.', '',
             'MC yields follow the normalization in the reports. Negative weighted contributions '
             'are drawn below zero. Weighted in fractions can lie outside 0–100%; '
             'zero-inclusive-yield fractions are undefined.', '',
             'Era yields include their respective luminosities; this is a yield comparison, '
             'not an efficiency comparison. Data counts include the designated blinded region '
             '(120–130 GeV inclusive), sidebands, below 100 GeV, and above 180 GeV. '
             'Input data is used by default because conversion removes out-of-range events.', '']
    differences = sum(r['differences'] for r in reports)
    lines += [f'Report consistency checks marked DIFFERENCE: **{differences}**.', '',
              f'[Negative-yield tracking table]({"negative_yields.md"}) — {negative_count} entries.', '']
    for name in names:
        lines += [f'![{name}]({name}.png)', '', f'[PDF]({name}.pdf)', '']
    with (output_dir / 'README.md').open('w' if args.force else 'x', encoding='utf-8') as handle:
        handle.write('\n'.join(lines))
    print(f'Saved {len(names)} plots as PNG/PDF, README.md, and negative_yields.md in {output_dir.resolve()}')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        raise SystemExit('ERROR: ' + str(error))
