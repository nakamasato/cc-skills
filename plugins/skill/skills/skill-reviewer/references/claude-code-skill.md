# Claude Code skill review

Apply these checks only to skills intended for Claude Code. Use the [official skills documentation](https://code.claude.com/docs/en/skills) to verify version-sensitive fields and limits.

## Discovery and invocation

- Check placement in a supported skill location or plugin and the resulting slash-command name, including the plugin namespace where applicable.
- Claude Code permits omitted `name` and `description` with fallbacks. Prefer explicit discovery text; do not report omission as a universal loading failure.
- Check `disable-model-invocation` and `user-invocable` against the intended caller. The former controls automatic invocation; the latter controls menu visibility. Neither is a portable cross-host setting.
- Verify optional field support and limits in the target version before flagging reserved names, truncation or YAML fallback behavior.

## Tools and execution context

- `allowed-tools` grants tools that can run without asking permission while the skill is active; it is not a list of the only tools the skill can ever use. An omitted tool may require approval, so do not automatically report it as unavailable. Flag unnecessarily broad grants when relevant.
- Check `context: fork` and `agent` only when present: the task must provide the context its subagent needs.
- Check Claude-specific substitutions such as `$ARGUMENTS` and `${CLAUDE_SKILL_DIR}` where used. Bundled script paths should resolve from the skill directory rather than assuming the working directory is the skill directory.

## Dynamic context

Claude Code runs shell injection such as `` !`command` `` before passing the rendered skill to the model. Review expected non-zero outcomes and failure handling. Handle benign outcomes explicitly; suggest `|| true` only when ignoring every failure is actually intended, since it also hides real errors.

For skills supporting other hosts, require an alternative to Claude-only injection, substitutions and invocation controls where the workflow depends on them.
