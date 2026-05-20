import os, sys
import glob
import re
import ROOT
import math
from collections import OrderedDict as od
from commonObjects import *

# Function for iterating over ROOT argsets in workspace
def rooiter(x):
  iter = x.iterator()
  ret = iter.Next()
  while ret:
    yield ret
    ret = iter.Next()

def extractWSFileNames( _inputWSDir ): 
  if not os.path.isdir(_inputWSDir):
    print(" --> [ERROR] No such directory (%s)")
    return False
  return glob.glob("%s/output_*.root"%_inputWSDir)

def extractListOfProcs( _listOfWSFileNames ):
  procs = []
  for fName in _listOfWSFileNames:
    p = fName.split("pythia8_")[1].split(".root")[0]
    if p not in procs: procs.append(p)
  return ",".join(procs)

def extractListOfCats( _listOfWSFileNames ):
  f0 = ROOT.TFile(_listOfWSFileNames[0]) 
  ws = f0.Get(inputWSName__)
  allData = ws.allData()
  cats = []
  for d in allData:
    # Skip systematics shifts
    if "sigma" in d.GetName(): continue
    # Skip NOTAG
    elif "NOTAG" in d.GetName(): continue
    # Add to list: name of the form {proc}_{mass}_{sqrts}_{cat}
    cats.append(d.GetName().split("_%s_"%sqrts__)[-1])
  ws.Delete()
  f0.Close()
  return ",".join(cats)

def extractListOfCatsFromData( _fileName ):
  f = ROOT.TFile(_fileName)
  ws = f.Get(inputWSName__)
  allData = ws.allData()
  cats = []
  for d in allData:
    c = d.GetName().split("Data_%s_"%sqrts__)[-1]
    cats.append(c)
  cats.sort()
  ws.Delete()
  f.Close()
  return ",".join(cats)

# [FLORIAN] Read categories directly from DiphotonTree in raw HiggsDNA output
# Used by Signal/Datacard steps before trees2ws has been run
def extractListOfCatsFromHiggsDNAAllData( _fileName ):
  f = ROOT.TFile(_fileName)
  trees = f.Get(inputHiggsDNAAllData__)
  cats = []
  for key in trees.GetListOfKeys():
    c = key.GetName().split("Data_%s_"%sqrts__)[-1]
    cats.append(c)
  cats.sort()
  trees.Delete()
  f.Close()
  return ",".join(cats)

# [FLORIAN] Build the list of process strings (ggh_in, ggh_out, tth_in, tth_out...)
# from a list of input subdirectories.
# Used by Signal/ and Datacard/ steps to know what processes to loop over.
# _listOfSubDirectories : list of ws subdirectory paths
# _variable             : differential variable string ('' for inclusive)
# _inoutSplitting       : bool, whether doInOutSplitting was used
def extractListOfProcsFromHiggsDNASignal(_listOfSubDirectories, _variable, _inoutSplitting):
  procs = []      # e.g. ggh_in, ggh_out, tth_in, tHqHad_in ...
  main_procs = [] # e.g. ggh, tth, tHqHad ...
  for dName in _listOfSubDirectories:
    dName = dName.split("/")[-1]
    p = conversionTable_[dName.split("_")[0]]
    if p not in main_procs:
      main_procs.append(p)
      if (_inoutSplitting) and (_variable == ''):
        # inclusive in/out splitting
        procs.append(p+'_in')
        procs.append(p+'_out')
      if (_inoutSplitting) and (_variable != ''):
        # differential splitting
        for i, currentTuple in enumerate(differentialProcTable_[_variable]):
          currentBin = currentTuple[1]
          procs.append(p+'_'+currentBin)
      if not (_inoutSplitting) and (_variable == ''):
        # fully inclusive, no splitting
        procs.append(p)
      if not (_inoutSplitting) and (_variable != ''):
        # differential, no in/out
        for i, currentTuple in enumerate(differentialProcTable_[_variable]):
          currentBin = "_".join(currentTuple[1].split("_")[:-1])
          procs.append(p+'_'+currentBin)
  return ",".join(procs)

def containsNOTAG( _listOfWSFileNames ):
  f0 = ROOT.TFile(_listOfWSFileNames[0]) 
  ws = f0.Get(inputWSName__)
  allData = ws.allData()
  for d in allData:
    if "NOTAG" in d.GetName(): return True
  return False

