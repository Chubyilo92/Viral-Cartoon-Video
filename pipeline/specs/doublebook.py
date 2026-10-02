import sys; sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
from dialogue import D, ENDCARD
import biscuit as B, anniversary as A

# VIRAL-BLUEPRINT, shared calendar variant 2: DOUBLE-BOOKING (not forgetting).
# He booked a work meeting on top of the dinner she arranged with the neighbours.
# App check proves her right (dinner was in the shared calendar, added 2 weeks ago).
# He adds his meeting so he can move it -> both events sit at 7pm side by side -> TWIST: his meeting is WITH Tom,
# the neighbour. Laugh: "Business dinner. Tom's paying."
TITLE = "she called me short over THIS"
MUSIC_N = 2
PRELUDE = A.PRELUDE
RED, CALM, FLICK, SH = B.RED, B.CALM, B.FLICK, B.SH
HOOK = "corner('guess who is actually wrong 👇',1);"
WHO = "corner('who\\'s apologising? 👀',1);"

def cal(x, y, s, rows, extra=''):
    return "calPhone(%s,%s,%s,-.04,'Friday · 7:00 pm',%s,false);%s" % (x, y, s, rows, extra)

DINNER = "['🍝 Tom & Sarah','dinner · added by her']"
MEET = "['💼 work meeting','7pm · added by him']"

LINES = [
D('girl', "This is why I never wanted to marry a short guy!", RED + HOOK + '''
  SP('girl',u,{x:320,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'open',earLift:.5,tilt:-.08,%s,s:1.45});
  SP('boy',u,{x:790,look:[-.6,-.1],brows:'sad',mouth:'o',eyes:'wide',earLift:-.3,s:1.15});''' % SH, '😤'),
D('boy', "I'm not short. You're just freakishly tall!", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',mouth:'o',eyes:'wide',earLift:.5,s:1.45});
  SP('boy',u,{x:790,look:[-.6,-.2],brows:'angry',talk:1,mouth:'open',earLift:.5,tilt:.08,%s,s:1.2});''' % SH, '🤬'),
D('girl', "Your friends only invite you because they feel sorry for you.", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,-.1],brows:'angry',talk:1,mouth:'flat',eyes:'squint',tilt:-.12,s:1.45});
  SP('boy',u,{x:790,look:[-.6,0],brows:'sad',mouth:'o',eyes:'wide',earLift:-.5,s:1.15,squash:lerp(1,.93,P(u,2.4,3))});
  raincloudSmall(540,640,win(u,.3,9));''', '💔'),
D('boy', "At least I HAVE friends!", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'sad',mouth:'o',eyes:'wide',earLift:-.4,s:1.45});
  SP('boy',u,{x:790,look:[-.6,-.1],brows:'angry',talk:1,mouth:'open',earLift:.5,%s,s:1.2});
  raincloudSmall(540,640,1);raincloudSmall(400,580,win(u,.3,9));''' % SH, '😤'),
D('girl', "ONE plan with the neighbours, and you booked a work meeting!", RED + HOOK + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'open',earLift:.4,s:1.45,paw:{x:120,y:-120,k:P(u,.2,.5)}});
  SP('boy',u,{x:790,look:[-.6,0],brows:'angry',mouth:'flat',s:1.2});
  raincloudSmall(540,640,1);raincloudSmall(400,580,1);raincloudSmall(700,600,win(u,.3,9));''', '🍝'),
D('boy', "Because you NEVER tell me anything!", RED + "corner('wait for it 👀',win(u,.4,9));" + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',mouth:'pout',eyes:'squint',s:1.45});
  SP('boy',u,{x:790,look:[-.6,-.1],brows:'angry',talk:1,mouth:'open',earLift:.5,%s,s:1.2});
  raincloudSmall(540,640,1);raincloudSmall(400,580,1);raincloudSmall(700,600,1);''' % SH, '🙄'),
D('girl', "I told you two weeks ago. Check the app. If it's not there, I'll apologise.", CALM + "corner('who\\'s apologising? 👀',win(u,2.4,9));" + '''
  SP('girl',u,{x:300,flip:-1,look:[.6,0],brows:'angry',talk:1,mouth:'flat',eyes:'squint',tilt:-.1,s:1.35});
  SP('boy',u,{x:790,look:[-.6,0],brows:'angry',mouth:'flat',s:1.15});''', '📱'),
D('boy', "Friday, seven o'clock... just my meeting.", CALM + WHO + '''
  const r=pop(u,.2,.5);
  SP('girl',u,{x:240,s:1.05,flip:-1,look:[.5,-.2],eyes:u>1.8?'wide':'squint',mouth:u>1.8?'o':'smile',earLift:u>1.8?.3:0});
  SP('boy',u,{x:450,s:.95,look:[.5,-.2],talk:1,mouth:'flat',paw:{x:90,y:-150,k:P(u,.1,.5)}});
  ''' + cal('770', '1010-r*40', '1.5*r+.01', '[%s]' % MEET), '📅'),
D('boy', "No dinner. Nothing.", CALM + "corner('plot twist 👀',win(u,.2,9));" + '''
  SP('girl',u,{x:240,s:1.05,flip:-1,look:[.5,-.2],eyes:'wide',mouth:'o',earLift:.4,blush:lerp(0,.8,P(u,.3,1))});
  SP('boy',u,{x:450,s:.95,look:[-.4,0],eyes:'squint',talk:1,mouth:'flat',tilt:.1});
  ''' + cal('770', '970', '1.5', '[%s]' % MEET), '🤨'),
D('girl', "...I was so sure I put it in.", CALM + '''
  SP('girl',u,{x:330,flip:-1,look:[.3,.4],eyes:'closed2',brows:'sad',talk:1,mouth:'pout',blush:1,earLift:-.5,hy:6,s:1.35});
  SP('boy',u,{x:780,look:[-.5,.1],eyes:'open',mouth:'flat',s:1.15});''', '🙈'),
D('girl', "I'm sorry, babe. I shouldn't have called you short.", CALM + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],eyes:'open',brows:'sad',talk:1,mouth:'flat',blush:.8,s:1.35});
  SP('boy',u,{x:780,look:[-.5,.1],eyes:'squint',mouth:'smile',tilt:.1,s:1.15});''', '🥺'),
D('boy', "And?", CALM + '''
  SP('girl',u,{x:330,flip:-1,look:[.5,.1],eyes:'open',brows:'sad',mouth:'pout',blush:.8,s:1.35});
  SP('boy',u,{x:780,look:[-.5,.1],eyes:'squint',talk:1,mouth:'smile',tilt:.14,s:1.15});''', '😏'),
D('girl', "...And you're the perfect height.", CALM + '''
  const hug=P(u,1,1.8);
  SP('girl',u,{x:lerp(330,420,hug),flip:-1,look:[.5,0],eyes:'happy',talk:1,mouth:'smile',blush:.8,paw:{x:70,y:-190,k:hug},s:1.3});
  SP('boy',u,{x:lerp(780,670,hug),look:[-.5,0],eyes:'happy',mouth:'smile',blush:.5,wag:1,s:1.15});
  if(u>1.2)floatHearts(540,800,1.2,u,6,170);''', '💗'),
]

END = D('boy', "This is what CoupleIn is for.",
        ENDCARD('one calendar for two', '', speaker='boy'), '💗')
