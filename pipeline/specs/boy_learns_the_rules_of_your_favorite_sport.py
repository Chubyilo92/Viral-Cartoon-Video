import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a boy learns your sport for you"
PRELUDE = R3_PROPS
LINE_SPEED = {}
# TV reuses boy_argues_with_the_tv_only_during_her_shows.py's proven-safe couch()+TV composition
# (absolute position, already confirmed clean this account), with a green "pitch" screen instead
# of a blue drama screen and a halfway-line stroke.
TV = '''  blob(rectPts(640,G-540,280,180,16),'#1c2430',{lw:5});
  ctx.save();ctx.globalAlpha=.5+Math.sin(u*9)*.12;ctx.fillStyle='#7fbf6f';ctx.fillRect(652,G-526,256,152);
  ctx.strokeStyle='rgba(255,255,255,.5)';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(780,G-526);ctx.lineTo(780,G-374);ctx.stroke();
  ctx.restore();'''
JERSEY = '''  ctx.save();ctx.translate(x,y);
  ctx.fillStyle='#ec7489';ctx.strokeStyle=INK;ctx.lineWidth=4;ctx.lineJoin='round';
  ctx.beginPath();
  ctx.moveTo(-70,-40);ctx.lineTo(-96,-70);ctx.lineTo(-62,-104);ctx.lineTo(-30,-92);
  ctx.quadraticCurveTo(0,-104,30,-92);ctx.lineTo(62,-104);ctx.lineTo(96,-70);ctx.lineTo(70,-40);
  ctx.lineTo(70,40);ctx.lineTo(-70,40);ctx.closePath();
  ctx.fill();ctx.stroke();
  ctx.strokeStyle='#c24f63';ctx.lineWidth=3;
  ctx.beginPath();ctx.moveTo(-30,-92);ctx.quadraticCurveTo(0,-78,30,-92);ctx.stroke();
  ctx.fillStyle='#fffaf0';ctx.font='bold 54px Poppins';ctx.textAlign='center';
  ctx.fillText('10',0,20);
  ctx.restore();'''
BALL = '''  ctx.save();ctx.translate(x,y);
  ctx.fillStyle='#fffaf0';ctx.strokeStyle=INK;ctx.lineWidth=4;ctx.beginPath();ctx.arc(0,0,34,0,7);ctx.fill();ctx.stroke();
  ctx.fillStyle='#2b2830';
  ctx.beginPath();ctx.moveTo(0,-14);ctx.lineTo(12,-4);ctx.lineTo(7,10);ctx.lineTo(-7,10);ctx.lineTo(-12,-4);ctx.closePath();ctx.fill();
  ctx.strokeStyle='#2b2830';ctx.lineWidth=2.5;
  ctx.beginPath();ctx.moveTo(0,-14);ctx.lineTo(0,-34);ctx.moveTo(12,-4);ctx.lineTo(30,-10);ctx.moveTo(7,10);ctx.lineTo(18,28);ctx.moveTo(-7,10);ctx.lineTo(-18,28);ctx.moveTo(-12,-4);ctx.lineTo(-30,-10);ctx.stroke();
  ctx.restore();'''
BODY_LINES = [
"When a boy learns the rules of your favourite sport just to watch it with you, he's not becoming a fan.",
"He googles the offside rule at halftime so he can actually follow the game.",
"He asks real questions, not the polite kind, because he actually wants to understand it.",
"He remembers your favourite player's name without being told twice.",
"If he's ever learned the rules just to sit through a game with you... send this to him.",
"But if you've always watched alone because he says it's boring... you're allowed to want someone who asks.",
"Because a boy who learns the rules for you... wants to understand the things you love, not just tolerate them.",
]
D = [
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');couch();
  ''' + TV + '''
  pup({kind:'boy',x:660,y:G-100,s:1.24,flip:1,look:[.3,-.1],eyes:'open',mouth:'smile'});
  pup({kind:'girl',x:340,y:G-100,s:1.2,flip:1,look:[.3,0],eyes:'happy',mouth:'smile',blush:.2});''',
'''  room('#e8d8c8','#c2a98f');
  bigPhone(760,780,1.0,()=>{chatTxt(-100,-40,"offside?",false);});
  pup({kind:'boy',x:360,y:G+10,s:1.25,eyes:'squint',mouth:'flat',look:[.4,-.1]});''',
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');couch();
  ''' + TV + '''
  pup({kind:'boy',x:660,y:G-100,s:1.24,flip:1,look:[.3,-.1],eyes:'open',mouth:'open'});
  pup({kind:'girl',x:340,y:G-100,s:1.2,flip:1,look:[.3,0],eyes:'squint',mouth:'smile',blush:.2});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(540,560,"wait, why's that a foul?",1,.6);ctx.restore();}''',
'''  room('#f1d5b0','#caa070');
  ''' + JERSEY.replace('x,y', '260,G-140') + '''
  ''' + BALL.replace('x,y', '420,G-60') + '''
  pup({kind:'boy',x:740,y:G+10,s:1.2,flip:-1,eyes:'happy',mouth:'smile',look:[-.3,-.1]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(740,560,"great header from her!",1,.55);ctx.restore();}''',
SHARE,
'''  room('#333c54','#28304a','rgba(255,255,255,.05)');
  pup({kind:'girl',x:540,y:G+10,s:1.2,look:[0,-.1],brows:'sad',mouth:'flat',shadow:false});''',
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');couch();
  ''' + TV + '''
  pup({kind:'boy',x:660,y:G-100,s:1.24,flip:1,look:[.3,-.1],eyes:'happy',mouth:'smile',blush:.2});
  pup({kind:'girl',x:340,y:G-100,s:1.2,flip:1,look:[.3,0],eyes:'happy',mouth:'smile',blush:.3});
  sparkle(500,G-440,22,win(u,.2,3.8));
  if(u>.6)floatHearts(500,700,.6,u,3,130);''',
]
SCENES = spec(BODY_LINES, D, [{'a fan':'⚽'},{'halftime':'📱'},{'understand it':'🤔'},{'told twice':'🏆'},{'to him':'💌'},{'who asks':'🤍'},{'tolerate them':'⚽'}])
IG_LINE = "The offside rule he googled at halftime. The real questions. The player's name he never forgets. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'offside':'⚽','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
