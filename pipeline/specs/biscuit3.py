import sys; sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
import biscuit2 as B2
from sting import sting, OUTRO_SECS
TITLE = B2.TITLE; MUSIC_N = B2.MUSIC_N; PRELUDE = B2.PRELUDE
q, a = sting('girl', 'Ex 🚩', 'I got your favourite', 'biscuits 🍪😉', '1k')
LINES = list(B2.LINES) + [B2.END, q]
END = a
END_TAIL = OUTRO_SECS
# faaaack on: the opening insult, the "something stupid" reveal, the spare-packet twist, the ex's text
SFX = [(0, 'end', 'faaak'), (10, 'end', 'faaak'), (16, 'end', 'faaak'), (18, 'start', 'text+faaak')]
