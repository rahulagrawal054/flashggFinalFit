import os

# Paths and directory
cmsswbase__ = os.environ['CMSSW_BASE']
# [FLORIAN] Allow ANALYSIS_PATH env variable so you can run from anywhere,
# not just inside CMSSW directory structure
if 'ANALYSIS_PATH' in os.environ:
    cwd__ = os.environ['ANALYSIS_PATH']
else:
    cwd__ = os.environ['CMSSW_BASE']+"/src/flashggFinalFit"
swd__ = "%s/Signal"%cwd__
bwd__ = "%s/Background"%cwd__
dwd__ = "%s/Datacard"%cwd__
fwd__ = "%s/Combine"%cwd__
pwd__ = "%s/Plots"%cwd__
twd__ = "%s/Trees2WS"%cwd__

# Centre of mass energy string
sqrts__ = "13TeV"

# Luminosity map in fb^-1
# [FLORIAN] corrected 2022 values + added 2023 entries
# Reference: https://twiki.cern.ch/twiki/bin/view/CMS/PdmVRun3Analysis#DATA_AN2
lumiMap = {
    '2016'        : 36.33,
    '2017'        : 41.48,
    '2018'        : 59.83,
    'combined'    : 137.65,
    'merged'      : 137.65,
    '2022preEE'   : 7.98,    # [FLORIAN] was 8.00
    '2022postEE'  : 26.67,   # [FLORIAN] was 26.70
    '2022'        : 34.65,   # [FLORIAN] combined 2022
    '2023preBPix' : 18.063,  # [FLORIAN]
    '2023postBPix': 9.693,   # [FLORIAN]
    '2023'        : 27.756   # [FLORIAN] combined 2023
}
# If using ReReco samples then switch to lumiMap below (missing data in 2018 EGamma data set)
#lumiMap = {'2016':36.33, '2017':41.48, '2018':59.35, 'combined':137.17, 'merged':137.17}
lumiScaleFactor = 1000. # Converting from pb to fb

# Constants
BR_W_lnu = 3.*10.86*0.01
BR_Z_ll = 3*3.3658*0.01
BR_Z_nunu = 20.00*0.01
BR_Z_qq = 69.91*0.01
BR_W_qq = 67.41*0.01

# List of years
# [FLORIAN] added 2023 eras
years_to_process = ['2016','2017','2018','2022preEE','2022postEE','2023preBPix','2023postBPix']

# Production modes and decay channel: for extracting XS from combine
productionModes = ['ggH','qqH','ttH','tHq','tHW','ggZH','WH','ZH','bbH']
decayMode = 'hgg'

# flashgg/HiggsDNA input WS objects
inputWSName__          = "tagsDumper/cms_hgg_13TeV"
inputHiggsDNAAllData__ = "DiphotonTree"   # [FLORIAN] for reading raw HiggsDNA output
inputNuisanceExtMap    = {'scales':'','scalesCorr':'','smears':'','smearsCorr':''}  # [FLORIAN] added smearsCorr

# Signal output WS objects
outputWSName__          = "wsig"
outputWSObjectTitle__   = "hggpdfsmrel"
outputWSNuisanceTitle__ = "CMS_hgg_nuisance"
#outputNuisanceExtMap = {'scales':'%sscale'%sqrts__,'scalesCorr':'%sscaleCorr'%sqrts__,'smears':'%ssmear'%sqrts__,'smearsCorr':'%ssmearCorr'%sqrts__,'scalesGlobal':'%sscale'%sqrts__}
outputNuisanceExtMap = {'scales':'','scalesCorr':'','smears':'','smearsCorr':'','scalesGlobal':''}  # [FLORIAN] added smearsCorr

# Bkg output WS objects
bkgWSName__ = "multipdf"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# [FLORIAN] Input mass points
input_masses = [120, 125, 130]

# [FLORIAN] Production modes with their process string equivalents
# (also adding 2G naming conventions used in newer samples)
production_modes = [
    ("ggh",    "GluGluHtoGG"),
    ("ggh",    "GluGluHto2G"),
    ("vbf",    "VBFHtoGG"),
    ("vbf",    "VBFHto2G"),
    ("vh",     "VHtoGG"),
    ("vh",     "VHto2G"),
    ("tth",    "ttHtoGG"),
    ("tth",    "ttHto2G"),
]

# [FLORIAN] Era definitions
TwentyTwentyTwoEras   = ["preEE", "postEE"]
TwentyTwentyThreeEras = ["preBPix", "postBPix"]
allErasMap = {
    '2022': TwentyTwentyTwoEras,
    '2023': TwentyTwentyThreeEras
}

# [FLORIAN] Conversion table: process string → production mode key
# Used by extractListOfProcsFromHiggsDNASignal() in commonTools.py
# [RAHUL] Added tHqHad, tHqLep, tHW entries for your analysis
conversionTable_ = {
    "GluGluHtoGG" : "ggh",
    "GluGluHto2G" : "ggh",
    "ttHtoGG"     : "tth",
    "ttHto2G"     : "tth",
    "VBFHtoGG"    : "vbf",
    "VBFHto2G"    : "vbf",
    "VHtoGG"      : "vh",
    "VHto2G"      : "vh",
    "tHqHad"      : "tHqHad",   # [RAHUL]
    "tHqLep"      : "tHqLep",   # [RAHUL]
    "tHW"         : "tHW",      # [RAHUL]
}

