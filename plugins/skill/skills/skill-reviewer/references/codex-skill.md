# Codex skill review

Apply these checks only to skills intended for Codex. Source: [official skill documentation](https://learn.chatgpt.com/docs/build-skills). Verify host-version details there when needed.

## Discovery and invocation

- Require non-empty `name` and `description` in SKILL.md frontmatter. Keep the main use case early in the description because discovery text can be shortened.
- Check discovery through the intended local skill location or plugin package; do not require a plugin skill to live in a standalone local installation directory.
- Codex CLI and IDE support explicit `$skill-name` invocation and implicit selection from the description. Review trigger examples against the intended invocation mode.

## Optional agent metadata

`agents/openai.yaml` is optional and host-consumed, so its absence is not a defect and it does not need a prose link to avoid being an orphan.

When present, inspect UI metadata, resource paths, tool dependencies and `policy.allow_implicit_invocation`. A false value disables implicit selection while retaining explicit invocation; absence defaults to true. Check consistency with the intended workflow, not whether every optional field exists.

## Runtime portability

Resolve supporting resources relative to the actual skill location. Do not assume Claude Code variables, shell injection or frontmatter controls have equivalent Codex behavior. If the workflow relies on them, flag the missing Codex path; their mere presence in a shared skill is not enough to prove failure.

Check required tools against the target environment. Metadata does not replace runtime permissions or make an unavailable tool callable.
