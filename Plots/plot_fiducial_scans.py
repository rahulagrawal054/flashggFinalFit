#!/usr/bin/env python3
"""Plot matched expected total/stat-only scans without smoothing or recentering."""
import argparse,csv,json,math,pathlib,re,hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run-dir',required=True);p.add_argument('--label',default=None);p.add_argument('--other-mode',default='profile_other');p.add_argument('--output-dir',default=None);p.add_argument('--y-max',type=float,default=20.0);a=p.parse_args()
run=pathlib.Path(a.run_dir).resolve();out=pathlib.Path(a.output_dir).resolve() if a.output_dir else run/'plots/scans/custom';out.mkdir(parents=True,exist_ok=True)
summary={'run':str(run),'label':a.label or run.name,'other_mode':a.other_mode,'method':'Raw q=2*deltaNLL; straight lines between neighboring valid points; no smoothing/recentering. Linear interval interpolation at q=1 and q=3.841458820694124. Invalid points omitted and listed; never joined across gaps.','pois':{}}
for poi in ['r_ttH','r_tHq']:
 curves={};meta={};item={};fig,ax=plt.subplots(figsize=(8.4,7.3))
 for scenario,color,style,label in [('total','black','-','Total Uncert.'),('statOnly','red',':','Stat-Only')]:
  src=run/'scans'/poi/scenario/a.other_mode;meta[scenario]=json.loads((src/'manifest.json').read_text());rows=[{k:float(v) for k,v in r.items()} for r in csv.DictReader((src/'points.csv').open())]
  assert len(rows)==meta[scenario]['points']+1
  valid=lambda r:all(math.isfinite(v) for v in r.values()) and -0.001<=r['deltaNLL']<999
  bad=[{'grid_point':i,'value':r['poi'],'deltaNLL':r['deltaNLL']} for i,r in enumerate(rows[1:]) if not valid(r)]
  good=[r for r in rows[1:] if valid(r)];curves[scenario]=good;segments=[];segment=[]
  for r in rows[1:]:
   if valid(r):segment.append((r['poi'],2*r['deltaNLL']))
   elif segment:segments.append(segment);segment=[]
  if segment:segments.append(segment)
  crossings={}
  for q in [1,3.841458820694124]:
   values=[]
   for seg in segments:
    # Include the actual best fit for linear interpolation close to the minimum.
    pairs=sorted(seg+([(rows[0]['poi'],0.0)] if seg[0][0]<=rows[0]['poi']<=seg[-1][0] else []))
    for (x0,y0),(x1,y1) in zip(pairs,pairs[1:]):
     if y0==q:values.append(x0)
     elif (y0-q)*(y1-q)<0:values.append(x0+(q-y0)*(x1-x0)/(y1-y0))
   crossings[str(q)]=sorted(set(values))
  for i,seg in enumerate(segments):
   pairs=sorted(seg+([(rows[0]['poi'],0.0)] if seg[0][0]<=rows[0]['poi']<=seg[-1][0] else []));ax.plot([x for x,y in pairs],[y for x,y in pairs],color=color,linestyle=style,lw=1.8,label=label if i==0 else None)
  text=(src/'scan.log').read_text();pattern=r'^Point (\d+)/'+str(meta[scenario]['points'])+' '+poi+r' = ([^\n]+)';matches=list(re.finditer(pattern,text,re.M));badfinal=[]
  for i,m in enumerate(matches):
   block=text[m.start():matches[i+1].start() if i+1<len(matches) else len(text)];statuses=re.findall(r'Minimization finished with status=(-?\d+)',block)
   if int(m.group(1)) not in {x['grid_point'] for x in bad} and (not statuses or statuses[-1]!='0'):badfinal.append(int(m.group(1)))
  item[scenario]={'best_fit':rows[0]['poi'],'crossings':crossings,'valid_grid_points':len(good),'invalid_points':bad,'valid_points_with_bad_final_status':badfinal,'snapshot_sha256':meta[scenario]['snapshot_sha256'],'source_csv_sha256':hashlib.sha256((src/'points.csv').read_bytes()).hexdigest()}
  assert not badfinal,'Convergence issue in plotted region'
 assert meta['total']['snapshot_sha256']==meta['statOnly']['snapshot_sha256'];assert meta['total']['scan_range']==meta['statOnly']['scan_range'];assert meta['total']['points']==meta['statOnly']['points']
 for field in ['other_mode','other_value']:assert meta['total'][field]==meta['statOnly'][field]
 c0={round(r['poi'],7):2*r['deltaNLL'] for r in curves['total']};c1={round(r['poi'],7):2*r['deltaNLL'] for r in curves['statOnly']};keys=c0.keys()&c1.keys();violations=[x for x in sorted(keys) if c0[x]-c1[x]>0.001];item['total_above_stat_by_more_than_0p001']=violations
 ax.axhline(1,color='0.65',ls='-',lw=.6);ax.axhline(3.841458820694124,color='0.65',ls='-',lw=.6)
 ax.set_ylim(0,a.y_max);ax.set_xlim(meta['total']['scan_range'])
 symbol=r'\mu_{t\bar{t}H+tHW}' if poi=='r_ttH' else r'\mu_{tHq}'
 ax.set_xlabel('$'+symbol+'$',fontsize=22,loc='right');ax.set_ylabel(r'$-2\,\Delta\ln L$',fontsize=22,loc='top')
 ax.tick_params(which='both',direction='in',top=True,right=True,labelsize=14);ax.minorticks_on();ax.tick_params(which='major',length=7);ax.tick_params(which='minor',length=4)
 ax.text(.015,.975,'CMS',transform=ax.transAxes,va='top',fontsize=25,fontweight='bold')
 ax.text(.015,.895,'Private work',transform=ax.transAxes,va='top',fontsize=19,fontstyle='italic')
 ax.legend(loc='upper left',bbox_to_anchor=(.035,.825),frameon=False,fontsize=17,handlelength=1.6,handletextpad=.4)
 td=item['total'];sd=item['statOnly'];ci=td['crossings']['1'];si=sd['crossings']['1'];require_intervals=len(ci)==len(si)==2
 if require_intervals:
  center=td['best_fit'];down=center-ci[0];up=ci[1]-center;sdown=sd['best_fit']-si[0];sup=si[1]-sd['best_fit']
  residuals=[down*down-sdown*sdown,up*up-sup*sup]
  item['approx_quadrature_systematic_errors']={'down':math.sqrt(max(0,residuals[0])),'up':math.sqrt(max(0,residuals[1])),'qualification':'Approximate asymmetric quadrature subtraction of total and stat-only interval errors; not an independently fitted component.','nonnegative_variances':all(v>=0 for v in residuals)}
  qd,qu=[math.sqrt(max(0,v)) for v in residuals]
  line1=rf'${symbol} = {center:.3f}^{{+{up:.3f}}}_{{-{down:.3f}}}$'
  line2=rf'${symbol} = {center:.3f}^{{+{sup:.3f}}}_{{-{sdown:.3f}}}\,\mathrm{{(Stat)}}\;^{{+{qu:.3f}}}_{{-{qd:.3f}}}\,\mathrm{{(Syst)}}$'
  ax.text(.48,.94,line1,transform=ax.transAxes,fontsize=14,va='top')
  ax.text(.48,.82,line2,transform=ax.transAxes,fontsize=12.5,va='top')
 ax.text(.99,1.015,(a.label or run.name)+' · Expected SM Asimov',transform=ax.transAxes,ha='right',fontsize=12)
 other='tHq' if poi=='r_ttH' else 'ttH+tHW';note=f'Other signal strength ({other}): '+('profiled' if a.other_mode.startswith('profile_other') else 'fixed; see manifest')
 fig.text(.13,.025,note+'; background profiled',fontsize=10)
 fig.subplots_adjust(left=.13,right=.97,bottom=.16,top=.94)
 for ext in ['png','pdf']:fig.savefig(out/(poi+'.'+ext),dpi=180)
 plt.close(fig);summary['pois'][poi]=item
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
with (out/'intervals.csv').open('w') as h:
 w=csv.writer(h);w.writerow(['poi','scenario','best_fit','lower68','upper68','lower95','upper95'])
 for poi,item in summary['pois'].items():
  for sc in ['total','statOnly']:
   d=item[sc];w.writerow([poi,sc,d['best_fit'],*d['crossings']['1'],*d['crossings']['3.841458820694124']])
print('Saved custom plots and interval reports:',out)
