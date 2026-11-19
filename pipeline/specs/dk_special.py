"""Remake of @dinklygame DcUXDfBhkxO (2.5M, 20.07s, Ross Lara - Love Is Like The Wind). Small dark lowercase notes on pastels."""
TARGET = 20.067
STYLE = 'dark'
SONG = 'Ross Lara - Love Is Like The Wind'
CAPTION = "you make me feel special 🫶\n\n#loveyou #couples #relationshipgoals #soulmate #fridaynight"
P = lambda kb='happy', kg='happy', extra='', y='G+60': ("pup({kind:'boy',x:440,y:%s,s:1.05,eyes:'%s',mouth:'smile',blush:.8,tilt:.06%s});"
                                                         "pup({kind:'girl',x:640,y:%s,s:1.05,flip:-1,eyes:'%s',mouth:'smile',blush:.8,tilt:.06});") % (y, kb, extra, y, kg)
BEATS = [
 ("doing nothing with you is my favourite thing", "room('#bcd2ee','#acc2de','rgba(255,255,255,.12)');tv(540,G-330,1.1);" + P() + "blanket(300,780,G-30,'#fbf5ec');popcorn(540,G+30,.7);", 2.6),
 ("you turn normal days into good ones", "room('#fbe2d6','#f2d2c4','rgba(255,255,255,.12)');flower(220,G+60,1);flower(880,G+60,.9);" + P('open','open') + "heart(540,G-380,22,'#ec7489');", 2.0),
 ("i love what we are", "room('#bfd8c2','#afc8b2','rgba(255,255,255,.12)');rain(40,.7);puddle(540,G+70,500);" + P('closed','closed') + "umbrella(540,G-420,1.1,'#fbf1e2');", 2.2),
 ("thank you for choosing me, again and again", "room('#d6c8f0','#c6b8e0','rgba(255,255,255,.12)');" + P('closed','closed') + "bigHeart(540,G-40,.42,'#f29bb3');sparkle(300,700,22);sparkle(800,760,18);", 3.1),
 ("you feel like home", "room('#f7e6b0','#ead8a0','rgba(255,255,255,.12)');bed(540,G+60,640);pillow(450,G-80);pillow(640,G-80);" + P('closed','closed','', 'G-50').replace('s:1.05','s:.9') + "quilt(540,G+170,640,'#fbf5ec');cupS(900,G+50,'#9fbf9a');", 2.4),
 ("you're my person", "room('#fbe8de','#f2dcd0','rgba(255,255,255,.12)');line([[540,G-260],[560,G-480]],{lw:3});heart(560,G-560,60,'#f08a80');" + P() + "floatHearts(540,G-300,0,u,2,80);", 2.1),
 ("you're my calm when it's chaos", "room('#a8d4f0','#98c4e0','rgba(255,255,255,.1)');crescent(800,520,50,'#a8d4f0');ctx.save();ctx.fillStyle='#7fb8e0';ctx.fillRect(-200,G+20,W+400,800);ctx.restore();blob([[260,G-90],[820,G-90],[740,G+40],[340,G+40]],'#e0b888');" + P('closed','closed','', 'G-70').replace('s:1.05','s:.95'), 1.7),
 ("you're the best part of every single day", "room('#f7d8dc','#ecc8cc','rgba(255,255,255,.12)');" + P('closed','closed') + "bigHeart(540,G-40,.38,'#f29bb3');floatHearts(540,G-360,0,u,3,90);", 0),
]
