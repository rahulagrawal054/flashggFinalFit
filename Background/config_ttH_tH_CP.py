# Background modelling for the ttH/tH CP analysis

backgroundScriptCfg = {
  
  # Setup
  'inputWS':'/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/workspaces/Data/allData.root',
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'tth_th_analysis', # extension to add to output directory
  'lumi':61.9, # integrated luminosity in fb^-1
  'sqrts':13.6, # collision energy in TeV
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'local', # [condor,condor_lxplus,SGE,IC,local]
  'queue':'microcentury' # for condor e.g. microcentury
  
}
