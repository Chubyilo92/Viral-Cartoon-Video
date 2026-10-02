import sys; sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
import biscuit2 as B2
from sting import sting
TITLE = B2.TITLE; MUSIC_N = B2.MUSIC_N; PRELUDE = B2.PRELUDE
q, a = sting('girl', 'Ex 🚩', 'I got your favourite', 'biscuits 🍪😉', '1k likes for part 2 👀')
LINES = list(B2.LINES) + [B2.END, q]
END = a
