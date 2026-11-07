#!/usr/bin/env python3
"""Count the raw entries used by the fTest threshold; never run or change fits."""
import argparse
import csv
import json
import sys
from pathlib import Path


def options():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputWSDir', required=True, type=Path,
                        help='Parent containing ERA/ws_signal directories, or one ws_signal directory')
    parser.add_argument('--threshold', type=int, default=30, help='Minimum raw RV entries; default 30')
    parser.add_argument('--replacementThreshold', type=int, default=100,
                        help='signalFit minimum total entries with skipVertexScenarioSplit; default 100')
    parser.add_argument('--mass', default='125')
    parser.add_argument('--eras', nargs='+', help='Optional era subset')
    parser.add_argument('--outputDir', type=Path, default=Path('../my_checks/fTest_entries'))
    args = parser.parse_args()
    if args.threshold < 1 or args.replacementThreshold < 1:
        parser.error('Both thresholds must be at least 1')
    return args


def make_plots(rows, eras, processes, categories, threshold, output, count_key="rv_entries", prefix="", label="RV"):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.colors import ListedColormap
    from matplotlib.backends.backend_pdf import PdfPages

    lookup = {(r['era'], r['process'], r['category']): r for r in rows}
    with PdfPages(output / (prefix+'entry_threshold_plots.pdf')) as book:
        fig, ax = plt.subplots(figsize=(10, 5))
        passed = [sum(r['status'] == 'available' and r[count_key] >= threshold
                      for r in rows if r['era'] == era) for era in eras]
        below = [sum(r['status'] == 'available' and r[count_key] < threshold
                     for r in rows if r['era'] == era) for era in eras]
        missing = [sum(r['status'] != 'available' for r in rows if r['era'] == era) for era in eras]
        x = np.arange(len(eras))
        ax.bar(x, passed, label='%s entries >= %s' % (label, threshold), color='#277c62')
        ax.bar(x, below, bottom=passed, label='%s entries < %s' % (label, threshold), color='#dfa748')
        ax.bar(x, missing, bottom=np.array(passed) + below, label='Missing dataset', color='0.7')
        for i, (yes, no) in enumerate(zip(passed, below)):
            if yes:
                ax.text(i, yes/2, str(yes), ha='center', va='center', color='white')
            if no:
                ax.text(i, yes+no/2, str(no), ha='center', va='center')
        ax.set_xticks(x)
        ax.set_xticklabels(eras)
        ax.set_ylabel('Process / in-out / category combinations')
        ax.set_title('Input MC: raw %s-entry threshold %s' % (label, threshold))
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        fig.text(.02, .015, 'RV: |dZ| <= 1 cm; total: RV + WV. All stored masses. Entry counts alone do not establish fit quality.', fontsize=9)
        fig.tight_layout(rect=(0, .04, 1, 1))
        fig.savefig(output/(prefix+'entry_threshold_summary.png'), dpi=180)
        fig.savefig(output/(prefix+'entry_threshold_summary.pdf'))
        book.savefig(fig)
        plt.close(fig)

        for era in eras:
            values = np.full((len(processes), len(categories)), np.nan)
            codes = np.full_like(values, np.nan)
            for i, proc in enumerate(processes):
                for j, cat in enumerate(categories):
                    row = lookup.get((era, proc, cat))
                    if row and row['status'] == 'available':
                        values[i, j] = row[count_key]
                        codes[i, j] = int(row[count_key] >= threshold)
            fig, ax = plt.subplots(figsize=(14, max(6, len(processes)*.38)))
            cmap = ListedColormap(['#f5d79e', '#9cd2bb'])
            cmap.set_bad('#dddddd')
            ax.imshow(np.ma.masked_invalid(codes), cmap=cmap, vmin=0, vmax=1, aspect='auto')
            for i in range(len(processes)):
                for j in range(len(categories)):
                    ax.text(j, i, 'NA' if np.isnan(values[i,j]) else str(int(values[i,j])),
                            ha='center', va='center', fontsize=7)
            ax.set_xticks(range(len(categories)))
            ax.set_xticklabels(categories, rotation=55, ha='right')
            ax.set_yticks(range(len(processes)))
            ax.set_yticklabels(processes)
            ax.set_xlabel('Category')
            ax.set_title('%s: raw %s entries (threshold %s)' % (era, label, threshold))
            fig.text(.02, .015, 'Green: >= threshold; orange: below; grey: missing. Counts are for own MC, before borrowing or beamspot reweighting.', fontsize=9)
            fig.tight_layout(rect=(0, .045, 1, 1))
            fig.savefig(output/('%sentries_%s.png' % (prefix or 'rv_', era)), dpi=180)
            fig.savefig(output/('%sentries_%s.pdf' % (prefix or 'rv_', era)))
            book.savefig(fig)
            plt.close(fig)


