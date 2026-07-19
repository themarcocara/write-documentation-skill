# Prose Review Rubric

Read this in full when running Pass 2 (prose advisory review) of `copydesk-write` mode. It is a reference, not a script — apply it by judgment against the text in front of you.

You are reviewing text written for outside consumption. Your job is to find problems. Be specific and blunt. The hard-fail checks (fatal pattern, em dashes, banned phrases, AI-vocabulary and ChatGPT-isms hard fails) already ran in Pass 1, using the Always-Active Rules in the main instruction text — don't re-litigate those here. This rubric covers everything past that: mid-tier vocabulary, voice drift, and structural advisory patterns.

## CRITICAL: What good prose looks like

Good prose has VARIED rhythm. Short sentences and long sentences working together. Parenthetical asides. Qualifications mid-sentence. Sentences that take their time. Your job is NOT to make every sentence shorter or simpler. Compression is just as much a failure mode as bloat. If every sentence is a short declarative (subject-verb-object), that is MONOTONY and you should flag it. If every sentence is long and compound, that is also monotony. The goal is natural variation, like a person actually talking.

DO NOT recommend:
- Making sentences shorter unless they are genuinely bloated
- Removing qualifications, asides, or hedging (these are human)
- Simplifying sentence structure when the current structure serves the idea
- Flattening tone to be more "direct" when the original has personality

DO flag:
- Mechanical repetition of the same sentence architecture
- AI vocabulary and banned phrases (always)
- Lack of voice, personality, or opinion
- Abstraction without grounding

## Voice Drift Detection

If the active register's voice feature description is available (it always should be — load it per the Register System section of the main instruction text before running this pass), use it to check for voice drift. The feature description defines the target voice. Flag any passage where the writing drifts away from the described voice toward generic AI prose.

Specific drift patterns to watch for:
- **Register flattening:** The feature description calls for register mixing (casual + technical, profane + analytical) but the text stays in a single consistent register throughout.
- **Authority performance:** The feature description calls for demonstrated knowledge without credentialing moves, but the text announces expertise ("As someone who has studied..." / "It's important to understand...").
- **Smoothness where roughness is specified:** The feature description calls for abrupt transitions, visible course-corrections, or anti-conclusion, but the text flows smoothly from point to point and lands on a tidy summary.
- **Missing parenthetical functions:** The feature description specifies parentheticals that anticipate reader objections or subvert overly clean sentences, but the text uses parentheticals for informational footnotes or random asides.
- **Enthusiasm dampening:** The feature description calls for open, unguarded enthusiasm, but the text hedges positive claims into measured assessment.
- **TED Talk naming announcements:** The feature description may call for naming patterns or concepts. Flag when the text announces the name with fanfare ("I call this the X principle" or "There's a name for this: X") instead of just starting to use the term.
- **Self-affirming transitions:** Transitions that congratulate the argument ("And this is where it gets interesting" / "This is the crucial part") instead of just making the next point.
- **Softened endings:** The feature description may call for anti-conclusion or blunt terminals, but the text wraps up with a warm, encouraging, or summarizing final paragraph.
- **Retrospective narrator:** The text steps above the timeline to announce discoveries from the future: "I'd later call this," "What fell out of the analysis," "I'd later learn." The feature description may call for writing from inside the experience. Flag when the text names or frames something from retrospective distance instead of encountering it in the moment.
- **Promotional confidence on own work:** The text makes confident capability claims about the writer's own tool, project, or output without hedging. The feature description may call for genuine hedging. Flag claims like "generates text in your voice" or "produces genuinely good output" where the writer would naturally say "close to your voice" or "as good as I could get it."

Report voice drift findings as advisories (not hard fails) in the advisory table.

## What you're checking

### Mid-tier AI vocabulary (FLAG in advisory table, not auto-fixed)

These are words/phrases the register's voice feature description should prevent naturally. If they show up, it means the voice drifted. Flag them in the advisory table so the user can decide.

**Dead AI language:**
- "Furthermore" / "Additionally" / "Moreover"
- "Harness" / "Leverage" / "Utilize"
- "Landscape" / "Realm" / "Robust"
- "Game-changer" / "Cutting-edge" / "Straightforward"
- "Supercharge" / "Unlock" / "Future-proof"
- "In order to"

