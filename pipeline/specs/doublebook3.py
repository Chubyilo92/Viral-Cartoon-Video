import sys; sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
import doublebook as DB
from sting import sting
TITLE = DB.TITLE; MUSIC_N = DB.MUSIC_N; PRELUDE = DB.PRELUDE
q, a = sting('boy', 'Mum 💐', "She's not the one.", "Don't marry her.", '5k likes for part 2 👀')
LINES = list(DB.LINES) + [DB.END, q]
END = a
