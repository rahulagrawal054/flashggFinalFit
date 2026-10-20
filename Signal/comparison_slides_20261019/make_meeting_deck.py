"""Build a meeting deck with verified common yields, links and a model recommendation."""
from pathlib import Path
import csv,json,re
HERE=Path(__file__).resolve().parent
COMBINE=HERE.parent.parent/'Combine'
WEB='https://rkumarag.web.cern.ch/ttH-tH-CP-Analysis/'
check=json.loads((HERE/'meeting_inputs/yield_comparison.json').read_text())
assert check['rows']==563 and check['max_absolute_difference']==0
source=(HERE/'signal_model_comparison.tex').read_text()
frames=re.findall(r'\\begin\{frame\}.*?\\end\{frame\}',source,re.S)
def select(prefix):
 hits=[f for f in frames if f.startswith(r'\begin{frame}{'+prefix)]
 assert len(hits)==1,prefix
 return hits[0]
def esc(x):return str(x).replace('_',r'\_').replace('%',r'\%').replace('&',r'\&')
def frame(title,body):return r'\begin{frame}{'+title+'}\n'+body+'\n'+r'\end{frame}'
def linked(content,path):return '\\gdef\\plotlink{'+WEB+path+'}\n'+content+'\n'
root=COMBINE/'DCB/yield_tables_composition_20261017/slide_tables_regions'
with (root/'three_components_incl_counts_percent.csv').open() as h:yieldrows=list(csv.DictReader(h))
assert len(yieldrows)==17
cols=['cat','Total','ttH+tHW','tHq','Res. Higgs bkg']
def table(rows):
 lines=[r'\begin{center}\renewcommand{\arraystretch}{1.05}\setlength{\tabcolsep}{6pt}',r'\resizebox{0.86\linewidth}{!}{\begin{tabular}{lrrrr}\toprule',r'Category & Total Higgs & ttH+tHW & tHq & Other Higgs \\\midrule']
 for row in rows:lines.append(' & '.join(esc(row[c]) for c in cols)+r' \\')
 lines += [r'\bottomrule\end{tabular}}\end{center}']
 return '\n'.join(lines)
head=r'''\documentclass[aspectratio=169,10pt]{beamer}
\usepackage{booktabs,graphicx}
\setbeamertemplate{navigation symbols}{}
\setbeamercolor{frametitle}{fg=blue!60!black}
\hypersetup{colorlinks=true,urlcolor=blue!60!black}
\gdef\plotlink{https://rkumarag.web.cern.ch/ttH-tH-CP-Analysis/Combine/}
\setbeamertemplate{footline}{\leavevmode\hbox{\begin{beamercolorbox}[wd=.86\paperwidth,ht=3ex,dp=1ex,leftskip=2ex]{author in head/foot}\tiny CMS Private work\hspace{1em}\href{\plotlink}{Supporting plots and numerical results (CERN www)}\end{beamercolorbox}\begin{beamercolorbox}[wd=.14\paperwidth,ht=3ex,dp=1ex,rightskip=2ex plus1fil]{date in head/foot}\hfill\insertframenumber/\inserttotalframenumber\end{beamercolorbox}}}
\title{Signal-model choice for the fiducial ttH / tHq analysis}
\subtitle{DCB+Gaussian versus sum of Gaussians}
\author{Rahul Kumar Agrawal}
\date{20 October 2026}
\begin{document}
'''
parts=[head]
parts.append(linked(r'\begin{frame}\titlepage\begin{center}\small Proposed nominal: \textbf{DCB+Gaussian}. Retain SoG as an alternative cross-check.\\[2mm]\href{'+WEB+r'Combine/}{Open complete comparison and result galleries}\end{center}\end{frame}','Combine/'))
parts.append(linked(frame('What is being compared?',r'''\begin{itemize}
\item Two signal-shape families, with the same selections, 16 categories and four eras: 2022preEE, 2022postEE, 2023preBPix and 2023postBPix.
\item Signal-MC shape checks use the generated mass, 125 GeV. Combine uses $M_H=125.09$ GeV.
\item The non-shape datacard lines and background files are identical. The 91 constrained nuisances and physics-model mapping are matched.
\item $r_{ttH}$ scales fiducial-in ttH+tHW; $r_{tHq}$ scales fiducial-in tHq. Out-of-fiducial and other Higgs contributions retain their prescribed fixed strengths.
\item For each one-dimensional scan/impact, profile the other strength and the background envelope; compare total and stat-only results.
\end{itemize}
\textbf{Scope:} separate model-generated Asimov datasets, rather than one shared reference. Snapshot convergence and closure warnings remain. No observed signal-strength measurement is presented here.'''),'Combine/Comparison/'))
parts.append(linked(select('How should we choose the signal PDF?'),'Signal/ModelComparison/'))
for title,rows in [('Nominal expected yields: ttH-enriched categories',yieldrows[:8]),('Nominal expected yields: tH and background categories',yieldrows[8:])]:
 body=table(rows)+r'''\small Entries: \textbf{events (row \% of Higgs yield)}; incl = in+out. Other Higgs = ggH+VBF+VH+bbH; continuum excluded.
\vspace{2mm}

\textbf{Identical DCB/SoG yields:} all 563 retained terms checked. Four eras, $M_H=125.09$ GeV, strengths 1, nuisances 0; after 0.1\% pruning.
\vfill\tiny Full model mass range; no observed counts. Detailed in/out and production tables are linked below.'''
 parts.append(linked(frame(title,body),'Combine/DCB/yield_tables_composition_20261017/slide_tables_regions/'))
