# =====================================================================
# SYSTEMATICS CONFIGURATION Run 3 (2022-2023) ttH / tH Analysis
# =====================================================================

# ---------------------------------------------------------------------
# THEORY SYSTEMATICS
# ---------------------------------------------------------------------

theory_systematics = [
    # Normalisation uncertainties
    {'name': 'BR_hgg', 'title': 'BR_hgg', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': "0.98/1.021"},
    {'name': 'QCDscale_ggH', 'title': 'QCDscale_ggH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_ggh.json'},
    {'name': 'QCDscale_qqH', 'title': 'QCDscale_qqH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_qqh.json'},
    {'name': 'QCDscale_VH', 'title': 'QCDscale_VH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_vh.json'},
    {'name': 'QCDscale_ttH', 'title': 'QCDscale_ttH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_tth.json'},
    {'name': 'QCDscale_tHq', 'title': 'QCDscale_tHq', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_thq.json'},
    {'name': 'QCDscale_tHW', 'title': 'QCDscale_tHW', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_thw.json'},
    {'name': 'QCDscale_bbH', 'title': 'QCDscale_bbH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_bbh.json'},

    {'name': 'pdf_Higgs_ggH', 'title': 'pdf_Higgs_ggH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_ggh.json'},
    {'name': 'pdf_Higgs_qqH', 'title': 'pdf_Higgs_qqH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_qqh.json'},
    {'name': 'pdf_Higgs_VH', 'title': 'pdf_Higgs_VH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_vh.json'},
    {'name': 'pdf_Higgs_ttH', 'title': 'pdf_Higgs_ttH', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_tth.json'},
    {'name': 'pdf_Higgs_tHq', 'title': 'pdf_Higgs_tHq', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_thq.json'},
    {'name': 'pdf_Higgs_tHW', 'title': 'pdf_Higgs_tHW', 'type': 'constant', 'prior': 'lnN', 'correlateAcrossYears': 1, 'value': 'theory_uncertainties/thu_thw.json'},

    # Shape (scale weight) uncertainties
    #{'name': 'weight_LHEScal_0', 'title': 'CMS_hgg_scaleWeight_0', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']},
    #{'name': 'weight_LHEScal_1', 'title': 'CMS_hgg_scaleWeight_1', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']},
    #{'name': 'weight_LHEScal_2', 'title': 'CMS_hgg_scaleWeight_2', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']},  # Unphysical
    #{'name': 'weight_LHEScal_3', 'title': 'CMS_hgg_scaleWeight_3', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']},
    #{'name': 'weight_LHEScal_4', 'title': 'CMS_hgg_scaleWeight_4', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']},  # Nominal
    #{'name': 'weight_LHEScal_5', 'title': 'CMS_hgg_scaleWeight_5', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']},
    #{'name': 'weight_LHEScal_6', 'title': 'CMS_hgg_scaleWeight_6', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']},  # Unphysical
    #{'name': 'weight_LHEScal_7', 'title': 'CMS_hgg_scaleWeight_7', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']},
    #{'name': 'weight_LHEScal_8', 'title': 'CMS_hgg_scaleWeight_8', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']},

    {'name': 'weight_AlphaS', 'title': 'CMS_hgg_AlphaS', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']},
    {'name': 'weight_PS_ISR', 'title': 'CMS_hgg_PS_ISR', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']},
    {'name': 'weight_PS_FSR', 'title': 'CMS_hgg_PS_FSR', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1, 'tiers': ['shape']}
]

# ---------------------------------------------------------------------
# EXPERIMENTAL SYSTEMATICS
# ---------------------------------------------------------------------

experimental_systematics = [

                # Updated luminosity partial-correlation scheme: 13/5/21 (recommended simplified nuisances)
                #{'name':'lumi_13TeV_Uncorrelated','title':'lumi_13TeV_Uncorrelated','type':'constant','prior':'lnN','correlateAcrossYears':0,'value':{'2016':'1.010','2017':'1.020','2018':'1.015'}},
                #{'name':'lumi_13TeV_Correlated','title':'lumi_13TeV_Correlated','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'1.006','2017':'1.009','2018':'1.020'}},
                #{'name':'lumi_13TeV_Correlated_1718','title':'lumi_13TeV_Correlated_1718','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'-','2017':'1.006','2018':'1.002'}},
                {'name':'lumi_13p6TeV_2022','title':'lumi_13p6TeV_2022','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"1.014"},
                {'name':'lumi_13p6TeV_2023','title':'lumi_13p6TeV_2023','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"1.02"},  # updated value
                # {'name':'weight_Pileup','title':'CMS_hgg_PileupWeight','type':'factory','prior':'lnN','correlateAcrossYears':1},
                # {'name':'weight_TriggerSF','title':'CMS_hgg_TriggerWeight','type':'factory','prior':'lnN','correlateAcrossYears':1},
                # {'name':'weight_ElectronVetoSF','title':'CMS_hgg_ElectronVetoSF','type':'factory','prior':'lnN','correlateAcrossYears':1},
                # {'name':'weight_PreselSF','title':'CMS_hgg_PreselSF','type':'factory','prior':'lnN','correlateAcrossYears':1},
                # {'name':'weight_SF_photon_ID','title':'CMS_hgg_phoIdMva','type':'factory','prior':'lnN','correlateAcrossYears':1},
                #{'name':'LooseMvaSF','title':'CMS_hgg_LooseMvaSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'PreselSF','title':'CMS_hgg_PreselSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'electronVetoSF','title':'CMS_hgg_electronVetoSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'TriggerWeight','title':'CMS_hgg_TriggerWeight','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'MuonIDWeight','title':'CMS_hgg_MuonID','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'MuonIsoWeight','title':'CMS_hgg_MuonIso','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'ElectronIDWeight','title':'CMS_hgg_ElectronID','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'ElectronRecoWeight','title':'CMS_hgg_ElectronReco','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'JetBTagCutWeight','title':'CMS_hgg_BTagCut','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'JetBTagReshapeWeight','title':'CMS_hgg_BTagReshape','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'prefireWeight','title':'CMS_hgg_prefire','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'energyErrShift','title':'CMS_hgg_SigmaEOverEShift','type':'factory','prior':'lnN','correlateAcrossYears':1},
                #{'name':'SigmaEOverEShift','title':'CMS_hgg_SigmaEOverEShift','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'MvaShift','title':'CMS_hgg_phoIdMva','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'PUJIDShift','title':'CMS_hgg_PUJIDShift','type':'factory','prior':'lnN','correlateAcrossYears':0},
                # New partial correlation scheme for JECs (do not use in addition to nominal 'JEC')
                #{'name':'JECAbsolute','title':'CMS_scale_j_Absolute','type':'factory','prior':'lnN','correlateAcrossYears':1},
                #{'name':'JECFlavorQCD','title':'CMS_scale_j_FlavorQCD','type':'factory','prior':'lnN','correlateAcrossYears':1},
                #{'name':'JECBBEC1','title':'CMS_scale_j_BBEC1','type':'factory','prior':'lnN','correlateAcrossYears':1},
                #{'name':'JECHF','title':'CMS_scale_j_HF','type':'factory','prior':'lnN','correlateAcrossYears':1},
                #{'name':'JECEC2','title':'CMS_scale_j_EC2','type':'factory','prior':'lnN','correlateAcrossYears':1},
                #{'name':'JECRelativeBal','title':'CMS_scale_j_RelativeBal','type':'factory','prior':'lnN','correlateAcrossYears':1},
                #{'name':'JECAbsoluteYEAR','title':'CMS_scale_j_Absolute_y','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'JECBBEC1YEAR','title':'CMS_scale_j_BBEC1_y','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'JECHFYEAR','title':'CMS_scale_j_HF_y','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'JECEC2YEAR','title':'CMS_scale_j_EC2_y','type':'factory','prior':'lnN','correlateAcrossYears':0},
                #{'name':'JECRelativeSampleYEAR','title':'CMS_scale_j_RelativeSample_y','type':'factory','prior':'lnN','correlateAcrossYears':0},

    {'name': 'weight_Pileup', 'title': 'CMS_hgg_PileupWeight', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},
    {'name': 'weight_TriggerSF', 'title': 'CMS_hgg_TriggerWeight', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},
    {'name': 'weight_ElectronVetoSF', 'title': 'CMS_hgg_ElectronVetoSF', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},
    {'name': 'weight_PreselSF', 'title': 'CMS_hgg_PreselSF', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},

    {'name': 'weight_atLeast1LeptonIdSF_ele_Reco', 'title': 'CMS_hgg_LeptonSF_eleReco', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    {'name': 'weight_atLeast1LeptonIdSF_ele_wp90iso', 'title': 'CMS_hgg_LeptonSF_eleWP90', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    {'name': 'weight_atLeast1LeptonIdSF_mu_NUM_MediumID_DEN_TrackerMuons', 'title': 'CMS_hgg_LeptonSF_muMediumID', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    {'name': 'weight_atLeast1LeptonIdSF_mu_NUM_TightPFIso_DEN_MediumID', 'title': 'CMS_hgg_LeptonSF_muTightIso', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},

    #{'name': 'weight_bTagSF_sys_cferr1', 'title': 'CMS_hgg_bTag_cferr1', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    #{'name': 'weight_bTagSF_sys_cferr2', 'title': 'CMS_hgg_bTag_cferr2', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    #{'name': 'weight_bTagSF_sys_hfstats1', 'title': 'CMS_hgg_bTag_hfstats1', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    #{'name': 'weight_bTagSF_sys_hfstats2', 'title': 'CMS_hgg_bTag_hfstats2', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    #{'name': 'weight_bTagSF_sys_lfstats1', 'title': 'CMS_hgg_bTag_lfstats1', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    #{'name': 'weight_bTagSF_sys_lfstats2', 'title': 'CMS_hgg_bTag_lfstats2', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    #{'name': 'weight_bTagSF_sys_hf', 'title': 'CMS_hgg_bTag_hf', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    #{'name': 'weight_bTagSF_sys_lf', 'title': 'CMS_hgg_bTag_lf', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    #{'name': 'weight_bTagSF_sys_jes', 'title': 'CMS_hgg_bTag_jes', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},

    {'name': 'ElectronScale', 'title': 'CMS_hgg_eleScale', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},
    {'name': 'ElectronSmearing', 'title': 'CMS_hgg_eleSmear', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},
    {'name': 'MuonScale', 'title': 'CMS_hgg_muScale', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},
    {'name': 'MuonResolution', 'title': 'CMS_hgg_muReso', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 1},

    {'name': 'JecSystTotal', 'title': 'CMS_scale_j', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    {'name': 'JerSyst', 'title': 'CMS_res_j', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0},
    {'name': 'MET', 'title': 'CMS_hgg_MET_Unclustered', 'type': 'factory', 'prior': 'lnN', 'correlateAcrossYears': 0}
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

