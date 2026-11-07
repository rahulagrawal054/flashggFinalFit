"""Cross-section and H→γγ branching-ratio mappings for the ttH/tH analysis.

Current fiducial configs use globalXSBRMap['tth_th_analysis_fiducial'].
Retained numerical prescriptions and ttH/tH variants match the previous map.
Cross-section factors are in pb; mode='hgg' supplies the branching ratio.
"""
from collections import OrderedDict as od
from commonTools import procToDatacardName

globalXSBRMap = od()

# ttH / tH Run3 CP analysis
# using 125.08 (CMS Run 1+2 4-lepton combination) values, obtained by linear interpolation from ad-interim recommmendations: https://arxiv.org/pdf/2402.09955
kt_diag = (2.0**0.5) / 2.0  # 0.7071...
tth_sm_xs = 0.5689
tth_cpodd_xs = tth_sm_xs * (0.2352 / 0.5582)

tHq_sm_xs = 0.08354
tHq_lep_frac = 0.3258
# Least-squares fit of inclusive tHq cross-section ratios (BSM/SM) from simulation points:
# (1,0)->1.0, (0,1)->0.09406/0.02127, (-1,0)->0.246/0.02127,
# (1/sqrt2,1/sqrt2)->0.03508/0.02127, (1/sqrt2,-1/sqrt2)->0.03462/0.02127,
# (0,-1)->0.09523/0.02127, (0,0)->0.07338/0.02127.
tHq_ratio_coeffs = (
    3.4499294781382264,
    -5.280065742366744,
    -0.02750352609308848,
    2.8347914135875216,
    0.06052256389225552,
    1.0016931531267788,
)


def tth_xs(kt, ktt):
    return tth_sm_xs * (kt**2) + tth_cpodd_xs * (ktt**2)


def tHq_ratio(kt, ktt):
    c0, c1, c2, c3, c4, c5 = tHq_ratio_coeffs
    return c0 + c1 * kt + c2 * ktt + c3 * (kt**2) + c4 * kt * ktt + c5 * (ktt**2)


def tHq_xs(kt, ktt):
    return tHq_sm_xs * tHq_ratio(kt, ktt)


def tHq_lep_xs(kt, ktt):
    return tHq_xs(kt, ktt) * tHq_lep_frac


def tHq_had_xs(kt, ktt):
    return tHq_xs(kt, ktt) * (1.0 - tHq_lep_frac)


tHW_sm_xs = 0.0172


def tHW_ratio(kt, ktt):
    # Relative to SM (kt=1, ktt=0) using the tHW polynomial from reweighting.
    return 2.62 * (kt**2) + 1.91 * (ktt**2) - 3.51 * kt + 1.89


def tHW_xs(kt, ktt):
    return tHW_sm_xs * tHW_ratio(kt, ktt)


def _add_incl_entries(base_map):
    rename = {
        "GG2H": "ggh_incl",
        "VBF": "vbf_incl",
        "VH": "vh_incl",
        "TTH": "tth_incl",
    }
    for key, cfg in list(base_map.items()):
        if key == "decay":
            continue
        if key.endswith("_incl") or key.endswith("_in") or key.endswith("_out"):
            continue
        incl_key = rename.get(key, f"{key}_incl")
        if incl_key in base_map:
            continue
        base_map[incl_key] = dict(cfg)

