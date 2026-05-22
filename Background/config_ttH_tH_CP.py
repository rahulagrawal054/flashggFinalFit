# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  'inputWS':'/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/workspaces/data/ws/allData.root',
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'tth_th_analysis_GMM_2', # extension to add to output directory
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'local', # [condor,condor_lxplus,SGE,IC,local]
  'queue':'microcentury' # for condor e.g. microcentury
  
}
