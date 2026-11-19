"""Remake of @dinklygame DeEvaNDA5OB (2.1M, 14.16s, Maroon 5 - Sunday Morning). 4 split panels + grid."""
from _dkhalf import meh, happy2
TARGET = 14.163
CUTS = [0, 2.7, 5.1, 7.8]
GRID_AT = 10.2
SONG = 'Maroon 5 - Sunday Morning'
CAPTION = "sundays with you 💛\n\n#couplegoals #sundaymorning #loveyou #soulmate #maroon5"
PANELS = [
 dict(bg='#f6e3c0', left_label='SUNDAYS', right_label='SUNDAYS WITH YOU',
      left="table(0,0,360);plate(0,-150,.9,'#e9d8b0');cupS(110,-150);" + meh(0, .66).replace("y:0", "y:-60"),
      right="table(0,0,440);" + happy2(-115, 115, .62).replace("y:0", "y:-60") + "pancakes(0,-152,5,.8);plate(-150,-150,.6,'#e8484f');cupS(160,-150);"),
 dict(bg='#c9dcf2', left_label='MUSIC', right_label='MUSIC WITH YOU',
      left=meh(0, .76) + "headphones(0,-310,.8);",
      right=happy2(-80, 80, .72) + "note(-170,-420,1,.4+.6*Math.abs(Math.sin(T*2)));note(150,-470,1,.4+.6*Math.abs(Math.cos(T*2)));floatHearts(0,-380,0,u,3,80);"),
 dict(bg='#cfe0d6', left_label='WALKS', right_label='WALKS WITH YOU',
      left="rain(25);puddle(0,10,260);umbrella(0,-470,.75,'#8a8f99');" + meh(0, .7),
      right="tree(-200,0,.7);tree(220,0,.6,'#9cc78a');" + happy2(-80, 80, .7, ",paw:{k:1,x:150,y:-70}") + "floatHearts(0,-360,0,u,3,80);"),
 dict(bg='#d8c6dc', left_label='BEDTIME', right_label='BEDTIME WITH YOU',
      left="ctx.save();ctx.fillStyle='#3e4a6b';ctx.fillRect(-300,-1400,600,1400);ctx.restore();bed(0,0,420);pillow(-60,-140);" + "pup({kind:'boy',x:-10,y:-150,s:.62,eyes:'open',look:[1,.5],brows:'sad',mouth:'flat',shadow:false});quilt(0,70,420,'#7f8fd0');phoneS(90,-150,.8);",
      right="bed(0,0,460);pillow(-80,-140);pillow(80,-140);" + "pup({kind:'boy',x:-70,y:-150,s:.6,eyes:'closed',mouth:'smile',blush:.7,tilt:.15,shadow:false});pup({kind:'girl',x:70,y:-150,s:.6,flip:-1,eyes:'closed',mouth:'smile',blush:.7,tilt:.15,shadow:false});quilt(0,70,460,'#f29bb3');zzz(80,-330,u);"),
]
