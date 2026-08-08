---
version: 1.11.0
last_updated: 2026-07-29
status: active
audience: internal
name: ama-research-engine
description: >-
  Dee Patience's AMA ("Ask Me Anything") research-and-writing system (AMA1-15).
  Invoke on "Run AMA#" / "run the AMA sequence", any VOC / voice-of-customer, audience,
  jobs-to-be-done, or keyword research, a competitor teardown, a transcript/decision-trace
  audit, or writing a pitch, listing, landing page, email, proposal, or SOP "in Dee's
  voice." Also invoke before ANY pitch/hook/headline/copy to enforce the rule that AMA4
  (VOC) + AMA5 (keyword) run first. Bakes in Dee's style rules (6th-grade, active voice,
  benefits-first, WIFE method, numerals-not-words, cite sources, no guessing, no em dashes).
when_to_use: "Buyer research, VOC, keyword work, competitor teardown, transcript audit, or writing copy in Dee's voice. NOT for live-conversation mining of calls/DMs/comments (that's prospect-interaction-analyzer) or scoring a finished pitch (that's ssp-analyzer)."
---

# AMA Research Engine

AMA is Dee Patience's research-and-writing operating system. It is two things at once:
1. **A sequence** — the order you run research so a pitch or piece of copy is built on real buyer language, not guesses.
2. **The "gold"** — the exact prompt instructions that make output come out punchy, brief, and in Dee's voice (the WIFE method).

This skill makes that system invokable. When the user types "Run AMA#", you become that AMA. When they ask for a pitch or copy, you make sure the research ran first.

## The one hard rule (why this skill exists)

**Never write a pitch, hook, headline, listing, or marketing copy before AMA4 (VOC) and AMA5 (keyword/deep research) have run.** Without them, an AI guesses — and guessed copy uses *internal* language, not the words real buyers use. That is the difference between copy that converts and copy that sounds like everyone else.

So if a user asks for a pitch/hook/copy and no AMA4 + AMA5 research exists yet in the conversation or project files, say so plainly and offer to run the research first. Do not silently invent buyer language.

**Free vs. paid line (do not cross it):** The free SSP analyzer scores the user's *own* words against the Clarity rubric — no outside research. The AMA4/AMA5 research (VOC pulled from Reddit/reviews/forums, keyword validation, competitor teardown) is the **paid** layer. Run the full AMA sequence only for paid "full Six Second Pitch" work, never as a freebie.

## The SSP sequence — run in this order

For any Six Second Pitch, brand message, or content build:

```
AMA13  →  AMA4  →  AMA5  →  SSP SOP  →  guide / content build
(align)   (VOC)    (keyword/   (write the pitch)
                    validate)
```

