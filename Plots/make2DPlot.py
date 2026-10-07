import os
import sys
import json
from optparse import OptionParser
import ROOT
import numpy as np
from scipy.interpolate import griddata

# Scripts for plotting
from shanePalette import set_color_palette

print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HGG 2D PLOTTER RUN II ~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")

def leave():
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HGG 2D PLOTTER RUN II (END) ~~~~~~~~~~~~~~~~~~~~~~~~ ")
    exit(0)

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetLineStyleString(2, "4 10")

def get_options():
    parser = OptionParser()
    parser.add_option("--inputTreeFile", dest="inputTreeFile", default=None, help="Input ROOT tree")
    parser.add_option("--xparam", dest="xparam", default="r_tHq:-20,25", help="X-parameter:range")
    parser.add_option("--yparam", dest="yparam", default="r_ttH:-0.5,3.0", help="Y-parameter:range")
    parser.add_option("--nPoints", dest="nPoints", default=1000, type='int', help="N grid points")
    parser.add_option("--nBins", dest="nBins", default=200, type='int', help="N bins")
    parser.add_option("--interpolation", dest="interpolation", default='linear', help="Interpolation mode")
    parser.add_option("--translatePOIs", dest="translatePOIs", default=None, help="JSON to store poi translations")
    parser.add_option("--doShift", dest="doShift", default=False, action="store_true", help="Shift minimum to 0")
    parser.add_option("--doBestFit", dest="doBestFit", default=False, action="store_true", help="Do best fit point")
    parser.add_option("--doSM", dest="doSM", default=False, action="store_true", help="Do SM point")
    parser.add_option("--ext", dest="ext", default='', help="Extension for saving")
    parser.add_option("--placeLegend", dest="placeLegend", default='', help="Legend position")
    parser.add_option("--no-colour", dest="no_colour", default=False, action="store_true", help="Disable color palette")
    return parser.parse_args()

(opt, args) = get_options()

# Set color palette
if opt.no_colour:
    set_color_palette('boring')
else:
    set_color_palette('jonno_flip')

def Translate(name, ndict):
    return ndict[name] if name in ndict else name

def LoadTranslations(jsonfilename):
    with open(jsonfilename) as jsonfile:
        return json.load(jsonfile)

#translatePOIs = {} if opt.translatePOIs is None else LoadTranslations(opt.translatePOIs)
#Hard code here remove when you need
translatePOIs = {
    "r_ttH": "r_{t#bar{t}H+tHW}",
    "r_tHq": "r_{tHq}"
}
# Extract parameters and ranges
x, x_range = opt.xparam.split(":")[0], [float(p) for p in opt.xparam.split(":")[1].split(",")]
y, y_range = opt.yparam.split(":")[0], [float(p) for p in opt.yparam.split(":")[1].split(",")]

# Open tree and extract points and deltaNLL values
f_in = ROOT.TFile(opt.inputTreeFile)
t_in = f_in.Get("limit")

xvals, yvals, deltaNLL = [], [], []
for ev in t_in:
    xvals.append(getattr(ev, x))
    yvals.append(getattr(ev, y))
    deltaNLL.append(getattr(ev, "deltaNLL"))

# Convert to numpy arrays for interpolation
dnll = np.asarray(deltaNLL)
points = np.array([xvals, yvals]).transpose()

# Set up grid
grid_x, grid_y = np.mgrid[x_range[0]:x_range[1]:opt.nPoints*1j, y_range[0]:y_range[1]:opt.nPoints*1j]

# --------------------------------------------------------------------------
# FIX 1: single interpolation only (no nearest-neighbor fallback / no
# extrapolation). Points outside the convex hull of the scanned data come
# back as NaN -- that is correct and expected.
# --------------------------------------------------------------------------
grid_vals = griddata(points, dnll, (grid_x, grid_y), method=opt.interpolation)

# Now flatten the arrays so they can be looped over
grid_x = grid_x.flatten()
grid_y = grid_y.flatten()
grid_vals = grid_vals.flatten()

# --------------------------------------------------------------------------
# FIX 2: remove NaNs (points outside the convex hull) instead of filling
# them with nearest-neighbor extrapolation. NaN != NaN in numpy, so this
# keeps only the real, valid interpolated points.
# --------------------------------------------------------------------------
grid_x = grid_x[grid_vals == grid_vals]
grid_y = grid_y[grid_vals == grid_vals]
grid_vals = grid_vals[grid_vals == grid_vals]

# Safe now -- no NaNs left in grid_vals
min_val = np.min(grid_vals)

# Define Profile2D histogram
h2D = ROOT.TProfile2D("h", "h", opt.nBins, x_range[0], x_range[1], opt.nBins, y_range[0], y_range[1])

# Fill histogram (Always shift relative to min_val so 2*deltaNLL == 0 at best fit)
for i in range(len(grid_vals)):
    val = 2 * (grid_vals[i] - min_val) if opt.doShift else 2 * grid_vals[i]
    h2D.Fill(grid_x[i], grid_y[i], val)

