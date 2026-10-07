#!/bin/bash

Tree2WSDIR=/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS
CONFIG=$Tree2WSDIR/config_ttH_tH_2022_2023.py
BASE=/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs/

# GluGluH
python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root --inputMass 125 --productionMode ggh --year 2022preEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root --inputMass 125 --productionMode ggh --year 2022postEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root --inputMass 125 --productionMode ggh --year 2023preBPix --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root --inputMass 125 --productionMode ggh --year 2023postBPix --doInOutSplitting --doSystematics


# VBFH
python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode vbf --year 2022preEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode vbf --year 2022postEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode vbf --year 2023preBPix --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode vbf --year 2023postBPix --doInOutSplitting --doSystematics


# VH
python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode vh --year 2022preEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode vh --year 2022postEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode vh --year 2023preBPix --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode vh --year 2023postBPix --doInOutSplitting --doSystematics


# bbH
python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root --inputMass 125 --productionMode bbh --year 2022preEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root --inputMass 125 --productionMode bbh --year 2022postEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root --inputMass 125 --productionMode bbh --year 2023preBPix --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root --inputMass 125 --productionMode bbh --year 2023postBPix --doInOutSplitting --doSystematics


# tHqHad
python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tHqHad --year 2022preEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tHqHad --year 2022postEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tHqHad --year 2023preBPix --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tHqHad --year 2023postBPix --doInOutSplitting --doSystematics


# tHqLep
python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tHqLep --year 2022preEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tHqLep --year 2022postEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tHqLep --year 2023preBPix --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tHqLep --year 2023postBPix --doInOutSplitting --doSystematics


# ttH
python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tth --year 2022preEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tth --year 2022postEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tth --year 2023preBPix --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root --inputMass 125 --productionMode tth --year 2023postBPix --doInOutSplitting --doSystematics

#tHW
python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root --inputMass 125 --productionMode tHW --year 2022preEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root --inputMass 125 --productionMode tHW --year 2022postEE --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root --inputMass 125 --productionMode tHW --year 2023preBPix --doInOutSplitting --doSystematics

python3 $Tree2WSDIR/trees2ws.py --inputConfig $CONFIG --inputTreeFile $BASE/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root --inputMass 125 --productionMode tHW --year 2023postBPix --doInOutSplitting --doSystematics
