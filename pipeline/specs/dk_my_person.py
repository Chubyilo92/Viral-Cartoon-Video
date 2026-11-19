"""Remake of @dinklygame DcjTOpvhj08 (2.1M, 15.7s, Coldplay - The Scientist). Four cards, each three stacked mini-scenes with one word."""
TARGET = 15.7
SONG = 'Coldplay - The Scientist'
CAPTION = "you're my person 🫶\n\n#soulmate #relationshiptips #loveyou #lovestory #couples"
PRELUDE = r'''
function row(y,word,fn,u){ctx.save();ctx.font='84px Neucha';ctx.fillStyle='#2b2b2b';ctx.textAlign='center';ctx.fillText(word,540,y+70);ctx.restore();
  ctx.save();ctx.translate(540,y+500);ctx.scale(.8,.8);fn(u);ctx.restore();}
function card(words,fns,u){ctx.fillStyle='#fbeee4';ctx.fillRect(0,0,W,H);[200,760,1320].forEach((y,i)=>row(y,words[i],fns[i],u));}
const P2=(eb,eg,mb='smile',mg='smile',dx=170,ex='')=>{pup({kind:'boy',x:-dx,y:0,s:1,eyes:eb,mouth:mb,blush:.6});pup({kind:'girl',x:dx,y:0,s:1,flip:-1,eyes:eg,mouth:mg,blush:.6});};
'''
BEATS = [
 ("", r'''card(['cracked','mend','stronger'],[
  u=>{P2('open','open','flat','flat',260);bigHeart(0,-170,.55,'#f29bb3',1);},
  u=>{P2('happy','open','smile','smile',200);bigHeart(0,-170,.55,'#f29bb3',.25);bandage(0,-180,.5);},
  u=>{P2('happy','happy','smile','smile',150);bigHeart(0,-200,.6,'#ec7489');}],u);''', 4.0, {'raw': True}),
 ("", r'''card(['plant','water','bloom'],[
  u=>{P2('open','open','smile','smile',230);sprout(0,0,.8,0);},
  u=>{P2('happy','open','smile','o',230);sprout(0,0,.8,1.5);for(let i=0;i<5;i++){ctx.save();ctx.globalAlpha=.8;ell(-30+i*15,-260+fract(T*1.5+i*.2)*120,6,9,'#7fb8e0',{stroke:false});ctx.restore();}},
  u=>{P2('happy','happy','open','smile',230);sprout(0,0,.8,3);floatHearts(0,-380,0,u,2,60);}],u);''', 4.1, {'raw': True}),
 ("", r'''card(['empty','fill','full'],[
  u=>{P2('open','open','flat','flat',220);jar(0,0,0);},
  u=>{P2('happy','happy','smile','smile',220);jar(0,0,.5);heart(0,-260+fract(T)*60,16,'#ec7489');},
  u=>{P2('happy','happy','open','smile',220);jar(0,0,1);}],u);''', 4.0, {'raw': True}),
 ("", r'''card(['wait','hope','home'],[
  u=>{door(-60,0,0);pup({kind:'girl',x:200,y:0,s:1,flip:-1,eyes:'open',look:[-1,0],mouth:'flat',brows:'sad'});},
  u=>{door(-60,0,.7);pup({kind:'girl',x:200,y:0,s:1,flip:-1,eyes:'wide',look:[-1,0],mouth:'o'});pup({kind:'boy',x:-60,y:0,s:.9,eyes:'happy',mouth:'smile'});},
  u=>{door(-260,0,.7);pup({kind:'boy',x:-60,y:0,s:1,eyes:'closed',mouth:'smile',blush:.9,paw:{k:1,x:160,y:-110}});pup({kind:'girl',x:110,y:0,s:1,flip:-1,eyes:'closed',mouth:'smile',blush:.9});floatHearts(30,-330,0,u,3,70);}],u);''', 0, {'raw': True}),
]
