---
name: write-documentation
description: Create a new contributor-facing document from a rough idea, or revise an existing one (by file path or pasted text), in the tech-docs voice and at a target reading level (defaults to general adult, technically inclined if none is given). Chains copydesk-write and readability with a mandatory discipline_check guard and a final score check. These steps are never optional and never skipped, regardless of how the request is phrased.
user-invocable: true
argument-hint: "[create: rough idea | revise: file path or pasted text] [optional target level, defaults to general adult, technically inclined]"
---

# Write Documentation

Produces a contributor-facing document that is both voice-correct (`tech-docs` register) and leveled to a target reading score (general adult, technically inclined by default). This skill exists so that a single request can't accidentally skip the level pass, the guard check, or the final score check the way a hand-written one-shot prompt could. Every invocation runs all of steps 3-6 below. None of them are optional, and none of them get skipped because the user's request didn't mention them.

See `docs/Writing-Documentation-Guide.md` for the full rationale behind this sequence and its ordering.

## 1. Determine intent

- **Create**: the user describes a rough idea, topic, or outline with no existing file to revise. If they didn't give a save path, ask for one.
- **Revise**: the user gives a file path (read it) or pastes text inline to work from.

If it's ambiguous which one they mean, ask.

## 2. Establish the target level

If the user stated a target (a grade, an audience label, or a raw score), resolve it to a numeric range the way the `readability` skill does, and state the resolved range back before continuing so the user can correct it.

If they didn't state one, don't ask. Default to **general adult, technically inclined: Flesch 50-65 / FK grade 9-11** (see `docs/Writing-Documentation-Guide.md#picking-a-target`) and say so explicitly, citing that exact numeric range, before starting the level pass, e.g. "No reading level specified, defaulting to general adult, technically inclined (Flesch 50-65 / FK grade 9-11)." Do this every time the default applies, not just the first time.

## 3. Voice pass (mandatory)

Invoke the `copydesk-write` skill with the `tech-docs` register named explicitly (don't rely on trigger auto-detection here; this skill's whole point is removing ambiguity):

- **Create**: source material is the rough idea, topic, and any notes from step 1.
- **Revise**: source material is the existing file's content or the pasted text. Ask `copydesk-write` to rewrite it in the `tech-docs` register.

Let its review gate run to completion (hard fails fixed silently, advisory findings resolved with the user) before continuing. Save the result as the step-1 draft.

## 4. Level pass (mandatory)

Invoke the `readability` skill in Revise mode on the step-1 draft, targeting the range from step 2. Tell it explicitly:

- Preserve `tech-docs`' voice markers as invariants, not defects to simplify away: first-person ownership ("I propose," "I believe"), personal parentheticals, sentences opening with coordinating conjunctions, "so that" consequence clauses.
- Prefer vocabulary as the lever, not structure. Split at the coordinating conjunctions and clause boundaries the register already uses rather than cutting the personal framing.

Let it run its baseline, rewrite, re-measure loop (capped at 3 passes). Save the result as the step-2 draft.

## 5. Guard (mandatory, never skip)

Run this regardless of whether the user's request mentioned it:

```bash
python3 .claude/copydesk/scripts/discipline_check.py --diff <step1-file> <step2-file>
```

If `introduced_new: true`, fix the flagged sentence and re-run the check before moving on. One known false positive: a CLI flag like `--diff` written in inline code can register as a stray em dash, since the check strips fenced code blocks but not inline code spans; that's safe to ignore.

## 6. Final score verification (mandatory, never skip)

Run this regardless of whether the user's request mentioned it:

```bash
python3 .claude/skills/readability/scripts/readability_score.py <final-file>
```

Confirm `flesch_reading_ease` and `flesch_kincaid_grade` land in the target range from step 2. If not, run one more level pass (still capped at 3 total across step 4) and re-verify.

## 7. Deliver

Present the final text (or its saved path), the before/after score table, and the guard result. Report steps 5 and 6 even when both come back clean: showing "guard: clean" and "score: in range" is what proves the pipeline actually ran, not just a claim that it did.
