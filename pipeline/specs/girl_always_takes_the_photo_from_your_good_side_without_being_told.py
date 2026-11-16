import sys; sys.path.insert(0,'/home/claude/jj'); sys.path.insert(0,'/home/claude/jj/specs')
from _kit2 import spec, HUG, SHARE, TT_STD, C
from _r3props import R3_PROPS
from _gapfill1116 import GAPFILL_PROPS
TITLE = "the photo she always gets right"
PRELUDE = R3_PROPS + GAPFILL_PROPS
LINE_SPEED = {}
BODY_LINES = [
"When a girl always gets your good side in photos without being told, she's not just a good photographer.",
"She angles the camera down and to the left before you've even posed.",
"She retakes it three times so you never see the one where you blinked.",
"She stands on her tiptoes because she knows you hate the angle from below.",
"If you've never seen a bad photo of yourself since you met her... send this to her.",
"But the day she stops checking the shot before she posts it... she's stopped looking at you the way she used to.",
"Because a girl who always finds your good side... is always looking for it.",
]
D = [
'''  room('#f1d5b0','#caa070');
  pup({kind:'girl',x:360,y:G+10,s:1.2,look:[.3,-.1],eyes:'happy',mouth:'smile'});
  cameraProp(400,G-90,.8,-.1);
  pup({kind:'boy',x:740,y:G+10,s:1.25,flip:-1,look:[-.3,0],eyes:'open',mouth:'smile'});
  cameraFraming(740,G-260,260,360,win(u,.4,9));''',
'''  room('#e8d8c8','#c2a98f');
  pup({kind:'girl',x:380,y:G+10,s:1.2,look:[.3,-.2],eyes:'happy',mouth:'smile'});
  cameraProp(430,G-60,.9,-.55);
  labelCard(690,460,'down + left 📐',.78,1,21);
  pup({kind:'boy',x:740,y:G+10,s:1.25,flip:-1,look:[-.3,0],eyes:'open',mouth:'smile'});''',
'''  room('#cfe3ec','#98b6c2');
  pup({kind:'girl',x:330,y:G+10,s:1.2,look:[.3,-.2],eyes:'open',mouth:'flat'});
  cameraProp(380,G-60,.85,-.2);
  pup({kind:'boy',x:750,y:G+10,s:1.25,flip:-1,look:[-.3,0],eyes:'closed',mouth:'o'});
  labelCard(540,460,'take 1 😳',.85,1,24);
  labelCard(540,560,'take 2 😐',.85,1,24);
  labelCard(540,660,'take 3 😊',.85,1,24);''',
'''  room('#f6d7c6','#d6a286');
  blob(rectPts(345,G-165,150,190,10),'#8a5a35');
  line([[345,G-30],[495,G-30]],{lw:4,c:'#6f4728'});
  pup({kind:'girl',x:420,y:G-110,s:1.2,look:[.3,-.3],eyes:'open',mouth:'smile',tilt:-.08});
  cameraProp(470,G-180,.8,-.2);
  labelCard(300,480,'stood on a crate for the angle 👣',.68,1,19);
  pup({kind:'boy',x:760,y:G+10,s:1.25,flip:-1,look:[-.3,-.1],eyes:'happy',mouth:'smile'});''',
SHARE,
'''  room('#6f6a78','#5a5562','rgba(255,255,255,.05)');
  pup({kind:'girl',x:360,y:G+10,s:1.2,look:[.1,.8],eyes:'open',mouth:'flat'});
  bigPhone(545,G-60,.4,()=>{});
  labelCard(300,480,"posts it without looking up",.68,1,19);
  pup({kind:'boy',x:780,y:G+10,s:1.2,flip:-1,look:[-.3,0],eyes:'open',mouth:'flat',brows:'sad'});''',
HUG,
]
SCENES = spec(BODY_LINES, D, [{'photographer':'📷'},{'posed':'📸'},{'blinked':'😳'},{'from below':'🙆'},{'send this to her':'💌'},{'used to':'💔'},{'looking for it':'🤍'}])
IG_LINE = "The angle she finds before you've even posed. The third take so you never see the blink. The photo that's always, somehow, your best one. Everyone shows love their own way... Want to know yours? There's a sixty second test in our bio. Take it together."
IG_CAPS = C(IG_LINE, {'posed.':'📷','yours?':'🤍','bio':'🔗'})
IG_RESULT = "Quality Time"
TT_LINE = TT_STD
