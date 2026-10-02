import sys; sys.path.insert(0, '/home/claude/jj')
from dialogue import D
import biscuit as B

OUTRO_SECS = 2.6   # spec.END_TAIL — full-screen like-goal outro after "...No one."

def text_js(sender, line1, line2, popin=True):
    """The message, shown big at the top like a caption (the phone itself is in the pup's paws)."""
    k = "pop(u,.05,.35)" if popin else "1"
    return r'''
  const k=%s;
  ctx.save();ctx.translate(540,560);ctx.scale(k,k);
  ctx.fillStyle='#fff';ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.beginPath();ctx.roundRect(-300,-110,600,220,34);ctx.fill();ctx.stroke();
  ctx.fillStyle='#2b2830';ctx.beginPath();ctx.arc(-240,-58,30,0,7);ctx.fill();ctx.fillStyle='#fff';ctx.font='bold 28px Poppins';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(%r,-240,-56);
  ctx.textAlign='left';ctx.fillStyle=INK;ctx.font='bold 30px Poppins, "Noto Color Emoji"';ctx.fillText(%r,-196,-70);
  ctx.fillStyle='#8a7b80';ctx.font='20px Poppins';ctx.fillText('message · now',-196,-38);
  ctx.fillStyle='#e9e9ee';ctx.beginPath();ctx.roundRect(-270,-6,540,96,26);ctx.fill();
  ctx.fillStyle=INK;ctx.font='bold 30px Poppins, "Noto Color Emoji"';ctx.fillText(%r,-246,28);ctx.fillText(%r,-246,66);
  ctx.restore();''' % (k, sender[0], sender, line1, line2)

def held_phone(owner, lit=True):
    """Phone in the owner's paws, screen glowing, angled up at their face."""
    x, d = (430, 1) if owner == 'girl' else (650, -1)
    glow = "const gl=ctx.createRadialGradient(%d,%d,10,%d,%d,170);gl.addColorStop(0,'rgba(190,225,255,.45)');gl.addColorStop(1,'rgba(190,225,255,0)');ctx.fillStyle=gl;ctx.fillRect(%d,%d,340,340);" % (x, 1000, x, 1000, x - 170, 830) if lit else ''
    return glow + '''
  phoneMock(%d,G-70,.5,%s,()=>{ctx.fillStyle='#1d2433';ctx.fillRect(-70,-290,140,280);
    ctx.fillStyle='#fff';ctx.beginPath();ctx.roundRect(-58,-250,116,70,12);ctx.fill();
    ctx.fillStyle='#2b2830';ctx.font='bold 13px Poppins';ctx.textAlign='left';ctx.fillText('1 new message',-48,-222);
    ctx.fillStyle='#8a7b80';ctx.font='11px Poppins';ctx.fillText('now',-48,-202);});''' % (x, ".35" if d > 0 else "-.35")

def outro_js(goal_num):
    return r'''
  const ot=u-(CURLEAD+CURVO+.35);
  if(ot>0){ctx.save();ctx.setTransform(1,0,0,1,0,0);
    ctx.globalAlpha=clamp(ot/.25);ctx.fillStyle='#ff6b9d';ctx.fillRect(0,0,W,H);
    ctx.globalAlpha=1;const kk=back(clamp(ot/.45));const pul=1+.04*Math.sin(ot*7);
    ctx.translate(540,880);ctx.scale(kk*pul,kk*pul);ctx.textAlign='center';ctx.textBaseline='middle';
    ctx.lineJoin='round';ctx.strokeStyle='#2c1d13';ctx.lineWidth=22;ctx.fillStyle='#fffaf0';
    ctx.font='bold 230px Poppins';ctx.strokeText(%r,0,-60);ctx.fillText(%r,0,-60);
    ctx.font='bold 110px Poppins';ctx.lineWidth=16;ctx.strokeText('likes',0,120);ctx.fillText('likes',0,120);
    ctx.font='bold 84px Poppins';ctx.lineWidth=14;ctx.strokeText('for part 2',0,260);ctx.fillText('for part 2',0,260);
    ctx.font='120px "Noto Color Emoji"';ctx.fillText('👀',0,430);
    ctx.restore();}''' % (goal_num, goal_num)

def sting(owner, sender, line1, line2, goal_num):
    """owner = pup whose phone gets the text; the other asks 'who was that?', owner says '...No one.'
    Returns (question_line, answer_line). Add to spec: SFX (..., (q_idx,'start','text+faaak')) and END_TAIL = OUTRO_SECS."""
    asker = 'boy' if owner == 'girl' else 'girl'
    pos = {'girl': "x:300,flip:-1", 'boy': "x:780"}
    lk = {'girl': '.6', 'boy': '-.6'}
    down = '-.4,.8'
    q = D(asker, "Babe... who was that?", B.CALM + "corner('wait... WHAT 👀',win(u,.4,9));" + held_phone(owner) + text_js(sender, line1, line2) + '''
  SP('%s',u,{%s,look:[%s],eyes:u<CURLEAD?'open':'wide',mouth:'o',earLift:.4,blush:.6,tilt:%s,paw:{x:%d,y:-115,k:1},hy:8});
  SP('%s',u,{%s,look:[%s,-.2],eyes:'squint',talk:1,mouth:'flat',brows:'angry',tilt:.08});''' % (
        owner, pos[owner], down, '.1', -100, asker, pos[asker], lk[asker]), '🤨')
    a = D(owner, "...No one.", B.CALM + held_phone(owner, False) + text_js(sender, line1, line2, False) + '''
  SP('%s',u,{%s,look:[%s,.2],eyes:'squint',talk:1,mouth:'smile',blush:.8,tilt:-.1,hx:Math.sin(u*3)*3,paw:{x:%d,y:-115,k:1}});
  SP('%s',u,{%s,look:[%s,0],eyes:'squint',mouth:'flat',brows:'angry',tilt:.1});''' % (
        owner, pos[owner], '.6', -100, asker, pos[asker], lk[asker]) + outro_js(goal_num), '🙂')
    return q, a