parts.append(linked(select('Visible shape difference: tH\\_had\\_4'),'Signal/IndividualYears/'))
parts.append(linked(select('A documented poor SoG solution:'),'Signal/ModelComparison/'))
parts.append(linked(select('How does the smearing nuisance change the signal shape?'),'Signal/Smearing/'))
parts.append(linked(select('Current impacts:'),'Combine/SoG/impacts/'))
parts.append(linked(frame('Asimov scans: saved data versus postfit regeneration',r'''\small
Write the expected bin contents as $D_A(r,\theta,k)$: strengths $r$, continuous nuisance/background parameters $\theta$, and background-function indices $k$.
\begin{center}\renewcommand{\arraystretch}{1.3}
\begin{tabular}{p{.19\linewidth}p{.34\linewidth}p{.34\linewidth}}\toprule
 & Our production scans & Regeneration from a postfit snapshot \\\midrule
Data construction & Save $D_0=D_A(1,\theta_0,k_0)$ in the first command. & Load the fit to $D_0$, reset both strengths to 1; generate $D_1=D_A(1,\hat\theta_0,\hat k_0)$. \\
Scan input & Snapshot + \texttt{--toysFile}; every scan reads $D_0$. & Snapshot + \texttt{-t -1} without \texttt{--toysFile}; Combine generates new expected data. \\
What changes? & Snapshot supplies starting values; data remain fixed. & Expected background shape, normalization and nuisance settings may change the data. \\\bottomrule
\end{tabular}\end{center}
\textbf{Florian's verified wrapper:} without a toys file it uses \texttt{--expectSignal 1 -t -1}; with a toys file it explicitly reuses it. Snapshot loading is optional. Regeneration is therefore a configuration choice, not a universal Florian rule.
\vfill\tiny Source: FloMau/flashggFinalFit, commit d9031abb4e8c, Combine/RunFits.py:58--64,195--200. Our two-POI adaptation explicitly sets both strengths to 1; \texttt{--expectSignal} alone targets a parameter named \texttt{r}.
'''),'Combine/Comparison/'))
parts.append(linked(frame('Which convention is correct, and what did we test?',r'''\begin{itemize}
\item Both are legitimate \textbf{specified expected-data constructions}. $D_0$ tests the original generation model; $D_1$ tests a model conditioned on the first fit. They answer different conditional questions.
\item For a controlled total/stat-only comparison, use \textbf{the same dataset}, POI definitions, ranges and stated nuisance-freezing convention. Moving the best fit towards 1 is not itself validation.
\item Existing DCB diagnostic: fitting saved $D_0$ gave $(r_{ttH},r_{tHq})=(1.0422,1.0203)$; postfit-regenerated $D_1$ gave $(1.00005,1.00119)$. Dataset hashes differ: these are genuinely different expected data.
\end{itemize}
\begin{block}{Isolated DCB and SoG tests: completed}
For each family, generated $D_1$ once from its saved postfit snapshot, reset both strengths to 1, and reused $D_1$ in all four scans: each strength scanned with the other profiled, total and stat-only. 300 points per scan; $r_{ttH}\in[0,2.5]$, $r_{tHq}\in[-8,15]$.
\end{block}
\small Stat-only freezes constrained nuisances at the \textbf{source snapshot} values, keeping that convention fixed when changing datasets. Background parameters/indices and the other strength remain profiled. Original production results are preserved. This is an explicit saved-data adaptation of postfit regeneration, not four independent generations.
'''),'Combine/Comparison/'))
results=(HERE/'postfit_asimov_results.tex').read_text()
for content in re.findall(r'\\begin\{frame\}.*?\\end\{frame\}',results,re.S):
 parts.append(linked(content,'Combine/Comparison/'))