**Dead transitions:**
- "Moving forward" / "At the end of the day"
- "To put this in perspective..."
- "What makes this particularly interesting is..."
- "The implications here are..."
- "In other words..."
- "It goes without saying..."

**Engagement bait:**
- "This changes everything"
- "Are you paying attention?"
- "You're not ready for this"

**AI cringe:**
- "10x your productivity"
- "The AI revolution"
- "In the age of AI"

**Generic insider claims:**
- Anything with "nobody" or "most people don't realize"

### Advisory patterns (flagged, not auto-fixed)

Check for these and report in the advisory table. Each is a potential issue, not an automatic fail. The user decides.

**1. Dramatic pivots.** "Here's what I actually believe," "That last part is what I can't stop picking at." Flag if the pivot phrase could be deleted and the paragraph still flows. The pivot is doing performative work, not structural work.

**2. Softened negation-correction.** Acknowledging a framing only to replace it with the "real" explanation. Flag if the acknowledged framing gets no development (no specific detail, quotation, or genuine engagement). Do NOT flag the ventriloquize-then-dismantle move when the opposition framing is developed with specific detail.

**3. Frictionless transitions.** Count paragraph transitions. If zero are abrupt, flag it. At least 1 in 5 transitions should feel like a rough join where one paragraph ends and the next starts somewhere slightly different. Consistently smooth flow is a machine signal.

**4. Present participial tails.** Any sentence ending with a comma followed by a present participle, where the participial phrase could be deleted without losing the point. Example: "The company expanded rapidly, becoming a leader in the field." Flag the participial tail.

**5. Cascading triples.** X which causes Y which causes Z. Flag if the cascade could be stated as a single causal claim. The triple-cascade is an AI pattern for creating false complexity.

**6. Conclusion symmetry.** Final 2-3 paragraphs mirroring each other's sentence structure. Flag the structural echo. Human endings are asymmetric.

**7. Caps overuse.** All-caps on single words for emphasis is an endorsed advocacy technique. Do NOT flag single-word caps on quantifiers, absolutes, or scope words (ANY, NO, ZERO, EXACTLY, etc.) when used sparingly. DO flag: caps on phrases (2+ words), caps on neutral adjectives, or more than 1 caps instance per section.

**8. Performed specificity.** Concrete details (numbers, named items, day-of-week) that look grounded but don't refer to anything irreplaceable. Test: can you swap each specific for a different specific of the same shape without changing the meaning? If yes, flag it. Example: "what used to take three systems and a Friday spreadsheet" — swap to "five tools and a Monday dashboard" and the meaning is unchanged. Often shows up in compressed callbacks where a vivid earlier detail gets reduced to a verbal token in a later paragraph, stripping the load-bearing part. Distinct from #5 (vague attributions about WHO is speaking) and #4 (promotional vocabulary). This is structural — about the relationship between specifics and the underlying claim.

**9. Hollow anadiplosis.** Word-echo (last word of one clause becomes the first word of the next) used to create rhetorical shape, where the second clause asserts a tautological implication of the first instead of developing it. Real anadiplosis develops each link (Yoda: "fear leads to anger, anger leads to hate, hate leads to suffering" — each step adds a new concept). Hollow anadiplosis just restates. Example: "The operational sprawl becomes readable, and readable sprawl is the kind that gets fixed" — the second clause asserts readability implies fixability, which the first clause already implied. Adjacent to #24 (generic positive conclusions) but more specific: that one is about empty upbeat endings; this is about device-without-substance using word-echo structure.

**10. Asyndeton tricolon.** Three items listed without conjunctions, each longer and more emotionally weighted than the last: "Two hours of degraded service, six engineers figuring out what I'd done wrong, a postmortem where I had to explain my reasoning to people who had been paged at home." AI builds these to manufacture escalating emotional weight where a plainer statement would do. Flag the three items and note the increasing length.

**11. Parallel reason chains.** Three consecutive sentences sharing the same "subject + because/when + reason" clause shape, even when the subjects differ: "I filed patents because X. The project started because Y. I gave talks when Z." The parallel shape is detectable even across different subjects. Flag the run and suggest varying the clause structure (one "because," one bare assertion, one gerund or fragment).

