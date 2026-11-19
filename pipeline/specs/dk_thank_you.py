"""Remake of @dinklygame Ddw9wJwRH0Q (5.2M, 24.01s, Goo Goo Dolls - Iris). Six 4-second thank-you notes."""
TARGET = 24.008
SONG = 'Goo Goo Dolls - Iris'
CAPTION = "thank you for loving me ❤️\n\n#loveyou #soulmate #couplegoals #relationshiptips #lovestory"
BEATS = [
 ("i don't tell you this enough, so here it is: thank you for how you love me.", r'''sky('#24345e','#e8a58a');stars(30,.8);hill('#4d6a5a',1250);
pup({kind:'girl',x:430,y:G+90,s:1.1,eyes:'closed',mouth:'smile',tilt:.15});pup({kind:'boy',x:650,y:G+90,s:1.1,flip:-1,eyes:'closed',mouth:'smile',tilt:.15});''', 4.0),
 ("when i feel like i'm not enough, you remind me that i am.", r'''room('#5f6f68','#536159','rgba(255,255,255,.05)');frame(160,560,160,190,null);
pup({kind:'girl',x:390,y:G+40,s:1.15,eyes:'closed',mouth:'smile',blush:.8,tilt:.12});pup({kind:'boy',x:700,y:G+40,s:1.15,flip:-1,eyes:'closed',mouth:'smile',blush:.8,tilt:-.1,paw:{k:1,x:190,y:-110}});''', 4.1),
 ("when i doubt myself, you never doubt me for a second.", r'''sky('#1f2c45','#34445f');for(let i=0;i<6;i++){blob(rectPts(40+i*180,700-hash(i)*200,140,700,6),'#2a3854',{lw:3});for(let k=0;k<6;k++)if(hash(i*10+k)>.5){ctx.fillStyle='#f7d98a';ctx.fillRect(70+i*180+(k%2)*50,760-hash(i)*200+Math.floor(k/2)*80,26,34);}}
ctx.fillStyle='#3a4a5c';ctx.fillRect(-200,G,W+400,800);bench(540,G+40,460,'#5a6a7a');
pup({kind:'girl',x:420,y:G-110,s:.95,eyes:'closed',mouth:'smile',tilt:.18});pup({kind:'boy',x:660,y:G-110,s:.95,flip:-1,eyes:'happy',mouth:'smile',tilt:.12});''', 4.0),
 ("when everything feels too loud, you're my quiet place.", r'''room('#3e4a6b','#34405c','rgba(255,255,255,.05)');lamp(860,720,1);sofa('#6a7aa0','#7a8ab0');
pup({kind:'boy',x:440,y:G-150,s:.95,eyes:'closed',mouth:'smile',tilt:.15});pup({kind:'girl',x:650,y:G-150,s:.95,flip:-1,eyes:'closed',mouth:'smile',tilt:.18});blanket(330,780,G-190,'#e3d4f0');''', 4.0),
 ("thank you for your patience, your kindness, and for loving me on the days i find it hard to love myself.", r'''room('#a86a5f','#955c52','rgba(255,255,255,.06)');lamp(200,720,1);
pup({kind:'girl',x:390,y:G+40,s:1.15,eyes:'closed',mouth:'smile',blush:.8,tilt:.12});pup({kind:'boy',x:700,y:G+40,s:1.15,flip:-1,eyes:'closed',mouth:'smile',blush:.8,tilt:-.1,paw:{k:1,x:190,y:-110}});''', 3.9, {'size': 60}),
 ("you've never once asked me to be anyone but me.", r'''room('#4a5a78','#3f4d68','rgba(255,255,255,.05)');windowBox(360,760,360,250,()=>{sky('#1f2a4d','#2c3a63');stars(12);});
blob(rectPts(80,G-260,920,40,10),'#6a7a98');pup({kind:'boy',x:420,y:G+60,s:1.05,eyes:'happy',mouth:'smile'});pup({kind:'girl',x:660,y:G+60,s:1.05,flip:-1,eyes:'happy',mouth:'smile'});''', 0),
]