parts.append(linked(select('Expected profile scans:'),'Combine/Comparison/'))
original_numbers=select('Numerical comparison and what it establishes').replace('Numerical comparison and what it establishes','Original-dataset results: impacts, significance and limits')
original_numbers=original_numbers.replace('Both best fits are near $(1.042,1.020)$, rather than exact closure at $(1,1)$.','Original-data best fits are near $(1.042,1.020)$. New postfit-regenerated scans close near 1; impacts, significances and limits here still use the original data.')
parts.append(linked(original_numbers,'Combine/Comparison/'))
parts.append(linked(frame('Proposed choice: DCB+Gaussian as the nominal model',r'''\begin{block}{Recommendation for the analysis}
Use \textbf{DCB+Gaussian as the nominal family}; retain SoG as an alternative validation model. This is a proposed modeling prescription, not a claim that the current outputs have passed final validation.
\end{block}
\begin{itemize}
\item It avoids the additional Gaussian-count selection step. In the illustrated problematic returned SoG fits, DCB gives smoother shapes and/or better agreement with MC.
\item This preference is conditional on adequate signal-MC agreement: DCB is not universally better. A converged example favoring SoG is retained in the backup slides.
\item Expected intervals and impacts are nearly unchanged; neither a sensitivity advantage nor nuisance rank is used to select the PDF.
\end{itemize}
\textbf{Before final sign-off:} resolve important component convergence/boundary problems; establish a consistent negative/zero-rate prescription; calibrate the goodness-of-fit checks; review the original nonzero snapshot statuses and nonclosure. The postfit-regenerated tests now close near 1, with almost unchanged widths; this does not validate the original snapshot. A shared cross-family reference would isolate fitted-model effects.'''),'Combine/Comparison/'))
links=[('DCB: scans, limits, impacts and tables','Combine/DCB/'),('SoG: scans, limits and impacts','Combine/SoG/'),('Comparison plots, numbers and meeting slides','Combine/Comparison/'),('All signal-model plots, individually by year and category','Signal/IndividualYears/'),('Process-level shape comparisons and residuals','Signal/ModelComparison/'),('Signal PDF response to the smearing nuisance','Signal/Smearing/'),('Yield tables: inclusive, fiducial-in and fiducial-out','Combine/DCB/yield_tables_composition_20261017/slide_tables_regions/'),('DCB full impact PDF (ttH)','Combine/DCB/impacts/impacts_r_ttH.pdf'),('SoG full impact PDF (ttH)','Combine/SoG/impacts/impacts_r_ttH.pdf')]
parts.append(linked(frame('Clickable supporting material',r'\begin{itemize}'+'\n'+'\n'.join(r'\item \href{'+WEB+path+'}{'+label+'}' for label,path in links)+ '\n'+r'\end{itemize}'+'\n'+r'\small Main result galleries contain page-wise PNG/JPG exports, PDFs and numerical summaries. Original fit outputs were preserved.'),'Combine/'))
parts.append(r'\appendix'+'\n')
parts.append(linked(select('Visible shape difference: tH\\_had\\_3'),'Signal/IndividualYears/'))
parts.append(linked(select('Keep the comparison balanced:'),'Signal/ModelComparison/'))
history=select('Historical DCB change:')
history=history.replace('Run fresh SoG Combine fits with matched mass, POIs, data-generation prescription, constraints, background envelope, pruning and numerical settings. Check Asimov closure and fit quality before comparing impacts.','The fresh SoG comparison uses matched workflow settings. It does not establish which historical changes caused the earlier DCB asymmetry.')
parts.append(linked(history,'Combine/Comparison/'))
# Distinguish the fiducial-in terms controlled by the POIs from fixed out terms.
region_rows=[]
for region in ['all','in','out']:
 with (COMBINE/f'DCB/yield_tables_20261017/yield_table_{region}.csv').open() as h:
  rows=list(csv.DictReader(h));r=rows[-1];assert next(iter(r.values()))=='Total'
  vals=[float(r['Total Higgs']),float(r['ttH'])+float(r['tHW']),float(r['tHq']),sum(float(r[x]) for x in ['ggH','VBF','VH','bbH'])]
  region_rows.append(('incl' if region=='all' else region,vals))
rt=r'\begin{center}\begin{tabular}{lrrrr}\toprule Region & Total Higgs & ttH+tHW & tHq & Other Higgs\\\midrule'+'\n'
for name,values in region_rows:rt+=name+' & '+' & '.join(f'{v:.3f}' for v in values)+r' \\'+'\n'
rt+=r'\bottomrule\end{tabular}\end{center}'
parts.append(linked(frame('Backup: inclusive, fiducial-in and fiducial-out yields',rt+r'''\begin{itemize}
\item Inclusive = in+out. The yield comparison between DCB and SoG is exact at the nominal point for every retained process/category/year term.
\item Only \textbf{in} ttH+tHW terms are multiplied by $r_{ttH}$, and only \textbf{in} tHq terms by $r_{tHq}$; the corresponding out terms are fixed to their SM strengths.
\item The table contains Higgs events, not continuum background. Large out-of-fiducial Higgs yields are concentrated in the background-enriched categories.
\end{itemize}
\href{'''+WEB+r'''Combine/DCB/yield_tables_composition_20261017/slide_tables_regions/}{Open all numerical and percentage tables}'''),'Combine/DCB/yield_tables_composition_20261017/slide_tables_regions/'))
parts.append(r'\end{document}'+'\n')
(HERE/'meeting_DCB_SoG_20261020.tex').write_text('\n'.join(parts))
print('Built meeting deck:',len([s for s in parts if '\\begin{frame}' in s]),'frames; exact DCB/SoG prefit yield agreement verified.')
