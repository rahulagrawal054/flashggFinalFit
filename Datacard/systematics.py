# =====================================================================
# SYSTEMATICS CONFIGURATION Run 3 (2022-2023) ttH / tH Analysis
# =====================================================================

# ---------------------------------------------------------------------
# THEORY SYSTEMATICS
# ---------------------------------------------------------------------

theory_systematics = [

    # Normalisation uncertainties: enter interpretations
    {'name':'BR_hgg','title':'BR_hgg','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"0.98/1.021"},

    {'name': 'QCDscale_ggH', 'title': 'QCDscale_ggH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_ggh.json'},
    {'name': 'QCDscale_qqH', 'title': 'QCDscale_qqH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_qqh.json'},
    #{'name': 'QCDscale_vH', 'title': 'QCDscale_vH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_vh.json'},
    {'name': 'QCDscale_ttH', 'title': 'QCDscale_ttH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_tth.json'},
    #{'name': 'QCDscale_tHq', 'title': 'QCDscale_tHq', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_thq.json'},
    {'name': 'QCDscale_tHW', 'title': 'QCDscale_tHW', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_thw.json'},
    #{'name': 'QCDscale_bbH', 'title': 'QCDscale_bbH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_bbh.json'},

    {'name':'pdf_Higgs_ggH','title':'pdf_Higgs_ggH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_ggh.json'},
    {'name':'pdf_Higgs_qqH','title':'pdf_Higgs_qqH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_qqh.json'},
    #{'name':'pdf_Higgs_vH','title':'pdf_Higgs_vH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_vh.json'},
    {'name':'pdf_Higgs_ttH','title':'pdf_Higgs_ttH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_tth.json'},
    #{'name':'pdf_Higgs_tHq','title':'pdf_Higgs_tHq','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_thq.json'},
    {'name':'pdf_Higgs_tHW','title':'pdf_Higgs_tHW','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_thw.json'},
    #{'name':'pdf_Higgs_bbH','title':'pdf_Higgs_bbH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_bbh.json'},
    
    {'name':'alphaS_ggH','title':'alphaS_ggH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_ggh.json'},
    {'name':'alphaS_qqH','title':'alphaS_qqH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_qqh.json'},
    #{'name':'alphaS_vH','title':'alphaS_VH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_vh.json'},
    {'name':'alphaS_ttH','title':'alphaS_ttH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_tth.json'},
    #{'name':'alphaS_tHq','title':'alphaS_tHq','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_thq.json'},
    {'name':'alphaS_tHW','title':'alphaS_tHW','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_thw.json'},
    #{'name':'alphaS_bbH','title':'alphaS_bbH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_bbh.json'},


    # AlphaS and Parton Shower (from your list)
     {'name':'weight_AlphaS','title':'CMS_hgg_AlphaS','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},
     {'name':'weight_PS_ISR','title':'CMS_hgg_PS_ISR','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},
     {'name':'weight_PS_FSR','title':'CMS_hgg_PS_FSR','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},

    # --- NEW: Higgs b/c Systematics (Correlated) ---
     {'name':'weight_Higgs_plus_b_syst','title':'CMS_hgg_Higgs_b_syst','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},
     {'name':'weight_Higgs_plus_c_syst','title':'CMS_hgg_Higgs_c_syst','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},
    
    # The scheme below is valid for v13, you need to explicitly check the nanoAOD documentation to validate your setup
     {'name':'weight_LHEScal_0','title':'CMS_hgg_scaleWeight_0','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},
     {'name':'weight_LHEScal_1','title':'CMS_hgg_scaleWeight_1','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},
     #{'name':'weight_LHEScal_2','title':'CMS_hgg_scaleWeight_2','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']}, #Unphysical
     {'name':'weight_LHEScal_3','title':'CMS_hgg_scaleWeight_3','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},
     {'name':'weight_LHEScal_4','title':'CMS_hgg_scaleWeight_4','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']}, #nominal weight
     {'name':'weight_LHEScal_5','title':'CMS_hgg_scaleWeight_5','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},
     #{'name':'weight_LHEScal_6','title':'CMS_hgg_scaleWeight_6','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']}, #Unphysical
     {'name':'weight_LHEScal_7','title':'CMS_hgg_scaleWeight_7','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},
     {'name':'weight_LHEScal_8','title':'CMS_hgg_scaleWeight_8','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']}

     # Add this loop *after* your theory_systematics list is defined
# (Or just add the entries to the list directly)
#
# Check your ntuple for the exact name (e.g., 'LHEPdf' or 'LHEPd')
# and the number of weights (e.g., 101 or 103)

# for i in range(1,101):
#    theory_systematics.append(
#        {'name':'weight_LHEPdf_%g'%i,
#         'title':'CMS_hgg_pdfWeight_%g'%i,
#         'type':'factory',
#         'prior':'lnN',
#         'correlateAcrossYears':1,
#         'tiers':['shape']
#        }
#    )
]

# ---------------------------------------------------------------------
# EXPERIMENTAL SYSTEMATICS
# ---------------------------------------------------------------------

experimental_systematics = [

   {'name':'lumi_13p6TeV_2022','title':'lumi_13p6TeV_2022','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"1.014"},
   {'name':'lumi_13p6TeV_2023','title':'lumi_13p6TeV_2023','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"1.02"},  # updated value

   {'name':'weight_Pileup','title':'CMS_hgg_PileupWeight','type':'factory','prior':'lnN','correlateAcrossYears':1},
   {'name':'weight_TriggerSF','title':'CMS_hgg_TriggerWeight','type':'factory','prior':'lnN','correlateAcrossYears':1},
   {'name':'weight_ElectronVetoSF','title':'CMS_hgg_ElectronVetoSF','type':'factory','prior':'lnN','correlateAcrossYears':1},
   {'name':'weight_PreselSF','title':'CMS_hgg_PreselSF','type':'factory','prior':'lnN','correlateAcrossYears':1},

  # Lepton Scale Factors
   {'name':'weight_atLeast1LeptonIdSF_ele_Reco','title':'CMS_hgg_ele_Reco','type':'factory','prior':'lnN','correlateAcrossYears':0},
   {'name':'weight_atLeast1LeptonIdSF_ele_wp90iso','title':'CMS_hgg_ele_wp90iso','type':'factory','prior':'lnN','correlateAcrossYears':0},
   {'name':'weight_atLeast1LeptonIdSF_mu_NUM_MediumID_DEN_TrackerMuons','title':'CMS_hgg_mu_MediumID','type':'factory','prior':'lnN','correlateAcrossYears':0},
   {'name':'weight_atLeast1LeptonIdSF_mu_NUM_TightPFIso_DEN_MediumID','title':'CMS_hgg_mu_TightPFIso','type':'factory','prior':'lnN','correlateAcrossYears':0},

  # # b-Tagging Scale Factors
   {'name':'weight_bTagSF_sys_cferr1','title':'CMS_hgg_bTag_cferr1','type':'factory','prior':'lnN','correlateAcrossYears':0},
   {'name':'weight_bTagSF_sys_cferr2','title':'CMS_hgg_bTag_cferr2','type':'factory','prior':'lnN','correlateAcrossYears':0},
   {'name':'weight_bTagSF_sys_hf','title':'CMS_hgg_bTag_hf','type':'factory','prior':'lnN','correlateAcrossYears':0},
   {'name':'weight_bTagSF_sys_hfstats1','title':'CMS_hgg_bTag_hfstats1','type':'factory','prior':'lnN','correlateAcrossYears':0},
   {'name':'weight_bTagSF_sys_hfstats2','title':'CMS_hgg_bTag_hfstats2','type':'factory','prior':'lnN','correlateAcrossYears':0},
   {'name':'weight_bTagSF_sys_jes','title':'CMS_hgg_bTag_jes','type':'factory','prior':'lnN','correlateAcrossYears':0},
   {'name':'weight_bTagSF_sys_lf','title':'CMS_hgg_bTag_lf','type':'factory','prior':'lnN','correlateAcrossYears':0},
   {'name':'weight_bTagSF_sys_lfstats1','title':'CMS_hgg_bTag_lfstats1','type':'factory','prior':'lnN','correlateAcrossYears':0},
   {'name':'weight_bTagSF_sys_lfstats2','title':'CMS_hgg_bTag_lfstats2','type':'factory','prior':'lnN','correlateAcrossYears':0},

   {'name':'ElectronScale', 'title': 'CMS_hgg_eleScale', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},
   {'name':'ElectronSmearing', 'title': 'CMS_hgg_eleSmear', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},
   {'name':'MuonScale', 'title': 'CMS_hgg_muScale', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},
   {'name':'MuonResolution', 'title': 'CMS_hgg_muReso', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},
   {'name':'JecSystTotal', 'title': 'CMS_scale_j', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
   {'name':'JerSyst', 'title': 'CMS_res_j', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
   {'name':'MET', 'title': 'CMS_hgg_MET_Unclustered', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0}

]

# ---------------------------------------------------------------------
# SIGNAL SHAPE SYSTEMATICS
# ---------------------------------------------------------------------

signal_shape_systematics = [
    {'name': 'ScaleEB', 'title': 'ScaleEB', 'type': 'signal_shape', 'mode': 'scales', 'mean': '0.0', 'sigma': '1.0'},
    {'name': 'ScaleEE', 'title': 'ScaleEE', 'type': 'signal_shape', 'mode': 'scales', 'mean': '0.0', 'sigma': '1.0'},
    {'name': 'Smearing', 'title': 'Smearing', 'type': 'signal_shape', 'mode': 'smears', 'mean': '0.0', 'sigma': '1.0'},
    {'name': 'Material', 'title': 'Material', 'type': 'signal_shape', 'mode': 'scalesCorr', 'mean': '0.0', 'sigma': '1.0'},
    {'name': 'FNUF', 'title': 'FNUF', 'type': 'signal_shape', 'mode': 'scalesCorr', 'mean': '0.0', 'sigma': '1.0'}
]

