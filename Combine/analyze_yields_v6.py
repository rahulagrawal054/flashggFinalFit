import pandas as pd
import matplotlib.pyplot as plt
import sys
import re
import os

# Load input CSV (defaults to workspace_yields.csv if no argument given)
csv_file = sys.argv[1] if len(sys.argv) > 1 else "workspace_yields.csv"
print(f"Reading input data from: {csv_file}")

# Automatically extract directory path from input CSV
out_dir = os.path.dirname(csv_file)

def get_out_path(filename):
    """Helper to route output files directly to the input file directory."""
    return os.path.join(out_dir, filename) if out_dir else filename

df = pd.read_csv(csv_file)

# ---------------------------------------------------------
# 1. Map Processes into 8 Standard Columns
# ---------------------------------------------------------
def classify_process(proc):
    p = str(proc).lower()
    is_in = "_in" in p
    is_out = "_out" in p

    if "tth" in p or "thw" in p:
        return "ttH+tHW (in)" if is_in else ("ttH+tHW (out)" if is_out else "ttH+tHW (in)")
    elif "thq" in p:  # Combines tHqHad and tHqLep
        return "tHq (in)" if is_in else ("tHq (out)" if is_out else "tHq (in)")
    elif "ggh" in p:
        return "ggH (in+out)"
    elif "vbf" in p:
        return "VBF (in+out)"
    elif any(x in p for x in ["vh", "wzh", "wh", "zh"]):
        return "VH (in+out)"
    elif "bbh" in p:
        return "bbH (in+out)"
    else:
        return "Other"

df['proc_group'] = df['proc'].apply(classify_process)

target_cols_8 = [
    "ttH+tHW (in)",
    "tHq (in)",
    "ttH+tHW (out)",
    "tHq (out)",
    "ggH (in+out)",
    "VBF (in+out)",
    "VH (in+out)",
    "bbH (in+out)"
]

# ---------------------------------------------------------
# 2. Build Pivot Table & Apply Category Sorting
# ---------------------------------------------------------
grid_8col = df.pivot_table(index='cat', columns='proc_group', values='nominal_yield', aggfunc='sum', fill_value=0.0)

for col in target_cols_8:
    if col not in grid_8col.columns:
        grid_8col[col] = 0.0
grid_8col = grid_8col[target_cols_8]

def get_row_sort_key(cat_name):
    c = str(cat_name)
    num_match = re.search(r'\d+$', c)
    num = int(num_match.group()) if num_match else 0
    c_low = c.lower()
    
    if "tth_had" in c_low or "tthhad" in c_low:
        return (1, num, c)
    elif "tth_lep" in c_low or "tthlep" in c_low:
        return (2, num, c)
    elif "th_had" in c_low or "thhad" in c_low:
        return (3, num, c)
    elif "th_lep" in c_low or "thlep" in c_low:
        return (4, num, c)
    elif "bkg_had" in c_low or "bkghad" in c_low:
        return (5, num, c)
    elif "bkg_lep" in c_low or "bkglep" in c_low:
        return (6, num, c)
    else:
        return (7, num, c)

sorted_cats = sorted(grid_8col.index, key=get_row_sort_key)
grid_8col = grid_8col.loc[sorted_cats]

# ---------------------------------------------------------
# Helper Function for Table Formatting: Value (Pct%)
# ---------------------------------------------------------
def create_formatted_df(raw_df):
    """Formats each cell as: Nominal_Yield (Percentage%) relative to category Total."""
    df_calc = raw_df.copy()
    df_calc['Total'] = df_calc.sum(axis=1)
    
    # Calculate Total Row
    total_row = df_calc.sum(axis=0).to_frame(name='Total').T
    df_calc = pd.concat([df_calc, total_row])

    formatted = pd.DataFrame(index=df_calc.index, columns=df_calc.columns)
    for idx in df_calc.index:
        row_tot = df_calc.loc[idx, 'Total']
        for col in df_calc.columns:
            val = df_calc.loc[idx, col]
            if col == 'Total':
                formatted.loc[idx, col] = f"{val:.3f}"
            else:
                pct = (val / row_tot * 100.0) if row_tot > 0 else 0.0
                formatted.loc[idx, col] = f"{val:.3f} ({pct:.1f}%)"
    return formatted

# ---------------------------------------------------------
# 3. Build & Save Table 1: Detailed 8-Column Table
# ---------------------------------------------------------
fmt_8col = create_formatted_df(grid_8col)

path_8col_csv = get_out_path("formatted_8col_yields.csv")
path_8col_txt = get_out_path("formatted_8col_yields.txt")
fmt_8col.to_csv(path_8col_csv)
with open(path_8col_txt, "w") as f:
    f.write(fmt_8col.to_string())

print(f"\n--> Saved Detailed 8-Column Table to:\n    - {path_8col_csv}\n    - {path_8col_txt}")

