import sys; sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
import doublebook as DB
from sting import sting, OUTRO_SECS
TITLE = DB.TITLE; MUSIC_N = DB.MUSIC_N; PRELUDE = DB.PRELUDE
q, a = sting('boy', 'Mum 💐', "She's not the one.", "Don't marry her.", '5k')
LINES = list(DB.LINES) + [DB.END, q]
END = a
END_TAIL = OUTRO_SECS
# faaaack on: "short guy", the dinner isn't in the app, his mum's text
SFX = [(14, 'start', 'text')]
