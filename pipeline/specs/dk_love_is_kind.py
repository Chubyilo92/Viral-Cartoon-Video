"""Remake of @dinklygame Dbrd2D-BLw3 (9.1M, 18.2s, Ross Lara - Love Is Like The Wind)."""
TARGET = 18.2
SONG = 'Ross Lara - Love Is Like The Wind'
CAPTION = "love is kind 🤍\n\n#couplegoals #loveiskind #relationships #cartoons #loveyou"
BEATS = [
 ("we fight.", r'''room('#2f3a4a','#28303d','rgba(255,255,255,.04)');lamp(540,720,1);sofa('#8a7a9a','#9a8aaa');
pup({kind:'girl',x:345,y:G-150,s:.95,eyes:'open',look:[-1,0],brows:'angry',mouth:'pout',shadow:false});pup({kind:'boy',x:735,y:G-150,s:.95,flip:-1,eyes:'open',look:[-1,0],brows:'sad',mouth:'flat',shadow:false});''', 2.1),
 ("we make up.", r'''room('#e9b44c','#d9a03c','rgba(255,255,255,.12)');ctx.save();ctx.fillStyle='#b97a3a';ctx.beginPath();ctx.ellipse(540,G+60,420,80,0,0,7);ctx.fill();ctx.restore();
pup({kind:'boy',x:400,y:G+30,s:1.05,eyes:'happy',mouth:'smile',blush:.8,paw:{k:1,x:150,y:-90}});pup({kind:'girl',x:690,y:G+30,s:1.05,flip:-1,eyes:'open',mouth:'o',blush:.8});flower(560,G-70,1.0);heart(560,G-380,24,'#ec7489');''', 2.0),
 ("we get it wrong.", r'''room('#8a4b4a','#7a403f','rgba(255,255,255,.05)');lamp(540,700,1);sofa('#d9806b','#e3907c');table(540,G+60,300,'#3b2f2a');cupS(480,G-90);cupS(600,G-90);
pup({kind:'girl',x:345,y:G-150,s:.95,eyes:'open',look:[-1,.4],brows:'sad',mouth:'flat',shadow:false});pup({kind:'boy',x:735,y:G-150,s:.95,flip:-1,eyes:'open',look:[-1,.4],brows:'sad',mouth:'flat',shadow:false});''', 2.1),
 ("we talk it out.", r'''sky('#2e5d7a','#3c6e8c');flowerField(1050);
pup({kind:'girl',x:420,y:G+60,s:1.05,eyes:'happy',mouth:'open',blush:.7});pup({kind:'boy',x:660,y:G+60,s:1.05,flip:-1,eyes:'open',mouth:'smile',blush:.7});heart(540,G-330,22,'#ec7489');''', 2.0),
 ("until one day we realise...", r'''sky('#24382e','#33493c');tree(140,G+40,1.1,'#2f5a3f');tree(960,G+40,1.0,'#2f5a3f');rain(70);
pup({kind:'boy',x:420,y:G+60,s:1.05,eyes:'closed',mouth:'smile',tilt:.15});pup({kind:'girl',x:660,y:G+60,s:1.05,flip:-1,eyes:'closed',mouth:'smile',tilt:.15});umbrella(540,G-440,1.1,'#e8484f');''', 2.1),
 ("love isn't only the easy days. it's growing, learning and choosing each other through the hard ones too.", r'''sky('#d9874a','#e8a05a');for(let i=0;i<60;i++){const x=hash(i*2.1)*W,y=1000+hash(i*4.3)*700;ctx.save();ctx.translate(x,y);ctx.rotate(Math.sin(T+i)*.2);blob([[0,0],[-10,-90],[0,-110],[10,-90]],i%2?'#f0b060':'#c96a2a',{lw:3});ctx.restore();}
pup({kind:'girl',x:470,y:G+80,s:1.1,eyes:'closed',mouth:'smile',tilt:.18,blush:.8});pup({kind:'boy',x:610,y:G+80,s:1.1,flip:-1,eyes:'closed',mouth:'smile',tilt:.18,blush:.8});
blob([[300,G+25],[780,G+25],[830,G+120],[250,G+120]],'#c98a5a');''', 0, {'size': 60}),
]
