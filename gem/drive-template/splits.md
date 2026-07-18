# Held-Out Splits

Defines the selection-set (`D_sel`) and test-set (`D_test`) pieces per register, used by the generative-gate harness (see `copydesk-learn` SKILL.md, Mode 2 Step 9, and the ablation operation).

`D_sel` pieces are used to gate candidate edits during routine learning runs. `D_test` is held separate and untouched by the gate, reserved for a final check before a release so the gate's own picks can be sanity-checked against pieces it never optimized against.

Each piece's brief lives at a durable path under `{learning_dir}/held-out-briefs/<register>/` (see `copydesk-learn` SKILL.md's Directory Resolution section for how `{learning_dir}` resolves) — never inside `snapshots/`, which gets cleaned up per-session.

## tech-docs

### Selection Set (D_sel)

| Piece | Brief | Notes |
|---|---|---|
| alpha-build-tdd | `learning/held-out-briefs/tech-docs/alpha-build-tdd-brief.md` | Stripped from a hand-written technical design doc. Exercises: engine-comparison reasoning with real trade-offs, decision narration (criteria → options → recommendation with caveats), speculative/contingent milestone framing, data-pipeline rationale tied back to a hedge against being wrong. |

### Test Set (D_test)

(empty — add pieces here once available; keep separate from D_sel so the gate's picks can be checked against pieces it never saw)
