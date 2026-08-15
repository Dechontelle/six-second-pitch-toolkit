# RELEASE HOLD — the repo is public, the ANNOUNCEMENT is held

**Written:** 2026-07-28. **Corrected:** 2026-08-04.

## What actually happened

v0.2.0 (the one-path README, the per-skill `zips/`, the description-limit fixes) was committed
locally on 2026-07-27 with the intent to hold it until the website and email were ready.
**It got pushed anyway, the same session, and more work has landed on top of it since** — a
name/folder bugfix on 2026-08-04, plus skill-version bumps from later sessions. As of right
now the public repo is live and current.

**Corrected mechanism note (the 2026-07-28 version of this file blamed "the nightly 11pm
cron" — that was never checked, and it was wrong. Verified 2026-08-04: no system cron job
exists on this Mac (`crontab -l` is empty). `cowork-push.sh` (the Cowork sandbox's own push
script) doesn't even push this repo — it's not in that script's list.** The real mechanism is
a person or a Claude Code session on the Mac running `save`, which follows Step 4.6 and pushes
directly. **This file does not stop that.** It's prose in `save`'s SKILL.md that a session has
to notice and choose to honor — not a code-level gate. Nothing enforces it automatically.

**Lesson: "committed locally, not pushed" is not a durable hold in this repo, and this file's
existence is not either — both rely on a session reading and following instructions.** If you
need a real hold, keep the work on a branch, or ask directly whenever `save` runs here.

## What is still held (VERIFIED LIVE 2026-08-04, not assumed)

**The announcement, not the code.** Checked just now:
1. **sixsecondpitch.com/toolkit still has no download section** — fetched fresh, 18,233 bytes,
   zero mentions of "download," "zips," or "Upload a skill." Unchanged since this file was
   written. The README links here, so anyone following the site link finds nothing to
   download; the in-repo `zips/` folder is still the only working download source.
2. **SendFox automation 118885 status not reverified this pass** — last known PAUSED with
   plugin-command copy in E1. Check the live automation directly before assuming either way.

## Release the announcement when all 3 are true
1. ✅ **DONE 2026-08-15.** The /toolkit page download section is designed, approved, and deployed.
   Merged `toolkit-download-section` → `main`, pushed, verified LIVE on sixsecondpitch.com/toolkit
   (not just a preview): 5 real tool cards, install steps, FAQ, version reads 0.2.1. Confirmed a
   real download works end to end — `curl`'d `sixsecondpitch.com/downloads/skill-trainer.zip`
   live, got HTTP 200 and a valid zip with `SKILL.md` inside.
2. ⬜ **Still open, NOT reverified this pass.** SendFox E1 last known PAUSED with plugin-command
   copy in it (automation 118885). Check the live automation directly before assuming either way.
3. ⬜ **Still open.** "Push v0.2.1" and "merge the download page" were both explicitly approved by
   Dee (2026-08-15) — but that is not the same approval as "send the announcement email" / "call
   the toolkit officially relaunched." Get that go separately before touching #2.

Once #2 and #3 are both true, delete this file. (There's no push to hold back at that point — the
repo's already live.)

Full plan: `Six Second Pitch/2026-07-28-HANDOFF-toolkit-v020-launch.md`

## STATUS UPDATE 2026-08-09
The held CONTENT is already public: a parallel session pushed 85a1ca4 (README plan-requirement fix)
on 2026-08-08 18:18, which carried the committed AMA 1.11.0 + skill-trainer 1.11.0 rebuilds with it.
So the repo now serves current skill versions; this hold now governs (a) the ANNOUNCEMENT timing and
(b) future pushes only. The nightly `auto-commit.sh` now has a guard: repos with this file get
committed locally but never auto-pushed.

## STATUS UPDATE 2026-08-15
v0.2.1 pushed live (Dee's explicit go) — skill versions caught up to canon, `ssp-analyzer` got its
first version number, the sync script now mirrors zips to the site automatically so this class of
drift can't recur. Then the download page itself shipped (condition 1 above). **This hold now
governs ONLY the announcement (condition 2 + 3) — the product itself is fully live and current.**
