import json
def S(cap, body):
    return '{cap:%s,draw(u){\n%s\n}}' % (json.dumps(cap, ensure_ascii=False), body)
HUG = '''  room('#f1d5b0','#caa070');plant(970,G+6,.9);
  const hug=P(u,.4,1.4);
  pup({kind:'girl',x:lerp(560,500,hug),y:G+10,s:1.34,flip:-1,look:[-.3,.2],eyes:'happy',mouth:'smile',tilt:-.1,blush:.5,paw:{x:70,y:-190,k:hug}});
  pup({kind:'boy',x:lerp(380,440,hug),y:G+10,s:1.34,look:[.4,.1],eyes:'happy',mouth:'smile',tilt:.08,blush:.4,earLift:.1});
  if(u>1.6)floatHearts(470,800,1.6,u,5,140);'''
SHARE = '''  room('#e9ceb8','#c39a76',1180,'rgba(255,255,255,.2)');
  ell(540,G+16,300,30,'#00000010',{stroke:false});
  const k=pop(u,.2,.4);
  pup({kind:'girl',x:400,y:G+10,s:1.5,flip:-1,eyes:'happy',mouth:'smile',blush:.5,tilt:-.08,wag:.3});
  pup({kind:'boy',x:700,y:G+10,s:1.5,eyes:'happy',mouth:'smile',blush:.4,tilt:.08,wag:.3});
  if(u>.6)floatHearts(540,760,.6,u,5,160);
  sparkle(540,650,50*k,win(u,.2,3.8));'''
