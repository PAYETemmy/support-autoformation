#!/usr/bin/env python3
"""Construit une carte de molécules : construire.py <donnees.js> <Sujet> <dossier du site> <nom court>"""
import sys,json,shutil,os
don,sujet,dossier,court=sys.argv[1:5]
ici=os.path.dirname(os.path.abspath(__file__));site='/home/claude/support-autoformation'
h=open(os.path.join(ici,'gabarit-guide.html')).read()
assert h.count('/*DATA*/')==1
h=h.replace('/*DATA*/',open(os.path.join(ici,don)).read().strip(),1)
h=h.replace('<title>Molécules — GitHub</title>','<title>Molécules — %s</title>'%sujet,1).replace('molecules-guide-GitHub','molecules-guide-'+sujet.replace(' ','-'),1)
open(os.path.join(ici,'carte-%s.html'%dossier),'w').write(h)
h=h.replace('<meta name="theme-color" content="#0e0e10">','''<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#0e0e10">
<meta name="apple-mobile-web-app-title" content="%s">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="manifest.webmanifest">
<meta name="color-scheme" content="dark">'''%court,1)
d=os.path.join(site,dossier);os.makedirs(d,exist_ok=True)
open(os.path.join(d,'index.html'),'w').write(h)
for i in ('apple-touch-icon.png','icon-512.png'):shutil.copy(os.path.join(site,'github-molecules',i),d)
m=json.load(open(os.path.join(site,'github-molecules','manifest.webmanifest')))
m['name']='Molécules — '+sujet;m['short_name']=court
json.dump(m,open(os.path.join(d,'manifest.webmanifest'),'w'),ensure_ascii=False,indent=1)
print('ok',d)
