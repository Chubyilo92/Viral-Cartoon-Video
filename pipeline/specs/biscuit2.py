import sys; sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
# Fight = the original worst-fight script up to "Then I'm done" (unchanged lines, plus the hook labels).
# Everything after = the biscuit version (app unnamed, live stakes, failed repeat-back, spare packet).
import worstfight as WF, biscuit as B

TITLE = B.TITLE
MUSIC_N = 2
PRELUDE = B.PRELUDE

fight = [dict(s) for s in WF.LINES[:6]]   # can't stand you / your mom / dare / break / never good enough / I'm done
for i, s in enumerate(fight):
    tag = B.HOOK if i < 5 else "corner('wait for it 👀',win(u,.5,9));"
    s['js'] = s['js'].replace("room('#d98f84','#a55f55','rgba(255,255,255,.08)');", "room('#d98f84','#a55f55','rgba(255,255,255,.08)');" + tag, 1)

LINES = fight + B.LINES[5:]               # from "...Why did I say that?" onward
END = B.END
