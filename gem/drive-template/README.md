# Drive Setup for the Copydesk Gem

This sets up the "project scope" the Gem's Register System section falls back to before the uploaded `register-tech-docs.md` knowledge file. Project scope wins when present — same priority order the original Claude Code skill used between `.claude/data/copydesk/registers/` (project) and `~/.claude/data/copydesk/registers/` (user).

## Setup steps

1. Create a folder called `copydesk` in your Google Drive.
2. Inside it, create two subfolders: `registers` and `learning`.
3. Create a new Google Doc at `copydesk/registers/tech-docs.md` and paste in the content of the uploaded `register-tech-docs.md` knowledge file (or your own register, once you've run `init` mode). This is the doc the Gem's Drive search looks for first.
4. Create a Google Doc at `copydesk/learning/accumulator.md` and paste in the content of `accumulator.md` in this folder (a blank starter template).
5. Create a Google Doc at `copydesk/learning/splits.md` and paste in the content of `splits.md` in this folder. This isn't actively used by the simplified `learn` mode in v1 (there's no pairwise gate to feed it), but it's included so the structure is in place if a future version reintroduces that gate.
6. In the Gemini app, enable the Google Workspace extension for this Gem (Gemini settings → Extensions → Google Workspace). Without this, the Gem has no way to search Drive and will always fall back to the uploaded register.
7. Verify: start a conversation with the Gem and ask "What register is active for writing technical docs?" It should report finding `tech-docs.md` in Drive, not the uploaded fallback. If it reports the uploaded fallback instead, check that the extension is enabled and that the Doc name/location matches what's described above.

## What write-back looks like day to day

The Gem cannot write to these Drive docs directly — Google Workspace grounding in Gemini is a read/search capability, not a general file-write tool. After a `learn` mode session, or any time the register or accumulator would change, the Gem ends its response with a copy-pasteable block and an instruction like "copy this into your Drive `copydesk/registers/tech-docs.md`." Open the corresponding Doc and replace its content with what the Gem gave you. This is manual by design in v1 — treat it as your review step before the change takes effect, not as a missing feature to work around.

## Files in this folder

- `accumulator.md` — blank starter template for the Drive-backed accumulator (paste into step 4 above).
- `splits.md` — a copy of the held-out-splits structure from the source skill set, included for forward compatibility with a future pairwise-gate version (paste into step 5 above, or skip it if you'd rather not carry the placeholder).
