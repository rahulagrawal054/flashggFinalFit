for cat in ttH_had_1 ttH_had_2 ttH_had_3 ttH_had_4 ttH_lep_1 ttH_lep_2 ttH_lep_3 ttH_lep_4 tH_had_1 tH_had_2 tH_had_3 tH_had_4 tH_lep_1 tH_lep_2 bkg_had bkg_lep; do
  python3 RunText2Workspace.py \
    --mode r_2D_fiducial \
    --ext ${cat} \
    --common_opts "-m 125.08" \
    --batch local
done
