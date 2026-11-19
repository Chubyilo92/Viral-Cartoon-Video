"""Remake of @dinklygame DdXMTX0Bkom (1.8M, 19.03s, 'Stuff We Did' from Up, piano). Dark handwritten caps."""
TARGET = 19.033
STYLE = 'caps'
SONG = "your movie soundtrack - Stuff We Did (from 'Up') (Piano Version)"
CAPTION = "so happy i met you ❤️\n\n#relationshiptips #soulmate #loveyou #couplegoals #lovestory"
BEATS = [
 ("Thank you for showing me healthy love is real", r'''room('#9fbf9a','#8faf8a','rgba(255,255,255,.12)');
pup({kind:'girl',x:440,y:G+60,s:1.1,eyes:'happy',mouth:'smile',blush:.8,tilt:.08});pup({kind:'boy',x:640,y:G+60,s:1.1,flip:-1,eyes:'happy',mouth:'smile',blush:.8,tilt:.08});''', 3.6),
 ("And for helping me grow", r'''room('#a9b8f0','#99a8e0','rgba(255,255,255,.12)');sprout(540,G+60,1.0,clamp(u/1.2)*3);
pup({kind:'boy',x:330,y:G+60,s:1,eyes:'happy',mouth:'smile'});pup({kind:'girl',x:760,y:G+60,s:1,flip:-1,eyes:'open',mouth:'open'});''', 3.5),
 ("However bad my day, you make it feel okay", r'''room('#c9b8e8','#b9a8d8','rgba(255,255,255,.12)');bed(540,G+60,700);pillow(430,G-80);pillow(650,G-80);
pup({kind:'girl',x:440,y:G-50,s:.9,eyes:'closed',mouth:'smile',tilt:.18,shadow:false});pup({kind:'boy',x:640,y:G-50,s:.9,flip:-1,eyes:'closed',mouth:'smile',tilt:.18,shadow:false});quilt(540,G+160,700,'#a8c4ec');''', 4.0),
 ("In a world this big, I refuse to believe finding you was just luck", r'''sky('#141a2e','#1f2945');stars(60);ctx.save();ctx.fillStyle='#e8e0c8';ctx.beginPath();ctx.arc(540,2000,900,0,7);ctx.fill();ctx.strokeStyle=INK;ctx.lineWidth=6;ctx.stroke();
for(let i=0;i<8;i++){ctx.fillStyle='#cfc6aa';ctx.beginPath();ctx.ellipse(200+hash(i)*700,1250+hash(i+3)*500,30+hash(i+1)*40,14+hash(i+2)*14,0,0,7);ctx.fill();}ctx.restore();
pup({kind:'girl',x:470,y:G+60,s:1.05,eyes:'happy',mouth:'smile',blush:.8,tilt:.12});pup({kind:'boy',x:620,y:G+60,s:1.05,flip:-1,eyes:'happy',mouth:'smile',blush:.8,tilt:.12});''', 0, {'col': '#fffdf7'}),
]