**12. Participial reframe pivot.** A list of plain facts followed by a participial opener that reframes them as insight: "Laid out in a petition, the same facts read like a deliberate strategy." "Seen this way, the whole arc reads differently." AI uses this pivot to manufacture the appearance of insight; the observation should be stated directly without the reframing device. Quote the participial opener.

### AI-edited fraction estimate

Separately from line-level findings, estimate what portion of the text reads as AI-written or AI-edited. This covers the common case where a human drafts over an AI scaffold, or edits an AI draft rather than writing from scratch.

Look for distribution clues:
- Uniform AI signature across the whole text suggests pure AI generation.
- Specific paragraphs polished, others rough, suggests selective AI editing.
- AI vocabulary clustering in transitions and conclusions while the body stays concrete suggests an AI scaffold with human substance dropped in.
- Voice changing mid-text (formal to casual or back) suggests mixed sources.

Report one bucket: `Pure human (~0%)` / `Lightly AI-assisted (~10-30%)` / `Mixed authorship (~30-60%)` / `Heavily AI-edited (~60-90%)` / `Pure AI (~100%)`.

### Engagement

- Does the opening earn the next sentence?
- Is there a reason to keep reading past the first paragraph?
- If the opening is generic or could apply to any article on this topic, flag it.

### Soullessness

- Does this read like a person wrote it, or like a committee produced it?
- Is there a voice? Opinions? Honest uncertainty?
- If you stripped the byline, could you tell a human from a language model? If not, flag it.

### Grounding

- Are abstract claims anchored to specific people, numbers, scenes, or objects?
- Flag any passage that goes 3+ sentences of pure abstraction without a concrete anchor.

### Monotony

- Is the same sentence structure repeating mechanically?
- 3+ sentences in a row with identical architecture is a flag.
- This includes staccato (all short declaratives) AND bloat (all long compound sentences).

### Structural uniformity (paragraph level)

- Count sentences in each paragraph. If 3+ consecutive paragraphs have the same sentence count, flag it.
- Check paragraph openings. If 3+ consecutive paragraphs open the same way, flag it.
- Check section architecture. If every section follows the same internal pattern, flag it.

### Declarative sentence dominance

- 5+ consecutive declarative sentences without an interrogative, conditional, imperative, or exclamatory fragment is a flag.
- Also check for register monotony. If every sentence sounds like "writing" (precise, formal, crafted) with no "talking" sentences, flag it.

### Clause density uniformity

- Check whether sentences within a paragraph carry roughly the same amount of information. Human writers pair short headline sentences with longer unpacking sentences. Flag passages of 4+ sentences where clause density doesn't vary.

### Missing self-correction

- Does the writer ever change direction, qualify a prior claim, or admit uncertainty? If the piece reads as a smooth, confident march from thesis to conclusion with no visible thinking, flag it.

## Output format

**Advisory table:** all findings (mid-tier vocabulary, voice drift, advisory patterns, structural issues, engagement, soullessness, grounding, monotony):

| # | Line | Pattern | Current | Proposed fix |
|---|---|---|---|---|
| 1 | [quote the text] | [pattern name] | [what's wrong] | [a proposed replacement or direction] |

**AI-edited fraction:** one bucket from the estimate above.

**What's working:** 1-2 sentences on what the prose does well. This prevents over-correction of good writing.

If no issues found, return: "Clean. No issues detected."

---

## AI Pattern Reference

The following reference catalogs 24 patterns of AI-generated writing. Use it to identify problems in the text you're reviewing. Based on Wikipedia's "Signs of AI writing" page, maintained by WikiProject AI Cleanup.

---

## PERSONALITY AND SOUL

Avoiding AI patterns is only half the job. Sterile, voiceless writing is just as obvious as slop. Good writing has a human behind it.

### Signs of soulless writing (even if technically "clean"):
- Every sentence is the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective when appropriate
- No humor, no edge, no personality
- Reads like a Wikipedia article or press release

---

## CONTENT PATTERNS

### 1. Undue Emphasis on Significance, Legacy, and Broader Trends

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted

**Problem:** LLM writing puffs up importance by adding statements about how arbitrary aspects represent or contribute to a broader topic.

### 2. Undue Emphasis on Notability and Media Coverage

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

**Problem:** LLMs hit readers over the head with claims of notability, often listing sources without context.

### 3. Superficial Analyses with -ing Endings

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**Problem:** AI chatbots tack present participle ("-ing") phrases onto sentences to add fake depth.

### 4. Promotional and Advertisement-like Language

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

**Problem:** LLMs have serious problems keeping a neutral tone, especially for "cultural heritage" topics.

### 5. Vague Attributions and Weasel Words

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)

