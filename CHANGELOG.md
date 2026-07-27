# What's New — Six Second Pitch Toolkit

*Newest on top. Plain English: what changed and what it means for you.*
*Your copy updates automatically (or run `/plugin marketplace update six-second-pitch`).*
*The version you have = the `version` line in `plugin.json`.*

---

## 0.2.0 — 2026-07-27
**The no-terminal install is here.** You can now run the toolkit in the regular Claude app — no Claude Code, no GitHub, no commands.

- **New `zips/` folder:** one small zip per skill. In Claude (claude.ai), go to Customize -> Skills -> Add -> Upload a skill and drag a zip in. Upload them **one at a time** — that's a Claude limit, not ours.
- **Fixed:** Route Review's description was longer than Claude's upload limit, so its zip was rejected (and could silently stop a multi-file drag). Trimmed. A build check now makes sure no skill can ship over the limit again.
- **Updated:** the Audience Recon research prompt library is now the current v10.5 edition.
- **Updating your copy:** Claude Code users update like always. Zip users: download the new zip and upload it again — same name replaces the old version, about a minute per skill.

---

## 0.1.1
- Tidied the bundled research prompt library: swapped internal examples for generic placeholders so every prompt reads cleanly for any brand.

---


## 0.1.0 — 2026-07 (first release)

The toolkit is live. 5 skills that work as a team:

- **The Kickoff** — interviews you once, writes your Team Bible so you never repeat yourself.
- **The Navigator** — your project manager. Tell it what you need; it routes the work.
- **The Six Second Pitch** — scores your message with a Clarity Score (5 modes).
- **Audience Recon** — pulls your buyer's real words before anything gets written.
- **Route Review** — reviews finished work and folds the lessons back into the tools.

A page-design skill is coming as a free update. What you get: install once, updates arrive
on their own. Free to use, even on client work, when you keep the credit. Full terms in LICENSE.md.
