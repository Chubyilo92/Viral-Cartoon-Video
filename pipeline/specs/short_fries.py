HOOK = "when he asks if I want anything 🍟"
WARM = "room('#f6d7b0','#d8a878');plant(990,G+6,.8);"
BEATS = [
("me: \"no, I'm good\" 🙂", WARM + '''
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.7,0],eyes:'open',mouth:'smile',paw:{x:150,y:-70,k:1}});
  friesBag(540,G-40,.85,1,.08);
  const sh=Math.sin(u*9)*.12*win(u,.4,2.2);
  pup({kind:'girl',x:790,y:G+10,s:1.3,flip:-1,look:[-.5,0],eyes:'happy',mouth:'smile',tilt:sh});''', 3.0),
("5 minutes later... 👀", WARM + '''
  const ch=Math.floor(u*5)%2;
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.3,0],eyes:'happy',mouth:ch?'chomp':'smile',paw:{x:110,y:-150,k:1}});
  fry(470,G-210,-.6,60);
  friesBag(560,G-10,.85,1,0);
  const lean=P(u,.3,1.8);
  pup({kind:'girl',x:lerp(800,720,lean),y:G+10,s:1.3,flip:-1,look:[-.9,.4],eyes:'wide',mouth:'o',tilt:lerp(0,.12,lean)});''', 2.6),
("\"can I have ONE?\" 🥺", WARM + '''
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.6,0],eyes:'happy',mouth:'smile',blush:.3});
  friesBag(560,G-10,.85,1,0);
  const r=P(u,.4,1.2),bk=P(u,1.5,2.3),k=r*(1-bk);
  pup({kind:'girl',x:720,y:G+10,s:1.3,flip:-1,look:[-.6,.2],eyes:'open',mouth:'pout',brows:'sad',paw:{x:110,y:-40,k:k}});
  if(bk>0)fry(lerp(580,650,bk),lerp(G-90,G-150,bk),.5,62);''', 2.8),
("the \"one\":", WARM + '''
  const ch=Math.floor(u*6)%2;
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.5,.6],eyes:'open',mouth:'flat',brows:'sad',earLift:-.3});
  friesBag(540,G-10,.85,0,0);
  for(let i=0;i<4;i++)fry(450+i*60,G+4,1.5+hash(i)*.4,20);
  pup({kind:'girl',x:720,y:G+10,s:1.3,flip:-1,look:[0,0],eyes:'happy',mouth:ch?'chomp':'w',puff:1,blush:.4,paw:{x:60,y:-170,k:1}});
  fry(660,G-230,.3,60);fry(680,G-235,.6,60);fry(645,G-225,0,60);''', 2.8),
("then he pulls out a second one he got just for me 🥹", WARM + '''
  const rv=P(u,.5,1.4);
  friesBag(600,G-4,.6,0,0);
  if(rv<.35)friesBag(lerp(260,550,rv),lerp(G-20,G-60,rv),.85*lerp(.6,1,rv),1,lerp(-.4,.08,rv));
  pup({kind:'boy',x:340,y:G+10,s:1.3,look:[.6,0],eyes:'happy',mouth:'smile',blush:.5,paw:{x:150,y:-80,k:rv}});
  if(rv>=.35)friesBag(lerp(260,550,rv),lerp(G-20,G-60,rv),.85*lerp(.6,1,rv),1,lerp(-.4,.08,rv));
  if(rv>.9)sparkle(560,G-230,40*pop(u,1.4,.3),win(u,1.4,4));
  const sur=u>1.5;
  pup({kind:'girl',x:740,y:G+10,s:1.3,flip:-1,look:[-.6,0],eyes:sur?(u>2.3?'happy':'wide'):'open',mouth:sur?(u>2.3?'smile':'o'):'flat',blush:sur?.8:0});
  if(u>2.5)floatHearts(700,780,2.5,u,4,140);''', 4.0),
("he knows me better than I know myself 🤍", '''  room('#f1d5b0','#caa070');plant(990,G+6,.8);
  const hug=P(u,.3,1.2);
  pup({kind:'boy',x:lerp(380,430,hug),y:G+10,s:1.34,look:[.4,.1],eyes:'happy',mouth:'smile',tilt:.08,blush:.4});
  pup({kind:'girl',x:lerp(640,580,hug),y:G+10,s:1.34,flip:-1,look:[-.3,.2],eyes:'happy',mouth:'smile',tilt:-.1,blush:.6,paw:{x:110,y:-60,k:1}});
  friesBag(700,G-40,.7,1,-.15);
  if(u>1)floatHearts(500,780,1,u,5,160);''', 3.0),
]