globalXSBRMap['tth_th_analysis'] = od()
globalXSBRMap['tth_th_analysis']['decay'] = {'mode':'hgg'}
globalXSBRMap['tth_th_analysis']['GG2H'] = {'mode':'constant','factor':52.18}
globalXSBRMap['tth_th_analysis']['VBF'] = {'mode':'constant','factor':4.075}
globalXSBRMap['tth_th_analysis']['VH'] = {'mode':'constant','factor':2.3958}
globalXSBRMap['tth_th_analysis']['TTH'] = {'mode':'constant','factor':tth_sm_xs}
globalXSBRMap['tth_th_analysis']['bbh'] = {'mode':'constant','factor':0.5258}
# the BSM cross sections follow σ = σ_SM * k^2 + σ_CPodd * ktilde^2
globalXSBRMap['tth_th_analysis']['tthCPodd'] = {'mode':'constant','factor':tth_cpodd_xs}
globalXSBRMap['tth_th_analysis']['tthKt0p7Ktt0p7'] = {'mode':'constant','factor':tth_sm_xs * (kt_diag**2) + tth_cpodd_xs * (kt_diag**2)}
globalXSBRMap['tth_th_analysis']['tthKt0p7Kttm0p7'] = {'mode':'constant','factor':tth_sm_xs * (kt_diag**2) + tth_cpodd_xs * (kt_diag**2)}
globalXSBRMap['tth_th_analysis']['tthKt0Kttm1'] = {'mode':'constant','factor':tth_cpodd_xs * (1.0**2)}
globalXSBRMap['tth_th_analysis']['tthKt0Ktt0'] = {'mode':'constant','factor':tth_sm_xs * (0.0**2) + tth_cpodd_xs * (0.0**2)}
globalXSBRMap['tth_th_analysis']['tthKt0p500Ktt0p000'] = {'mode':'constant','factor':tth_xs(0.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tthKt0p354Ktt0p354'] = {'mode':'constant','factor':tth_xs(0.354, 0.354)}
globalXSBRMap['tth_th_analysis']['tthKt0p000Ktt0p500'] = {'mode':'constant','factor':tth_xs(0.0, 0.5)}
globalXSBRMap['tth_th_analysis']['tthKtm0p500Ktt0p000'] = {'mode':'constant','factor':tth_xs(-0.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tthKt0p000Kttm0p500'] = {'mode':'constant','factor':tth_xs(0.0, -0.5)}
globalXSBRMap['tth_th_analysis']['tthKt0p354Kttm0p354'] = {'mode':'constant','factor':tth_xs(0.354, -0.354)}
globalXSBRMap['tth_th_analysis']['tthKt1p500Ktt0p000'] = {'mode':'constant','factor':tth_xs(1.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tthKt1p061Ktt1p061'] = {'mode':'constant','factor':tth_xs(1.061, 1.061)}
globalXSBRMap['tth_th_analysis']['tthKt0p000Ktt1p500'] = {'mode':'constant','factor':tth_xs(0.0, 1.5)}
globalXSBRMap['tth_th_analysis']['tthKtm1p500Ktt0p000'] = {'mode':'constant','factor':tth_xs(-1.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tthKt0p000Kttm1p500'] = {'mode':'constant','factor':tth_xs(0.0, -1.5)}
globalXSBRMap['tth_th_analysis']['tthKt1p061Kttm1p061'] = {'mode':'constant','factor':tth_xs(1.061, -1.061)}
# tHq: evaluate all coupling points from the same polynomial ratio model
globalXSBRMap['tth_th_analysis']['tHqLep'] = {'mode':'constant','factor': tHq_sm_xs * tHq_lep_frac}
globalXSBRMap['tth_th_analysis']['tHqHad'] = {'mode':'constant','factor': tHq_sm_xs * (1 - tHq_lep_frac)}
globalXSBRMap['tth_th_analysis']['tHqLepKtm1Ktt0'] = {'mode':'constant','factor': tHq_lep_xs(-1.0, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqHadKtm1Ktt0'] = {'mode':'constant','factor': tHq_had_xs(-1.0, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqLepCPodd'] = {'mode':'constant','factor': tHq_lep_xs(0.0, 1.0)}
globalXSBRMap['tth_th_analysis']['tHqHadCPodd'] = {'mode':'constant','factor': tHq_had_xs(0.0, 1.0)}
globalXSBRMap['tth_th_analysis']['tHqLepKt0p7Ktt0p7'] = {'mode':'constant','factor': tHq_lep_xs(kt_diag, kt_diag)}
globalXSBRMap['tth_th_analysis']['tHqHadKt0p7Ktt0p7'] = {'mode':'constant','factor': tHq_had_xs(kt_diag, kt_diag)}
globalXSBRMap['tth_th_analysis']['tHqLepKt0p7Kttm0p7'] = {'mode':'constant','factor': tHq_lep_xs(kt_diag, -kt_diag)}
globalXSBRMap['tth_th_analysis']['tHqHadKt0p7Kttm0p7'] = {'mode':'constant','factor': tHq_had_xs(kt_diag, -kt_diag)}
globalXSBRMap['tth_th_analysis']['tHqLepKt0Kttm1'] = {'mode':'constant','factor': tHq_lep_xs(0.0, -1.0)}
globalXSBRMap['tth_th_analysis']['tHqHadKt0Kttm1'] = {'mode':'constant','factor': tHq_had_xs(0.0, -1.0)}
globalXSBRMap['tth_th_analysis']['tHqLepKt0Ktt0'] = {'mode':'constant','factor': tHq_lep_xs(0.0, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqHadKt0Ktt0'] = {'mode':'constant','factor': tHq_had_xs(0.0, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqLepKt0p500Ktt0p000'] = {'mode':'constant','factor': tHq_lep_xs(0.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqHadKt0p500Ktt0p000'] = {'mode':'constant','factor': tHq_had_xs(0.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqLepKt0p354Ktt0p354'] = {'mode':'constant','factor': tHq_lep_xs(0.354, 0.354)}
globalXSBRMap['tth_th_analysis']['tHqHadKt0p354Ktt0p354'] = {'mode':'constant','factor': tHq_had_xs(0.354, 0.354)}
globalXSBRMap['tth_th_analysis']['tHqLepKt0p000Ktt0p500'] = {'mode':'constant','factor': tHq_lep_xs(0.0, 0.5)}
globalXSBRMap['tth_th_analysis']['tHqHadKt0p000Ktt0p500'] = {'mode':'constant','factor': tHq_had_xs(0.0, 0.5)}
globalXSBRMap['tth_th_analysis']['tHqLepKtm0p500Ktt0p000'] = {'mode':'constant','factor': tHq_lep_xs(-0.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqHadKtm0p500Ktt0p000'] = {'mode':'constant','factor': tHq_had_xs(-0.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqLepKt0p000Kttm0p500'] = {'mode':'constant','factor': tHq_lep_xs(0.0, -0.5)}
globalXSBRMap['tth_th_analysis']['tHqHadKt0p000Kttm0p500'] = {'mode':'constant','factor': tHq_had_xs(0.0, -0.5)}
globalXSBRMap['tth_th_analysis']['tHqLepKt0p354Kttm0p354'] = {'mode':'constant','factor': tHq_lep_xs(0.354, -0.354)}
globalXSBRMap['tth_th_analysis']['tHqHadKt0p354Kttm0p354'] = {'mode':'constant','factor': tHq_had_xs(0.354, -0.354)}
globalXSBRMap['tth_th_analysis']['tHqLepKt1p500Ktt0p000'] = {'mode':'constant','factor': tHq_lep_xs(1.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqHadKt1p500Ktt0p000'] = {'mode':'constant','factor': tHq_had_xs(1.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqLepKt1p061Ktt1p061'] = {'mode':'constant','factor': tHq_lep_xs(1.061, 1.061)}
globalXSBRMap['tth_th_analysis']['tHqHadKt1p061Ktt1p061'] = {'mode':'constant','factor': tHq_had_xs(1.061, 1.061)}
globalXSBRMap['tth_th_analysis']['tHqLepKt0p000Ktt1p500'] = {'mode':'constant','factor': tHq_lep_xs(0.0, 1.5)}
globalXSBRMap['tth_th_analysis']['tHqHadKt0p000Ktt1p500'] = {'mode':'constant','factor': tHq_had_xs(0.0, 1.5)}
globalXSBRMap['tth_th_analysis']['tHqLepKtm1p500Ktt0p000'] = {'mode':'constant','factor': tHq_lep_xs(-1.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqHadKtm1p500Ktt0p000'] = {'mode':'constant','factor': tHq_had_xs(-1.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHqLepKt0p000Kttm1p500'] = {'mode':'constant','factor': tHq_lep_xs(0.0, -1.5)}
globalXSBRMap['tth_th_analysis']['tHqHadKt0p000Kttm1p500'] = {'mode':'constant','factor': tHq_had_xs(0.0, -1.5)}
globalXSBRMap['tth_th_analysis']['tHqLepKt1p061Kttm1p061'] = {'mode':'constant','factor': tHq_lep_xs(1.061, -1.061)}
globalXSBRMap['tth_th_analysis']['tHqHadKt1p061Kttm1p061'] = {'mode':'constant','factor': tHq_had_xs(1.061, -1.061)}
# tHW: apply the BSM cross-section polynomial here
globalXSBRMap['tth_th_analysis']['tHW'] = {'mode':'constant','factor':tHW_sm_xs}
globalXSBRMap['tth_th_analysis']['tHWCPodd'] = {'mode':'constant','factor':tHW_xs(0.0, 1.0)}
globalXSBRMap['tth_th_analysis']['tHWKtm1Ktt0'] = {'mode':'constant','factor':tHW_xs(-1.0, 0.0)}
globalXSBRMap['tth_th_analysis']['tHWKt0p7Ktt0p7'] = {'mode':'constant','factor':tHW_xs(0.7, 0.7)}
globalXSBRMap['tth_th_analysis']['tHWKt0p7Kttm0p7'] = {'mode':'constant','factor':tHW_xs(0.7, -0.7)}
globalXSBRMap['tth_th_analysis']['tHWKt0Kttm1'] = {'mode':'constant','factor':tHW_xs(0.0, -1.0)}
globalXSBRMap['tth_th_analysis']['tHWKt0Ktt0'] = {'mode':'constant','factor':tHW_xs(0.0, 0.0)}
globalXSBRMap['tth_th_analysis']['tHWKt0p500Ktt0p000'] = {'mode':'constant','factor':tHW_xs(0.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHWKt0p354Ktt0p354'] = {'mode':'constant','factor':tHW_xs(0.354, 0.354)}
globalXSBRMap['tth_th_analysis']['tHWKt0p000Ktt0p500'] = {'mode':'constant','factor':tHW_xs(0.0, 0.5)}
globalXSBRMap['tth_th_analysis']['tHWKtm0p500Ktt0p000'] = {'mode':'constant','factor':tHW_xs(-0.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHWKt0p000Kttm0p500'] = {'mode':'constant','factor':tHW_xs(0.0, -0.5)}
globalXSBRMap['tth_th_analysis']['tHWKt0p354Kttm0p354'] = {'mode':'constant','factor':tHW_xs(0.354, -0.354)}
globalXSBRMap['tth_th_analysis']['tHWKt1p500Ktt0p000'] = {'mode':'constant','factor':tHW_xs(1.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHWKt1p061Ktt1p061'] = {'mode':'constant','factor':tHW_xs(1.061, 1.061)}
globalXSBRMap['tth_th_analysis']['tHWKt0p000Ktt1p500'] = {'mode':'constant','factor':tHW_xs(0.0, 1.5)}
globalXSBRMap['tth_th_analysis']['tHWKtm1p500Ktt0p000'] = {'mode':'constant','factor':tHW_xs(-1.5, 0.0)}
globalXSBRMap['tth_th_analysis']['tHWKt0p000Kttm1p500'] = {'mode':'constant','factor':tHW_xs(0.0, -1.5)}
globalXSBRMap['tth_th_analysis']['tHWKt1p061Kttm1p061'] = {'mode':'constant','factor':tHW_xs(1.061, -1.061)}

# same keys with _incl added here:
_add_incl_entries(globalXSBRMap['tth_th_analysis'])

# Alias for not decorrelated setup: reuse the same XSBR map
globalXSBRMap['tth_th_analysis_noDeco'] = globalXSBRMap['tth_th_analysis']

# Fiducial XS map (in/out splitting) built from ttH/tH inclusive map
def _build_inout_map(base_map):
    inout_map = od()
    inout_map["decay"] = base_map["decay"]
    for proc, cfg in base_map.items():
        if proc == "decay":
            continue
        if proc.endswith("_incl") or proc.endswith("_in") or proc.endswith("_out"):
            continue
        base_name = procToDatacardName(proc)
        fallback = {"VH": "vh", "VBF": "vbf", "GG2H": "ggh", "TTH": "tth"}
        base_name = fallback.get(proc, base_name)
        in_key = f"{base_name}_in"
        out_key = f"{base_name}_out"
        inout_map[in_key] = dict(cfg)
        inout_map[out_key] = dict(cfg)
    return inout_map

globalXSBRMap["tth_th_analysis_fiducial"] = _build_inout_map(
    globalXSBRMap["tth_th_analysis"]
)

# in one setup, we perform the fiducial analysis with BSM shapes but SM cross sections. 
# This is because the out-of-fiducial events are not scaled with the POI. 
# That can bias the measurement quite much when the cross sections assumed in the fit differ much from data 
# by now we work with SM Asimov data and use the SM cross sections also when testing different shape assumptions in the fit
def _apply_sm_rates_to_fiducial(fiducial_map, sm_map):
    sm_rates = {
        "tth": sm_map["TTH"]["factor"],
        "thw": sm_map["tHW"]["factor"],
        "thqlep": sm_map["tHqLep"]["factor"],
        "thqhad": sm_map["tHqHad"]["factor"],
    }
    updated = od()
    updated["decay"] = fiducial_map["decay"]
    for proc, cfg in fiducial_map.items():
        if proc == "decay":
            continue
        new_cfg = dict(cfg)
        proc_lower = proc.lower()
        if proc_lower.startswith("tth"):
            new_cfg["factor"] = sm_rates["tth"]
        elif proc_lower.startswith("thw"):
            new_cfg["factor"] = sm_rates["thw"]
        elif proc_lower.startswith("thqlep"):
            new_cfg["factor"] = sm_rates["thqlep"]
        elif proc_lower.startswith("thqhad"):
            new_cfg["factor"] = sm_rates["thqhad"]
        updated[proc] = new_cfg
    return updated

# SM-rate scan variant for fiducial fits.
globalXSBRMap["tth_th_analysis_fiducial_SM_rates"] = _apply_sm_rates_to_fiducial(
    globalXSBRMap["tth_th_analysis_fiducial"],
    globalXSBRMap["tth_th_analysis"],
)
globalXSBRMap["tth_th_analysis_fiducial_noDeco"] = globalXSBRMap["tth_th_analysis_fiducial"]

globalXSBRMap["tth_th_analysis_fiducial_noDeco_SM_rates"] = _apply_sm_rates_to_fiducial(
    globalXSBRMap["tth_th_analysis_fiducial_noDeco"],
    globalXSBRMap["tth_th_analysis"],
)

# Same 13.6 TeV process definitions; categorization does not change XS*BR.
globalXSBRMap['tth_th_analysis_hybrid_fiducial'] = globalXSBRMap['tth_th_analysis_fiducial']