# Function to return signal production (and decay extension if required) from input file name
def signalFromFileName(_fileName):
  p, d = None, None
  if "ggZH" in _fileName:
    p = "ggzh"
    if "ZToLL" in _fileName: d = "_ZToLL"
    elif "ZToNuNu" in _fileName: d = "_ZToNuNu"
    else: d = "_ZToQQ"
  elif "GluGlu" in _fileName: p = "ggh"
  elif "VBF"    in _fileName: p = "vbf"
  elif "WH"     in _fileName: p = "wh"
  elif "ZH"     in _fileName: p = "zh"
  # [FLORIAN] VH added
  elif "VH"     in _fileName: p = "vh"
  elif "ttH"    in _fileName: p = "tth"
  # [RAHUL] tHqHad/tHqLep MUST come before generic THQ check
  # because "THQtoGG_had" and "THQtoGG_lep" both contain "THQ"
  elif "THQtoGG_had" in _fileName: p = "tHqHad"
  elif "THQtoGG_lep" in _fileName: p = "tHqLep"
  elif "THWtoGG"     in _fileName: p = "tHW"
  elif "THQ"    in _fileName: p = "thq"   # fallback for other THQ samples
  elif "THW"    in _fileName: p = "thw"   # fallback for other THW samples
  elif "bbH"    in _fileName: p = "bbh"
  else:
    print(" --> [ERROR]: cannot extract production mode from input file name. Please update commonTools.signalFromFileName")
    exit(1)
  return p,d

def massFromFileName(_fileName):
  m = 125 #default
  if "_M" in _fileName:
    m = _fileName.split("_M")[-1].split("_")[0]
  return m

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# procToDataMap: maps STXS/process string → dataset name used in workspace
# [FLORIAN] added VH, lowercase self-maps, in/out versions for ggh/vbf/vh/tth
# [RAHUL]   added tHqHad, tHqLep, tHW and their in/out versions
procToDataMap = od()
procToDataMap['GG2H']        = 'ggh'
procToDataMap['VBF']         = 'vbf'
procToDataMap['VH']          = 'vh'        # [FLORIAN]
# lowercase self-maps (used when productionMode string is already lowercase)
procToDataMap['ggh']         = 'ggh'       # [FLORIAN]
procToDataMap['vbf']         = 'vbf'       # [FLORIAN]
procToDataMap['vh']          = 'vh'        # [FLORIAN]
procToDataMap['tth']         = 'tth'       # [FLORIAN]
# in/out versions for fiducial XS measurement
procToDataMap['GG2H_in']     = 'ggh_in'    # [FLORIAN]
procToDataMap['GG2H_out']    = 'ggh_out'   # [FLORIAN]
procToDataMap['VBF_in']      = 'vbf_in'    # [FLORIAN]
procToDataMap['VBF_out']     = 'vbf_out'   # [FLORIAN]
procToDataMap['VH_in']       = 'vh_in'     # [FLORIAN]
procToDataMap['VH_out']      = 'vh_out'    # [FLORIAN]
# TTH: inclusive commented out, in/out versions added
# procToDataMap['TTH']       = 'tth'       # [FLORIAN] commented out
procToDataMap['TTH_in']      = 'tth_in'    # [FLORIAN]
procToDataMap['TTH_out']     = 'tth_out'   # [FLORIAN]
# tHqHad, tHqLep, tHW: your analysis-specific processes
procToDataMap['tHqHad']      = 'tHqHad'    # [RAHUL]
procToDataMap['tHqLep']      = 'tHqLep'    # [RAHUL]
procToDataMap['tHW']         = 'tHW'       # [RAHUL]
procToDataMap['tHqHad_in']   = 'tHqHad_in' # [RAHUL]
procToDataMap['tHqHad_out']  = 'tHqHad_out'# [RAHUL]
procToDataMap['tHqLep_in']   = 'tHqLep_in' # [RAHUL]
procToDataMap['tHqLep_out']  = 'tHqLep_out'# [RAHUL]
procToDataMap['tHW_in']      = 'tHW_in'    # [RAHUL]
procToDataMap['tHW_out']     = 'tHW_out'   # [RAHUL]
# Standard VH modes
procToDataMap['WH2HQQ']      = 'wh'
procToDataMap['ZH2HQQ']      = 'zh'
procToDataMap['QQ2HLNU']     = 'wh'
procToDataMap['QQ2HLL']      = 'zh'
procToDataMap['bbh']         = 'bbh'       # [FLORIAN] lowercase
procToDataMap['THQ']         = 'thq'
procToDataMap['THW']         = 'thw'
procToDataMap['GG2HQQ']      = 'ggzh'
procToDataMap['GG2HLL']      = 'ggzh'
procToDataMap['GG2HNUNU']    = 'ggzh'

