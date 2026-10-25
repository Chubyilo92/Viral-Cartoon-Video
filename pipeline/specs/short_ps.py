HOOK = "I don't say it enough... so the puppies will 🐾"
BEATS = [
("you always save me the last bite 🍪", '''  room('#f6d7b0','#d8a878');
  blob(rectPts(330,G-150,420,30,10),'#b98a5e');blob(rectPts(360,G-120,30,120,6),'#a07450');blob(rectPts(690,G-120,30,120,6),'#a07450');
  const sl=P(u,.5,1.6);
  cookie(lerp(470,620,sl),G-186,40);
  pup({kind:'boy',x:280,y:G+10,s:1.25,look:[.7,.4],eyes:'happy',mouth:'smile',paw:{x:130,y:-140,k:1-P(u,1.6,2.2)}});
  pup({kind:'girl',x:800,y:G+10,s:1.25,flip:-1,look:[-.6,.4],eyes:u>1.8?'happy':'open',mouth:u>1.8?'smile':'o',blush:u>1.8?.6:0});''', 3.2),
("you listen to my work drama like it's your favourite show 🍿", '''  room('#d9c7e6','#a993bb');couch();
  const ch=Math.floor(u*4)%2;
  pup({kind:'girl',x:340,y:G-90,s:1.15,look:[.7,0],eyes:'squint',mouth:'open',brows:'angry',tilt:Math.sin(u*7)*.06,shadow:false});
  pup({kind:'boy',x:730,y:G-90,s:1.15,flip:-1,look:[-.8,0],eyes:'wide',mouth:ch?'chomp':'o',shadow:false,paw:{x:60,y:-130,k:1}});
  popcorn(650,G-120,.7);
  bubbleText(360,640,"and THEN she said...",win(u,.3,9),1.15);''', 3.8),
("you let me put my freezing feet on you 🥶", '''  bedNight();bedBack();
  pup({kind:'girl',x:370,y:G-100,s:1.1,look:[.6,.2],eyes:'happy',mouth:'smile',blush:.4,shadow:false});
  const jolt=u>1?Math.max(0,1-(u-1)*1.6)*Math.sin(u*40)*10:0;
  pup({kind:'boy',x:720+jolt,y:G-100-(u>1?Math.max(0,1-(u-1)*2)*30:0),s:1.1,flip:-1,look:[-.7,.3],eyes:u>1?'wide':'happy',mouth:u>1?'o':'smile',earLift:u>1?.7:0,shadow:false});
  blanket(150,935,G-190);
  if(u>1){for(let i=0;i<3;i++)snowflake(820+i*45-((u-1)*10),G-420-i*55-((u-1)*30),24,win(u,1,9));}''', 3.4),
("and you still look at me like that 🥹", '''  room('#f3cfa8','#d09d72');
  pup({kind:'girl',x:330,y:G+10,s:1.3,look:[.4,0],eyes:'open',mouth:'smile'});
  pup({kind:'boy',x:760,y:G+10,s:1.3,flip:-1,look:[-.7,0],eyes:'happy',mouth:'smile',blush:.9,tilt:-.08,earLift:.2});
  for(let i=0;i<2;i++)heart(760+(i?-44:44)*1.3,G-305+Math.sin(u*6)*4,30*pop(u,.4,.4));
  if(u>.8)floatHearts(760,760,.8,u,4,120);''', 3.0),
("so thank you. for all of it 🤍", '''  room('#f1d5b0','#caa070');plant(990,G+6,.8);
  const hug=P(u,.3,1.2);
  pup({kind:'boy',x:lerp(380,430,hug),y:G+10,s:1.34,look:[.4,.1],eyes:'happy',mouth:'smile',tilt:.08,blush:.4});
  pup({kind:'girl',x:lerp(660,590,hug),y:G+10,s:1.34,flip:-1,look:[-.3,.2],eyes:'happy',mouth:'smile',tilt:-.1,blush:.6,paw:{x:110,y:-60,k:hug}});
  if(u>1)floatHearts(510,780,1,u,5,160);''', 3.0),
("p.s. I ate your fries 🍟", '''  room('#f6d7b0','#d8a878');
  const ch=Math.floor(u*6)%2;
  pup({kind:'girl',x:350,y:G+10,s:1.3,look:[.5,-.2],eyes:'happy',mouth:ch?'chomp':'w',puff:1,blush:.5,paw:{x:60,y:-170,k:1}});
  fry(410,G-232,-.3,60);fry(390,G-228,-.6,60);
  friesBag(560,G-10,.8,0,0);
  const tk=u>1.1;
  pup({kind:'boy',x:780,y:G+10,s:1.3,flip:-1,look:[-.7,.5],eyes:tk?'wide':'open',mouth:tk?'o':'smile',earLift:tk?.7:0});''', 3.0),
]
MUSIC_N = 3
