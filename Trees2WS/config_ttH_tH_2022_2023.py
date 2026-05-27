# Input config file for running trees2ws

trees2wsCfg = {
  # Name of RooDirectory storing input tree
  'inputTreeDir':'DiphotonTree',

  # Variables to be added to dataframe: use wildcard * for common strings
  'mainVars':["CMS_hgg_mass", "weight", "weight_central", "dZ", "*Up","*Down", "fiducialGeometricFlag", "GenNBJet"],
  'dataVars':["CMS_hgg_mass","weight"], # Vars to be added for data
  'stxsVar':'',
  'diffVar':'',
  'notagVars':[], # Vars to add to NOTAG RooDataset
  'systematicsVars':["CMS_hgg_mass","weight","fiducialGeometricFlag", "GenNBJet"], # Variables to add to sytematic RooDataHists
  #'theoryWeightContainers':{'weight_LHEScale':9, 'weight_LHEPdf' : 101 },
  'theoryWeightContainers':{'weight_LHEScale':9},

  # List of systematics: use string YEAR for year-dependent systematics
  # 'systematics':["ScaleEB", "ScaleEE", "Smearing", "Material", "FNUF", "energyErrShift"],
  'systematics': ['ScaleEB','ScaleEE','Smearing','MuonScale','MuonResolution','Material','MET','JerSyst','JecSystTotal','FNUF','ElectronSmearing','ElectronScale'],

  # Analysis categories: python list of cats or use 'auto' to extract from input tree
  'cats':'auto'
}