**Problem:** AI chatbots attribute opinions to vague authorities without specific sources.

### 6. Outline-like "Challenges and Future Prospects" Sections

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

**Problem:** Many LLM-generated articles include formulaic "Challenges" sections.

---

## LANGUAGE AND GRAMMAR PATTERNS

### 7. Overused "AI Vocabulary" Words

**High-frequency AI words:** Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**Problem:** These words appear far more frequently in post-2023 text. They often co-occur.

### 8. Avoidance of "is"/"are" (Copula Avoidance)

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]

**Problem:** LLMs substitute elaborate constructions for simple copulas.

### 9. Negative Parallelisms

**Problem:** Constructions like "Not only...but..." or "It's not just about..., it's..." are overused.

### 10. Rule of Three Overuse

**Problem:** LLMs force ideas into groups of three to appear comprehensive.

### 11. Elegant Variation (Synonym Cycling)

**Problem:** AI has repetition-penalty code causing excessive synonym substitution.

### 12. False Ranges

**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful scale.

---

## STYLE PATTERNS

### 13. Em Dash Overuse

**Problem:** LLMs use em dashes more than humans, mimicking "punchy" sales writing.

### 14. Overuse of Boldface

**Problem:** AI chatbots emphasize phrases in boldface mechanically.

### 15. Inline-Header Vertical Lists

**Problem:** AI outputs lists where items start with bolded headers followed by colons.

### 16. Title Case in Headings

**Problem:** AI chatbots capitalize all main words in headings.

### 17. Emojis

**Problem:** AI chatbots often decorate headings or bullet points with emojis.

### 18. Curly Quotation Marks

**Problem:** ChatGPT uses curly quotes instead of straight quotes.

---

## COMMUNICATION PATTERNS

### 19. Collaborative Communication Artifacts

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

**Problem:** Text meant as chatbot correspondence gets pasted as content.

### 20. Knowledge-Cutoff Disclaimers

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information...

**Problem:** AI disclaimers about incomplete information get left in text.

### 21. Sycophantic/Servile Tone

**Problem:** Overly positive, people-pleasing language.

### 22. Filler Phrases

**Problem:** Unnecessary padding like "In order to achieve this goal" (just "To achieve this"), "Due to the fact that" (just "Because"), "It is important to note that" (just state the thing).

### 23. Excessive Hedging

**Problem:** Over-qualifying statements beyond what honesty requires.

### 24. Generic Positive Conclusions

**Problem:** Vague upbeat endings like "The future looks bright" or "Exciting times lie ahead."

### 25. Performed Specificity

**Problem:** Concrete details (numbers, named items, day-of-week, etc.) that have the texture of grounded writing but don't refer to anything irreplaceable. The detail performs specificity without committing to a particular case.

**Test:** Can you swap each specific for a different specific of the same shape without changing the meaning? If yes, the detail is decorative.

**AI-tic example:** "what used to take three systems and a Friday spreadsheet to track" — swap to "five tools and a Monday dashboard" and the meaning is unchanged. The "three," the "Friday," and the "spreadsheet" are arbitrary tokens dressed as grounding detail.

**Real-specificity contrast:** "Allstate processed 22 million claims in 2024" — changing any of those words changes what's being claimed. Solnit's "Evan Snow, a thirtysomething user experience design professional" — each detail narrows the claim to one specific person.

Distinct from #5 (vague attributions, about WHO speaks) and #4 (promotional vocabulary). This is structural — about the relationship between the specifics and the underlying claim. Often shows up in compressed callbacks: a vivid detail in paragraph A gets reduced to a verbal token in paragraph B, stripping the load-bearing part.

---

## Key Insight

LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases. Your job is to catch every instance where the text defaulted to statistical likelihood instead of specific, human expression.
