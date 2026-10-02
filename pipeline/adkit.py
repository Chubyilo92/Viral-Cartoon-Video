#!/usr/bin/env python3
"""adkit - reusable kit for JJ puppy DIALOGUE ADS (the 10/10 format). Read docs/DIALOGUE-AD-TEMPLATE.md first.

A new video = one short spec that calls build(beats, ...). Each beat is one spoken line with a 'kind'
that decides the staging automatically (room, mood, labels, app screen, props). Override anything per beat.

    from adkit import build, beat as b
    TITLE, LINES, END, SFX, END_TAIL, PRELUDE = build(title, beats, app=..., sting=..., endline=..., tagline=...)

Beat kinds:
  fight     red shaking room, rainclouds stack up, open-loop label under captions
  walkout   speaker storms off screen, label -> 're-hook'
  alone     time cut ("1 HOUR LATER"), dark room, one pup alone
  return    the other pup walks back in (soft)
  stakes    the relationship is put on the line; stakes label appears and stays
  app       calm room, pups shift left, the feature's screen stays visible on the right (state per beat)
  reveal    the 'something stupid' is revealed: big prop emoji + label
  fail      the feature/attempt goes wrong: red flash returns
  line      plain two-pup line (mood-driven)
  twist     'plot twist' label
  solution  concrete fix: prop appears in the speaker's paws
  hug       hug + hearts (final warm beat before the end card)
Moods: angry, sad, shocked, smug, happy, sheepish, soft, flat.
"""
import json
from dialogue import D, ENDCARD

