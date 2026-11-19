"""Remake of @dinklygame DdzIFdxg26f (14.9M, 26.23s, 'Stuff We Did' from Up, piano). Ages 30->90, then the moon, then the next-life line."""
TARGET = 26.233
SONG = "your movie soundtrack - Stuff We Did (from 'Up') (Piano Version)"
CAPTION = "i'll always love you 🫶\n\n#relationshipgoals #loveyou #soulmate #afterlife #couples"
B = lambda kb, kg='': None
BEATS = [
 ("i'll love you\nat 30.", r'''room('#6f8577','#5f7568','rgba(255,255,255,.06)');lamp(880,700,1);roundTable(540,G+20,150,'#f3c6c6');
pup({kind:'girl',x:360,y:G,s:1,eyes:'happy',mouth:'smile',tilt:.08});pup({kind:'boy',x:720,y:G,s:1,flip:-1,eyes:'happy',mouth:'smile',tilt:.08});cupS(500,G-130,'#fbf5ec',.9);cupS(590,G-130,'#f29bb3',.9);''', 2.0),
 ("i'll love you\nat 40.", r'''room('#d8d4ec','#c9c4e2','rgba(255,255,255,.12)');sofa('#a9b8d9','#b9c7e6');
pup({kind:'girl',x:440,y:G-150,s:.95,eyes:'happy',mouth:'smile',tilt:.12});pup({kind:'boy',x:640,y:G-150,s:.95,flip:-1,eyes:'happy',mouth:'open',tilt:.12});blanket(300,780,G-200,'#f3ead9');popcorn(540,G-120,.8);''', 2.1, {'col':'#3b3550'}),
 ("i'll love you\nat 50.", r'''sky('#8fb0cc','#b9cfe0');hill('#c9dae6',1240);ctx.save();ctx.globalAlpha=.6;cloud(250,520,.8,'#ffffff');cloud(850,600,.6,'#ffffff');ctx.restore();
pup({kind:'boy',x:420,y:G+60,s:1.05,eyes:'happy',mouth:'smile',paw:{k:1,x:150,y:-70}});pup({kind:'girl',x:660,y:G+60,s:1.05,flip:-1,eyes:'happy',mouth:'open'});''', 2.0, {'col':'#2f3e4f'}),
 ("i'll love you\nat 60.", r'''room('#7c6a86','#6c5b77','rgba(255,255,255,.05)');tree(880,G-60,1.2,'#b8a6d9');picnic(540,G+30,520);
pup({kind:'girl',x:420,y:G+20,s:1,eyes:'happy',mouth:'smile'});pup({kind:'boy',x:660,y:G+20,s:1,flip:-1,eyes:'happy',mouth:'chomp',old:0});cookie(540,G-10,30);''', 2.1),
 ("i'll love you\nat 70.", r'''sunset('#e7a0a8','#f8d2c0');seaLine('#c98aa0',1080);bench(540,G+40,460,'#7a8f7a');
pup({kind:'girl',x:395,y:G-110,s:.95,eyes:'closed',mouth:'smile',tilt:.15,old:1});pup({kind:'boy',x:685,y:G-110,s:.95,flip:-1,eyes:'closed',mouth:'smile',tilt:.15,old:1});''', 2.0),
 ("i'll love you\nat 80.", r'''sky('#5d7486','#7f95a6');hill('#6f8a86',1230);ctx.save();ctx.fillStyle='#e7c7b8';ctx.beginPath();ctx.moveTo(300,1300);ctx.quadraticCurveTo(600,1240,900,1320);ctx.lineTo(900,1360);ctx.quadraticCurveTo(600,1290,300,1340);ctx.fill();ctx.restore();
pup({kind:'girl',x:385,y:G+80,s:1.05,eyes:'happy',mouth:'smile',old:1});pup({kind:'boy',x:695,y:G+80,s:1.05,flip:-1,eyes:'happy',mouth:'smile',old:1,paw:{k:1,x:150,y:-70}});''', 2.0),
 ("i'll love you\nat 90.", r'''sky('#3e5560','#5a7480');stars(20,.6);crescent(820,560,46,'#3e5560');bench(540,G+40,420,'#6f8a7a');
pup({kind:'girl',x:405,y:G-110,s:.9,eyes:'closed',mouth:'smile',tilt:.18,old:1});pup({kind:'boy',x:675,y:G-110,s:.9,flip:-1,eyes:'closed',mouth:'smile',tilt:.18,old:1});heart(540,G-400,26,'#ec7489',.8+.2*Math.sin(T*3));''', 2.0),
 ("i'll love you long after the years stop counting.", r'''sky('#1f2a4d','#3b4672');stars(50);moonBig(540,1000,190);for(let i=0;i<5;i++){ctx.save();ctx.globalAlpha=.85;cloud(120+i*220,1240+(i%2)*30,.9,'#4a5480');ctx.restore();}''', 4.0),
 ("and if there's another life after this one, i'll find you first and love you all over again.", r'''sky('#1d2b26','#34463d');for(let i=0;i<40;i++){ctx.save();ctx.globalAlpha=.4+.4*Math.sin(T*2+i);ctx.fillStyle='rgba(255,236,150,.6)';ctx.beginPath();ctx.arc(hash(i*3.7)*W,hash(i*1.9)*1400+400,5+hash(i)*5,0,7);ctx.fill();ctx.restore();}
ctx.save();const g=ctx.createRadialGradient(540,1050,10,540,1050,380);g.addColorStop(0,'rgba(255,230,160,.35)');g.addColorStop(1,'rgba(255,230,160,0)');ctx.fillStyle=g;ctx.fillRect(0,600,W,900);ctx.restore();
butterfly(460+Math.sin(T*.8)*30,1080,1.7,'#f7c948');butterfly(650+Math.cos(T*.7)*30,960,1.5,'#f2a8a0');''', 0, {'size': 62}),
]
