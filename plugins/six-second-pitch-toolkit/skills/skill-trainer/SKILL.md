---
version: 1.9.0
last_updated: 2026-07-28
status: active
audience: internal
name: skill-trainer
description: Dee's review + lessons-into-skills loop. After any work it runs an objective EVALUATE -> GAPS -> CLARIFY -> IMPROVE review of what was just done, through an ISO 9001 / Six Sigma lens (version control, single source of truth, doc sprawl, dates, repeated mistakes, false assumptions, which skills should have fired) AND folds the approved lessons back into the relevant skills so the team gets better over time. Fire it without waiting to be asked whenever the user reflects on how work went or how to improve, or says any of: "lessons learned", "what did we learn", "review", "retro", "retrospective", "process review", "what worked", "what didn't", "train the skills", or at the end of a major deliverable or session. Not for code correctness or pull-request review; it does not BUILD new skills (that is skill-creator) - it TRAINS the existing skills and the way of working.
when_to_use: After a deliverable, milestone, or session, to grade the WORK and the WAY OF WORKING and turn lessons into fixes that get folded back into the skills. Pair with the repo standards it cites; this skill RUNS the review and trains the skills, the standards GOVERN how skills are written and shipped.
---

# Skill Trainer — Dee's review + lessons-into-skills loop (was "Process Review")

Run this when Dee wants an honest look back at what was just done and how to make both the work AND the way of working better. It replaces the long prompt she used to paste. Treat it as a quality system, not a pep talk: the goal is fewer repeated mistakes, a cleaner paper trail, and a process a 6th grader could follow.

**How this fits the repo:** the `SKILL-AUTHORING-STANDARD.md` and `OUTPUT-QA-AND-DELIVERY-STANDARD.md` (repo root) are the *rulebooks* for how skills are written and shipped. This skill is the *action* that audits a session or deliverable against that same ISO/Six-Sigma thinking. When a review turns up a skill that breaks a standard, fix the skill and bump it per that standard.

## First: get on the strongest setting
This is judgment work, so quality scales with model strength. Recommend Dee run it on the most capable model / highest reasoning effort available (her original prompt said "switch to Opus"). If you cannot switch, say so plainly and proceed.

## The one rule that makes this work
Do the four steps **in order**. **Do not skip a step. Do not combine GAPS and IMPROVE** by quietly fixing things. Name what is wrong first, ask before revising, and only fix after the user answers. Quietly fixing hides the lesson, so the same mistake returns later. This guardrail is the whole point.

## Step 1 — EVALUATE (what actually happened)
Assess what was produced against the **stated goal**. Be specific: mark each part **strong / adequate / weak** and say WHY. Ground it in the real thread, not memory:
- The feedback and criticism the user gave (quote the turning points).
- The mistakes and **false assumptions** made along the way.
- How the output got corrected, and what was finally **approved or praised**.

