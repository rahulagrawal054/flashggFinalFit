"""Optional explicit production settings. No override unless FINALFIT_RUN_CONFIG is set."""
import json
import math
import os
from pathlib import Path


def load_run_config():
    filename = os.environ.get('FINALFIT_RUN_CONFIG')
    if not filename:
        return None
    config = json.loads(Path(filename).read_text())
    lumis = config['lumi_fb']
    if not lumis or any(isinstance(v, bool) or not isinstance(v, (int, float)) or
                        not math.isfinite(v) or v <= 0 for v in lumis.values()):
        raise ValueError('Fill approved positive luminosities for every era in FINALFIT_RUN_CONFIG')
    return config