# [FLORIAN] Jet-related variables — these get CMS_scale_j and CMS_res_j
# uncertainties added automatically in the Datacard step
jetVariables = [
    "Njets2p5",
    "ptJ0",
    "YJ0",
    "AbsPhiHJ0",
    "AbsYHJ0"
]

# [FLORIAN] Differential measurement bin definitions
# Each entry: (bin_number, bin_name_string)
# bin_number used internally, bin_name_string used in workspace/datacard naming
# Not needed for your inclusive ttH/tH analysis but kept for completeness
differentialProcTable_ = {
    "PTH": [
        (10, "PTH_0p0_15p0_in"),
        (11, "PTH_15p0_30p0_in"),
        (12, "PTH_30p0_45p0_in"),
        (13, "PTH_45p0_80p0_in"),
        (14, "PTH_80p0_120p0_in"),
        (15, "PTH_120p0_200p0_in"),
        (16, "PTH_200p0_350p0_in"),
        (17, "PTH_350p0_10000p0_in"),
        (18, "PTH_0p0_10000p0_out")
    ],
    "rapidity": [
        (20, "YH_0p0_0p15_in"),
        (21, "YH_0p15_0p3_in"),
        (22, "YH_0p3_0p6_in"),
        (23, "YH_0p6_0p9_in"),
        (24, "YH_0p9_2p5_in"),
        (25, "YH_0p0_2p5_out")
    ],
    "Njets2p5": [
        (30, "NJ_0p0_1p0_in"),
        (31, "NJ_1p0_2p0_in"),
        (32, "NJ_2p0_3p0_in"),
        (33, "NJ_3p0_100p0_in"),
        (34, "NJ_0p0_100p0_out")
    ],
    "ptJ0": [
        (40, "PTJ0_0p0_30p0_in"),
        (41, "PTJ0_30p0_75p0_in"),
        (42, "PTJ0_75p0_120p0_in"),
        (43, "PTJ0_120p0_200p0_in"),
        (44, "PTJ0_200p0_10000p0_in"),
        (45, "PTJ0_0p0_10000p0_out")
    ],
    "YJ0": [
        (50, "YJ0_0p0_0p5_in"),
        (51, "YJ0_0p5_1p2_in"),
        (52, "YJ0_1p2_2p0_in"),
        (53, "YJ0_2p0_2p5_in"),
        (54, "YJ0_NJ0_in"),
        (55, "YJ0_0p0_2p5_out")
    ],
    "AbsPhiHJ0": [
        (60, "AbsPhiHJ0_0p0_2p6_in"),
        (61, "AbsPhiHJ0_2p6_2p9_in"),
        (62, "AbsPhiHJ0_2p9_3p03_in"),
        (63, "AbsPhiHJ0_3p03_3p1415926_in"),
        (64, "AbsPhiHJ0_NJ_in"),
        (65, "AbsPhiHJ0_0p0_Pi_out")
    ],
    "AbsYHJ0": [
        (70, "AbsYHJ0_0p0_0p6_in"),
        (71, "AbsYHJ0_0p6_1p2_in"),
        (72, "AbsYHJ0_1p2_1p9_in"),
        (73, "AbsYHJ0_1p9_100p0_in"),
        (74, "AbsYHJ0_NJ0_in"),
        (75, "AbsYHJ0_0p0_100p0_out")
    ]
}

# [FLORIAN] BMW = Best Medium Worst — analysis categories by diphoton BDT score
BMW = ['cat0', 'cat1', 'cat2']

# [FLORIAN] Helper function to build combine parameter strings for differential measurements
def CreateVariableParameters(gen_variable, reco_variable, bins, year, BMW):
    paramStr        = [f"r_{gen_variable}_{bin}=1"                                    for bin in bins]
    paramStrNoOne   = [f"r_{gen_variable}_{bin}"                                       for bin in bins]
    catsStr         = [f"RECO_{reco_variable}_{bin}"                                   for bin in bins]
    catsStrWithBMW  = [f"RECO_{reco_variable}_{bin}_{bmw}"                             for bin in bins for bmw in BMW]
    pdfIndeces      = [f"pdfindex_RECO_{reco_variable}_{bin}_{bmw}_{year}_{sqrts__}"   for bin in bins for bmw in BMW]
    return {
        "paramStr"      : paramStr,
        "paramStrNoOne" : paramStrNoOne,
        "catsStr"       : catsStr,
        "catsStrWithBMW": catsStrWithBMW,
        "pdfIndeces"    : pdfIndeces,
    }

# [FLORIAN] Pre-built combine variable dictionaries for each differential observable
combineVariableDict = {
    "PTH"     : CreateVariableParameters("PTH",  "PTH",         ["0p0_15p0","15p0_30p0","30p0_45p0","45p0_80p0","80p0_120p0","120p0_200p0","200p0_350p0","350p0_10000p0"], "2022", BMW),
    "rapidity": CreateVariableParameters("YH",   "rapidity",    ["0p0_0p15","0p15_0p3","0p3_0p6","0p6_0p9","0p9_2p5"],                                                    "2022", BMW),
    "Njets2p5": CreateVariableParameters("NJ",   "Njets2p5",    ["0p0_1p0","1p0_2p0","2p0_3p0","3p0_100p0"],                                                              "2022", BMW),
    "ptJ0"    : CreateVariableParameters("PTJ0", "first_jet_pt",["0p0_30p0","30p0_75p0","75p0_120p0","120p0_200p0","200p0_10000p0"],                                       "2022", BMW),
}
