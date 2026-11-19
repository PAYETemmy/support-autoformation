"""Trace toute la carte : essai.py <fichier.html> <pc|iphone> [étapes à photographier, séparées par des virgules]"""
import sys
from playwright.sync_api import sync_playwright
f,mode=sys.argv[1],sys.argv[2];shots=[int(x) for x in sys.argv[3].split(',')] if len(sys.argv)>3 else []
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    if mode=='iphone':
        ctx=b.new_context(viewport={'width':402,'height':874},device_scale_factor=2,is_mobile=True,has_touch=True)
    else:
        ctx=b.new_context(viewport={'width':1280,'height':900})
    pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+f); pg.wait_for_timeout(1200)
    n=pg.evaluate("STEPS.length"); print(mode,'| étapes :',n,'| notions :',pg.evaluate("MOL.length"))
    hors=[]; petit=[]
    for i in range(n):
        # tout est-il prêt et visible ?
        for _ in range(40):
            if pg.evaluate("!!guide&&!busy"): break
            pg.wait_for_timeout(100)
        pg.evaluate("for(var k=0;k<140;k++){tick(false);var T=camTarget();cam.x+=(T.x-cam.x)*.05;cam.y+=(T.y-cam.y)*.05;cam.s+=(T.s-cam.s)*.05}render()")
        r=pg.evaluate("""(()=>{var st=guide.st,o=[];[st.s,st.o].forEach(function(id){var a=V[id];o.push((a.x-cam.x)*cam.s+W/2,(a.y-cam.y)*cam.s+H/2,a.r*cam.s)});return {p:o,W:W,H:H,s:cam.s,lk:st.lk,n:st.n}})()""")
        P=r['p']
        for j in (0,3):
            if P[j]-P[j+2]<0 or P[j]+P[j+2]>r['W'] or P[j+1]-P[j+2]<0 or P[j+1]+P[j+2]>r['H']: hors.append(i)
        if r['s']<0.5 and not r['lk']: petit.append((i,round(r['s'],2)))
        if i in shots: pg.wait_for_timeout(1000); pg.screenshot(path='/tmp/e-%s-%d.png'%(mode,i))
        pg.evaluate("link()")
    pg.wait_for_timeout(1800)
    pg.evaluate("for(var k=0;k<300;k++){tick(false);var T=camTarget();cam.x+=(T.x-cam.x)*.05;cam.y+=(T.y-cam.y)*.05;cam.s+=(T.s-cam.s)*.05}render()")
    pg.screenshot(path='/tmp/e-%s-fin.png'%mode)
    print('fait :',pg.evaluate("S.p"),'| atomes hors écran aux étapes :',sorted(set(hors)),'| vue petite (hors liaisons) :',petit)
    # chevauchements entre molécules à la fin
    print('paires d\'atomes trop proches (<20 px de vide) :',pg.evaluate("""(()=>{var L=Object.keys(V).map(k=>V[k]),o=[];for(var i=0;i<L.length;i++)for(var j=i+1;j<L.length;j++){var d=Math.hypot(L[i].x-L[j].x,L[i].y-L[j].y)-L[i].r-L[j].r;if(d<20)o.push(L[i].id+' ~ '+L[j].id+' '+Math.round(d))}return o})()"""))
    print('échelle finale :',round(pg.evaluate("cam.s"),2),'| page / écran :',pg.evaluate("document.documentElement.scrollHeight"),pg.evaluate("innerHeight"))
    pg.evaluate("localStorage.clear()"); print('erreurs :',errs); b.close()
