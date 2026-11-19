"""Remake of @dinklygame Db_Sl6sA8bd (2.0M, 13.0s, original audio). 'I WILL ALWAYS / CHOOSE / YOU' then a quick montage."""
TARGET = 13.002
SONG = "the source reel's own audio (open instagram.com/reel/Db_Sl6sA8bd > Use audio)"
CAPTION = "i will always choose you 🤍\n\n#couplegoals #relationshiptips #loveyou #soulmate #lovestory"
O = {'style': 'outline', 'size': 150, 'y': 320}
def ring(x, y): return "blob(rectPts(%d,%d,70,50,8),'#a0522d');ell(%d,%d,18,18,'none',{lw:7,sc:'#f7c948'});sparkle(%d,%d,22);" % (x-35, y-50, x, y-62, x+30, y-90)
BEATS = [
 ("I will always", r'''room('#e0a94a','#c98f3a','rgba(255,255,255,.12)');ctx.save();ctx.fillStyle='#8a5a3c';ctx.beginPath();ctx.ellipse(540,G+60,440,80,0,0,7);ctx.fill();ctx.restore();
pup({kind:'boy',x:400,y:G+40,s:1.05,eyes:'happy',mouth:'smile',blush:.8,paw:{k:1,x:150,y:-80}});pup({kind:'girl',x:690,y:G+40,s:1.05,flip:-1,eyes:'open',mouth:'o',blush:.8});flower(560,G-60,.9);''', 1.2, O),
 ("Choose", r'''room('#b9867a','#a9766a','rgba(255,255,255,.08)');ctx.save();ctx.fillStyle='#d8c2a8';ctx.beginPath();ctx.arc(540,800,300,Math.PI,0);ctx.lineTo(840,G);ctx.lineTo(240,G);ctx.fill();ctx.restore();
pup({kind:'boy',x:470,y:G+40,s:1.05,eyes:'closed',mouth:'smile',blush:.9,paw:{k:1,x:150,y:-110}});pup({kind:'girl',x:610,y:G+40,s:1.05,flip:-1,eyes:'closed',mouth:'smile',blush:.9});''', 1.3, O),
 ("You", r'''sky('#f6c6b8','#fbe2d2');for(let i=0;i<14;i++){ctx.save();ctx.globalAlpha=.8;ell(hash(i)*W,fract(T*.2+hash(i+3))*1400+300,10,7,'#ffffff',{stroke:false});ctx.restore();}
pup({kind:'boy',x:420,y:G+60,s:1.05,eyes:'happy',mouth:'open',blush:.9});pup({kind:'girl',x:660,y:G+60,s:1.05,flip:-1,eyes:'wide',mouth:'o',blush:1});''' + ring(540, 1150) + "floatHearts(540,G-360,0,u,3,90);", 2.5, O),
 ("", r'''sunset('#f2b78a','#f8d8b0');bench(540,G+40,460,'#8a6a52');
pup({kind:'girl',x:400,y:G-110,s:.9,eyes:'happy',mouth:'open',blush:1,tilt:.12});pup({kind:'boy',x:680,y:G-110,s:.9,flip:-1,eyes:'happy',mouth:'open',blush:1,tilt:.12});heart(540,G-440,26,'#ec7489');''', 1.5),
 ("", r'''sky('#f8d6d6','#fde8e0');ctx.fillStyle='#cfe0f2';ctx.fillRect(-200,G+20,W+400,800);
pup({kind:'girl',x:350,y:G+60,s:1.0,eyes:'wide',mouth:'o',blush:1});pup({kind:'boy',x:740,y:G+60,s:1.0,flip:-1,eyes:'happy',mouth:'smile',blush:.9,paw:{k:1,x:150,y:-60}});bouquet(545,G-30,1.45);heart(545,G-430,26,'#ec7489');''', 1.3),
 ("", r'''room('#5f7a5f','#506a50','rgba(255,255,255,.06)');
pup({kind:'boy',x:700,y:G+50,s:1.05,flip:-1,eyes:'closed',mouth:'smile',blush:.9,tilt:.12,paw:{k:1,x:230,y:-90}});pup({kind:'girl',x:370,y:G+50,s:1.05,eyes:'closed',mouth:'smile',blush:.9,tilt:.15});heart(540,G-470,26,'#f29bb3');''', 1.3),
 ("", r'''room('#fbe9da','#efd9c6','rgba(255,255,255,.12)');
pup({kind:'boy',x:350,y:G+50,s:1.0,eyes:'happy',mouth:'open',blush:.7});pup({kind:'girl',x:740,y:G+50,s:1.0,flip:-1,eyes:'happy',mouth:'smile',blush:.7});
blob(rectPts(410,G-40,260,26,6),'#555');for(let i=0;i<6;i++)heart(450+(i%3)*90,G-60-Math.floor(i/3)*34,16,'#7a4a2a');''', 1.2),
 ("", r'''room('#f3e6cf','#e3d6bf','rgba(255,255,255,.12)');pup({kind:'boy',x:400,y:G-20,s:.95,eyes:'happy',mouth:'chomp'});pup({kind:'girl',x:680,y:G-20,s:.95,flip:-1,eyes:'happy',mouth:'smile'});
table(540,G+80,520,'#a07a5a');plate(470,G-72,.8,'#e8b04a');friesBag(610,G-70,.6);''', 1.1),
 ("", r'''room('#c8d6ea','#b8c6da','rgba(255,255,255,.12)');
pup({kind:'girl',x:350,y:G+50,s:1.0,eyes:'wide',mouth:'o',blush:1});pup({kind:'boy',x:740,y:G+50,s:1.0,flip:-1,eyes:'happy',mouth:'smile',blush:.7,paw:{k:1,x:150,y:-60}});gift(545,G+10,.9);''', 1.0),
 ("", r'''sky('#2a3448','#3a465c');rain(70);ctx.fillStyle='#4a5468';ctx.fillRect(-200,G+20,W+400,800);
pup({kind:'girl',x:370,y:G+40,s:1.05,eyes:'closed',mouth:'smile',blush:1,tilt:.15,shadow:false});pup({kind:'boy',x:710,y:G+40,s:1.05,flip:-1,eyes:'closed',mouth:'smile',blush:1,tilt:.15,shadow:false});
blob([[250,G-30],[540,G-50],[830,G-30],[870,G+60],[210,G+60]],'#c9b8e6');ctx.save();ctx.globalAlpha=.3;line([[420,G-90],[440,G+30]],{c:'#fff',lw:6});line([[640,G-90],[620,G+30]],{c:'#fff',lw:6});ctx.restore();
umbrella(553,G-520,1.3,'#e8484f');heart(540,G-640,0,'#fff');''', 0),
]
