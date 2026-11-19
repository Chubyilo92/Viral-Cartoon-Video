"""Remake of @dinklygame De-B_Q1g13l (3.4M, 13.0s, Justin Hurwitz - Mia & Sebastian's Theme). Bold black caps."""
TARGET = 13.002
STYLE = 'bold'
SONG = "Justin Hurwitz - Mia & Sebastian's Theme"
CAPTION = "let's fall in love every day 🫶\n\n#couples #soulmate #relationshiptips #lovestory #loveyou"
BEATS = [
 ("I never want us to drift apart.", r'''room('#b8a8c8','#a898b8','rgba(255,255,255,.1)');frame(140,560,150,180,null);sofa('#8a7aa0','#9a8ab0');
pup({kind:'boy',x:350,y:G-150,s:.9,eyes:'open',look:[.5,.8],mouth:'flat'});phoneS(420,G-170,.8);pup({kind:'girl',x:730,y:G-150,s:.9,flip:-1,eyes:'open',look:[.5,.8],mouth:'flat'});phoneS(660,G-170,.8);''', 2.3),
 ("To stop asking how the other's day was.", r'''room('#a9bfa9','#99af99','rgba(255,255,255,.1)');lamp(900,760,1);pup({kind:'boy',x:360,y:G-10,s:.95,eyes:'open',look:[0,.8],mouth:'flat'});pup({kind:'girl',x:720,y:G-10,s:.95,flip:-1,eyes:'open',look:[0,.8],mouth:'flat'});table(540,G+60,520,'#a07a5a');plate(440,G-92,.8);plate(640,G-92,.8);''', 2.6),
 ("To get so busy we forget about us.", r'''room('#e3d6c8','#d3c6b8','rgba(255,255,255,.1)');door(540,G,0,'#c9b8a8');
pup({kind:'boy',x:340,y:G+40,s:.95,eyes:'open',look:[-1,0],mouth:'flat'});suitcase(200,G+40,.55);pup({kind:'girl',x:745,y:G+40,s:.95,flip:-1,eyes:'open',look:[-1,0],mouth:'flat'});''', 2.6),
 ("So let's keep making time,", r'''room('#b8a8c8','#a898b8','rgba(255,255,255,.1)');lamp(180,700,1);sofa('#8a7aa0','#9a8ab0');table(540,G+60,300,'#6a5a4a');phoneS(500,G-90,.6,0);phoneS(580,G-90,.6,0);
pup({kind:'boy',x:430,y:G-150,s:.9,eyes:'happy',mouth:'smile',blush:.7,tilt:.1});pup({kind:'girl',x:650,y:G-150,s:.9,flip:-1,eyes:'happy',mouth:'smile',blush:.7,tilt:.1});''', 2.6),
 ("And keep falling for each other, over and over.", r'''sky('#c9b8e0','#e0d4ee');tree(140,G+40,1.0,'#8fbf8a');tree(950,G+40,.9,'#8fbf8a');hill('#a8d0a0',1220);
pup({kind:'boy',x:420,y:G+60,s:1.05,eyes:'happy',mouth:'smile',blush:.8,paw:{k:1,x:160,y:-70}});pup({kind:'girl',x:660,y:G+60,s:1.05,flip:-1,eyes:'happy',mouth:'smile',blush:.8});floatHearts(540,G-330,0,u,3,90);''', 0),
]
