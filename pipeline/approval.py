"""Script approval lock (added 28 Oct 2026).

The 25 Oct batch was built from scripts the writer approved and scored itself. Now a script can only
be built if its EXACT text is recorded in docs/approvals.json by the independent reviewer step
(docs/REVIEWER.md), with status "approved" and scores that meet docs/RULES.md. make_video.py,
make_short.py and preflight.py all call check(); any edit to the text after approval changes the hash
and blocks the build until it is re-reviewed.

approvals.json entry:
  "boy_cries": {"sha256": "...", "status": "approved" | "hold" | "cut",
                "reviewer_avg": 7.25, "p_1k": 0.40, "review_file": "reviews/2026-10-27.md",
                "date": "2026-10-27", "note": "..."}
"""
import hashlib, json, os, sys

CANDIDATES = [
    os.environ.get('JJ_APPROVALS', ''),
    '/home/claude/viral-cartoon-video/docs/approvals.json',
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'approvals.json'),
]
MIN_AVG = 7.0    # 30 Oct 2026: Chuby told Claude to make the call; 8.5 left the channel empty (nothing reviewed scored above 7.25). See RULES.md §4.
MIN_P1K = 0.35  # 30 Oct 2026: audience-growth focus; Conversion dropped from the average (RULES.md §4)


def script_text(spec):
    """Normalised text of what the viewer reads/hears. Long format: BODY_LINES. Short: HOOK + beat captions."""
    if hasattr(spec, 'BODY_LINES'):
        lines = list(spec.BODY_LINES)
    elif hasattr(spec, 'BEATS'):
        lines = [getattr(spec, 'HOOK', '')] + [b[0] for b in spec.BEATS]
    else:
        raise SystemExit('approval: spec has neither BODY_LINES nor BEATS')
    return '\n'.join(' '.join(str(l).split()) for l in lines).strip()


def text_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def load():
    for p in CANDIDATES:
        if p and os.path.exists(p):
            return json.load(open(p)), p
    raise SystemExit('approval: docs/approvals.json not found — nothing is approved, refusing to build')


def check(slug, spec):
    data, path = load()
    e = data.get(slug)
    h = text_hash(script_text(spec))
    if not e:
        raise SystemExit(f'APPROVAL FAILED: {slug} is not in {path}. Run the independent reviewer (docs/REVIEWER.md) first.')
    if e.get('status') != 'approved':
        raise SystemExit(f'APPROVAL FAILED: {slug} status is {e.get("status")!r}, not approved.')
    if e.get('sha256') != h:
        raise SystemExit(f'APPROVAL FAILED: {slug} text differs from the reviewed text (hash mismatch). '
                         'Any change after review must be re-reviewed.')
    if float(e.get('reviewer_avg', 0)) < MIN_AVG or float(e.get('p_1k', 0)) < MIN_P1K:
        raise SystemExit(f'APPROVAL FAILED: {slug} reviewer scores {e.get("reviewer_avg")}/{e.get("p_1k")} '
                         f'below the floor ({MIN_AVG} avg, {MIN_P1K:.0%}).')
    return h


if __name__ == '__main__':
    # python3 approval.py hash <slug>   -> print the hash of a spec's text (to record after review)
    # python3 approval.py check <slug>  -> exit 0 only if approved
    import importlib
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'specs'))
    cmd, slug = sys.argv[1], sys.argv[2]
    spec = importlib.import_module(slug)
    if cmd == 'hash':
        print(text_hash(script_text(spec)))
    else:
        print('approved', check(slug, spec))
