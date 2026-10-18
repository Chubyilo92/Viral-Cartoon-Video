"""Caption helper for winners-blueprint scripts: captions are generated FROM the spoken
line so on-screen words always match what the narrator says (older specs hand-wrote
captions and some drifted from the voice)."""
import re
from _kit import S, HUG, SHARE  # noqa

TT_STD = "We're two little pups trying to find a thousand people who love like this... If this made you think of someone... follow us. We'll keep making them for you."


def C(line, emoji=None, maxw=3):
    emoji = emoji or {}
    parts = [p.strip() for p in re.split(r'\.\.\.|[.,;:!?]', line) if p.strip()]
    out = []
    weak = {'a','an','the','to','and','with','of','in','on','your','you\'re','her','his','my','who','for','at','it','that','like','if','but','just','she','he','you','is','was','when','there','their','what','how','not','because','so','or','no','one'}
    def cost(c, last):
        k = len(c)
        pen = {1: 5, 2: 0, 3: 0, 4: 2}.get(k, 9)
        if not last and c[-1].lower().strip("'\"") in weak:
            pen += 4
        return pen
    for p in parts:
        w = p.split()
        if len(w) <= 3:
            out.append(' '.join(w).lower().replace('"', "'")); continue
        best = {0: (0, [])}
        for i in range(1, len(w) + 1):
            opts = []
            for k in range(1, 5):
                if i - k in best:
                    c = w[i - k:i]
                    opts.append((best[i - k][0] + cost(c, i == len(w)), best[i - k][1] + [c]))
            best[i] = min(opts, key=lambda x: x[0])
        out += [' '.join(c).lower().replace('"', "'") for c in best[len(w)][1]]
    for k, e in emoji.items():
        for i, c in enumerate(out):
            if k in c:
                out[i] = c + ' ' + e
                break
    return out


def spec(lines, draws, emoji_per_line=None):
    emoji_per_line = emoji_per_line or [None] * len(lines)
    return [S(C(l, e), d) for l, d, e in zip(lines, draws, emoji_per_line)]
