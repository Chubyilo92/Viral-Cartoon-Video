import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _kitchenprops import KITCHEN_PROPS
TITLE = "when a girl taste-tests you first"
PRELUDE = KITCHEN_PROPS
LINE_SPEED = {}
BODY_LINES = [
"She makes you taste-test everything she cooks before she'll even try it herself, no exceptions, every time.",
"Spoon held up to your mouth before she's even plated her own.",
"Her flatmate's never been asked. Her mum's never been asked. Only you.",
"Turns out she doesn't believe it's good until you've said it is.",
"If someone needs to hear \"this is good\" before they believe it... send this to her.",
"But the night you say \"it's fine\" without actually tasting it... she'll know, and it'll cost more than the five seconds you saved.",
"Because the girl holding the spoon up to your mouth... doesn't want a chef's opinion. She wants yours.",
]
D = [
# 1: kitchen, girl at stove holding spoon up to boy's mouth, her own plate still empty
'''  room('#f1d9b8','#c9a06e');
  stove(800,G+60,1.0);
  potOnStove(800,G-20,1.0,u);
  plateProp(260,G+70,.95,0);
  pup({kind:'boy',x:330,y:G+10,s:1.18,flip:-1,look:[-.15,-.1],eyes:'wide',mouth:'open'});
  pup({kind:'girl',x:560,y:G+10,s:1.22,look:[.25,-.1],eyes:'open',mouth:'smile',tilt:-.05,
       paw:{x:-150,y:-190,k:pop(u,.2,.5)}});
  spoonProp(410,955,-1.5708,.85*pop(u,.2,.5));''',
# 2: close-up, spoon right at the mouth, her own plate empty beside her, anticipation
'''  room('#f6e4c8','#d4ad78');
  plateProp(820,G+80,.8,0);
  pup({kind:'girl',x:620,y:G+10,s:1.3,look:[.2,-.15],eyes:'wide',mouth:'smile',blush:.3,
       paw:{x:-170,y:-210,k:1}});
  pup({kind:'boy',x:340,y:G+10,s:1.3,flip:-1,look:[-.1,-.1],eyes:'closed',mouth:'open'});
  spoonProp(400,935,-1.5708,1.05);''',
# 3: checklist card, girl proud, boy chewing in background
'''  room('#e7ccae','#bb9164');
  pup({kind:'girl',x:360,y:G+10,s:1.25,look:[.2,.05],eyes:'happy',mouth:'smile',wag:.3});
  pup({kind:'boy',x:800,y:G+10,s:1.15,flip:-1,look:[-.2,0],eyes:'open',mouth:'w'});
  checklistCard(650,560,[["her flatmate",0],["her mum",0],["you",1]],1,pop(u,.15,.4));''',
# 4: close on girl's face, hopeful, small text bubble "well?"
'''  room('#f1d5b0','#caa070');
  pup({kind:'boy',x:800,y:G+10,s:1.1,flip:-1,look:[-.2,0],eyes:'closed',mouth:'o'});
  pup({kind:'girl',x:380,y:G+10,s:1.35,look:[.3,.0],eyes:'wide',mouth:'flat',brows:'sad',tilt:-.04});
  if(u>.5){const k=pop(u,.5,.4);ctx.save();ctx.globalAlpha=win(u,.5,9);bubbleText(430,610,"well...? 🥺",1,.85*k);ctx.restore();}''',
SHARE,
# 6: girl squinting (she knows), boy caught mid-sneaky-bite without the ritual
'''  room('#4a3f4f','#3a3140','rgba(255,255,255,.05)');
  pup({kind:'boy',x:760,y:G+10,s:1.22,flip:-1,look:[-.2,.1],eyes:'open',mouth:'chomp',blush:.2});
  pup({kind:'girl',x:350,y:G+10,s:1.25,look:[.5,.1],eyes:'squint',mouth:'flat',tilt:-.1});
  plateProp(880,G+70,.85,1);''',
HUG,
]
SCENES = spec(BODY_LINES, D, [
    {'every time':'🥄'},
    {'own':'🍽️'},
    {'only you':'🤍'},
    {'is':'🥺'},
    {'send this to her':'💌'},
    {'saved':'🚩'},
    {'yours':'🤍'},
])
IG_LINE = "The spoon. The hopeful look. The \"well...?\" Everyone needs their person to say it's good... Want to know how you show it? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'spoon.':'🥄','good...':'🥺','bio':'🔗'})
IG_RESULT = "Words of Affirmation"
TT_LINE = TT_STD
