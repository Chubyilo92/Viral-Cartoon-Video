import sys; sys.path.insert(0, '/home/claude/jj'); sys.path.insert(0, '/home/claude/jj/specs')
import anniversary as AN
from sting import sting, OUTRO_SECS
TITLE = AN.TITLE; MUSIC_N = AN.MUSIC_N; PRELUDE = AN.PRELUDE
q, a = sting('girl', 'Ex 🚩', 'Happy anniversary baby.', 'I miss you 🥺', '10k')
LINES = list(AN.LINES[:-1]) + [q]          # AN.LINES already ends with the end card + old question; swap in the new sting
END = a
END_TAIL = OUTRO_SECS
# faaaack on: the opening insult, "nothing" in the calendar, "why are you mad at ME?", the ex's text
SFX = [(17, 'start', 'text')]
