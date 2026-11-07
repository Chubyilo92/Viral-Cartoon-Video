import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
TITLE = "when a boy argues with the tv"
PRELUDE = R3_PROPS
LINE_SPEED = {}
TV = '''  blob(rectPts(640,G-540,280,180,16),'#1c2430',{lw:5});
  ctx.save();ctx.globalAlpha=.45+Math.sin(u*9)*.15;ctx.fillStyle='#8fd0ff';ctx.fillRect(652,G-526,256,152);ctx.restore();'''
BODY_LINES = [
"He trash-talks every character in her favourite show. Out loud. Constantly.",
"His mates say he's never watched a drama series in his life, calls them boring.",
"He's narrated three full seasons with increasingly specific opinions about side characters.",
"He's started reading the fan theories. He will deny this.",
"If he pretends to hate your show but has seen every single episode... send this to him.",
"But the night he watches a whole episode in total silence... look at his face. He's watched ahead without you, and he already knows the twist.",
"Because a boy who yells at your favourite show... still hates the genre. He just loves watching it with you.",
]
D = [
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');couch();
  ''' + TV + '''
  pup({kind:'boy',x:660,y:G-100,s:1.24,flip:1,look:[.3,-.1],eyes:'wide',mouth:'open'});
  pup({kind:'girl',x:340,y:G-100,s:1.2,flip:1,look:[.3,0],eyes:'happy',mouth:'smile',blush:.3});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(760,560,"don't trust him, Brenda!",1,.68);ctx.restore();}''',
'''  room('#e8d8c8','#c2a98f');
  bigPhone(560,780,1.0,()=>{chatBub(-90,-200,180,70,false);});
  pup({kind:'boy',x:280,y:G+10,s:1.25,eyes:'squint',mouth:'flat',look:[.4,-.1]});
  if(u>.5){ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(480,480,"dramas are so boring",1,.78);ctx.restore();}''',
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');couch();
  ''' + TV + '''
  pup({kind:'boy',x:660,y:G-100,s:1.24,flip:1,look:[.3,-.1],eyes:'open',mouth:'open'});
  pup({kind:'girl',x:340,y:G-100,s:1.2,flip:1,look:[.3,0],eyes:'squint',mouth:'smile',blush:.2});
  if(u>.6){ctx.save();ctx.globalAlpha=win(u,.6,9);bubbleText(540,560,"Brenda's motives are SO unclear",1,.52);ctx.restore();}''',
'''  room('#f1d5b0','#caa070');
  bigPhone(760,780,.9,()=>{chatTxt(-90,-40,'fan theory',false);});
  pup({kind:'boy',x:400,y:G+10,s:1.2,eyes:'squint',mouth:'flat',look:[.5,-.1]});''',
SHARE,
'''  room('#3a4454','#2c3442','rgba(255,255,255,.05)');couch();
  ''' + TV + '''
  pup({kind:'boy',x:680,y:G-100,s:1.22,flip:1,look:[.3,0],eyes:'squint',mouth:'smile',tilt:.02});
  pup({kind:'girl',x:340,y:G-100,s:1.2,flip:1,look:[.6,0],eyes:'squint',mouth:'flat'});''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'constantly':'📺'},{'boring':'🙄'},{'characters':'📺'},{'this':'🤫'},{'to him':'💌'},{'twist':'👀'},{'with you':'🤍'}])
IG_LINE = "The heckling. The denial. The fan theories he swears he never read. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'heckling':'📺','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
