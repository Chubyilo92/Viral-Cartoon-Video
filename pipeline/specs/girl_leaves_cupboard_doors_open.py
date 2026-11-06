import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a girl leaves cupboards open"
PRELUDE = R3_PROPS
LINE_SPEED = {}
def cab(x, open_amt, col='#d9c3a0'):
    # x,y anchor at floor; a bank of 3 cupboard doors, one swinging open by open_amt (0..1)
    return f'''  ctx.save();
  blob(rectPts({x}-180,G-420,360,330,16),'{col}',{{lw:5}});
  blob(rectPts({x}-180,G-420,360,70,10),'#c9a877',{{lw:4}});
  for(let i=0;i<3;i++){{
    const dx={x}-170+i*120;
    if(i===1){{
      const a=(-Math.PI/2.6)*{open_amt};
      ctx.save();ctx.translate(dx,G-80);ctx.rotate(a);
      blob(rectPts(0,-250,106,250,8),'#f3e4c4',{{lw:4}});
      ctx.fillStyle='#8a6a3f';ctx.beginPath();ctx.arc(90,-130,7,0,7);ctx.fill();
      ctx.restore();
    }} else {{
      blob(rectPts(dx,G-330,106,250,8),'#f3e4c4',{{lw:4}});
      ctx.fillStyle='#8a6a3f';ctx.beginPath();ctx.arc(dx+90,G-200,7,0,7);ctx.fill();
    }}
  }}
  ctx.restore();'''
BODY_LINES = [
"When a girl leaves every cupboard door open behind her, she's not being careless.",
"She grabs what she needs and moves straight on to the next thing, door still swinging.",
"You're the one who closes them, every time, without her ever noticing.",
"She never once does it at her mum's house, where everything still has to look perfect.",
"If you've become the designated door-closer in your own home... send this to her.",
"But the day you walk in and every single door is shut... she's not finally being tidy. She's started acting like a guest again.",
"Because a girl who leaves every door open around you... has stopped acting like a guest in your home.",
]
D = [
'''  room('#f1d5b0','#caa070');
  ''' + cab(640, 1) + '''
  pup({kind:'girl',x:360,y:G+10,s:1.25,look:[.5,-.1],eyes:'open',mouth:'flat'});''',
'''  room('#e3c9a0','#bf9670');
  ''' + cab(640, 1) + '''
  pup({kind:'girl',x:360,y:G+10,s:1.3,flip:-1,look:[-.4,-.1],eyes:'happy',mouth:'smile',blush:.2,wag:.3});''',
'''  room('#e8d8c8','#c2a98f');
  ''' + cab(640, 0) + '''
  pup({kind:'boy',x:640,y:G+10,s:1.2,look:[0,-.3],brows:'sad',mouth:'flat'});
  pup({kind:'girl',x:300,y:G+10,s:1.2,flip:-1,look:[-.4,0],eyes:'happy',mouth:'smile',blush:.2});''',
'''  room('#cfe3ec','#98b6c2');
  ''' + cab(640, 0) + '''
  pup({kind:'girl',x:420,y:G+10,s:1.25,look:[.4,0],eyes:'squint',mouth:'smile',blush:.3,tilt:.06});''',
SHARE,
'''  room('#4a4350','#3a3340','rgba(255,255,255,.05)');
  ''' + cab(560, 0) + '''
  pup({kind:'boy',x:830,y:G+10,s:1.05,flip:-1,look:[-.4,-.1],eyes:'wide',mouth:'flat'});
  pup({kind:'girl',x:250,y:G+10,s:1.15,look:[.3,-.1],eyes:'open',mouth:'flat'});
  if(u>1.2)raincloudSmall(250,G-440,win(u,1.2,9)*.6);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'careless':'🚪'},{'swinging':'👋'},{'noticing':'🙈'},{'perfect':'🏠'},{'home':'💌'},{'again':'💔'},{'home':'🤍'}])
IG_LINE = "The door still swinging. The closing them without her noticing. The one home where it's never perfect. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'swinging':'🚪','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
