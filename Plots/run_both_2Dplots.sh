#!/bin/bash

set -e

PLOTDIR="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Plots"

STATSYST_SCAN="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/make2D/condor_output/higgsCombine_2Dscan_statsyst.MultiDimFit.mH125.08.root"
STATONLY_SCAN="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/make2D/condor_output/higgsCombine_2Dscan_statonly.MultiDimFit.mH125.08.root"

# Combine POI branch names and ranges from ROOT tree
XPARAM="r_tHq:-10,23"
YPARAM="r_ttH:-0.2,3.3"

echo "========================================"
echo " Running ROOT version (Stat+Syst)"
echo "========================================"

python3 ${PLOTDIR}/make2DPlot.py \
    --inputTreeFile ${STATSYST_SCAN} \
    --xparam "${XPARAM}" \
    --yparam "${YPARAM}" \
    --doShift --doBestFit --doSM \
    --ext "_statsyst"

#echo "========================================"
#echo " Running ROOT version (Stat Only)"
#echo "========================================"
#
#python3 ${PLOTDIR}/make2DPlot.py \
#    --inputTreeFile ${STATONLY_SCAN} \
#    --xparam "${XPARAM}" \
#    --yparam "${YPARAM}" \
#    --doShift --doBestFit --doSM \
#    --ext "_statOnly"
#
#echo "========================================"
#echo " Running matplotlib version (Stat+Syst)"
#echo "========================================"
#
#python3 ${PLOTDIR}/make2DPlot_tri.py \
#    --inputTreeFile ${STATSYST_SCAN} \
#    --xparam "${XPARAM}" \
#    --yparam "${YPARAM}" \
#    --doShift --doBestFit --doSM \
#    --ext "_statsyst"
#
#echo "========================================"
#echo " Running matplotlib version (Stat Only)"
#echo "========================================"
#
#python3 ${PLOTDIR}/make2DPlot_tri.py \
#    --inputTreeFile ${STATONLY_SCAN} \
#    --xparam "${XPARAM}" \
#    --yparam "${YPARAM}" \
#    --doShift --doBestFit --doSM \
#    --ext "_statOnly"
#
#echo "========================================"
#echo " Running combined Stat vs Stat+Syst plot"
#echo "========================================"
#
#python3 ${PLOTDIR}/make2DPlot_tri_both.py \
#    --scanStatSyst ${STATSYST_SCAN} \
#    --scanStatOnly ${STATONLY_SCAN} \
#    --xparam "${XPARAM}" \
#    --yparam "${YPARAM}" \
#    --doShift --doBestFit --doSM \
#    --ext "_stat_vs_syst"
#
#mkdir -p /eos/user/r/rkumarag/www/flashggFinalFit/fiducial/Combine/SumOfGaussaian/Final2DPlots
#
#cp Final2DPlots/*.{pdf,png,root} \
#/eos/user/r/rkumarag/www/flashggFinalFit/fiducial/Combine/SumOfGaussaian/Final2DPlots/ 2>/dev/null || true
#
#echo ""
#echo "Done."
#echo "Plots copied to:"
#echo "/eos/user/r/rkumarag/www/flashggFinalFit/fiducial/Combine/SumOfGaussaian/Final2DPlots"
~                                                                                                 
