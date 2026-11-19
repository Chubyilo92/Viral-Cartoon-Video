"""Remake of @dinklygame Dduja8kg2MJ (2.2M, 11.12s, rhianne - Somewhere Only We Know). 4 split panels + grid."""
from _dkhalf import meh, happy2
TARGET = 11.121
CUTS = [0, 2.2, 4.2, 6.3]
GRID_AT = 8.4
SONG = 'rhianne - Somewhere Only We Know'
CAPTION = "everything is better with you 💛\n\n#soulmate #loveyou #lovestory #relationshiptips #weekendvibes"
PANELS = [
 dict(bg='#d9cbe8', left_label='TAKEAWAY', right_label='TAKEAWAY WITH YOU',
      left="roundTable(0,0,130);plate(0,-170,.9,'#e9d8b0');" + meh(0, .62).replace("y:0", "y:-40"),
      right="roundTable(0,0,190);" + happy2(-110, 110, .6).replace("y:0", "y:-40") + "plate(-60,-172,.8,'#e8484f');plate(60,-172,.8,'#f7c948');friesBag(0,-160,.6);"),
 dict(bg='#bfdcf2', left_label='MOVIE NIGHT', right_label='MOVIE NIGHT WITH YOU',
      left="tv(0,-380,.75);" + meh(0, .7) + "popcorn(110,0,.45);",
      right="tv(0,-380,.75);lblanket(400,-180,'#f3ead9');" + happy2(-85, 85, .66) + "popcorn(0,-10,.9);"),
 dict(bg='#c8e6d2', left_label='LAZY DAYS', right_label='LAZY DAYS WITH YOU',
      left="lsofa(400);" + meh(0, .66).replace("y:0", "y:-130"),
      right="lsofa(420,'#b8a6d9','#c9b8e6');" + happy2(-80, 80, .62).replace("y:0", "y:-130") + "ctx.save();ctx.translate(0,-30);lblanket(380,-120,'#f3ead9');ctx.restore();"),
 dict(bg='#f7c9d4', left_label='TESCO', right_label='TESCO WITH YOU',
      left=meh(-50, .72) + "basket(120,-10,.75,1);", right="trolley(10,-40,1.0,1);" + happy2(-150, 150, .6)),
]