PRELUDE = r'''__PREL__
function stepsPhone(x,y,s,head,steps,active,done,note){phoneMock(x,y,s,-.04,()=>{appUI(head);
  steps.forEach((t,i)=>{const ok=done.includes(i);pill(-200+i*42,(ok?'✓ ':'')+t,i===active,ok?'#3fae6a':'#ff6b9d');});
  if(note){ctx.fillStyle=note.startsWith('❌')?'#d9503f':(note.startsWith('✅')||note.startsWith('💗'))?'#3fae6a':INK;
    ctx.font='bold 14px Poppins, "Noto Color Emoji"';ctx.textAlign='center';ctx.fillText(note,0,-48);}});}
function bigEmoji(e,x,y,sz,a){if(a<=0)return;ctx.save();ctx.globalAlpha=clamp(a);ctx.font=sz+'px "Noto Color Emoji"';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(e,x,y);ctx.restore();}
'''.replace('__PREL__', '\nfunction appUI(head){const g=ctx.createLinearGradient(0,-290,0,-10);g.addColorStop(0,\'#fff5f8\');g.addColorStop(1,\'#ffe3ec\');ctx.fillStyle=g;ctx.fillRect(-70,-290,140,280);\n  heart(0,-256,12,\'#ff6b9d\');if(head){ctx.font=\'bold 13px Poppins\';ctx.fillStyle=\'#ff6b9d\';ctx.textAlign=\'center\';ctx.textBaseline=\'alphabetic\';ctx.fillText(head,0,-228);}}\nfunction corner(txt,a){if(a<=0)return;ctx.save();ctx.setTransform(1,0,0,1,0,0);ctx.globalAlpha=clamp(a);ctx.font=\'bold 46px Poppins, "Noto Color Emoji"\';const w=ctx.measureText(txt).width+56;\n  ctx.translate(540,1690);ctx.fillStyle=\'rgba(255,250,240,.95)\';ctx.strokeStyle=\'#2c1d13\';ctx.lineWidth=5;ctx.beginPath();ctx.roundRect(-w/2,-40,w,80,40);ctx.fill();ctx.stroke();\n  ctx.fillStyle=\'#2c1d13\';ctx.textAlign=\'center\';ctx.textBaseline=\'middle\';ctx.fillText(txt,0,3);ctx.restore();}\nfunction biscuit(x,y,s){ctx.save();ctx.translate(x,y);ctx.scale(s,s);ell(0,0,30,30,\'#e0a95c\',{lw:4});for(let i=0;i<5;i++){ctx.fillStyle=\'#b9793a\';ctx.beginPath();ctx.arc(Math.cos(i*1.3)*14,Math.sin(i*1.3)*14,3.5,0,7);ctx.fill();}ctx.restore();}\nfunction packet(x,y,s,rot=0){ctx.save();ctx.translate(x,y);ctx.rotate(rot);ctx.scale(s,s);\n  blob(rectPts(-110,-60,220,120,26),\'#3f7fc7\',{lw:6});blob(rectPts(-70,-40,140,80,14),\'#fbe9c8\',{lw:4});\n  biscuit(-30,0,.9);biscuit(26,0,.9);ctx.fillStyle=\'#fff\';ctx.font=\'bold 18px Poppins\';ctx.textAlign=\'center\';ctx.textBaseline=\'middle\';ctx.fillText(\'BISCUITS\',0,-48);ctx.restore();}\n\nfunction calPhone(x,y,s,rot,day,rows,empty){phoneMock(x,y,s,rot,()=>{appUI(\'shared calendar\');\n  ctx.fillStyle=INK;ctx.textAlign=\'center\';ctx.font=\'bold 15px Poppins\';ctx.fillText(day,0,-206);\n  if(empty){ctx.save();ctx.setLineDash([5,5]);ctx.strokeStyle=\'#c9b9be\';ctx.lineWidth=2;ctx.beginPath();ctx.roundRect(-58,-190,116,60,12);ctx.stroke();ctx.restore();\n    ctx.fillStyle=\'#a8979c\';ctx.font=\'12px Poppins\';ctx.fillText(\'nothing today\',0,-155);}\n  rows.forEach((r,i)=>{ctx.save();ctx.strokeStyle=\'#ff6b9d\';ctx.lineWidth=3;ctx.fillStyle=\'#fff\';ctx.beginPath();ctx.roundRect(-58,-190+i*64,116,56,12);ctx.fill();ctx.stroke();ctx.restore();\n    ctx.fillStyle=INK;ctx.textAlign=\'center\';ctx.font=\'bold 12px Poppins, "Noto Color Emoji"\';ctx.fillText(r[0],0,-166+i*64);ctx.font=\'10px Poppins, "Noto Color Emoji"\';ctx.fillText(r[1],0,-148+i*64);});});}\nfunction ping(x,y,s,title,sub,a){if(a<=0)return;ctx.save();ctx.translate(x,y);ctx.scale(s*(.8+.2*back(clamp(a*2))),s*(.8+.2*back(clamp(a*2))));ctx.globalAlpha=clamp(a*3);\n  ctx.fillStyle=\'rgba(255,255,255,.97)\';ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.beginPath();ctx.roundRect(-230,-70,460,140,30);ctx.fill();ctx.stroke();\n  heart(-180,-30,22,\'#ff6b9d\');ctx.fillStyle=\'#8a7b80\';ctx.font=\'bold 22px Poppins\';ctx.textAlign=\'left\';ctx.textBaseline=\'middle\';ctx.fillText(\'reminder · now\',-148,-30);\n  ctx.fillStyle=INK;ctx.font=\'bold 32px Poppins, "Noto Color Emoji"\';ctx.fillText(title,-200,14);ctx.font=\'22px Poppins, "Noto Color Emoji"\';ctx.fillText(sub,-200,48);ctx.restore();}\nfunction ring(x,y,u){ctx.save();ctx.strokeStyle=INK;ctx.lineWidth=5;ctx.lineCap=\'round\';for(let i=0;i<3;i++){const r=30+i*22+Math.sin(u*14)*3;ctx.globalAlpha=.7-i*.2;ctx.beginPath();ctx.arc(x,y,r,-.7,.7);ctx.stroke();ctx.beginPath();ctx.arc(x,y,r,Math.PI-.7,Math.PI+.7);ctx.stroke();}ctx.restore();}\n\nfunction ptsPhone(x,y,s,val,rows,label,col){phoneMock(x,y,s,-.04,()=>{appUI(\'browny points\');\n  ctx.fillStyle=val===0?\'#d9503f\':INK;ctx.textAlign=\'center\';ctx.font=\'bold 46px Poppins\';ctx.fillText(val,0,-168);\n  ctx.fillStyle=INK;ctx.font=\'12px Poppins\';ctx.fillText(label||\'his points\',0,-145);\n  rows.forEach((r,i)=>pill(-126+i*34,r,true,col||\'#3fae6a\'));});}\n')

