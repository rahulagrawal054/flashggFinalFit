import os
import re
import glob
import pandas as pd
import matplotlib.pyplot as plt

# 1. Collect 3-column yields across all scanned folders
scan_dirs = sorted(glob.glob("*_SoG"))
data = []

for d in scan_dirs:
    match = re.search(r'(\d+p\d+)_SoG', d)
    if not match:
        continue
    
    threshold_val = float(match.group(1).replace('p', '.'))
    pct_val = threshold_val * 100.0  # e.g., 0.001 -> 0.1%

    csv_path = os.path.join(d, "formatted_3col_yields.csv")
    if not os.path.exists(csv_path):
        continue

    df = pd.read_csv(csv_path, index_col=0)
    if 'Total' not in df.index:
        continue

    total_row = df.loc['Total']

    def parse_val(entry):
        return float(str(entry).split('(')[0].strip())

    tth_thw_in = parse_val(total_row['ttH+tHW (in)'])
    thq_in = parse_val(total_row['tHq (in)'])
    res_bkg = parse_val(total_row['Resonant Bkg'])
    tot_yield = parse_val(total_row['Total'])

    data.append({
        'Pruning_Cut_%': pct_val,
        'ttH+tHW (in)': tth_thw_in,
        'tHq (in)': thq_in,
        'Resonant Bkg': res_bkg,
        'Total Yield': tot_yield
    })

df_summary = pd.DataFrame(data).sort_values('Pruning_Cut_%').reset_index(drop=True)

# 2. Compute Relative Change (%) compared to 0p000 baseline
base_tth = df_summary.loc[0, 'ttH+tHW (in)']
base_thq = df_summary.loc[0, 'tHq (in)']
base_bkg = df_summary.loc[0, 'Resonant Bkg']

df_summary['ttH+tHW (in) Rel %'] = (df_summary['ttH+tHW (in)'] / base_tth) * 100.0
df_summary['tHq (in) Rel %'] = (df_summary['tHq (in)'] / base_thq) * 100.0
df_summary['Resonant Bkg Rel %'] = (df_summary['Resonant Bkg'] / base_bkg) * 100.0

df_summary.round(4).to_csv("pruning_scan_comparison.csv", index=False)

# 3. Generate Comparison Plot
fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(df_summary['Pruning_Cut_%'], df_summary['ttH+tHW (in) Rel %'], marker='o', color='#1f77b4', linewidth=2, label='ttH+tHW (in)')
plt.plot(df_summary['Pruning_Cut_%'], df_summary['tHq (in) Rel %'], marker='s', color='#ff7f0e', linewidth=2, label='tHq (in)')
plt.plot(df_summary['Pruning_Cut_%'], df_summary['Resonant Bkg Rel %'], marker='^', color='#7f7f7f', linewidth=2, label='Resonant Bkg')

plt.axhline(100.0, color='red', linestyle=':', alpha=0.7, label='Baseline (0.0%)')
plt.title("Yield Retention (%) vs Pruning Threshold", fontsize=12, fontweight='bold')
plt.xlabel("Pruning Threshold SoG (%)", fontsize=11)
plt.ylabel("Retention relative to 0% baseline (%)", fontsize=11)
plt.xticks(df_summary['Pruning_Cut_%'])
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig("pruning_scan_retention_comparison.png", dpi=300)

print("Saved comparison summary table to: pruning_scan_comparison.csv")
print("Saved comparison plot to: pruning_scan_retention_comparison.png")
