# Frontmatter rules

Everything here comes from [Agent Skills](https://code.claude.com/docs/en/skills). Check these when the frontmatter itself is the suspect; the fields a reviewer looks at most are already in SKILL.md.

## Validity

- The frontmatter has to start on line 1. A blank line or prose above it means there is no frontmatter at all.
- **Invalid YAML fails silently.** The skill still loads, with every field unset — no error appears. A skill whose description "stopped working" often has a YAML break, not a wording problem.
- Every field is optional. `name` defaults to the directory name, and `description` defaults to the first non-empty line of the body.
- A skill directory may not be called `synced`, in any capitalization. That path is reserved for skills downloaded from claude.ai, and one authored there is skipped.

## Naming

For personal and project skills the command name comes from **the directory name**; `name` only sets the label shown in listings. A mismatch is not a failure, but a reader who invokes `/<name>` and gets nothing has to work out why, so keep them the same unless there is a reason.

Plugin skills are the exception: there the command name comes from `name` (or the directory), namespaced with the plugin prefix.

## description and when_to_use

> The combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing to reduce context usage.

Triggering is decided from this text alone, so anything past the cut is invisible to the decision. `when_to_use` is appended to `description`; use it when the trigger conditions are long enough to crowd out what the skill does.

## Invocation control

| Field | When it applies |
|---|---|
| `disable-model-invocation: true` | A skill that performs a specific action — a deploy, a commit, a release — that should run when the user asks for it by name, not when Claude judges it relevant. Also keeps it out of subagents and scheduled runs |
| `user-invocable: false` | The reverse: Claude may use it, the `/` menu does not show it |
| `paths` | Auto-activation limited to matching files, in the same format as path-specific memory rules |

## allowed-tools

The grant applies for the turn the skill is invoked and clears on the next message. It is not gated by workspace trust: **a project skill's grant applies even in a folder that was never trusted**, so a broad grant in a repository skill is worth flagging in review.

## Dynamic context injection

`` !`command` `` and ` ```! ` blocks run before the skill content reaches Claude.

- A non-zero exit **aborts the whole invocation** — Claude never sees the skill. Append `|| true` to anything that legitimately exits non-zero.
- The inline form is recognized only when `!` starts a line or follows whitespace.
- Exit code 1 from search and comparison commands counts as a normal result.

## Content that stays

An invoked skill's rendered body enters the conversation as one message and **stays there for later turns**, so every line is a recurring cost. This is the reason the reviewer weighs how many invocations need a section, and why guidance meant to hold for a whole task reads better as a standing instruction than as a one-time step.