RED = "ctx.translate(Math.sin(u*47)*5,Math.cos(u*39)*3);room('#d98f84','#a55f55','rgba(255,255,255,.08)');"
SAD = "room('#56607e','#454e6a','rgba(255,255,255,.05)');"
CALM = "room('#f6dfc0','#cfa679');"
FLICK = "if(Math.sin(u*14)>.2){ctx.fillStyle='rgba(217,80,70,.35)';ctx.fillRect(-200,-200,W+400,H+400);}"
SHAKE = "hx:Math.sin(u*45)*4"

def corner(text, start=0.0):
    t = text.replace("'", "\\'")
    return "corner('%s',win(u,%s,99));" % (t, start)

def chip(text, a=.1, b=2.6):
    return "chip('%s',win(u,%s,%s));" % (text.replace("'", "\\'"), a, b)

MOODS = {   # speaker / listener pup props per mood
    'angry':   "brows:'angry',mouth:'open',earLift:.5",
    'sad':     "brows:'sad',mouth:'pout',earLift:-.3",
    'shocked': "eyes:'wide',mouth:'o',earLift:.4",
    'smug':    "eyes:'squint',mouth:'smile',tilt:.1",
    'happy':   "eyes:'happy',mouth:'smile',blush:.5,wag:.6",
    'sheepish':"eyes:'closed2',brows:'sad',mouth:'pout',blush:.9,earLift:-.4,hy:6",
    'soft':    "brows:'sad',mouth:'flat',earLift:-.2",
    'flat':    "mouth:'flat'",
}

def beat(who, text, kind='line', mood=None, other=None, emoji=None, **kw):
    """One spoken line. kw: label, prop, app=dict(active,done,note), chip, js (extra raw JS), sfx."""
    d = dict(who=who, text=text, kind=kind, mood=mood, other=other, emoji=emoji); d.update(kw); return d

def _pups(b, near=False, app=False):
    who = b['who']; oth = 'boy' if who == 'girl' else 'girl'
    dm = {'fight': 'angry', 'walkout': 'angry', 'stakes': 'soft', 'fail': 'angry', 'reveal': 'sad', 'hug': 'happy'}.get(b['kind'], 'flat')
    om = {'fight': 'shocked', 'walkout': 'shocked', 'fail': 'shocked', 'reveal': 'shocked', 'hug': 'happy'}.get(b['kind'], 'flat')
    sm, lm = MOODS[b['mood'] or dm], MOODS[b['other'] or om]
    if app:   pos = {'girl': "x:230,s:1.05,flip:-1,look:[.5,-.1]", 'boy': "x:480,s:1.0,look:[-.5,-.1]"}
    else:     pos = {'girl': "x:320,flip:-1,look:[.6,0]", 'boy': "x:780,look:[-.6,0]"}
    if b['kind'] == 'fight' or b['kind'] == 'fail':
        pos = {'girl': pos['girl'] + (",s:1.4" if not app else ""), 'boy': pos['boy'] + (",s:1.3" if not app else "")}
    shake = ("," + SHAKE) if b['kind'] in ('fight', 'fail') else ""
    sp = "SP('%s',u,{%s,talk:1,%s%s});" % (who, pos[who], sm, shake)
    lp = "SP('%s',u,{%s,%s});" % (oth, pos[oth], lm)
    if b['kind'] == 'walkout':
        x0 = 320 if who == 'girl' else 780; x1 = -80 if who == 'girl' else 1120
        sp = "SP('%s',u,{x:lerp(%d,%d,P(u,CURLEAD+CURVO-.4,CURLEAD+CURVO+.4)),%s,talk:1,%s});" % (
            who, x0, x1, "look:[-.5,.3]" if who == 'girl' else "flip:-1,look:[.5,.3]", sm)
    if b['kind'] == 'alone':
        return "SP('%s',u,{x:540,talk:1,%s,look:[.1,.5]});raincloudSmall(540,640,1);" % (who, MOODS[b['mood'] or 'sad'])
    if b['kind'] == 'return':
        x1 = 760 if who == 'boy' else 330; x0 = 1120 if who == 'boy' else -80
        fl = "" if who == 'boy' else "flip:-1,"
        sp = "SP('%s',u,{x:lerp(%d,%d,P(u,0,1)),%stalk:1,%s});" % (who, x0, x1, fl, sm)
        return sp + lp
    if b['kind'] == 'hug':
        return ("const hug=P(u,.3,1.1);SP('girl',u,{x:lerp(%s,%s,hug),flip:-1,eyes:'happy',mouth:'smile',blush:.7,paw:{x:70,y:-190,k:hug}%s});"
                "SP('boy',u,{x:lerp(%s,%s,hug),eyes:'happy',mouth:'smile',blush:.5,wag:1%s});if(u>.9)floatHearts(%s,800,.9,u,6,160);") % (
            (230, 280, ",s:1.05", 480, 440, ",s:1.0", 360) if app else (330, 420, "", 760, 650, "", 540))
    return lp + sp if who == 'boy' else lp + sp

