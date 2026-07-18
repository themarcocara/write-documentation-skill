# Accumulator

staleness_threshold: 5

## Longitudinal Guidance (PROTECTED — step-level edits MUST NOT modify this)
- copydesk-craft-review is intentionally high-recall; rejection is expected; do NOT tune its triggers down.
- Discipline wins on banned patterns: never restore em-dashes / fatal-pattern from a source corpus even if an influence uses them.
- User regularization labels (do-not-generalize): (none recorded yet)

## Observations

### Personal editorial aside cut under organizational voice pressure
- **Target:** `.claude/data/copydesk/registers/tech-docs.md` (Voice Qualities, "writer's personal stakes" rule)
- **Category:** cut
- **Sessions seen:** 1
- **Sessions since last seen:** 0
- **Status:** hold
- **Instances:**

| # | Before | After | Context | Session |
|---|---|---|---|---|
| 1 | "It's a mechanical backstop, and I'd call it one of the more underrated ones. It catches..." | "It's a mechanical backstop which catches..." | Apply section, after linting/formatting description | 2026-07-16 |

Notes: entangled with the I→we reversion sweep (same "I'd call" construction), so can't cleanly isolate whether this is an independent signal against personal-stakes asides or just collateral from the broader pronoun sweep. Single instance, ambiguous.

### Negation-qualifier avoidance beyond fatal-pattern scope
- **Target:** `.claude/skills/copydesk-write/SKILL.md` (Banned Phrases, fatal-pattern definition)
- **Category:** structural rework
- **Sessions seen:** 1
- **Sessions since last seen:** 0
- **Status:** hold
- **Instances:**

| # | Before | After | Context | Session |
|---|---|---|---|---|
| 1 | "That self-policing report is layered on top of, not instead of, a set of automated review gates..." | "On top of producing a self-policing report, the AI's implementation must clear a set of automated review gates..." | Apply section, transition to automated gate description | 2026-07-16 |

Notes: prose review agent correctly did NOT flag this as a fatal-pattern hard fail (it's a qualifier, not negation-then-correction). User restructured it anyway. Do not expand the fatal-pattern definition on this single data point; hold as a possible softer user style preference.

### Named approach promoted to heading
- **Target:** `.claude/data/copydesk/registers/tech-docs.md` (Sentence Structure section)
- **Category:** formatting
- **Sessions seen:** 1
- **Sessions since last seen:** 0
- **Status:** hold
- **Instances:**

| # | Before | After | Context | Session |
|---|---|---|---|---|
| 1 | "**What we do instead: prototype, then productionize.** This is really our overall approach..." (bold inline intro) | "### What we do instead: prototype, then productionize." (H3 heading, body split into paragraphs) | Not One-Shotting section, named discipline | 2026-07-16 |

Notes: single instance; may reflect a preference that named disciplines anchoring a sub-argument become headings rather than bold inline intros, or may just reflect this sub-section's length/importance. Flag: the live edit left a stray trailing `**` on the heading text (`...productionize.**`), likely an artifact of converting bold-inline to a heading rather than an intentional formatting choice — worth the user's attention independent of the learning loop.

## Rejected Edits (negative feedback for the optimizer)

| Edit | Target | Held-out score delta | Round |
|---|---|---|---|

---
