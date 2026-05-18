import os
import json
import re
import matplotlib.pyplot as plt
import mplhep as hep
from collections import defaultdict

# Set CMS style
plt.style.use(hep.style.CMS)

def get_data(base_path):
    data = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    folder_re = re.compile(r"(.+)_mu(\d+)")

    print(f"\n[INFO] Scanning directory: {base_path}")
    all_folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
    
    for idx, folder in enumerate(all_folders):
        match = folder_re.match(folder)
        if not match: continue
        
        cat, mu = match.group(1), int(match.group(2))
        full_path = os.path.join(base_path, folder)
        
        json_path = None
        for sub in os.listdir(full_path):
            if sub.startswith("BiasPlots"):
                p = os.path.join(full_path, sub, "BiasResults.json")
                if os.path.exists(p):
                    json_path = p
                    break
        
        if json_path:
            print(f"  [{idx+1}/{len(all_folders)}] Parsing {cat} at mu={mu}")
            try:
                with open(json_path, 'r') as f:
                    content = json.load(f)
                    for func, metrics in content.items():
                        for metric_name, val in metrics.items():
                            data[metric_name][cat][func][mu] = val
            except Exception as e:
                print(f"  [Skip] Error reading {json_path}: {e}")
                continue
    return data

def plot_all_with_thresholds(base_path):
    all_metrics = get_data(base_path)
    out_dir = os.path.join(base_path, "cms_bias_plots")
    os.makedirs(out_dir, exist_ok=True)

    for metric, categories in all_metrics.items():
        if metric in ['expectSignal', 'pullEntries']: continue
        
        metric_dir = os.path.join(out_dir, metric)
        os.makedirs(metric_dir, exist_ok=True)

        for cat, functions in categories.items():
            try:
                fig, ax = plt.subplots(figsize=(11, 9))
                
                # 1. CMS Labels (Removed 'lumenumber' for compatibility)
                hep.cms.label("Preliminary", data=True, ax=ax, com=13.6)
                
                # 2. Category Label INSIDE the box
                ax.text(0.05, 0.88, f"Category: {cat}", transform=ax.transAxes, 
                        fontsize=16, fontweight='bold', verticalalignment='top',
                        bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

                # 3. Bias Threshold Belts
                if metric == 'bias':
                    ax.axhspan(-0.1, 0.1, color='lightgreen', alpha=0.25, label='$\pm$10% Bias')
                    ax.axhspan(-0.2, -0.1, color='khaki', alpha=0.25, label='$\pm$20% Bias')
                    ax.axhspan(0.1, 0.2, color='khaki', alpha=0.25)
                    ax.axhline(0, color='black', linewidth=1, linestyle='-')

                # 4. Plotting Lines
                for func_name in sorted(functions.keys()):
                    mu_dict = functions[func_name]
                    sorted_mu = sorted(mu_dict.keys())
                    values = [mu_dict[m] for m in sorted_mu]
                    
                    if metric == 'failedToys':
                        line, = ax.plot(sorted_mu, values, marker='o', label=f"{func_name} (Fail)")
                        if 'boundaryHits' in all_metrics and cat in all_metrics['boundaryHits']:
                            b_mu_dict = all_metrics['boundaryHits'][cat].get(func_name, {})
                            b_vals = [b_mu_dict.get(m, 0) for m in sorted_mu]
                            ax.plot(sorted_mu, b_vals, marker='x', ls='--', color=line.get_color(), alpha=0.6, label=f"{func_name} (Bound)")
                    elif metric == 'boundaryHits':
                        continue 
                    else:
                        ax.plot(sorted_mu, values, marker='o', label=func_name)

                # 5. Formatting
                ax.set_xlabel(r"Expected Signal Strength $\mu$")
                y_label = "Number of Toys" if metric in ['failedToys', 'boundaryHits'] else metric
                ax.set_ylabel(y_label)
                
                # Grid lines
                ax.grid(True, which='both', linestyle=':', alpha=0.4)
                
                # Legend inside
                ax.legend(loc='upper right', fontsize=12, ncol=2 if len(functions)>4 else 1, 
                          frameon=True, framealpha=0.8)
                
                plt.tight_layout()
                save_name = "failed_boundary" if metric == 'failedToys' else metric
                plt.savefig(os.path.join(metric_dir, f"{cat}_{save_name}.png"))
                plt.savefig(os.path.join(metric_dir, f"{cat}_{save_name}.pdf"))
                plt.close()
                print(f"[SUCCESS] Saved {cat} {metric}")
                
            except Exception as e:
                print(f"[ERROR] Could not plot {cat} {metric}: {e}")
                plt.close()
                continue

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    plot_all_with_thresholds(path)
    print("\n[FINISH] Plots generated in 'cms_bias_plots'")
