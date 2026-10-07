# Config file: options for signal fitting
signalScriptCfg = {

  # Setup
  'inputWSDir':'/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/workspaces/fiducial/2022postEE/ws_signal/', # dir storing flashgg workspaces
  'procs':'auto', # if auto: inferred automatically from filenames (requires names to be of from *pythia8_{PROC}.root)
  'cats':'auto', # if auto: inferred automatically from (0) workspace
  'ext':'tth_th_analysis_2022postEE_SoG', # output directory extension
  'analysis':'tth_th_analysis_fiducial', # To specify replacement dataset and XS*BR mapping (defined in ./tools/replacementMap.py and ./tools/XSBRMap.py respectively)
  'year':'2022postEE', # Use 'combined' if merging all years: not recommended
  'massPoints':'125', # You can now run with a single mass point if necessary

  #Photon shape systematics  
  'scales':'', # separate nuisance per year
  'scalesCorr':'FNUF,Material,ScaleEB,ScaleEE', # correlated across years
  #'scalesGlobal':'', # affect all processes equally, correlated across years
  # Removed nonLinearity for HIG-23-014 
  'scalesGlobal':'', # affect all processes equally, correlated across years
  'smears':'', # separate nuisance per year
  'smearsCorr':'Smearing', # correlated across years

  # Job submission options
  'batch':'local', # ['condor_lxplus','condor','SGE','IC','local']
  'queue':'microcentury', # use hep.q for IC
  'jobOpts':'request_memory = 12000'
}
