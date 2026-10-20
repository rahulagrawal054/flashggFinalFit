# Separate DCB and SoG launchers

Run from Signal, one command at a time. All commands, flags and outputs are explained in [Analysis_README.md](../Analysis_README.md).

## DCB + Gaussian

```bash
bash runner/DCB/run_DCB_2022preEE.sh
bash runner/DCB/run_DCB_2022postEE.sh
bash runner/DCB/run_DCB_2023preBPix.sh
bash runner/DCB/run_DCB_2023postBPix.sh
```

## Sum of Gaussians

```bash
bash runner/SoG/run_SoG_2022preEE.sh
bash runner/SoG/run_SoG_2022postEE.sh
bash runner/SoG/run_SoG_2023preBPix.sh
bash runner/SoG/run_SoG_2023postBPix.sh
```

Each invocation creates a new isolated `runs/<model>/<era>/<timestamp>_<pid>/` with terminal output mirrored in `run.log`. Inspect a completed era before running the next. Current production already completed; these are commands for deliberate new runs, not a request to rerun it. Flat runner/config paths and the old era_model run folders are compatibility symlinks. No fitting settings changed during the organization.
