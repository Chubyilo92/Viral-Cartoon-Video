"""Multi-character staging for JJ dialogue ads: the couple + bestie, his mum, her ex.
Roles: girl, boy, friend, mum, ex.  P(role, x, face, mood, talk) -> JS for one pup.
face 'r' = looking right, 'l' = looking left."""
import sys; sys.path[:0] = ['/home/claude/jj', '/home/claude/jj/specs']
from dialogue import D
from adkit import MOODS, RED, SAD, CALM, FLICK, SHAKE, corner, chip, PRELUDE as KIT

STYLE = {
    'girl':   ('girl', ''),
    'boy':    ('boy', ''),
    'friend': ('girl', "pal:{fur:'#f0c27e',ear:'#c4864a',muz:'#fff4de'},bowCol:'#f2c230',bowCol2:'#f8dc7a'"),
    'mum':    ('girl', "pal:{fur:'#dcd7d2',ear:'#a59c96',muz:'#f7f4f1'},bowCol:'#a07ed6',bowCol2:'#c8b3ee',collar:1,bandana:1,bandCol:'#f5f0e6'"),
    'ex':     ('boy',  "pal:{fur:'#7c6b62',ear:'#3d322e',muz:'#d6c5b6',patch:'#5b4c45'},bandCol:'#d9473f'"),
}
TAGS = {'friend': ('HER BESTIE', '#f2c230'), 'mum': ('HIS MUM', '#a07ed6'), 'ex': ('HER EX 🚩', '#d9473f')}

PRELUDE = KIT + r'''
function nameTag(x,y,t,col){ctx.save();ctx.font='bold 30px Poppins, "Noto Color Emoji"';const w=ctx.measureText(t).width+36;ctx.fillStyle=col;ctx.strokeStyle=INK;ctx.lineWidth=4;
  ctx.beginPath();ctx.roundRect(x-w/2,y-24,w,48,24);ctx.fill();ctx.stroke();ctx.fillStyle='#fff';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(t,x,y+2);ctx.restore();}
function tank(x,y,s){ctx.save();ctx.translate(x,y);ctx.scale(s,s);blob(rectPts(-110,-150,220,150,14),'rgba(170,215,240,.75)',{lw:6});
  ctx.fillStyle='rgba(120,180,220,.5)';ctx.fillRect(-104,-110,208,104);ctx.font='70px "Noto Color Emoji"';ctx.textAlign='center';ctx.textBaseline='middle';
  ctx.fillText('🐠',Math.sin(T*1.3)*45,-60+Math.sin(T*2)*8);ctx.restore();}
function cake(x,y,s){ctx.save();ctx.translate(x,y);ctx.scale(s,s);blob(rectPts(-90,-70,180,70,10),'#fff3b0',{lw:5});blob(rectPts(-90,-80,180,22,10),'#ffe066',{lw:5});
  ctx.font='40px "Noto Color Emoji"';ctx.textAlign='center';ctx.fillText('🍋',0,-95);ctx.restore();}
'''

def P(role, x, face='r', mood='flat', talk=False, s=None, extra='', y=None):
    kind, st = STYLE[role]
    fl = "flip:-1,look:[.6,0]" if face == 'r' else "look:[-.6,0]"
    bits = ["x:%s" % x, fl, MOODS.get(mood, mood)]
    if st: bits.append(st)
    if s: bits.append("s:%s" % s)
    if y: bits.append("y:%s" % y)
    if talk: bits.append("talk:1")
    if extra: bits.append(extra)
    js = "SP('%s',u,{%s});" % (kind, ",".join(b for b in bits if b))
    if role in TAGS:
        t, c = TAGS[role]
        js += "nameTag(%s,%s,%s,'%s');" % (x if isinstance(x, (int, float)) else 540, 735, repr(t), c)
    return js

def S(who, text, room, cast, emoji=None, label=None, chipt=None, js=''):
    """cast = list of P(...) strings. Speaker's P must include talk=True."""
    body = room + (chip(chipt) if chipt else '') + (corner(label) if label else '') + ''.join(cast) + js
    return D(who, text, body, emoji)
