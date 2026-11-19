"""Half-panel scene snippets for the split-screen remakes (origin = half centre on the floor, y up is negative)."""
MEH = "pup({kind:'boy',x:%s,y:0,s:%s,eyes:'open',look:[0,.5],brows:'sad',mouth:'flat',blush:.3,shadow:true});"
def meh(x=0, s=.78): return MEH % (x, s)
def happy2(xb=-85, xg=85, s=.72, extra=''):
    return ("pup({kind:'boy',x:%s,y:0,s:%s,eyes:'happy',mouth:'open',blush:.7,tilt:.08,wag:.6%s});"
            "pup({kind:'girl',x:%s,y:0,s:%s,flip:-1,eyes:'happy',mouth:'smile',blush:.7,tilt:.08,wag:.6});") % (xb, s, extra, xg, s)
RAINWIN = "windowBox(-150,-640,300,250,()=>{ctx.fillStyle='#9fb3c8';ctx.fillRect(-300,-800,700,600);rain(30);});"