# ---------------------------------------------------------
# 4. Build & Save Table 2: 3-Column Combine Model Table
# ---------------------------------------------------------
grid_3col = pd.DataFrame(index=grid_8col.index)
grid_3col['ttH+tHW (in)'] = grid_8col['ttH+tHW (in)']
grid_3col['tHq (in)'] = grid_8col['tHq (in)']
grid_3col['Resonant Bkg'] = (
    grid_8col['ttH+tHW (out)'] + 
    grid_8col['tHq (out)'] + 
    grid_8col['ggH (in+out)'] + 
    grid_8col['VBF (in+out)'] + 
    grid_8col['VH (in+out)'] + 
    grid_8col['bbH (in+out)']
)

fmt_3col = create_formatted_df(grid_3col)

path_3col_csv = get_out_path("formatted_3col_yields.csv")
path_3col_txt = get_out_path("formatted_3col_yields.txt")
fmt_3col.to_csv(path_3col_csv)
with open(path_3col_txt, "w") as f:
    f.write(fmt_3col.to_string())

print(f"\n--> Saved 3-Column Combine Table to:\n    - {path_3col_csv}\n    - {path_3col_txt}\n")
print("=== 3-Column Combine Table Summary ===")
print(fmt_3col.to_string())

# ---------------------------------------------------------
# 5. Plotting with Total Event Numbers Annotated on Bars
# ---------------------------------------------------------
print("\n--> Generating quantified plots...")

category_totals = grid_8col.sum(axis=1)

# --- Plot 1: 3-Column Percentage Composition with Total Annotations ---
df_3col_pct = grid_3col.div(category_totals, axis=0) * 100.0

fig, ax = plt.subplots(figsize=(13, 6.5))
colors_3col = ['#1f77b4', '#ff7f0e', '#7f7f7f'] # Blue (r_ttH), Orange (r_tHq), Gray (Resonant Bkg)
df_3col_pct.plot(kind='bar', stacked=True, ax=ax, color=colors_3col)

# Add Total yield number on top of each 100% bar
for idx, (cat_name, total_val) in enumerate(category_totals.items()):
    ax.text(idx, 102, f"N={total_val:.1f}", ha='center', va='bottom', fontsize=8, fontweight='bold', rotation=45)

plt.title("Signal Composition & Purity per Category (%) [Total Events Annotated]", fontsize=12, fontweight='bold')
plt.xlabel("Analysis Category", fontsize=11)
plt.ylabel("Signal Share (%)", fontsize=11)
plt.ylim(0, 122) # Space for annotations
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(title="Fit Component", bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()

path_3col_pct_plot = get_out_path("combine_3col_yields_percentage.png")
plt.savefig(path_3col_pct_plot, dpi=300)

# --- Plot 2: 3-Column Absolute Log Scale with Total Annotations ---
fig, ax = plt.subplots(figsize=(13, 6.5))
grid_3col.plot(kind='bar', stacked=True, ax=ax, color=colors_3col)

ax.set_yscale('log')
ax.set_ylim(bottom=1e-2, top=category_totals.max() * 15)

# Add Total yield number on top of log bars
for idx, (cat_name, total_val) in enumerate(category_totals.items()):
    if total_val > 0:
        ax.text(idx, total_val * 1.35, f"{total_val:.1f}", ha='center', va='bottom', fontsize=8, fontweight='bold', rotation=45)

plt.title("Expected Signal Yield Breakdown (Log Scale) [Total Yield Annotated]", fontsize=12, fontweight='bold')
plt.xlabel("Analysis Category", fontsize=11)
plt.ylabel("Nominal Yield (Log Scale)", fontsize=11)
plt.xticks(rotation=45, ha='right')
plt.grid(True, which="both", ls="--", alpha=0.3)
plt.legend(title="Fit Component", bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()

path_3col_log_plot = get_out_path("combine_3col_yields_log.png")
plt.savefig(path_3col_log_plot, dpi=300)

# --- Plot 3: Full 8-Column Percentage Composition with Total Annotations ---
df_8col_pct = grid_8col.div(category_totals, axis=0) * 100.0

fig, ax = plt.subplots(figsize=(14, 6.5))
colors_8col = ['#1f77b4', '#ff7f0e', '#aec7e8', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#9467bd']
df_8col_pct.plot(kind='bar', stacked=True, ax=ax, color=colors_8col)

for idx, (cat_name, total_val) in enumerate(category_totals.items()):
    ax.text(idx, 102, f"N={total_val:.1f}", ha='center', va='bottom', fontsize=8, fontweight='bold', rotation=45)

plt.title("Detailed Process Share per Category (%) [Total Events Annotated]", fontsize=12, fontweight='bold')
plt.xlabel("Analysis Category", fontsize=11)
plt.ylabel("Process Share (%)", fontsize=11)
plt.ylim(0, 122)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(title="Process Group", bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()

path_8col_pct_plot = get_out_path("signal_yields_breakdown_percentage.png")
plt.savefig(path_8col_pct_plot, dpi=300)

print("All outputs generated successfully in directory:")
print(f" -> {out_dir if out_dir else '.'}")