- **AMA13 — Transcript Intelligence & Continuity Auditor.** Align on what's already decided vs. still a draft. Pull real language from past files/transcripts before anything new. Stops you from contradicting a locked decision.
- **AMA4 — Audience Research (VOC + JTBD).** Pull *exact* customer phrases (never paraphrased) from reviews, Reddit, forums, competitor testimonials. Group into pains, desired outcomes, trigger moments. Flag trust signals + objections.
  - **HARD BOUNDARY — VOC is the AUDIENCE's voice, never the creator's.** An AMA4 quote tells you what words to *echo to the reader*. It is NOT the creator's testimony. **Never put an audience VOC quote into the creator's mouth as her own lived experience** (e.g. do not open Dee's post with a buyer's "I felt guilty for three days" as if it happened to Dee). When you write a first-person story in the creator's voice, the facts and feelings come from HER own story — the timeline, an interview, or her transcripts — not from AMA4. If you do not have her lived version, ASK her; do not borrow the audience's. (Lesson logged 2026-06: a buyer quote got personalized as Dee's; she caught it.)
- **AMA5 — Deep Research + Keyword Validation.** Confirm the AMA4 problem language is actually *searched*. Rank options, cite every source.
- **SSP SOP** then writes the pitch using only AMA4/AMA5 language. (AMA8 builds the longer launch copy — landing pages, email, offers — after the pitch is set.)

Other AMAs (full library in `references/ama-prompts-v10.5.md`) cover business writing, RAMP reports, tool comparisons, partner discovery, and more. The **client-onboarding** chain is AMA4 → AMA3.2 → AMA3.3 → AMA3.1.

## Brand-aware: templates vs. saved instances (READ THIS)

The AMA / SSP / KDP prompts are **templates** — the reusable "how." Each **brand or client is an instance** — its own saved "what." The same AMA4 runs for any brand or client; only the brand data and names differ. So every run is tied to a brand.

**Pick the template by the task:**
- Writing or publishing a **book** → **KDP** prompts.
- A **Six Second Pitch** / positioning / brand message → **SSP** (with AMA4/AMA5 research first).
- Any other **writing or research** (VOC, listings, copy, proposals, reports) → the **AMA** library.

**Before running, load the brand's instance:**
1. **Resolve the brand.** Which brand/client is this for? (your own brand, or a client brand you're working on.)
2. **Load that brand's `NAME-REGISTRY.md`** for the correct names, then the **root `NAME-REGISTRY.md`** for shared system names. Use those exact names; never invent or rename; never output a ⛔ DO NOT USE term.
3. **Load the brand's saved answers** from its workspace so you don't make Dee repeat herself — prior AMA4/AMA5 VOC, the Profit Profile (Person), the locked pitch, past outputs. Reuse them; build on them.
4. **Run the template** with the brand's data.
5. **Save the output back to the brand's workspace** so it becomes part of that brand's instance for next time.

**Brand workspace = where a brand's instance lives:** e.g. `Projects/Six Second Pitch/clients/[brand]/` (registry + `00-master.md` + saved AMA/SSP outputs). If a brand has no workspace yet, create one and start its `NAME-REGISTRY.md` from the root template.

### AMA9 = the Name Registry layer (not "business copy")
AMA9's real job is the **glossary**: hold the proper names — services, frameworks, acronyms (your brand, RAMP, LOCK, the 6Ps), titles, domains — so every other thread uses them right and Dee never re-explains. It runs in two modes against `NAME-REGISTRY.md`:
- **Enforce:** before writing, use the registry's exact names; flag anything missing rather than guessing.
- **Capture:** when Dee names a new thing, add it to the registry.
The names live in the registry file (one place to fix), **not** hardcoded in the prompt. (The old AMA9 body had its 6P list as "...Product, *Profit*, Process..." — that dropped Promise; the registry is the corrected single source.)

## How to run an AMA

When the user says "Run AMA#":

1. **Open `references/ama-prompts-v10.5.md` and read that AMA's verbatim prompt.** That text is the spec. Follow its role, its steps, and its output format exactly — it is Dee's IP, refined over years. Do not improvise a different structure.
2. **Confirm context first if the prompt requires it.** AMA13 in particular must ask which mode before running: Summary (this transcript only), Continuity (scan prior threads for confirm/conflict/expand), or Decision Trace (audit who decided what, when). Never scan across threads/files without the user's say-so.
3. **Gather the inputs the prompt names** — the niche/product, the files or reviews to analyze, the folder to reference. If something required is missing, note it inside the response and research to fill the gap rather than stalling (that is how Dee's prompts are written to behave).
4. **Produce the output in the prompt's required format** (e.g. AMA4's VOC table grouped by pain / desired outcome / trigger moment; AMA13's Role → Mode → Findings → Recommendations → Gaps).
5. **Cite sources** for any external fact, quote, or number. Quotes must be real and verbatim.

If the user names a sequence ("run the AMA sequence", "run the SSP research"), run the steps in order, pausing after each so they can approve before you move on.

## Dee's style rules — bake these into every AMA output

These are non-negotiable across all AMAs. They are what makes the output sound like Dee:

- **3rd–5th grade reading level** (Dee's standing rule, not 6th). Short words, short sentences. Plain over clever.
- **Numbers as numerals, with symbols.** Write `$3,000` not "three thousand dollars," `33%` not "thirty-three percent," `2 in 3` not "two in three." The eye reads numerals AS numbers and jumps to them; spelled-out numbers and the word "percent" force people to slow down and read. Always numerals for money, stats, percentages, and data.
- **Active voice.** "Buyers want X," not "X is wanted by buyers."
- **Benefits first.** Lead with what's in it for the reader, then the feature. This is the **WIFE method**: **W**hat's In It For Me · voice that's punchy and active · **I**mage-rich language · **E**asy to read. (Also written WIFEY/WIFM — same idea: speak to the reader's payoff.)
- **Punchy, never casual.** Tight and confident. Not stiff, not chatty.
- **Mobile-friendly.** Short paragraphs, natural line breaks, scannable. Use tables when they make data clearer.
- **Facts only. No guessing. Cite sources.** If you don't know, say "I don't know" and look it up. Never invent claims, features, reviews, or numbers.
- **No emojis or symbols unless the user asks** for them.
- **No em dashes.** Dee reads them as AI writing. Use a period, comma, or "and" instead.
- **Never preachy**, even on faith-based brands. Respect the voice; don't sermonize.
- **For regulated products** (supplements/health): show how to make claims compliantly; never invent health claims.

After drafting, reread once as if you were the buyer on a phone. If a line is stiff, long, or feels AI-written, cut it.

## Human-Reading QC gate (run BEFORE any copy ships — AMA's copy gate)

AMA is the **COPY gate**, the way premium-ux is the **VISUAL gate**. Any copy — article, listing, page, email, pitch — PASSES this checklist before it ships. **Do not freehand copy and skip this.** When a copy-producing skill (premium-ux, KDP, SSP, the article-engine) writes, it routes the words through AMA and this gate. It does not write on its own.

- [ ] **Numerals + symbols** — money `$`, percentages `%`, stats as numerals (never spelled out).
- [ ] **Reading level 3rd–5th grade** — short words, short sentences (check it, don't assume).
- [ ] **Scannable (MEASURED, not eyeballed)** — front-loaded answer, question-style H2s, one bold key phrase per section, lists where 3+ parallel items appear. **Paragraphs: 2–3 sentences max (~50 words), one idea each — COUNT the sentences; any 4+ sentence block gets split or turned into a list.** "Short paragraphs" as a vibe is NOT the gate; the sentence count is. Copy that was hand-edited AFTER a cold-read or Council pass must RE-PASS this count before it ships. (Added 2026-07-10: a testimony article passed with 5–7 sentence walls because "scannable" had no number — the same gap the visual gate had before px/contrast made it enforceable; the walls were in hand-applied revisions that never went back through this gate. Dee: "seems like this isn't that scannable.")
- [ ] **WIIFM + curiosity loops** (non-negotiable) — EVERY line passes the "so what?" test. If the reader could say "so what," cut it or make it pay off. EVERY headline and subhead opens a curiosity loop that teases the payoff the reader wants, never scene-only or topic-only ("What God showed me when I prayed about AI," NOT "The night a machine broke apart in my dream"). They have to want to keep reading.
- [ ] **Per-H2 curiosity-loop audit (added 2026-07-03)** — go H2 by H2 and judge each ONE like a YouTube title/thumbnail: would a stranger who only read this heading want to know the answer? A topic-label H2 is weaker than a question/tension H2. Rewrite any H2 that reads as a label instead of an open question or a tease. (Lesson: an article had 2 flat H2s that weren't caught until Dee's own read, despite passing every measured QA number. Dee's actual bar: "does it have curiosity loops and would it make a good YouTube video.")
- [ ] **Sounds like a person, MEASURED two ways (added 2026-07-30).** The reading-level and paragraph-count checks do not catch robot cadence, so add both of these. **(a) Count the everyday contractions** (don't, you're, it's, isn't, we've, I'm, that's). For anything informal (an email, a note to a friend, a personal page), **ZERO contractions in a piece over ~200 words is an automatic FAIL** and near-zero is a warning. **(b) Get an outside cold read** before it ships: hand it to ChatGPT or a fresh session and ask two literal questions, *does this sound like a friend or like a consultant deliverable*, and *is this actually skimmable or is it secretly a blog post*. Quote back the exact lines it flags. **Why:** on 2026-07-28 a 503-word email to two friends passed every measured gate here with **0 contractions**, and Dee said "oof you're writing like AI no tlike it's my friends." A later ChatGPT cold read then caught two things no number here looks for: "30% friend, 70% consultant... the document quietly places you in that role", and "you're writing a blog post" when a checklist was asked for. The count is the floor; the cold read is the ceiling. Run both.
- [ ] **No em dashes. No AI filler** ("honestly," "delve," "in conclusion," "it's worth noting," "tapestry").
- [ ] **On-message** — headline/topic checked against AMA4 (VOC) + AMA5 (keyword) so it ranks for what people actually search.
- [ ] **LLM-rankable** — FAQ block + schema present; answers a real question clearly.
- [ ] **Dee's coined terms verbatim** (Six Second Pitch, Grounded Growth, ROOTS vs LIES, etc.).
- [ ] **Capability and tier claims are TESTED or ATTRIBUTED, never borrowed (added 2026-07-28)** — any public sentence about what a product/plan/platform *supports* ("works on every plan," "runs on any phone," "free version includes X") must either (a) have been verified on that exact tier/device/version, or (b) be stated as the vendor's claim with a link and an out for the reader ("Claude lists it on Free too; if you hit a snag, email me"). Never repeat a vendor's spec sheet in your own voice as if you tested it. Why: toolkit install copy said skills "work on every plan, including Free" sourced from a help-center page, while the live test had run only on a Max account — and a prerequisite (code execution) may not exist on Free, which would have sent the exact users we were rescuing straight back into a broken install. Dee caught it in 5 words: "yes but I have claude pro." Same family as [[verify-before-assert]], applied to outbound copy instead of internal claims.
- [ ] **Rewrites preserve locked/branded frameworks** (added 2026-07-01) — if this copy touches a piece with a named pillar/framework (ROOTS vs LIES, FIRST, 6P), diff the new draft against ALL of that framework's parts before it ships. Fixing one problem (a thesis, a voice pass, a trim) must never silently drop another locked part. (Lesson: a v1→v2 rewrite of "Is It a Sin to Use AI" fixed the thesis but silently dropped the entire ROOTS half of the ROOTS-vs-LIES pillar; it shipped live before Dee caught it — "you didt publish my ROOT pillar on either article. why.")

If any box fails, fix it before showing or publishing. The user is never the QC.

## The QC gate is a LOOP, run for real, never delegated (added 2026-07-02)
This mirrors what the design skill (premium-ux) locked in its v1.29.0: the writing gate is only real if it actually runs, as a loop, on this model.

1. **A brief that carries the voice rules is NOT the gate.** Handing a subagent (or yourself, from memory) a list of the rules above and having copy written "to spec" produces compliance, not voice. The gate is only satisfied when `ama-research-engine` is actually invoked and its Human-Reading QC is run against the drafted words. (Lesson, 2026-07-02: 4 your brand video-to-article drafts were written by cold subagents from a brief carrying the AMA rules; the gate had not really run. When it was invoked for real it immediately caught 3 em dashes hiding as `&mdash;` entities and a live `[FILL IN]` in an FAQ, both of which a plain-text scan and the design pass had missed. Applying the rules loosely from memory or a brief IS the failure mode this gate names.)
2. **Never delegate the write/voice pass to a cold subagent.** Subagents are for research and mechanical steps only (pulling transcripts, gathering reviews, first-pass structure). The actual voice pass, and this QC, stay with the top model in the main session, the same boundary premium-ux draws for composition. Cold agents executing a spec cannot hold Dee's / the brand's voice.
3. **Run it as a LOOP, not a one-shot checklist:** write → reread as the buyer on a phone → fix the stiff/long/AI-sounding lines → reread → only then ship. One pass is not the gate. Grep for em dashes **entity-aware** (`—`, `&mdash;`, `&#8212;`) and for `[FILL IN]`, not just the literal character, before calling it clean. **Grep for SPELLED-OUT NUMBERS too** (added 2026-07-29): the numerals rule is as much a voice rule as the em dash and it had no check, so `"Five moves"` and `"five minutes"` shipped all the way to PRODUCTION on faithfocushaven.com before a final pass caught them. Run this over the whole artifact and convert every hit to a numeral:
   ```
   grep -inE '\b(two|three|four|five|six|seven|eight|nine|ten|twenty|thirty|fifty|hundred|thousand) (minutes?|hours?|days?|weeks?|months?|years?|steps?|ways?|moves?|things?|reasons?|percent|dollars?)\b|\bone (minute|hour)\b' <files>
   ```
   **Bare `one` is deliberately EXCLUDED** (calibrated 2026-07-29 against the live site): including it produced 5 false positives in one pass, all the "One thing I can let go of today" kind, where `one` is a natural determiner in kid-facing prose, not a quantity. Dee's rule targets **money, stats, percentages and data**, not every occurrence of the word. Calibrating it this way still caught both real misses AND surfaced a third the manual pass had missed (`day1` also said "about five minutes"). Watch the ones hiding in non-body fields: the two that shipped were in a card subline and an email autoresponder string. **The grep runs over the WHOLE artifact, including its own scaffolding — title, headers, meta/frontmatter lines — not just the body you were mentally treating as "the copy," and "passed" is not sayable until that grep has actually run and returned clean.** (Lesson 2026-07-08: a WYR grading kit's 20 body prompts were clean, but the file TITLE carried an em dash straight through the voice pass; "voice QC passed, no em dashes" was said before the grep ran. Measure-first caught it. The scaffolding is where the miss hides precisely because you're not thinking of it as copy.)
4. **Floor, not ceiling (Dee, standing rule).** These rules are the minimum, written for lower models. Apply better judgment on top (does this actually sound like this person, would the buyer keep reading), and fold real improvements back here via skill-trainer.

## Voice of Creator (Dee's own words)

AMA13 and AMA4 both protect *exact phrasing*. When you capture Dee's coined terms, faith language, or framework names (Six Second Pitch, Profit Profile, Grounded Growth, WIFE, RAMP, LOCK), keep them verbatim. Do not neutralize or reword them. Tag faith-based content as "Faith Context" and never flatten its tone.

## Where the prompts live

- **`references/ama-prompts-v10.5.md`** — the full verbatim library (all 18 AMAs + AMA3.x subs + Quick Reference Table), v10.5 CURRENT approved by Dee 2026-07-14. This is bundled so the skill is portable. (`ama-prompts-v10.4.md` kept beside it for history.)
- **Canonical master:** `6P System/ama-prompts-verbatim-v10.5.md` in Dee's repo. If the master changes, re-copy it into this skill's `references/` so they stay in sync. The master wins if they ever disagree.

## Connection to the rest of the system

AMA4/AMA5 are the research behind the **Six Second Pitch** (P1–P3 of the 6P System) and the **Profit Profile™** Person work. This skill is the foundation the paid "full Six Second Pitch" and the SSP report upgrade are built on. See `12-ama-research-sequence.md` and `02-six-second-pitch.md` in the 6P System repo.

## Works with
- **Upstream (who calls AMA):** an internal brand-coaching flow can route here for the audience/problem/promise research; any pitch/copy/book task starts here so research runs before writing.
- **Downstream (where AMA output goes):** `ssp-analyzer` (AMA4+AMA5 feed the pitch), `kdp-prompt-system` (research → book description/launch), `premium-ux-conversion-designer` (VOC → page copy).
- **Boundary vs `prospect-interaction-analyzer`:** that skill mines *live conversational data* (call transcripts, DMs, comments) verbatim. AMA4 is *desk VOC* (reviews, forums, competitor sites) plus the writing voice. If the user hands over raw calls/DMs/comments to mine → that skill. If they want buyer research pulled + copy written → AMA.

*AMA Prompt System™ · © Dee Patience LLC · part of the Grounded Growth System.*