# --------------------------------------------------------------------------
# FIX 3: re-enable masking of untouched bins (this was commented out in
# your script). Use GetBinEntries() rather than GetBinContent()==0 -- a
# TProfile2D tracks fill-count separately from content, so a genuine
# best-fit bin whose (shifted) value is exactly 0 is still correctly
# recognized as "real data" (entries > 0), not mistaken for "no data here".
# --------------------------------------------------------------------------
for ibin in range(1, h2D.GetNbinsX() + 1):
    for jbin in range(1, h2D.GetNbinsY() + 1):
        gbin = h2D.GetBin(ibin, jbin)
        if h2D.GetBinEntries(gbin) == 0:
            xc = h2D.GetXaxis().GetBinCenter(ibin)
            yc = h2D.GetYaxis().GetBinCenter(jbin)
            h2D.Fill(xc, yc, 999)

# Find global minimum for proper scaling (safe -- no NaNs left)
best_idx = np.argmin(grid_vals)

# Set up ROOT Canvas
canv = ROOT.TCanvas("canv", "canv", 600, 600)
canv.SetTickx()
canv.SetTicky()

if not opt.no_colour:
    canv.SetRightMargin(0.15)
canv.SetLeftMargin(0.115)
canv.SetBottomMargin(0.115)

# Calculate bin widths
xw = (x_range[1] - x_range[0]) / opt.nBins
yw = (y_range[1] - y_range[0]) / opt.nBins

# Set histogram properties
h2D.SetContour(999)
h2D.SetTitle("")
h2D.GetXaxis().SetTitle(Translate(x, translatePOIs))
h2D.GetXaxis().SetTitleSize(0.05)
h2D.GetYaxis().SetTitle(Translate(y, translatePOIs))
h2D.GetYaxis().SetTitleSize(0.05)
h2D.GetZaxis().SetTitle(f"q({Translate(x, translatePOIs)},{Translate(y, translatePOIs)})")
h2D.GetZaxis().SetTitleSize(0.05)
h2D.GetZaxis().SetTitleOffset(0.8)
h2D.SetMaximum(10)

# Build CI Contour lines
c68, c95 = h2D.Clone(), h2D.Clone()

# 68% CL (1-sigma) Contour
c68.SetContour(2)
c68.SetContourLevel(1, 2.30)
c68.SetLineWidth(3)
c68.SetLineColor(ROOT.kBlack)

# 95% CL (2-sigma) Contour
c95.SetContour(2)
c95.SetContourLevel(1, 5.99)
c95.SetLineWidth(3)
c95.SetLineStyle(2)
c95.SetLineColor(ROOT.kBlack)

# Draw histogram and contour overlays
if opt.no_colour:
    h2D.Draw("COL")
else:
    h2D.Draw("COLZ")
c68.Draw("cont3same")
c95.Draw("cont3same")

# Plot Standard Model (SM) Point
if opt.doSM:
    gSM = ROOT.TGraph()
    gSM.SetPoint(0, 1, 1)
    gSM.SetMarkerStyle(33)  # Diamond
    gSM.SetMarkerSize(2)
    gSM.SetMarkerColor(ROOT.kRed)
    gSM.Draw("P")

# Plot Best Fit Point (Thin Cross)
if opt.doBestFit:
    gBF = ROOT.TGraph()
    gBF.SetPoint(0, grid_x[best_idx], grid_y[best_idx])
    gBF.SetMarkerStyle(5)   # Thin '+' cross
    gBF.SetMarkerSize(1.5)
    gBF.SetMarkerColor(ROOT.kBlack)
    gBF.Draw("P")

# CMS Title & Labeling
lat = ROOT.TLatex()
lat.SetTextFont(42)
lat.SetLineWidth(2)
lat.SetTextAlign(11)
lat.SetNDC()
lat.SetTextSize(0.042)
lat.DrawLatex(0.115, 0.92, "#bf{CMS} #it{Preliminary}")
lat.DrawLatex(0.62, 0.92, "62.4 fb^{-1} (13.6#scale[0.75]{ }TeV)")

# Legend Configuration
if opt.placeLegend == "bottom_right":
    leg = ROOT.TLegend(0.55, 0.16, 0.8, 0.36)
else:
    leg = ROOT.TLegend(0.6, 0.67, 0.8, 0.87)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
if opt.doBestFit:
    leg.AddEntry(gBF, "Best fit", "P")
leg.AddEntry(c68, "68% CL", "L")
leg.AddEntry(c95, "95% CL", "L")
if opt.doSM:
    leg.AddEntry(gSM, "SM", "P")
leg.Draw()
canv.Update()

# Create output directory cleanly & save files
out_dir = "./Final2DPlots"
os.makedirs(out_dir, exist_ok=True)
canv.SaveAs(f"{out_dir}/scan2D_{x}_vs_{y}{opt.ext}.png")
canv.SaveAs(f"{out_dir}/scan2D_{x}_vs_{y}{opt.ext}.pdf")
canv.SaveAs(f"{out_dir}/scan2D_{x}_vs_{y}{opt.ext}.root")

leave()
