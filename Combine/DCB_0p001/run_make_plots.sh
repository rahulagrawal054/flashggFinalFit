#!/bin/bash

# Create rename.json
cat > rename.json <<EOF
{
  "r_ttH": "#mu_{t#bar{t}H+tHW}",
  "r_tHq": "#mu_{tHq}"
}
EOF

# ttH plot
plot1DScan.py "higgsCombine_scan_syst_r_ttH.MultiDimFit.mH125.08.root" \
  --others "higgsCombine_scan_stat_r_ttH.MultiDimFit.mH125.08.root:Stat-Only:2" \
  --POI r_ttH \
  --output "CombinePlot_r_ttH" \
  --main-label "Total Uncert." \
  --main-color 1 \
  --y-cut 50 \
  --y-max 20 \
  --translate rename.json \
  --breakdown "Syst,Stat" \
  --logo-sub "Internal"

# tHq plot
plot1DScan.py "higgsCombine_scan_syst_r_tHq.MultiDimFit.mH125.08.root" \
  --others "higgsCombine_scan_stat_r_tHq.MultiDimFit.mH125.08.root:Stat-Only:2" \
  --POI r_tHq \
  --output "CombinePlot_r_tHq" \
  --main-label "Total Uncert." \
  --main-color 1 \
  --y-cut 50 \
  --y-max 20 \
  --translate rename.json \
  --breakdown "Syst,Stat" \
  --logo-sub "Internal"

echo "Done! Plots saved as:"
echo "  CombinePlot_r_ttH.*"
echo "  CombinePlot_r_tHq.*"
