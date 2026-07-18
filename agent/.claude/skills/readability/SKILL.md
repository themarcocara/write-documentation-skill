---
name: readability
description: Analyze text readability with Flesch-Kincaid, Gunning Fog, SMOG, and other metrics, and revise text to hit a target readability level (e.g. "6th grade," "general adult," "college"). Returns objective scores with interpretation, recommendations, and — on request — a rewritten draft that lands in the target range.
user-invocable: true
argument-hint: "[text to analyze or revise] [optional: target level, e.g. '8th grade' or 'adult']"
---

# Analyze and Revise for Readability

Two modes. Pick one before doing anything else:

- **Analyze** (default): score the text, report metrics, suggest fixes. No rewrite.
- **Revise**: the user wants the text rewritten to *land in* a target readability range. Triggers: "simplify this," "make this readable for a 6th grader," "lower the reading level," "rewrite for a general audience," or any explicit grade/score target.

If the request is ambiguous, analyze first, then ask whether they want a revision.

## Input

The user provides text in $ARGUMENTS. If no text is provided, ask for it.

## Scoring is procedural — never hand-compute or eyeball a score

All metrics in both modes come from `.claude/skills/readability/scripts/readability_score.py`, a stdlib-only Python script colocated with this file. Do not estimate syllables, sentence counts, or scores yourself, and do not do the arithmetic by hand — run the script and read its JSON output. This keeps scores reproducible and internally consistent (all metrics are derived from the same tokenization).

Invocation, via Bash:

```bash
# Analyze mode: write the text to a temp file, then score it
cat > /tmp/text.txt <<'EOF'
<the text>
EOF
python3 .claude/skills/readability/scripts/readability_score.py /tmp/text.txt

# Revise mode: score before/after in one call once you have a draft
python3 .claude/skills/readability/scripts/readability_score.py --diff /tmp/before.txt /tmp/after.txt

# Either mode also accepts stdin with "-" instead of a file path
echo "<text>" | python3 .claude/skills/readability/scripts/readability_score.py -
```

The script returns JSON with: `words`, `sentences`, `syllables`, `avg_sentence_length`, `avg_word_length`, `complex_words`, `complex_word_pct`, `polysyllable_words`, `passive_sentences`, `passive_pct`, `flesch_reading_ease`, `flesch_kincaid_grade`, `gunning_fog`, `smog_index`. Map these straight into the output tables below — don't recompute or round differently.

---

## Mode: Analyze

Run the script on the input text (see above) and display its metrics.

### Core Scores (reference — the script computes these; you only read the output)

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **Flesch Reading Ease** | 206.835 - 1.015(words/sentences) - 84.6(syllables/words) | 0-100, higher = easier |
| **Flesch-Kincaid Grade** | 0.39(words/sentences) + 11.8(syllables/words) - 15.59 | US grade level |
| **Gunning Fog Index** | 0.4[(words/sentences) + 100(complex words/words)] | Years of education |
| **SMOG Index** | 1.043 × √(polysyllable words × 30/sentences) + 3.1291 | Grade level |

*Complex words (Fog) = 3+ syllables, excluding likely proper nouns and words that only reach 3 syllables via -es/-ed/-ing. Polysyllable words (SMOG) = raw 3+ syllable count.*

### Text Statistics (from the script's JSON)

- Word count, sentence count
- Average sentence length (words), average word length (characters)
- Complex words count and %
- Passive voice sentences and % (heuristic estimate)

### Output Format

```
## Readability Analysis

### Scores
| Metric | Score | Meaning |
|--------|-------|---------|
| Flesch Reading Ease | [X] | [interpretation] |
| Flesch-Kincaid Grade | [X] | [grade level] |
| Gunning Fog | [X] | [years education] |
| SMOG | [X] | [grade level] |

### Statistics
- Words: [X]
- Sentences: [X]
- Avg sentence length: [X] words
- Complex words: [X] ([Y]%)

### Target Audience
[Who can easily read this based on scores]

### Recommendations
1. [Specific suggestion]
2. [Specific suggestion]
3. [Specific suggestion]
```

