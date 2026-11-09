"""Script approval lock (added 28 Oct 2026; numeric floor dropped 9 Nov 2026).

The 25 Oct batch was built from scripts the writer approved and scored itself. Now a script can only
be built if its EXACT text is recorded in docs/approvals.json by the independent reviewer step
(docs/REVIEWER.md), with status "approved". make_video.py, make_short.py and preflight.py all call
check(); any edit to the text after approval changes the hash and blocks the build until it is
re-reviewed.

9 Nov 2026 (Chuby): the MIN_AVG/MIN_P1K numeric gate below is REMOVED. It produced a ~1-in-30 approval
rate because the passing zone (floor 7.0, nothing the reviewer ever scored above 8.5) was a sliver at
the very top of the reviewer's own range — not a meaningful quality signal, closer to a lottery. The
floor is now docs/WINNERS-BLUEPRINT.md: a script is only marked "approved" in approvals.json if the
reviewer can name which current top-5 real performer it matches or beats and say why (see RULES.md §4
and WINNERS-BLUEPRINT.md). reviewer_avg/p_1k are still recorded for trend tracking but are no longer
checked here. MIN_AVG/MIN_P1K are kept below, unused, only so old approvals.json entries and review
files that cite them still make sense when read historically.

approvals.json entry:
  "boy_cries": {"sha256": "...", "status": "approved" | "hold" | "cut",
                "reviewer_avg": 7.25, "p_1k": 0.40, "benchmark": "matches girl_no_makeup",
                "review_file": "reviews/2026-10-27.md", "date": "2026-10-27", "note": "..."}
"""
import hashlib, json, os, sys

CANDIDATES = [
    os.environ.get('JJ_APPROVALS', ''),
    '/home/claude/viral-cartoon-video/docs/approvals.json',
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'approvals.json'),
]
MIN_AVG = 7.0    # historical reference only, no longer enforced — see module docstring (9 Nov 2026)
MIN_P1K = 0.35  # historical reference only, no longer enforced — see module docstring (9 Nov 2026)


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
