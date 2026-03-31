# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  #'inputWS':'/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/ws/allData.root',
  'inputWS':'/eos/user/r/rkumarag/OLD_OUTPUT/outputForFinalFits_03Nov2025/workspaces/Data/ws/allData.root', # location of 'allData.root' file
  'cats':'ttH_had_1', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'tth_th_analysis_ttH_had_1', # extension to add to output directory
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'local', # [condor,condor_lxplus,SGE,IC,local]
  'queue':'microcentury' # for condor e.g. microcentury
  
}
