# Combine Workflow README

This README explains how to run the combine scripts step by step.

## Step 1: Convert Datacard to Workspace
This converts `Datacard.txt` into the corresponding workspace.

```bash
rkumarag_Text2Workspace.sh

Step 2: Likelihood Scan

Run the following script:

rkumarag_ttH_tH_tHq_profiled_liklihood_scan.sh

Step 3: Significance and Limit

Open a NEW terminal and run:

rkumarag_significance_limit.sh

Note: This displays the Significance and Z value. Please note them down.

Step 4: Impact Plots (Run in Parallel)

Open 4 terminals and run one command in each terminal to save time.

Terminal 1:

rkumarag_Impacts_r_tHq.sh

Terminal 2:

rkumarag_Impacts_r_ttH_1D_tHq_profiled.sh

Terminal 3:

rkumarag_Impacts_r_ttH.sh

Terminal 4:

rkumarag_Impacts_r_tHq_1D_ttH_profiled.sh

Wait until all jobs finish.

Step 5: Combine Plots

In any one terminal, run:

rkumarag_CombinePlot.sh

Step 6: Publish to WWW

Finally, run:

rkumarag_www.sh

Workflow finished.
~                   
write in simple text 