**Measure before you opine.** If a fact is checkable (which branch is live, what files exist, the real date, what's deployed, whether work was pushed), check it with tools first. A review built on memory repeats the errors it is supposed to catch.

## Step 2 — GAPS (no softening)
State plainly what is missing, underdeveloped, wrong, or risky. No hedging. If something is off, name it. **Rank by impact** (Pareto: the vital few first, not a flat list).

### Mandatory process checklist (inspect EVERY time)
Walk this out loud. These are the defects that repeat across sessions:

- [ ] **Single source of truth** — is the work built on the CURRENT doc, or a stale/superseded one? (Newest date is NOT automatically the truth; check for a STATE file that says what's authoritative.) **A handoff/session-notes claim ("X is still not done," "cancel Y") is a hypothesis, not a fact — search for evidence (e.g. `find`/`grep` the project tree) before repeating it to the user or acting on it.** (Added 2026-07-01 after a handoff's "cancel Mailchimp" and "GHL CSV not exported yet" both turned out stale — the user doesn't have Mailchimp, and the CSV was already saved from a prior thread. Both surfaced as if current instead of being checked first. See [[verify-before-assert]].)
- [ ] **Version control** — branch hygiene: merged/dead branches pruned; nothing valuable stranded on an abandoned branch; the working branch is the right one.
- [ ] **Saving / backup** — is the work committed AND pushed? Anything living only on local disk (data-loss risk)? **MEASURE this with `git status` / `git log` — never assert commit/push state from memory or assumption** (added 2026-07-01 after "nothing has been committed yet" was told to Dee when a parallel process had already committed most of it). **Watch for concurrent writers:** in a shared repo, another thread or an automated import may be committing at the same time — check `git log` timestamps, and **stage your own files selectively** (`git add <file>`) so you don't commit another thread's changes under your message or get your work swept into theirs with a misleading label.
- [ ] **Organization** — doc sprawl: are superseded files marked or archived? Can a newcomer find "what's current" in 30 seconds? **Before hand-building ANY new deliverable — a doc, OR a design asset/component/template — search the target folder for an existing one on the same topic first** — a plausible-sounding gap ("X isn't built yet") can be wrong, and a duplicate can omit a real deadline, spec, or design decision the existing one already had. (Added 2026-07-01 after a redundant Meet-With-Dee rebuild handoff was written before checking Dee Website for the existing, more detailed one, which also carried a hard deadline the duplicate missed. Generalized 2026-07-01 after the SAME failure hit a design asset, not just a doc: a locked, Council-approved acronym-card template already existed in `Dee Website/article-templates/` while a plain hand-coded box shipped instead on the "Is It a Sin to Use AI" article.)
- [ ] **Date integrity** — were files/commits stamped with the REAL date? (Verify with the `date` command.) **Re-run `date` if the session has been long or spanned a break** — a session that started yesterday will happily keep stamping yesterday's date onto today's files.
- [ ] **Is the broken version still live?** (added 2026-07-28) When this session FIXED something that exists on a public surface, check what that surface serves *right now* (`curl` the live page/README/file) and say it out loud: "the fix is committed locally, the broken version is still up." A local fix plus an intentional hold is a legitimate choice, but it must be a *stated* choice with a known cost, not a quiet gap nobody names. Why: during the toolkit install relaunch, the crisis-causing "paste these 2 commands" README stayed live to the public for the entire session while a corrected version sat committed-unpushed, and no one said so until the review measured it. Sibling of [[verify-before-assert]]: "we fixed it" and "users see the fix" are different claims.
- [ ] **Secrets** — did any API key, password, or token get pasted into chat? If so, flag it for rotation.
- [ ] **Repeated mistakes** — what did the user have to say more than once? Each repeat is a process defect, not a one-off.
- [ ] **Locked work untouched** — was anything finished/locked changed without being asked? (Change only what was requested.)
- [ ] **Right tools** — which skills/plugins SHOULD have been used and weren't? When a lesson is approved, fold it back into the relevant skill (and bump it per the authoring standard), not just this one deliverable.
- [ ] **Inconsistencies** — names, numbers, dates, or statuses that disagree across docs.
- [ ] **Plain language** — did we speak the user's language, not the system's? Flag any internal IDs (post/attachment/page numbers, git hashes, version numbers) or DB/CMS/dev jargon used *in conversation* — refer to things by title + where they live. And when the user sounded lost/overwhelmed, did we zoom out to plain English proactively, or keep spiraling in detail? (Added 2026-07-01 after "fix post 864" + version-number talk lost Dee twice: "I have no idea what post you're talking about" / "what are you talking about and where are we?")

## Step 3 — CLARIFY (ask before fixing)
Ask the questions you need answered before revising. **Do not assume** intent, scope, or priority. Lead every choice with a recommendation, marked "(Recommended)", plus a one-line pro/con (the repo's Rule 11 — recommend, don't just ask). Then **STOP and wait**. Do not begin Step 4 until the user answers.

## Step 4 — IMPROVE (only after answers)
Produce the improved version, incorporating every gap the user signed off on. Make the fixes **reproducible and plain enough for a 6th grader**: where things live, what changed, and why. When a lesson is general, write it where it will be reused — a `STATE.md`, an SOP, or the relevant skill — so it sticks and is not relearned next time.

**Before writing into a shared skill file, re-read it fresh and check for conflicts with what you're about to add (2026-07-01).** Dee runs lessons-learned across several threads at once on purpose, and the same skill file can be mid-edit by another thread when you go to write yours. Don't write from the copy you read at the start of the session. Immediately before the edit: re-open the file, read what's already there (including any version bump another thread already made), and check whether it says something that agrees, disagrees, or overlaps with the lesson you're about to add. If it conflicts, surface that to Dee rather than silently picking a side or silently overwriting. If it's just a numbering collision with no real content conflict, bump past whichever version is highest and note the collision inline (see the article-engine 1.9.0/1.10.0 entries for the pattern). Dee's own words: "when things are being overwritten, go back and take a look at what's already written there and see if there's any conflicts with what you're about to write... we need the last one to double-check."

## ✅ Done when (acceptance criteria)
- [ ] All four steps done, **in order**, none skipped or merged.
- [ ] EVALUATE cited the **real thread** (feedback, corrections, what was approved), not memory, and verified checkable facts with tools.
- [ ] The **process checklist** was walked and its findings reported.
- [ ] GAPS were **ranked** and unsoftened; CLARIFY asked real questions, led with recommendations, and **stopped** for answers.
- [ ] IMPROVE happened **only after** the user answered, and general lessons were written somewhere reusable.

## Output shape (keep it scannable)
Use these headers exactly, in this order: **EVALUATE** → **GAPS** (including the checklist findings) → **CLARIFY** (the questions, then stop) → and, after answers, **IMPROVE**.

## Plain-English crosswalk (why these steps)
- EVALUATE + measure-first = ISO "check against the real thing," Six Sigma "Measure."
- GAPS + ranked checklist = Six Sigma "Analyze" + Pareto (fix the vital few).
- CLARIFY before fixing = mistake-proofing (poka-yoke): you cannot fix the wrong thing if you ask first.
- IMPROVE + write-the-lesson-down = Lean "kaizen": small logged improvements that compound.

## Works with
- **Governed by** `SKILL-AUTHORING-STANDARD.md` (how skills are written) and `OUTPUT-QA-AND-DELIVERY-STANDARD.md` (the visual ship gate). This skill RUNS the review and folds approved lessons back into whichever skill was used.
- **Not** `skill-creator` (which builds NEW skills) or `code-review` (code correctness). This trains existing skills and the way of working.
- **Pairs with** any skill that was just used; that is the one it grades and improves.