def build(title, beats, app=None, sting=None, endline=None, tagline='', end_speaker='girl', end_extra='',
          hook_label='it started over something stupid 👇', rehook='wait for it 👀', stakes_label='last try 💔',
          win_label='it worked 💗', music=2):
    """app = dict(head='Resolve', steps=['🗣️  her turn','👂  his turn','🤝  the fix'])  (the feature's screen)
    sting = dict(owner='girl', sender='Ex 🚩', l1='...', l2='...', goal='1k')
    Returns TITLE, LINES, END, SFX, END_TAIL, PRELUDE for a dialogue.py spec."""
    from sting import sting as mk_sting, OUTRO_SECS
    lines = []; stakes_on = False; app_on = False; clouds = 0
    for b in beats:
        k = b['kind']; js = ''
        if k in ('fight', 'walkout', 'fail') and not app_on:
            js += RED; clouds += 1 if k == 'fight' else 0
        elif k in ('alone', 'return', 'stakes') and not app_on:
            js += SAD
        else:
            js += CALM
        if k == 'fail': js += FLICK
        if k == 'app' or b.get('app') is not None: app_on = True
        if k == 'stakes': stakes_on = True
        if b.get('chip'): js += chip(b['chip'])
        if k == 'alone' and not b.get('chip'): js += chip('1 HOUR LATER')
        # label under captions
        lab = b.get('label')
        if lab is None:
            if k == 'fight': lab = hook_label
            elif k == 'walkout': lab = rehook
            elif k == 'twist': lab = 'plot twist 👀'
            elif stakes_on and k not in ('hug', 'solution'): lab = stakes_label
        if lab: js += corner(lab, .4 if k in ('walkout', 'stakes', 'twist') else 0)
        if k in ('fight', 'walkout') and not app_on:
            for i in range(min(clouds, 3)):
                js += "raincloudSmall(%d,%d,%s);" % ((540, 400, 700)[i], (640, 580, 600)[i], 'win(u,.3,9)' if i == clouds - 1 else '1')
        js += _pups(b, app=app_on)
        if app_on and app:
            st = b.get('app') or {}
            js += "stepsPhone(820,1010,1.35,%s,%s,%s,%s,%s);" % (json.dumps(app['head']), json.dumps(app['steps'], ensure_ascii=False),
                   st.get('active', -1), json.dumps(st.get('done', [])), json.dumps(st.get('note', ''), ensure_ascii=False))
        if b.get('prop'):
            px = 360 if app_on else 540
            py = 700 if k == 'reveal' else 1000
            js += "bigEmoji(%s,%d,%d,%d,pop(u,CURLEAD+.4,.4));" % (json.dumps(b['prop'], ensure_ascii=False), px, py, 150 if k == 'reveal' else 110)
            if k == 'reveal':
                js += "ctx.save();ctx.globalAlpha=win(u,CURLEAD+.4,99);ctx.font='bold 40px Poppins';ctx.textAlign='center';ctx.fillStyle=INK;ctx.fillText('the something stupid',%d,580);ctx.restore();" % px
        if k in ('hug',) or b.get('sparkle'): js += "sparkle(%d,640,46*pop(u,.4,.4),win(u,.4,9));" % (360 if app_on else 540)
        js += b.get('js', '')
        lines.append(D(b['who'], b['text'], js, b.get('emoji')))
    lines.append(D(end_speaker, endline, ENDCARD(tagline, end_extra, speaker=end_speaker), '🔗'))
    sfx = []
    END = None
    if sting:
        q, a = mk_sting(sting['owner'], sting['sender'], sting['l1'], sting['l2'], sting['goal'])
        lines.append(q); END = a; sfx.append((len(lines) - 1, 'start', 'text'))
        tail = OUTRO_SECS
    else:
        END = lines.pop(); tail = 0
    return title, lines, END, sfx, tail, PRELUDE
