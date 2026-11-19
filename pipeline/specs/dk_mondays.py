"""Remake of @dinklygame DcmYszGh799 (1.9M, 10.40s). Side-by-side panels, no grid. Audio: use the source reel's audio in-app."""
from _dkhalf import meh, happy2
TARGET = 10.401
CUTS = [0, 2.6, 5.4, 7.8]
GRID = False
SIDE = True
SONG = "the source reel's own audio (open instagram.com/reel/DcmYszGh799 > Use audio)"
CAPTION = "everything is better with you 🫶\n\n#loveyou #soulmates #fridayvibes #fridayfeels #couplegoals"
PANELS = [
 dict(bg='#f6c9b8', bg2='#f9d9c9', ink='#2b2b2b', left_label='MONDAYS', right_label='MONDAYS WITH YOU',
      left="table(0,0,360);" + meh(-60, .62).replace("y:0", "y:-60") + "laptop(110,-150,.6);",
      right="table(0,0,400);" + happy2(-100, 100, .58).replace("y:0", "y:-60") + "laptop(0,-150,.7);cupS(-150,-150,'#f29bb3');cupS(150,-150);floatHearts(0,-420,0,u,3,70);"),
 dict(bg='#dfe9c8', bg2='#f9eec3', ink='#2b2b2b', left_label='SUNNY DAYS', right_label='SUNNY DAYS WITH YOU',
      left="ctx.fillStyle='#fff3c4';ctx.beginPath();ctx.arc(150,-620,60,0,7);ctx.fill();" + meh(0, .72),
      right="ctx.fillStyle='#fff3c4';ctx.beginPath();ctx.arc(150,-620,60,0,7);ctx.fill();picnic(0,-10,380);flowerField(-40);" + happy2(-85, 85, .66)),
 dict(bg='#cfe0f2', bg2='#d8e8f7', ink='#2b2b2b', left_label='TRAVELLING', right_label='TRAVELLING WITH YOU',
      left=meh(-40, .7) + "suitcase(130,-6,.75);",
      right="suitcase(-200,-6,.65,'#f29bb3');suitcase(200,-6,.65);" + happy2(-70, 70, .64) + "floatHearts(0,-380,0,u,3,70);"),
 dict(bg='#f3e0c4', bg2='#f7e8d2', ink='#2b2b2b', left_label='COOKING', right_label='COOKING WITH YOU',
      left="table(0,0,340);plate(0,-150,.8,'#d9c9a8');" + meh(0, .62).replace("y:0", "y:-60"),
      right="table(0,0,420);" + happy2(-110, 110, .6).replace("y:0", "y:-60") + "pancakes(0,-152,7,.8);for(let i=0;i<8;i++){ctx.save();ctx.globalAlpha=.8;ell(-200+hash(i)*400,-500+hash(i+4)*300,10,10,'#ffffff',{stroke:false});ctx.restore();}"),
]
