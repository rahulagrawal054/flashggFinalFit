# Fiducial 2022preEE: all available processes and reconstructed categories.
# Run each stage separately and inspect its outputs before the next stage.
# First stage:
# python3 -u RunSignalScripts.py --inputConfig config_2022preEE_fiducial_SoG.py --mode calcPhotonSyst
# SoG requires the fTest stage before signalFit.
# python3 -u RunSignalScripts.py --inputConfig config_2022preEE_fiducial_SoG.py --mode signalFit --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit --MHPolyOrder 0 --doPlots"
# Set up the CMSSW runtime and source ../setup.sh before running these commands.
# Beamspot reweighting remains enabled by default in signalFit.py.
# Its default data/MC widths (3.5/3.7 cm) must be validated for this era.
# Signal parameter ranges and optimizer handling live in tools/simultaneousFit.py,
# not in this configuration; inspect them before launching signalFit.

signalScriptCfg = {
    'inputWSDir': '/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/workspaces/fiducial/2022preEE/ws_signal/',
    'procs': 'auto',  # All input processes, including fiducial in/out components.
    'cats': 'auto',   # All reconstructed categories; discovery excludes NOTAG.
    'ext': 'fiducial_2022preEE_SoG',
    'analysis': 'tth_th_analysis_fiducial',  # Existing XS*BR and replacement maps.
    'year': '2022preEE',
    'massPoints': '125',  # Single mass point: use MHPolyOrder 0 when fitting.

    # Preserve the existing analysis prescription for photon systematics.
    # Corr nuisances share names across eras; responses differ by process/category.
    'scales': '',
    'scalesCorr': 'FNUF,Material,ScaleEB,ScaleEE',
    'scalesGlobal': '',  # No additional global/nonLinearity nuisance.
    'smears': '',
    'smearsCorr': 'Smearing',

    'batch': 'local',
    'queue': 'microcentury',  # Unused by the local backend.
    'jobOpts': '',           # No Condor resource directives for local execution.
}
