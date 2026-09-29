import sys,importlib,os
sys.path.insert(0,'/home/claude/jj');sys.path.insert(0,'/home/claude/jj/specs')
import jjlib as J
slug=sys.argv[1];spec=importlib.import_module(slug)
W=f'{J.ROOT}/work/{slug}';os.makedirs(W,exist_ok=True)
n=len(spec.SCENES);dur=[7.0]*n
html=J.build_html(slug,spec.TITLE,spec.SCENES,dur,J.end_tt(3),6.0)
open(W+'/prev.html','w').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1920});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto('file://'+W+'/prev.html')
    pg.evaluate("async()=>{await document.fonts.load('bold 80px Poppins');await document.fonts.load('70px \"Noto Color Emoji\"');}")
    print('errs',errs[:3])
    for i in range(n):
        for j,f in enumerate((.3,.7)):
            t=i*7.0+7.0*f
            pg.evaluate("t=>render(t,true)",t)
            pg.evaluate("()=>document.getElementById('c').toBlob(()=>{})")
            pg.locator('#c').screenshot(path=f'{W}/pv_{i}_{j}.png')
    b.close()