def procToData( _proc ):
  k = _proc.split("_")[0]
  if k in procToDataMap: _proc = re.sub( k, procToDataMap[k], _proc )
  return _proc

def dataToProc( _d ):
  dataToProcMap = {v:k for k,v in procToDataMap.items()}
  if _d in dataToProcMap: return dataToProcMap[_d]
  else: return _d

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# procToDatacardNameMap: maps process string → name used in Combine datacard
# [FLORIAN] changed GG2H→ggh, VBF→vbf, TTH→tth (all lowercase now)
#           added in/out versions, added VH/vh
# [RAHUL]   added tHqHad, tHqLep, tHW and their in/out versions
procToDatacardNameMap = od()
procToDatacardNameMap['GG2H']        = "ggh"       # [FLORIAN] was "ggH"
procToDatacardNameMap['VBF']         = "vbf"       # [FLORIAN] was "qqH"
procToDatacardNameMap['ggh']         = "ggh"       # [FLORIAN]
procToDatacardNameMap['vbf']         = "vbf"       # [FLORIAN]
procToDatacardNameMap['tth']         = "tth"       # [FLORIAN]
procToDatacardNameMap['vh']          = "vh"        # [FLORIAN]
procToDatacardNameMap['GG2H_in']     = "ggh_in"    # [FLORIAN]
procToDatacardNameMap['VBF_out']     = "vbf_out"   # [FLORIAN]
procToDatacardNameMap['WH2HQQ']      = "WH_had"
procToDatacardNameMap["ZH2HQQ"]      = "ZH_had"
procToDatacardNameMap["QQ2HLNU"]     = "WH_lep"
procToDatacardNameMap["QQ2HLL"]      = "ZH_lep"
procToDatacardNameMap["TTH"]         = "tth"       # [FLORIAN] was "ttH"
procToDatacardNameMap["TTH_in"]      = "tth_in"    # [FLORIAN]
procToDatacardNameMap["TTH_out"]     = "tth_out"   # [FLORIAN]
# tHqHad, tHqLep, tHW: your analysis-specific processes
procToDatacardNameMap["tHqHad"]      = "tHqHad"    # [RAHUL]
procToDatacardNameMap["tHqLep"]      = "tHqLep"    # [RAHUL]
procToDatacardNameMap["tHW"]         = "tHW"       # [RAHUL]
procToDatacardNameMap["tHqHad_in"]   = "tHqHad_in" # [RAHUL]
procToDatacardNameMap["tHqHad_out"]  = "tHqHad_out"# [RAHUL]
procToDatacardNameMap["tHqLep_in"]   = "tHqLep_in" # [RAHUL]
procToDatacardNameMap["tHqLep_out"]  = "tHqLep_out"# [RAHUL]
procToDatacardNameMap["tHW_in"]      = "tHW_in"    # [RAHUL]
procToDatacardNameMap["tHW_out"]     = "tHW_out"   # [RAHUL]
procToDatacardNameMap["BBH"]         = "bbH"
procToDatacardNameMap["THQ"]         = "tHq"
procToDatacardNameMap["THW"]         = "tHW"
procToDatacardNameMap["TH"]          = "tHq"
procToDatacardNameMap["GG2HQQ"]      = "ggZH_had"
procToDatacardNameMap["GG2HLL"]      = "ggZH_ll"
procToDatacardNameMap["GG2HNUNU"]    = "ggZH_nunu"

def procToDatacardName( _proc ):
  k = _proc.split("_")[0]
  if k in procToDatacardNameMap: _proc = re.sub( k, procToDatacardNameMap[k], _proc )
  return _proc
