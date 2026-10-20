# Packaged DCB and SoG signals

Outputs are separated by model and era: `DCB/<era>/` and `SoG/<era>/`. Each contains 16 category ROOT files, each with `wsig_13TeV` and all 16 process PDFs, normalization functions and individual nominal datasets. This packaging does not refit or change the source signalFit workspaces, Gaussian counts or optimizer settings. Years and model families were not merged.

The existing packager omits the category-summed dataset for `bkg_had` to avoid the ROOT buffer limit; individual process datasets remain present. Other categories include their summed nominal dataset at mass 125.

`packaging_manifest.json` records inputs/output locations and completion. `workspace_validation.csv` records each process dataset, normalization and one PDF evaluation at MH=125.09, m=125.09, photon nuisances zero. These numerical settings were made only in the reopened READ workspaces in memory, not written back to disk. The saved MH value is not guaranteed to be 125.09; set the intended hypothesis downstream. `summary.json` gives the validation totals. Category logs are alongside their outputs; `packaging.log` tracks the overall run.

The completed fits still contain previously documented convergence/boundary and Gaussian-count-selection issues. Packaging and structural checks do not resolve those issues, validate full-range PDF positivity, nuisance responses, luminosity handling or Asimov closure. The user's visual review authorized packaging both existing model families.

## Validation results

All 128 category files were created and reopened; all 2,048 expected process PDFs, normalization functions and individual datasets are present. All tested central PDF values at m=MH=125.09 are finite and nonnegative. This is a single-point PDF test, not full shape validation.

There are 194 zero-normalization and 108 negative-normalization process models across both model families. The corresponding 97 zero and 54 negative process/category/era cases occur in each model family. `normalization_issues.csv` lists them. Zero-yield processes require an explicit downstream prescription; negative expected rates must be resolved before use as physical signal contributions in Combine. No clipping, omission, or normalization repair was performed during packaging.

| Model / era | Zero norm | Negative norm |
|---|---:|---:|
| DCB / 2022postEE | 19 | 7 |
| DCB / 2022preEE | 31 | 18 |
| DCB / 2023postBPix | 28 | 16 |
| DCB / 2023preBPix | 19 | 13 |
| SoG / 2022postEE | 19 | 7 |
| SoG / 2022preEE | 31 | 18 |
| SoG / 2023postBPix | 28 | 16 |
| SoG / 2023preBPix | 19 | 13 |

Eight representative zero/negative cases were checked against the original DCB source workspaces and match in normalization and signed dataset sum: see `normalization_provenance.json`. The combined counts and status reports are preserved alongside the output packages.
