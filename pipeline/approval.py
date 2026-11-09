"""Script approval lock.

A script can only be built if its EXACT text is recorded in docs/approvals.json by the independent
reviewer step (docs/REVIEWER.md), with status "approved". make_video.py, make_short.py and preflight.py
all call check(); any edit to the text after approval changes the hash and blocks the build until it is
re-reviewed. "Approved" means the reviewer judged the script MATCHES or BEATS a named script from the
current top-5 in docs/WINNERS-BLUEPRINT.md — there is no numeric threshold here or anywhere else in the
pipeline; the benchmark judgment itself is the gate.

approvals.json entry:
  "boy_cries": {"sha256": "...", "status": "approved" | "hold" | "cut",
                "benchmark": "matches girl_no_makeup",
                "review_file": "reviews/2026-10-27.md", "date": "2026-10-27", "note": "..."}
"""
import hashlib, json, os, sys

CANDIDATES = [
    os.environ.get('JJ_APPROVALS', ''),
    '/home/claude/viral-cartoon-video/docs/approvals.json',
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'approvals.json'),
]


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
