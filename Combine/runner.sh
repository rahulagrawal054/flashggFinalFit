#!/bin/bash
set -e
trap 'echo "Error at line $LINENO"; exit 1' ERR

SLEEP_TIME=5

########################################
### 2D Scan
########################################

python3 RunText2Workspace.py --mode r_2D --batch local
sleep $SLEEP_TIME

python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_2D --dryRun
sleep $SLEEP_TIME

for i in {0..99}; do
  ./runFits_r_2D/condor_profile2D_statonly_fixedMH_r_tHq_vs_r_ttH.sh $i
  sleep $SLEEP_TIME
done

python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_2D
sleep $SLEEP_TIME

python3 ../Plots/make2DPlot.py \
  --inputTreeFile runFits_r_2D/profile2D_statonly_fixedMH_r_tHq_vs_r_ttH.root \
  --xparam "r_tHq:-5.0,20.0" \
  --yparam "r_ttH:-1.0,3.0" \
  --nPoints 1000 \
  --nBins 200 \
  --interpolation linear \
  --doBestFit \
  --doSM \
  --ext "2D_rscan"
sleep $SLEEP_TIME

########################################
### 1D Scan r_tHq
########################################

python3 RunText2Workspace.py --mode r_tHq_1D --batch local
sleep $SLEEP_TIME

python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D --dryRun
sleep $SLEEP_TIME

for i in {0..19}; do
  ./runFits_r_tHq_1D/condor_profile1D_statonly_fixedMH_r_tHq.sh $i
  sleep $SLEEP_TIME
done

python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D
sleep $SLEEP_TIME

python3 RunText2Workspace.py --mode r_tHq_1D_ttH_profiled --batch local
sleep $SLEEP_TIME

python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D_ttH_profiled --dryRun
sleep $SLEEP_TIME

for i in {0..19}; do
  ./runFits_r_tHq_1D_ttH_profiled/condor_profile1D_statonly_fixedMH_r_tHq.sh $i
  sleep $SLEEP_TIME
done

python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D_ttH_profiled
sleep $SLEEP_TIME

########################################
### 1D Scan r_ttH
########################################

python3 RunText2Workspace.py --mode r_ttH_1D --batch local
sleep $SLEEP_TIME

python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D --dryRun
sleep $SLEEP_TIME

for i in {0..19}; do
  ./runFits_r_ttH_1D/condor_profile1D_statonly_fixedMH_r_ttH.sh $i
  sleep $SLEEP_TIME
done

python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D 
sleep $SLEEP_TIME

python3 RunText2Workspace.py --mode r_ttH_1D_tHq_profiled --batch local
sleep $SLEEP_TIME

python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D_tHq_profiled --dryRun
sleep $SLEEP_TIME

for i in {0..19}; do
  ./runFits_r_ttH_1D_tHq_profiled/condor_profile1D_statonly_fixedMH_r_ttH.sh $i
  sleep $SLEEP_TIME
done

python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D_tHq_profiled
sleep $SLEEP_TIME

########################################
### Significance for ttH
########################################

python3 RunText2Workspace.py --mode Z_ttH --batch local
combine -M Significance ./Datacard_Z_ttH.root --rMin 0 --rMax 5 -t -1 --setParameters r_ttH=1,MH=125.38 --freezeParameters MH
sleep $SLEEP_TIME

####################################
### Significance and limit for tHq
####################################

python3 RunText2Workspace.py --mode Z_tHq --batch local 
combine -M Significance ./Datacard_Z_tHq.root --rMin 0 --rMax 25 -t -1 --setParameters r_tHq=1,MH=125.38 --freezeParameters MH
combine -M AsymptoticLimits Datacard_Z_tHq.root --run expected --rMin 0 --rMax 25 -t -1 --setParameters MH=125.38 --freezeParameters MH
sleep $SLEEP_TIME

##########################################################
### for comparison with analyses where tHW is part of tH
##########################################################

# ttH fixed
python3 RunText2Workspace.py --mode r_tHq_plus_tHW_1D --batch local
sleep $SLEEP_TIME

# # rm -rv runFits_r_tHq_1D
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_plus_tHW_1D --dryRun
sleep $SLEEP_TIME

for i in {0..19}; do
  ./runFits_r_tHq_plus_tHW_1D/condor_profile1D_statonly_fixedMH_r_tH.sh $i
  sleep $SLEEP_TIME
done

python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_plus_tHW_1D
sleep $SLEEP_TIME

# # ttH profiled
python3 RunText2Workspace.py --mode r_tHq_plus_tHW_1D_ttH_profiled --batch local
sleep $SLEEP_TIME

# # rm -rv runFits_r_tHq_1D_ttH_profiled
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_plus_tHW_1D_ttH_profiled --dryRun
sleep $SLEEP_TIME

for i in {0..19}; do
  ./runFits_r_tHq_plus_tHW_1D_ttH_profiled/condor_profile1D_statonly_fixedMH_r_tH.sh $i
  sleep $SLEEP_TIME
done

python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_plus_tHW_1D_ttH_profiled
sleep $SLEEP_TIME


python3 RunText2Workspace.py --mode Z_tHq_plus_tHW --batch local
sleep $SLEEP_TIME

combine -M Significance ./Datacard_Z_tHq_plus_tHW.root --rMin 0 --rMax 25 -t -1 --setParameters r_tH=1,MH=125.38 --freezeParameters MH
sleep $SLEEP_TIME

combine -M AsymptoticLimits Datacard_Z_tHq_plus_tHW.root --run expected --rMin 0 --rMax 25 -t -1 --setParameters MH=125.38 --freezeParameters MH # -v 3
sleep $SLEEP_TIME
