# Copydesk (vendored)

This directory holds the supporting files for the [Copydesk](https://github.com/TimSimpsonJr/copydesk) skill set: the extraction/setup guides, the register template, and the deterministic discipline-check script. It's vendored directly into this repo rather than installed as a Claude Code plugin, so the skills and agents live at the project-standard locations instead:

- `.claude/skills/copydesk-init/SKILL.md` — bootstraps `~/.claude/data/copydesk/` and walks through voice extraction (source: `skills/init/SKILL.md`)
- `.claude/skills/copydesk-write/SKILL.md` — the review-gated writing skill (source: `skills/write/SKILL.md`)
- `.claude/skills/copydesk-learn/SKILL.md` — the learning loop (source: `skills/learn/SKILL.md`)
- `.claude/agents/{copydesk-prose-review,copydesk-craft-review,copydesk-fatal-pattern-recheck,copydesk-learn-review,copydesk-taste-judge}.md` — the review/optimizer/judge subagents

Because there's no plugin runtime here, every `${CLAUDE_PLUGIN_ROOT}/...` reference from the upstream skills was rewritten to a repo-relative path (e.g. `.claude/copydesk/setup/...`), and every `copydesk:agent-name` subagent dispatch was rewritten to the plain agent name (e.g. `copydesk-prose-review`).

One addition beyond upstream: `copydesk-write`'s register lookup also checks this repo's own `.claude/data/copydesk/registers/` first, so a project can vendor a shared, version-controlled register (like `tech-docs`) that's available to every contributor without each person running their own extraction. A project-scoped register takes priority over a same-named personal one.

A second addition beyond upstream: `copydesk-learn`'s learning state (snapshots, `accumulator.md`, `splits.md`, `ablation-log.md`, `judge-agreement.md`, `pending-upstream.md`, extraction artifacts, held-out briefs) resolves the same way — see `{learning_dir}` in that skill's Directory Resolution section. If this repo's `.claude/data/copydesk/learning/` exists, that's authoritative and shared across contributors (as it is here, for `tech-docs`); otherwise it falls back to `~/.claude/data/copydesk/learning/` (personal, follows the user across projects). `copydesk-init` is unchanged and still bootstraps only at `~/.claude/data/copydesk/` — it's a personal-machine setup tool by design, not a project-vendoring one. A project-scoped register or learning directory is something a maintainer vendors deliberately, not something copydesk-init creates on its own.

## Structure

```
copydesk/
  scripts/
    discipline_check.py    Deterministic banned-pattern check (stdlib only); --diff reports introduced violations.
    banned_phrases.txt     AI-vocab / ChatGPT-ism list read by the script above.
  setup/                   Extraction guides referenced by copydesk-init (sample-collection, pass-1/2 prompts, brief-stripping).
  template-data/           Templates copied into ~/.claude/data/copydesk/ on first init.
  tests/                   pytest suite for discipline_check.py (offline, stdlib-only).
  pytest.ini               `pythonpath = .`, `testpaths = tests` — run `pytest` from this directory.
```

## Updating

This is a point-in-time copy. To pull upstream changes, diff against the [source repo](https://github.com/TimSimpsonJr/copydesk) and reapply the path/namespace rewrites described above — don't just overwrite these files, since a straight copy would reintroduce the `${CLAUDE_PLUGIN_ROOT}` and `copydesk:` references that don't resolve outside a plugin install.

MIT licensed; see `LICENSE`.
