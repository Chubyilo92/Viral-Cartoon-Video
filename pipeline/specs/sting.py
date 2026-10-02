import sys; sys.path.insert(0, '/home/claude/jj')
from dialogue import D
import biscuit as B

def text_js(sender, line1, line2, popin=True):
    k = "pop(u,.0,.35)" if popin else "1"
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

def sting(owner, sender, line1, line2, goal):
    asker = 'boy' if owner == 'girl' else 'girl'
    pos = {'girl': "x:300,flip:-1", 'boy': "x:780"}
    lk = {'girl': '.6', 'boy': '-.6'}
    q = D(asker, "Babe... who was that?", B.CALM + "corner('wait... WHAT 👀',win(u,.4,9));" + text_js(sender, line1, line2) + '''
  SP('%s',u,{%s,look:[%s,-.3],eyes:'wide',mouth:'o',earLift:.4,blush:.6});
  SP('%s',u,{%s,look:[%s,-.3],eyes:'squint',talk:1,mouth:'flat',brows:'angry',tilt:.08});''' % (owner, pos[owner], lk[owner], asker, pos[asker], lk[asker]), '🤨')
    a = D(owner, "...No one.", B.CALM + "corner('%s',win(u,.5,99));" % goal + text_js(sender, line1, line2, False) + '''
  SP('%s',u,{%s,look:[%s,.2],eyes:'squint',talk:1,mouth:'smile',blush:.8,tilt:-.1,hx:Math.sin(u*3)*3});
  SP('%s',u,{%s,look:[%s,0],eyes:'squint',mouth:'flat',brows:'angry',tilt:.1});''' % (owner, pos[owner], '-'+lk[owner] if owner=='girl' else '.6', asker, pos[asker], lk[asker]), '🙂')
    return q, a
