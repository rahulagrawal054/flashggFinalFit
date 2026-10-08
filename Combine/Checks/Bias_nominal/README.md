# Impacts

Impacts documentation to come here. 

# Bias studies

Here we provide a script to perform a simple bias study. 

## Inputs

The only pre-requisite is a workspace with a single category, 
and therefore a single multipdf (the object that controls the envelope method) 
and a single pdf index corresponding to the choice of functional form.

To create this, it's simple to use the existing combineCards functionality, for example:
```
combineCards.py Datacard.txt --ic cat_name > Datacard_cat_name.txt
```

This creates a .txt datacard with only categories matching the reg exp `cat_name` included. 
Be careful: you will probably have to manually delete some pdfindex lines at the bottom; 
the script does not know that these correspond to the analysis categories, 
and therefore will leave them all in (you only want the one corresponding to the category you are studying). 

Once that is done, you can run your usual `text2workspace` command to generate the `-d, --datacard` input for this script. 

## Usage

The script is split into three different stages:
 * `-t, --toys`:  throw and save a total of `-n,--nToys` toys for each of the candidate functions included in the envelope
 * `-f, --fits`:  fit each of those toys and extract the uncertainty
 * `-p, --plots`: plot the pull distribution of the resulting fits

You can then inspect the output plots and hope to see an approximately gaussian shape with zero mean and unit width.
Normally, provided that the absolute value of the mean is less than 0.14, this is considered satisfactory. 

The three steps can be run in one go, but it's probably safer to run them one-by-one. 
Here is an example:

```
./RunBiasStudy.py -d Datacard_mu_ggH_cat0.root -t 
./RunBiasStudy.py -d Datacard_mu_ggH_cat0.root -f -c "--cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --freezeParameters MH" 
./RunBiasStudy.py -d Datacard_mu_ggH_cat0.root -p --gaussianFit
```
The options for the second step are passed to combine; these are recommended to get the fit to converge. 
The additional option on the plotting is fairly self-explanatory; it adds a gaussian fit to the output plot.

## More options

There are various things one can tweak for these studies. 
Here is a list of the common options: 
 * `-n,--nToys`: the default number of toys is 1000 per function, but can be lowered or raised. 
 * `-e,--expectSignal`: the injected signal strength is 1 by default, but zero can also be checked, or higher values for searches. 
 * `-s,--seed`: the default value of -1 finds a random seed; you can fix this for reproducility if you prefer.
 * `--poi`: if your parameter of interest is called something other than `r`, say so here.
 * `--split`: default number of toys to be thrown or fits to be performed in one go. Set to 500 but may need to be lowered for memory reasons if you have a more complicated fit. 
 * `--selectFunction`: you can specify a string here to only select certain functions for these studies (e.g. `bern` to match all Bernstein polynomials, `exp1` to match just the first-order exponential).


## Two-POI nominal bias study

`RunBiasStudy_twoPOI.py` requires a single-category workspace whose
ModelConfig has both `r_ttH` and `r_tHq` as POIs, with one RooMultiPdf and
one pdfindex. Each truth point injects both signal strengths. Each fit
measures the selected POI while profiling the other POI and the background
pdfindex. Constrained nuisances are floated unless explicitly overridden
with `--combineOptions`. Toy generation uses `--toysNoSystematics`.

Run from this directory with a two-POI workspace. For example:

```bash
# Preview commands first. --grid 0,1 means (0,0), (0,1), (1,0), (1,1).
python3 RunBiasStudy_twoPOI.py -d workspace.root --toys --grid 0,1 -n 1000 -s 12345 --dryRun

# Generate toys once, then fit/plot each POI using the same toys and seed.
python3 RunBiasStudy_twoPOI.py -d workspace.root --toys --grid 0,1 -n 1000 -s 12345
python3 RunBiasStudy_twoPOI.py -d workspace.root --fits --plots --poi r_ttH --grid 0,1 -n 1000 -s 12345 --gaussianFit
python3 RunBiasStudy_twoPOI.py -d workspace.root --fits --plots --poi r_tHq --grid 0,1 -n 1000 -s 12345 --gaussianFit
```

Choose suitable fit ranges with `--rMinTtH`, `--rMaxTtH`, `--rMinTHq`, and
`--rMaxTHq`; defaults are [-5,15] and [-25,25], respectively. These defaults
are starting settings, not validated ranges for every category. For split
runs pass the same `--split` value at every stage; nToys must be divisible
by it. Each split uses seed + split index.

Outputs go to BiasToys/, BiasFits/, BiasPlots/, and BiasLogs/. Names include
both injected values and the seed; fit/plot names also include the selected
POI. Repeating the same settings replaces the corresponding outputs.
Commands stop on a nonzero subprocess exit. Dry runs print commands without
creating outputs, moving files, or plotting. Gaussian fit results are null
if disabled or unsuccessful; raw mean/RMS and accepted/failed toy counts
are recorded separately. A completed run still needs fit-quality review.


### Debugging JSON (schema version 2)

Each point retains the original summary keys and adds run/workspace/software
metadata, fit settings, exact command sidecars when available, log warning
counts, tree entry counts, missing results, rejection reasons, and per-triplet
POI values/quantiles/pulls. Toy IDs come from iToy when available; missing
fits are counted without inventing IDs. Boundary flags include best-fit and
interval endpoints within 1e-4 times the range width (minimum scale 1).
They are diagnostic flags and do not exclude a fit. Histogram underflow and
overflow and Gaussian-fit status/errors/chi2/ndf are also recorded.
Nonfinite numeric values are written as null, with rejection reasons.

Each executed command writes a `.command.json` next to its log, including
arguments, return code, timestamps, elapsed time, and host, even if the
command fails. For older fits without sidecars, command provenance is
unavailable; metadata explicitly identifies settings from the plot invocation.
A missing tree result is distinct from a saved triplet rejected by plotting.