Base recommendations on scores:
- Sentences to shorten (if avg > 20 words)
- Complex words to simplify
- Passive voice to convert to active
- Specific examples of what to fix

### Interpretation Guide (real-world ↔ score)

Use this table both to interpret scores and to translate a plain-language target into numbers.

| Flesch Reading Ease | FK Grade | Real-world label | Audience |
|---|---|---|---|
| 90-100 | ~5 | Elementary | Very easy |
| 80-89 | ~6 | Middle school | Easy |
| 70-79 | ~7 | Middle school | Fairly easy |
| 60-69 | 8-9 | High school | Standard / **general adult** |
| 50-59 | 10-12 | High school | Fairly difficult |
| 30-49 | 13-16 | College | Difficult |
| 0-29 | 16+ | Graduate | Very difficult |

Default mapping when a user gives a vague target instead of a number:
- "kid-friendly" / "elementary" → Flesch 80-90, FK grade 5-6
- "general public" / "adult" / "plain language" → Flesch 60-70, FK grade 8-9
- "educated adult" / "broadsheet newspaper" → Flesch 50-60, FK grade 10-12
- "professional" / "trade publication" → Flesch 30-50, FK grade 13-16
- "academic" / "technical" / "expert" → Flesch <30, FK grade 16+

---

## Mode: Revise

Goal: produce a rewrite whose measured scores fall inside a target range, not just text that "feels simpler."

### 1. Establish the target — ask, don't assume

If the user hasn't given a concrete target, ask one question that offers both framings at once, e.g.:

> "What reading level should this land at? You can name a grade (e.g. '8th grade'), a real-world audience ('general adult,' 'kids,' 'technical expert'), or a specific Flesch/FK score. If unsure, I'd suggest **general adult (Flesch 60-70, ~8th-9th grade)** — the level of most news writing."

Convert their answer to a numeric target range using the table above. State the range back in one line before rewriting (e.g. "Target: Flesch 60-70 / FK grade 8-9") so the user can correct it before you do the work.

### 2. Baseline

Run the script on the input text. Note the gap: which metrics are off-target, and by how much.

### 3. Rewrite toward the gap, not away from meaning

Apply only the levers that close the measured gap — don't rewrite lines that are already in range.

| If current score is... | Lever |
|---|---|
| Too hard (grade/Fog too high, Flesch too low) | Split sentences >20 words at conjunctions; replace 3+ syllable words with shorter synonyms; convert passive → active; cut subordinate clauses |
| Too easy (grade too low, Flesch too high — rare, but happens when a target skews academic) | Combine choppy sentences; restore precise/technical terms; add subordination |

Preserve: facts, structure (same number of ideas/paragraphs), and tone. Simplify vocabulary and syntax, not content — a simpler reading level is not a shorter or dumber summary.

### 4. Re-measure, iterate, stop

Save the draft to a file and run the script's `--diff` mode against the original (or just re-run it standalone on the draft). If Flesch Reading Ease and FK Grade are both within ±5 / ±1 of the target range, stop. If not, apply another targeted pass and re-run the script again. **Cap at 3 passes** — if still out of range after 3, report the closest result and say why (e.g. dense subject-matter vocabulary can't simplify further without losing accuracy).

### Output Format

```
## Readability Revision

Target: [range, e.g. Flesch 60-70 / FK grade 8-9 — "general adult"]

### Before → After
| Metric | Before | After | Target met? |
|--------|--------|-------|-------------|
| Flesch Reading Ease | [X] | [Y] | [✓/✗] |
| Flesch-Kincaid Grade | [X] | [Y] | [✓/✗] |
| Gunning Fog | [X] | [Y] | [✓/✗] |
| Avg sentence length | [X] | [Y] | — |

### Revised Text
[full rewrite]

### What changed
1. [Specific edit, e.g. "split 3 sentences over 25 words"]
2. [Specific edit]
3. [Specific edit]
```

If the target couldn't be hit within 3 passes, add a one-line note on the blocker instead of silently returning an out-of-range draft.
