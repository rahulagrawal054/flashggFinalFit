#!/usr/bin/env python3
"""Publish existing DCB/SoG plots and numerical summaries to the CERN www area.
No fits, input workspaces, model ROOT files or raw impact logs are published.
"""
from pathlib import Path
import hashlib,html,json,shutil
from urllib.parse import quote

BASE=Path(__file__).resolve().parent
DEST=Path('/eos/user/r/rkumarag/www/ttH-tH-CP-Analysis/Combine')
ALLOWED={'.png','.pdf','.jpg','.jpeg','.json','.csv','.txt','.log','.tex'}
records=[]
def copy_tree(src,dest):
    if not src.exists():return
    files=[src] if src.is_file() else sorted(x for x in src.rglob('*') if x.is_file())
    for f in files:
        if f.suffix.lower() not in ALLOWED or f.name.startswith('.'):continue
        rel=Path(f.name) if src.is_file() else f.relative_to(src)
        out=dest/rel;out.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(f,out)
        digest=hashlib.sha256(f.read_bytes()).hexdigest()
        assert hashlib.sha256(out.read_bytes()).hexdigest()==digest
        records.append(dict(source=str(f),published=str(out.relative_to(DEST.parent)),sha256=digest))
for model in ('DCB','SoG'):
    source=BASE/model;dest=DEST/model
    assert (source/'workspace.root').is_file(), 'Missing model workspace: '+model
    copy_tree(source/'plots',dest/'plots')
    impacts=source/'impacts'/('collected_auto' if model=='SoG' else 'collected_20261017')
    assert (impacts/'impacts.json').is_file()
    copy_tree(impacts,dest/'impacts')
    if model=='SoG':
        copy_tree(source/'impacts/validation',dest/'checks/impact_validation')
    for poi in ('r_ttH','r_tHq'):
        for scenario in ('total','statOnly'):
            mode='profile_other__refined' if model=='SoG' else 'profile_other'
            stage=source/'scans'/poi/scenario/mode
            for name in ('validation.json','manifest.json','points.csv','exit_status.txt'):
                copy_tree(stage/name,dest/'checks/scans'/poi/scenario)
        for step in ('significance','limits'):
            stage=source/step/poi/'total/profile_other'
            for name in ('results.json','manifest.json','exit_status.txt'):
                copy_tree(stage/name,dest/'results'/step/poi)
    copy_tree(source/'snapshot/validation.json',dest/'checks/snapshot')
    for folder in source.glob('yield_tables*'):
        copy_tree(folder,dest/folder.name)
slides=BASE.parent/'Signal/comparison_slides_20261019'
for name in ('signal_model_comparison.pdf','combine_scan_comparison.png','combine_scan_comparison.pdf','smearing_impact_comparison.png','smearing_impact_comparison.pdf','combine_comparison.json','meeting_DCB_SoG_20261020.pdf','postfit_asimov_comparison.png','postfit_asimov_comparison.pdf','postfit_asimov_comparison.json'):
    copy_tree(slides/name,DEST/'Comparison')
signal=BASE.parent/'Signal'
for source_name,public_name in [('runplotter_individual_years_20261014','IndividualYears'),('shape_review_20261014','ModelComparison'),('smearing_pdf_scan_20261015','Smearing')]:
    copy_tree(signal/source_name,DEST.parent/'Signal'/public_name)
copy_tree(slides/'meeting_inputs',DEST/'Comparison/meeting_inputs')
(DEST/'publication_manifest.json').write_text(json.dumps({'files':records,'qualification':'Provisional separate-model Asimov results. Snapshot status/covariance and internal fit warnings remain. Archived old_16OCT unchanged.'},indent=2)+'\n')
style='''body{font:16px system-ui,sans-serif;max-width:1300px;margin:30px auto;padding:0 20px;color:#172534}a{color:#165ca0}h1{font-size:27px}.note{padding:15px;background:#fff3d4;border-left:4px solid #be8c18}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:20px}figure{margin:0;padding:12px;border:1px solid #dce3eb;border-radius:6px}img{width:100%;height:300px;object-fit:contain;background:white}figcaption{overflow-wrap:anywhere}li{margin:8px 0}.dirs{display:flex;flex-wrap:wrap;gap:12px}.dirs a{padding:10px;background:#eef4fa;border-radius:4px}'''
gallery_roots=[DEST,DEST.parent/'Signal']
folders=[f for root in gallery_roots for f in [root]+[p for p in root.rglob('*') if p.is_dir() and not any(x.startswith('.') for x in p.relative_to(root).parts)]]
for folder in sorted(folders,key=lambda p:len(p.parts),reverse=True):
    relative=folder.relative_to(DEST.parent);title='DCB and SoG results' if folder==DEST else str(relative)
    dirs=sorted(p for p in folder.iterdir() if p.is_dir() and not p.name.startswith('.'))
    files=sorted(p for p in folder.iterdir() if p.is_file() and p.name!='index.html' and not p.name.startswith('.'))
    images=[p for p in files if p.suffix.lower()=='.png']
    body=f'<h1>{html.escape(title)}</h1><p><a href="'+'../'+'">Parent folder</a></p>'
    body+='<p class="note">Provisional expected results: DCB and SoG use separate Asimov datasets. Snapshot convergence/covariance warnings remain. See checks and numerical summaries. No observed mass-window plots were added by this publication.</p>'
    body+='<nav class="dirs">'+''.join(f'<a href="{quote(p.name)}/">{html.escape(p.name)}</a>' for p in dirs)+'</nav>'
    body+='<ul>'+''.join(f'<li><a href="{quote(p.name)}">{html.escape(p.name)}</a></li>' for p in files if p.suffix.lower()!='.png')+'</ul>'
    body+='<div class="grid">'+''.join(f'<figure><a href="{quote(p.name)}"><img loading="lazy" src="{quote(p.name)}" alt="{html.escape(p.stem)}"></a><figcaption><a href="{quote(p.name)}">{html.escape(p.name)}</a></figcaption></figure>' for p in images)+'</div>'
    (folder/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+style+'</style>'+body+'</html>')
# Make the fresh area and old archive discoverable without touching the archive.
parent=DEST.parent
if not (parent/'index.html').exists():
    (parent/'index.html').write_text('<!doctype html><meta charset="utf-8"><title>ttH and tH analysis</title><h1>ttH and tH analysis</h1><p><a href="Combine/">Current DCB / SoG Combine results and comparison</a></p><p><a href="old_16OCT/">Archived results: old_16OCT</a></p>')
landing=parent/'index.html'
text=landing.read_text()
if 'Signal/' not in text:
    text=text.replace('<p><a href="old_16OCT/">','<p><a href="Signal/">Current signal-model plots by year, shape comparisons and smearing</a></p><p><a href="old_16OCT/">')
    landing.write_text(text)
print('Published verified files:',len(records))
print('Destination:',DEST)
print('URL: https://rkumarag.web.cern.ch/ttH-tH-CP-Analysis/Combine/')
