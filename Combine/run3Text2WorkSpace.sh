#!/bin/bash

# ==============================================================================
# Step 1: Create workspaces for Measurements (Signal Strength & 2D)
# ==============================================================================

# 1. 2D Scan (r_tHq vs r_ttH)
# ----------------------------------------------------
python3 RunText2Workspace.py --mode r_2D --batch local

# 2. r_ttH (ttH + tHW)
# ----------------------------------------------------
python3 RunText2Workspace.py --mode r_ttH_1D --batch local
python3 RunText2Workspace.py --mode r_ttH_1D_tHq_profiled --batch local

# 3. r_tH (tHqHad + tHqLep + tHW)
# ----------------------------------------------------
python3 RunText2Workspace.py --mode r_tHq_plus_tHW_1D --batch local
python3 RunText2Workspace.py --mode r_tHq_plus_tHW_1D_ttH_profiled --batch local

# 4. r_tHq (tHqHad + tHqLep)
# ----------------------------------------------------
python3 RunText2Workspace.py --mode r_tHq_1D --batch local
python3 RunText2Workspace.py --mode r_tHq_1D_ttH_profiled --batch local


# ==============================================================================
# Step 2: Create workspaces for Significance
# ==============================================================================

# Z_ttH (ttH + tHW)
# ----------------------------------------------------
python3 RunText2Workspace.py --mode Z_ttH --batch local

# Z_tH (tHqHad + tHqLep + tHW)
# ----------------------------------------------------
python3 RunText2Workspace.py --mode Z_tHq_plus_tHW --batch local

# Z_tHq (tHqHad + tHqLep)
# ----------------------------------------------------
python3 RunText2Workspace.py --mode Z_tHq --batch local


# ==============================================================================
# Step 3: Create workspaces for Limits
# ==============================================================================

# Limit tH (tHqHad + tHqLep + tHW)
# ----------------------------------------------------
python3 RunText2Workspace.py --mode limit_tHq_plus_tHW --batch local
python3 RunText2Workspace.py --mode limit_tHq_plus_tHW_HybridNew --batch local

# Limit tHq (tHqHad + tHqLep)
# ----------------------------------------------------
python3 RunText2Workspace.py --mode limit_tHq --batch local
python3 RunText2Workspace.py --mode limit_tHq_HybridNew --batch local
