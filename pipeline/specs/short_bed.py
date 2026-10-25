HOOK = "we never go to bed angry 🐾"
B = "bedNight();bedBack();"
BLK = "blanket(150,935,G-190);"
BEATS = [
("she's mad 😤", B + '''
  pup({kind:'girl',x:370,y:G-100,s:1.1,flip:-1,look:[-.6,0],eyes:'closed',mouth:'pout',brows:'angry',tilt:.05,shadow:false});
  pup({kind:'boy',x:720,y:G-100,s:1.1,flip:-1,look:[-.8,.2],eyes:'open',mouth:'flat',brows:'sad',shadow:false});
  ''' + BLK + '''
  bigCloud(370,G-560,win(u,.4,9));''', 3.0),
("attempt #1 👉", B + '''
  const pk=P(u,.4,1.1)*(1-P(u,1.6,2.1));const sh=u>1.1&&u<1.6?Math.sin(u*50)*.12:0;
  pup({kind:'girl',x:370,y:G-100,s:1.1,flip:-1,look:[-.6,0],eyes:'closed',mouth:'pout',brows:'angry',tilt:.05+sh,shadow:false});
  pup({kind:'boy',x:700,y:G-100,s:1.1,flip:-1,look:[-.8,.1],eyes:'open',mouth:'smile',shadow:false,paw:{x:150,y:-160,k:pk}});
  ''' + BLK + '''
  bubbleText(300,560,"hmph.",win(u,1.1,9),1.1);''', 3.0),
("attempt #2 🤗", B + '''
  const sc=P(u,.3,1.1),bk=P(u,1.7,2.4);const bx=lerp(lerp(720,540,sc),720,bk);
  pup({kind:'girl',x:350,y:G-100,s:1.1,flip:-1,look:[-.6,0],eyes:'closed',mouth:'pout',brows:'angry',tilt:.05,shadow:false});
  pup({kind:'boy',x:bx,y:G-100,s:1.1,flip:-1,look:[-.8,0],eyes:bk>.2?'wide':'happy',mouth:bk>.2?'o':'smile',blush:bk>.2?0:.5,shadow:false});
  ''' + BLK + '''
  bubbleText(300,560,"no.",win(u,1.4,9),1.2);''', 3.0),
("attempt #3: he gives up 😔", B + '''
  pup({kind:'girl',x:370,y:G-100,s:1.1,flip:-1,look:[.4,0],eyes:u>1.6?'open':'closed',mouth:'flat',brows:u>1.6?null:'angry',shadow:false});
  pup({kind:'boy',x:720,y:G-100,s:1.1,flip:1,look:[.6,.4],eyes:'open',mouth:'flat',brows:'sad',earLift:-.4,shadow:false});
  ''' + BLK + '''
  bigCloud(720,G-560,win(u,.5,9));''', 3.2),
("...and then SHE does this 🥹", B + '''
  const mv=P(u,.3,1.3);
  pup({kind:'boy',x:740,y:G-100,s:1.1,flip:1,look:[.3,0],eyes:u>1.5?(u>2.2?'happy':'wide'):'open',mouth:u>2.2?'smile':(u>1.5?'o':'flat'),brows:u>1.5?null:'sad',blush:u>2.2?.8:0,shadow:false});
  pup({kind:'girl',x:lerp(370,560,mv),y:G-100,s:1.1,flip:1,look:[.6,0],eyes:'happy',mouth:'smile',blush:.6,tilt:.12*mv,shadow:false,paw:{x:150,y:-110,k:P(u,1,1.6)}});
  ''' + BLK + '''
  if(u>2.2)floatHearts(650,G-480,2.2,u,4,140);''', 3.4),
("rule kept 🤍", B + '''
  pup({kind:'boy',x:700,y:G-100,s:1.1,flip:-1,look:[0,0],eyes:'closed',mouth:'smile',blush:.5,tilt:-.12,shadow:false});
  pup({kind:'girl',x:520,y:G-100,s:1.1,flip:1,look:[0,0],eyes:'closed',mouth:'smile',blush:.5,tilt:.14,shadow:false});
  ''' + BLK + '''
  zzz(800,G-480,u);floatHearts(610,G-470,.4,u,4,120);''', 2.8),
]
