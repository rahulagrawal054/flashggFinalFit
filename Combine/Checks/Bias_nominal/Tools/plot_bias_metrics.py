import os
import json
import re
import matplotlib.pyplot as plt
from collections import defaultdict

def run_plotter(base_path):
    # Output directory
    out_dir = os.path.join(base_path, "plots_summary")
    os.makedirs(out_dir, exist_ok=True)

    # data[category][function][mu] = {'failed': X, 'boundary': Y}
    data = defaultdict(lambda: defaultdict(dict))

    # Regex to capture category and mu (e.g., tH_had_2_mu10 -> group1: tH_had_2, group2: 10)
    folder_re = re.compile(r"(.+)_mu(\d+)")

    print(f"--> Scanning: {base_path}")

    # 1. Collect Data
    for folder in os.listdir(base_path):
        match = folder_re.match(folder)
        if not match:
            continue

        category = match.group(1)
        mu_val = int(match.group(2))
        full_folder_path = os.path.join(base_path, folder)

        # Search for the BiasResults.json inside ANY subfolder starting with 'BiasPlots'
        json_path = None
        if os.path.isdir(full_folder_path):
            for subfolder in os.listdir(full_folder_path):
                if subfolder.startswith("BiasPlots"):
                    temp_path = os.path.join(full_folder_path, subfolder, "BiasResults.json")
                    if os.path.exists(temp_path):
                        json_path = temp_path
                        break
        
        if json_path:
            with open(json_path, 'r') as f:
                results = json.load(f)
                for func, metrics in results.items():
                    data[category][func][mu_val] = {
                        'failed': metrics.get('failedToys', 0),
                        'boundary': metrics.get('boundaryHits', 0)
                    }
        else:
            print(f"    [Warning] No JSON found in {folder}")

    # 2. Plotting
    for cat, functions in data.items():
        print(f"--> Creating plot for: {cat}")
        plt.figure(figsize=(10, 6))
        
        # Sort functions to keep legend consistent
        for func_name in sorted(functions.keys()):
            mu_dict = functions[func_name]
            
            # Sort by Mu value to ensure the line connects 0 -> 1 -> 2...
            sorted_mus = sorted(mu_dict.keys())
            failed_vals = [mu_dict[m]['failed'] for m in sorted_mus]
            boundary_vals = [mu_dict[m]['boundary'] for m in sorted_mus]

            # Plot Failed Toys (Solid Line)
            line, = plt.plot(sorted_mus, failed_vals, marker='o', linestyle='-', 
                             label=f"{func_name} (Failed)")
            
            # Plot Boundary Hits (Dotted Line) - Use same color as the failed line
            plt.plot(sorted_mus, boundary_vals, marker='x', linestyle='--', 
                     color=line.get_color(), alpha=0.6, label=f"{func_name} (Boundary)")

        plt.title(f"Bias Study Stability: {cat}", fontsize=14)
        plt.xlabel(r"Expected Signal Strength ($\mu$)", fontsize=12)
        plt.ylabel("Number of Toys", fontsize=12)
        plt.xticks(range(0, 11))
        plt.grid(True, linestyle=':', alpha=0.7)
        
        # Place legend to the right of the plot
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
        plt.tight_layout()

        # Save
        plt.savefig(os.path.join(out_dir, f"Stability_{cat}.png"), dpi=300)
        plt.savefig(os.path.join(out_dir, f"Stability_{cat}.pdf"))
        plt.close()

    print(f"Done! Check the '{out_dir}' directory.")

if __name__ == "__main__":
    import sys
    # Use path from command line or default to current directory
    path_arg = sys.argv[1] if len(sys.argv) > 1 else "."
    run_plotter(path_arg)
