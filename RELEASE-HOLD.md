# RELEASE HOLD — the repo is public, the ANNOUNCEMENT is held

**Written:** 2026-07-28

## What actually happened

v0.2.0 (the one-path README, the per-skill `zips/`, the description-limit fixes) was committed
locally on 2026-07-27 with the intent to hold it until the website and email were ready.
**The nightly 11pm auto-push shipped it anyway.** As of 2026-07-28 the public repo serves
v0.2.0 and the new install instructions.

Nobody was harmed by this: the version that went out is strictly better than what it replaced
(the old README told people to paste Claude Code commands, which is what caused the support
crisis). The zips shipped with it, so the instructions in the live README actually work.

**Lesson recorded:** in this repo, "committed locally, not pushed" is NOT a durable hold. The
cron pushes overnight. To truly hold work here, keep it on a branch or leave it uncommitted.

## What is still held

**The announcement, not the code.** Do not drive traffic here yet:
1. sixsecondpitch.com/toolkit still has NO download section. The README links there, so anyone
   following the site link finds nothing to download. The in-repo `zips/` folder is the working
   download source until that page ships.
2. SendFox automation 118885 (`Toolkit Quick-Start`) is PAUSED and its first email still tells
   people to paste plugin commands. Do not unpause it until it is rewritten.

## Release the announcement when all 3 are true
1. The /toolkit page download section is designed, approved, and deployed.
2. SendFox E1 no longer mentions plugin commands.
3. Dee says go.

Then delete this file, push, and verify:
`curl -s https://raw.githubusercontent.com/Dechontelle/six-second-pitch-toolkit/main/.claude-plugin/marketplace.json | grep version`

*While this file exists, `save` (Step 4.6) must not push this repo without telling Dee.*

Full plan: `Six Second Pitch/2026-07-28-HANDOFF-toolkit-v020-launch.md`
