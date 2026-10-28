# QA checklist (rewritten 28 Oct 2026)

The old version of this file described checks that never failed the run: "audio muxed in" only checked
that an audio stream existed, its sample code pointed at paths that don't exist in this pipeline, and
nothing enforced "look at the frames". A silent or platform-muted video and banned hashtags all got
through. QA is now code that exits non-zero. Follow `docs/RULES.md` §5. In short:

| Check | Enforced by | Fails when |
|---|---|---|
| Script text approved by the independent reviewer, unchanged since | `approval.py` (called by both builders and preflight) | slug missing, status not "approved", text hash differs, reviewer avg < 8.5 or P(1k) < 40% |
| Voice lines don't overlap; duration; size | builder writes `<file>.qa.json`; preflight fails if any `*_ok` is false | overlap, 35-75 s (long) / 15-25 s (short), > 25 MB |
| Narration pace, rising endings, pauses, mispronunciation (long only) | `voicecheck.py` exits 1 on any FLAG; preflight requires `<slug>.voicecheck.json` with 0 flags | any FLAG |
| Music is original | builder writes `<file>.music.json`; preflight | record missing or not `original*.wav` |
| Audio actually audible | preflight (`volumedetect`, `silencedetect`) | mean < -30 dB or > -8 dB, any silence > 1.5 s |
| Right cut for the platform (long) | preflight | file not `*-instagram.mp4` / `*-tiktok.mp4` matching `--platform` |
| Caption | preflight | banned tag (#fyp #foryou #foryoupage #viral #trending #explore), > 5 tags, duplicate tag, TikTok link/"bio", long IG caption without the bio test |
| Scheduled file = the file that passed | preflight `--url` (sha256 of the downloaded file) | URL not commit-pinned, download fails, bytes differ |
| What Metricool saved | read-back after createScheduledPost (RULES §5.7) | caption differs, banned tag, wrong time/providers/draft |
| Frames look right | **manual**: look at `work/<slug>/sheet.png` (short) or `*_f0..5.png` (long), name them in the log | can't be enforced by code |

**Can't be checked from here:** the copy Metricool re-hosts (static.metricool.com is blocked by this
environment's network), and whether a platform mutes audio after publishing. Original music is the
only protection against muting.

If any gate fails: fix the cause and rebuild once. If it fails again, don't schedule. Log it as failed
with the reason and leave the slot empty.
