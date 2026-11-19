"""Remake of @dinklygame Ddc4hbWAoh2 (8.2M, 14.07s, Maroon 5 - She Will Be Loved). 4 split panels + 2x2 grid."""
from _dkhalf import meh, happy2, RAINWIN
TARGET = 14.07
CUTS = [0, 2.6, 5.0, 7.8]
GRID_AT = 10.1
SONG = 'Maroon 5 - She Will Be Loved'
CAPTION = "everything is better with you ❤️\n\n#relationshiptips #soulmate #loveyou #maroon5 #fridayvibes"
PANELS = [
 dict(bg='#d9cbe8', left_label='RAINY DAYS', right_label='RAINY DAYS WITH YOU',
      left=RAINWIN + meh(), right=RAINWIN + "lblanket(400,-200,'#f3ead9');" + happy2(extra='') + "popcorn(0,-20,.8);"),
 dict(bg='#bfe0f2', left_label='FOOD SHOP', right_label='FOOD SHOP WITH YOU',
      left=meh(-40) + "basket(120,-10,.8,1);", right="trolley(10,-40,1.0,1);" + happy2(-150, 150, .62)),
 dict(bg='#f6e6c8', left_label='BREAKFAST', right_label='BREAKFAST WITH YOU',
      left="table(0,0,380);plate(0,-150,1,'#e9d8b0');" + meh(0, .7).replace("y:0", "y:-60") ,
      right="table(0,0,420);" + happy2(-110, 110, .66).replace("y:0", "y:-60") + "pancakes(0,-152,6,.9);cupS(130,-150);cupS(-130,-150,'#f29bb3');"),
 dict(bg='#f7d6c9', left_label='A NEW CITY', right_label='A NEW CITY WITH YOU',
      left="skyline();" + meh(-40) + "suitcase(130,-6,.8);",
      right="skyline();suitcase(-210,-6,.7,'#f29bb3');suitcase(210,-6,.7);" + happy2(-75, 75, .66, ",paw:{k:1,x:150,y:-70}")),
]