def save_signal_table(rows, eras, threshold, output):
    selected = ['tth_in', 'tHW_in', 'tHqHad_in', 'tHqLep_in']
    labels = {'tth_in': 'ttH_in', 'tHW_in': 'tHW_in', 'tHqHad_in': 'tHqHad_in', 'tHqLep_in': 'tHqLep_in'}
    subset = [r for r in rows if r['process'] in selected]
    with (output/'signal_only_entries.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(subset)
    summary = []
    for proc in selected:
        for era in eras:
            data = [r for r in subset if r['process'] == proc and r['era'] == era]
            valid = [r for r in data if r['status'] == 'available']
            summary.append(dict(process=labels[proc], era=era, categories=len(data),
                                total_entries_ge_threshold=sum(r['total_entries'] >= threshold for r in valid),
                                total_entries_below_threshold=sum(r['total_entries'] < threshold for r in valid),
                                missing=len(data)-len(valid), threshold=threshold))
    with (output/'signal_only_100_entry_summary.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary[0]))
        writer.writeheader()
        writer.writerows(summary)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis('off')
    ax.set_title('Fiducial signal components: total raw-entry threshold %s' % threshold, fontsize=15, pad=15)
    cells = [[r['process'], r['era'], r['categories'], r['total_entries_ge_threshold'], r['total_entries_below_threshold']] for r in summary]
    table = ax.table(cellText=cells, colLabels=['Process', 'Era', 'Categories', 'Entries >= %s' % threshold, 'Entries < %s' % threshold],
                     loc='center', cellLoc='center', colWidths=[.19,.25,.16,.20,.20])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.8)
    for (i,j), cell in table.get_celld().items():
        if i == 0:
            cell.set_facecolor('#dce7ef')
            cell.set_text_props(weight='bold')
        elif ((i-1)//len(eras)) % 2:
            cell.set_facecolor('#f1f4f6')
    fig.text(.04, .025, 'Counts own nominal total MC (RV + WV), before borrowing/reweighting.\nNegative summed weights can additionally trigger borrowing even with >= threshold entries.', fontsize=10)
    fig.tight_layout(rect=(0,.06,1,1))
    fig.savefig(output/'signal_only_100_entry_summary.png', dpi=180)
    fig.savefig(output/'signal_only_100_entry_summary.pdf')
    plt.close(fig)


def save_report(rows, eras, processes, categories, args):
    for row in rows:
        available = row['status'] == 'available'
        row['passes_rv_threshold'] = (row['rv_entries'] >= args.threshold) if available else ''
        row['threshold'] = args.threshold
        row['replacement_threshold'] = args.replacementThreshold
        row['rv_entries_ge_replacement_threshold'] = (row['rv_entries'] >= args.replacementThreshold) if available else ''
        row['total_entries_ge_replacement_threshold'] = (row['total_entries'] >= args.replacementThreshold) if available else ''
        row['negative_total_sumw'] = (row['total_sumw'] < 0) if available else ''
        row['would_borrow_total_shape'] = (row['total_entries'] < args.replacementThreshold or row['total_sumw'] < 0) if available else ''
    with (args.outputDir/'entries.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    def aggregate(subset):
        available = [r for r in subset if r['status'] == 'available']
        return dict(combinations=len(subset), available=len(available),
                    rv_ge_threshold=sum(r['rv_entries'] >= args.threshold for r in available),
                    rv_below_threshold=sum(r['rv_entries'] < args.threshold for r in available),
                    rv_ge_replacement_threshold=sum(r['rv_entries'] >= args.replacementThreshold for r in available),
                    rv_below_replacement_threshold=sum(r['rv_entries'] < args.replacementThreshold for r in available),
                    total_ge_replacement_threshold=sum(r['total_entries'] >= args.replacementThreshold for r in available),
                    total_below_replacement_threshold=sum(r['total_entries'] < args.replacementThreshold for r in available),
                    negative_total_sumw=sum(r['total_sumw'] < 0 for r in available),
                    would_borrow_total_shape=sum(r['would_borrow_total_shape'] for r in available),
                    own_shape_entry_and_sign_checks_pass=sum(not r['would_borrow_total_shape'] for r in available),
                    missing=len(subset)-len(available))
    summary = dict(inputWSDir=str(args.inputWSDir.resolve()), mass=args.mass,
                   threshold=args.threshold, replacement_threshold=args.replacementThreshold,
                   rv_definition='abs(dZ)<=1 cm; no additional mass-window cut',
                   replacement_definition='total entries < replacement threshold OR signed total sumw < 0; assumes skipVertexScenarioSplit and no explicit shape override',
                   **aggregate(rows))
    summary['by_era'] = {era: aggregate([r for r in rows if r['era'] == era]) for era in eras}
    (args.outputDir/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    for key, groups in [('era', eras), ('process', processes)]:
        grouped = [dict({key: value}, **aggregate([r for r in rows if r[key] == value])) for value in groups]
        with (args.outputDir/('summary_by_%s.csv' % key)).open('w', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(grouped[0]))
            writer.writeheader()
            writer.writerows(grouped)
    save_signal_table(rows, eras, args.replacementThreshold, args.outputDir)
    make_plots(rows, eras, processes, categories, args.threshold, args.outputDir)
    make_plots(rows, eras, processes, categories, args.replacementThreshold, args.outputDir,
               count_key='total_entries', prefix='total_', label='total')
    print('TOTAL: %d combinations; RV >= %d: %d; RV below: %d' %
          (len(rows), args.threshold, summary['rv_ge_threshold'], summary['rv_below_threshold']))
    print('Total entries >= %d: %d; below: %d; negative sumw: %d; total-shape borrowing triggers: %d' %
          (args.replacementThreshold, summary['total_ge_replacement_threshold'],
           summary['total_below_replacement_threshold'], summary['negative_total_sumw'], summary['would_borrow_total_shape']))
    print('Saved reports in %s' % args.outputDir.resolve())
    return summary


def main():
    args = options()
    # Reuse the production naming and RV/WV functions.
    signal = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(signal.parent/'commonTools'))
    sys.path.insert(0, str(signal))
    import ROOT
    from commonTools import procToData
    from commonObjects import inputWSName__, sqrts__
    from tools.signalTools import splitRVWV
    ROOT.gROOT.SetBatch(True)
    source = args.inputWSDir.resolve()
    if list(source.glob('output_*.root')):
        era_dirs = [(source.parent.name, source)]
    else:
        era_dirs = [(d.name, d/'ws_signal') for d in sorted(source.iterdir())
                    if d.is_dir() and (d/'ws_signal').is_dir()]
    if args.eras:
        era_dirs = [(e, d) for e, d in era_dirs if e in args.eras]
        if set(args.eras) != {e for e, _ in era_dirs}:
            raise RuntimeError('Requested eras not found under inputWSDir')
    if not era_dirs:
        raise RuntimeError('No ERA/ws_signal directories or input ROOT files found')
    args.outputDir.mkdir(parents=True, exist_ok=True)
    rows, allprocs, allcats = [], set(), set()
    for era, directory in era_dirs:
        files = {}
        for path in sorted(directory.glob('output_*M%s*.root' % args.mass)):
            if 'pythia8_' not in path.stem:
                raise RuntimeError('Cannot identify process from filename: %s' % path)
            proc = path.stem.split('pythia8_', 1)[1]
            if proc in files:
                raise RuntimeError('Multiple files for %s / %s' % (era, proc))
            files[proc] = path
        if not files:
            raise RuntimeError('No mass-%s files in %s' % (args.mass, directory))
        allprocs.update(files)
        # Discover categories from nominal datasets across the input files.
        cats = set()
        for proc, path in files.items():
            f = ROOT.TFile.Open(str(path), 'READ')
            if not f or f.IsZombie():
                raise RuntimeError('Cannot open %s' % path)
            try:
                ws = f.Get(inputWSName__)
                if not ws:
                    raise RuntimeError('Missing workspace in %s' % path)
                for data in ws.allData():
                    name = data.GetName()
                    if 'sigma' in name or 'NOTAG' in name:
                        continue
                    token = '_%s_%s_' % (args.mass, sqrts__)
                    if token in name:
                        cats.add(name.split(token, 1)[1])
            finally:
                f.Close()
        if not cats:
            raise RuntimeError('No nominal categories in %s' % directory)
        allcats.update(cats)
        for proc, path in files.items():
            f = ROOT.TFile.Open(str(path), 'READ')
            if not f or f.IsZombie():
                raise RuntimeError('Cannot open %s' % path)
            try:
                ws = f.Get(inputWSName__)
                if not ws or not ws.var('CMS_hgg_mass') or not ws.var('dZ'):
                    raise RuntimeError('Missing workspace, mass or dZ in %s' % path)
                aset = ROOT.RooArgSet(ws.var('CMS_hgg_mass'), ws.var('dZ'))
                for cat in sorted(cats):
                    parts = proc.split('_')
                    stem = (procToData(parts[0])+'_'+procToData(parts[-1])
                            if len(parts) <= 2 and parts[-1] in ['in','out','incl']
                            else procToData(parts[0]))
                    name = '%s_%s_%s_%s' % (stem, args.mass, sqrts__, cat)
                    row = dict(era=era, process=proc, category=cat, dataset=name,
                               input_file=str(path), status='missing_dataset',
                               total_entries='', rv_entries='', wv_entries='',
                               total_sumw='', rv_sumw='', passes_rv_threshold='', threshold=args.threshold)
                    data = ws.data(name)
                    if data:
                        reduced = data.reduce(aset)
                        rv = splitRVWV(reduced, aset, mode='RV')
                        wv = splitRVWV(reduced, aset, mode='WV')
                        total = int(reduced.numEntries())
                        nr, nw = int(rv.numEntries()), int(wv.numEntries())
                        if nr+nw != total:
                            raise RuntimeError('RV+WV count does not match total: %s' % name)
                        row.update(status='available', total_entries=total, rv_entries=nr,
                                   wv_entries=nw, total_sumw=float(reduced.sumEntries()),
                                   rv_sumw=float(rv.sumEntries()), passes_rv_threshold=nr >= args.threshold)
                    rows.append(row)
            finally:
                f.Close()
        current = [r for r in rows if r['era'] == era]
        yes = sum(r['passes_rv_threshold'] is True for r in current)
        below = sum(r['passes_rv_threshold'] is False for r in current)
        print('%s: %d combinations; RV >= %d: %d; below: %d; missing: %d' %
              (era, len(current), args.threshold, yes, below, len(current)-yes-below), flush=True)
    summary = save_report(rows, [e for e, _ in era_dirs], sorted(allprocs), sorted(allcats), args)
    return 1 if summary['missing'] else 0


if __name__ == '__main__':
    sys.exit(main())
