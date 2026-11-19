"""Remake of @dinklygame DcbqU-TAFj9 ('it's always you', 29.7M views, 18.83s, song: Goo Goo Dolls - Iris).
Structure copied: 4 short 'we ___, i still love you.' beats -> one long paragraph -> one closing line.
Lines are new (same frame), JJ pups, Dinkly flat pastel look. Silent: Iris is added in-app."""
TARGET = 18.833
SONG = 'Goo Goo Dolls - Iris'
CAPTION = "it's always been you ❤️\n\n#couplegoals #relationships #soulmates #loveyou #cartoons"

BEATS = [
    ("we bicker,\ni still love you.", r'''
room('#d9a9a6','#c98f8a','rgba(255,255,255,.10)');lamp(880,700,1);
sofa('#e7a48f','#f0b5a0');
pup({kind:'girl',x:370,y:G-150,s:0.95,eyes:'open',look:[-1,0],brows:'angry',mouth:'pout',shadow:false,tilt:-.1,blink:.3});
pup({kind:'boy',x:705,y:G-150,s:0.95,flip:-1,eyes:'open',look:[-1,0],brows:'angry',mouth:'flat',shadow:false,tilt:-.1});
''', 4.3),
    ("we're both exhausted,\ni still love you.", r'''
room('#7a6f8f','#665c7a','rgba(255,255,255,.06)');lamp(150,720,1);
sofa('#c7889a','#d499aa');
pup({kind:'girl',x:400,y:G-150,s:1.0,eyes:'closed',mouth:'flat',shadow:false,tilt:.18,squash:.96});
pup({kind:'boy',x:690,y:G-150,s:1.0,eyes:'closed',mouth:'flat',shadow:false,tilt:-.12,squash:.96});
blob(rectPts(380,G+60,320,40,16),'#8a6a52');mug(470,G+60,.5);mug(610,G+60,.5);
''', 1.6),
    ("you've had a long day,\ni still love you.", r'''
room('#f2c46d','#e3ae5a','rgba(255,255,255,.14)');
pup({kind:'girl',x:450,y:G+40,s:1.1,eyes:'closed',brows:'sad',mouth:'flat',shadow:true,tilt:.16});
pup({kind:'boy',x:650,y:G+40,s:1.1,flip:-1,eyes:'happy',mouth:'smile',blush:.6,tilt:-.15,paw:{k:1,x:150,y:-120}});
floatHearts(560,700,0,u,3,90);
''', 3.0),
    ("we're miles apart,\ni still love you.", r'''
sky('#26325a','#46507e');stars(40);crescent(180,560,50,'#26325a');constellation(540,820,12,u);
hill('#7fae9b',1300);
pup({kind:'girl',x:330,y:1430,s:0.9,eyes:'open',look:[1,-1],mouth:'smile',shadow:false});
pup({kind:'boy',x:750,y:1430,s:0.9,flip:-1,eyes:'open',look:[1,-1],mouth:'smile',shadow:false});
''', 2.9),
    ("nothing in this world could ever change how i feel about you. whatever we go through, at the end of every day, i will always choose you.", r'''
sky('#1f2a4d','#3b4672');stars(46);fireflyHeart(540,800,13);
hill('#5d8a7d',1320);
pup({kind:'boy',x:370,y:1440,s:1.1,eyes:'happy',mouth:'smile',blush:.4,shadow:false,tilt:.08});
pup({kind:'girl',x:710,y:1440,s:1.1,flip:-1,eyes:'happy',mouth:'smile',blush:.4,shadow:false,tilt:.08});
''', 5.2),
    ("it's still you.\nit was always\ngoing to be you.", r'''
sky('#8fb4dd','#c7d8ee');crescent(880,620,50,'#9cbde2');stars(10,.6);
hill('#9cc7a8',1260);
pup({kind:'girl',x:680,y:1380,s:1.15,flip:-1,eyes:'happy',mouth:'smile',blush:.7,shadow:false,tilt:.1});
pup({kind:'boy',x:420,y:1380,s:1.15,eyes:'happy',mouth:'smile',blush:.7,shadow:false,tilt:.1,paw:{k:1,x:150,y:-70}});
floatHearts(530,880,0,u,4,110);
''', 0),
]
