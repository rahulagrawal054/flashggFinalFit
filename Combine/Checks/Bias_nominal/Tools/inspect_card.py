import ROOT as r
import sys

def inspect_datacard(filename):
    f = r.TFile.Open(filename)
    w = f.Get("w")
    if not w:
        print(f"Error: No workspace 'w' found in {filename}")
        return

    print("\n" + "="*50)
    print(f"INSPECTING DATACARD: {filename}")
    print("="*50)

    # 1. Get POI range
    poi = w.var("r_tH")
    if poi:
        print(f"POI: {poi.GetName()} | Range: [{poi.getMin()}, {poi.getMax()}]")
    
    # 2. Extract Signal Yields (tH only)
    print("\n--- tH Signal Yields by Era ---")
    total_sig = 0
    all_funcs = w.allFunctions()
    
    # We look for the final expected yields for tH
    for func in all_funcs:
        fname = func.GetName()
        if "n_exp_final" in fname and "proc_tth" in fname:
            val = func.getVal()
            era = fname.split("incl_")[-1].replace("_hgg", "")
            print(f"Era: {era:<15} | Yield: {val:.4f}")
            total_sig += val
    
    print(f"TOTAL tH Yield: {total_sig:.4f}")

    # 3. Extract Background Yield
    print("\n--- Background Yield ---")
    bkg_yield_func = all_funcs.selectByName("*proc_bkg_mass*")
    if bkg_yield_func.getSize() > 0:
        bval = bkg_yield_func.first().getVal()
        print(f"Total Background: {bval:.2f}")
        if bval > 0:
            print(f"S/B Ratio: {(total_sig/bval):.6f}")

    # 4. Check Background MultiPdf Functions
    print("\n--- MultiPdf Configuration ---")
    multipdfs = w.allPdfs().selectByName("shapeBkg_*")
    if multipdfs.getSize() > 0:
        mpdf = multipdfs.first()
        print(f"MultiPdf Name: {mpdf.GetName()}")
        
        # We find the index variable name from the ModelConfig or the PDF directly
        # For Flashgg workspaces, it is usually pdfindex_...
        all_cats = w.allCats()
        idx_var = None
        for cat in all_cats:
            if "pdfindex" in cat.GetName():
                idx_var = cat
                break
        
        if idx_var:
            print(f"Index Variable: {idx_var.GetName()}")
            print(f"Current Index: {idx_var.getIndex()} ({idx_var.getLabel()})")
            
            # Count how many PDFs are in the envelope
            # We can find this by looking at the number of 'state' labels in the category
            num_pdfs = idx_var.numTypes()
            print(f"Number of functions in envelope: {num_pdfs}")

    print("="*50 + "\n")
    f.Close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 inspect_card.py Datacard_Name.root")
    else:
        inspect_datacard(sys.argv[1])
