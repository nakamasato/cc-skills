---
name: skill-reviewer
description: Use when a SKILL.md and its supporting files need a structural review - after writing or editing a skill, when a SKILL.md has grown long, when deciding what belongs in references/ versus the skill body, or when the user asks to check, audit or clean up a skill. Reports the findings worst first and applies only the ones the user picks.
allowed-tools: Read, Glob, Grep, Bash, Edit, Write
---

# Skill structure review

Review one skill for whether a reader reaches what they need and reads no more than that. This reviews structure, not whether the content is correct.

A skill loads in layers: the frontmatter is always in context, SKILL.md enters the conversation in full when the skill triggers and stays there for later turns, and the supporting files (`references/`, `scripts/`, `assets/`) are opened only when something sends a reader to them. Misplaced material is paid for on every invocation, or sits where nobody looks.

## Review procedure

1. Run the mechanical checks. They cover sizes, the heading tree, dangling pointers, orphan files, frontmatter validity and prose density, so the reading time goes to what needs judgment.

   ```bash
   python3 "${CLAUDE_SKILL_DIR}/scripts/audit.py" <skill-dir>
   ```

2. Read SKILL.md and every supporting file, then apply the checks below. They are ordered by how much damage the fault does.
3. Report worst first, and **apply only what the user picks** — structure is often deliberate, and rewriting before reporting destroys the reasoning behind it.

The user may cap how many findings to report (`top 3`). Without a cap, report at most five and say how many were left out.

## 1. Broken invocation

The skill never runs, or runs without what it needs. The audit script finds most of these.

| Fault | Why it matters |
|---|---|
| Frontmatter missing, misplaced or invalid YAML | The skill loads with no fields and no error |
| `allowed-tools` narrower than the body's own promises | A skill that offers to apply fixes but cannot write them stops halfway |
| `description` that omits what the skill does or when to use it | Triggering is decided from that text alone |
| An injected shell command (the `!`-prefixed inline form) that can exit non-zero without `\|\| true` | A failure aborts the whole invocation |

Field limits, reserved names, `disable-model-invocation` and the rest: [references/frontmatter.md](references/frontmatter.md).

## 2. Where the content lives

| Look for | Fix |
|---|---|
| A procedure, command sequence or pitfall that only one situation needs, sitting in SKILL.md | Move it to `references/` and leave the list of situations in SKILL.md. The measure is what share of invocations need it, not its length — content needed every time belongs in the body however long, and a rarely-needed page earns its own file however short |
| A supporting file nothing points to | It is never opened. Point to it, or delete it |
| A pointer to a path that does not exist | Fix the path |
| A pointer that never says when to open the file | Put it beside the symptom or situation it answers. The docs ask that a reader can tell what a file holds and when to load it; a markdown link and a bare path both do that |
| The same procedure or value in both SKILL.md and a supporting file | One copy goes stale. Keep one source and point at it |
| SKILL.md over 500 lines | Add a layer: group by situation, move the detail out |

## 3. Order and proportion

- **What gets decided first comes first.** A reader picks their situation before they need the settings every situation shares. Opening with shared detail and listing the situations last forces them to read all of it.
- **Group by the reader's errand.** When a skill serves two errands, alternating sections make both readers skim.
- **Keep sections comparable.** A section several times longer than its siblings usually covers two things; a run of three-line sections usually belongs under one heading.
- **Give sibling reference files the same shape.** If one is steps only and another is steps plus pitfalls, the layout has to be worked out again each time.

## 4. Headings

A reader scans the heading tree and jumps, so judge each heading by whether it predicts what the section holds.

| Weak heading | Why | Better |
|---|---|---|
| `Two sources` | Counts instead of answering the reader's question | `Choosing a source` |
| `Constraints`, `Notes`, `Tips` | Fits anything, so it says nothing | `Runtime constraints` |
| `About the API` | Hides the conclusion the section reaches | `What the Instructor API covers` |
| `Fetching it`, `Reading it` | Conversational | Documentation headings are noun phrases: `Fetch procedure`, `Snapshot structure` |

**For a skill written in Japanese, use [references/headings-ja.md](references/headings-ja.md) instead** — 体言止め, mixed 常体/敬体, katakana spelling drift and spacing are what go wrong there, and the English rules above do not catch them.

Check that names agree: the wording in SKILL.md against the title of the file it points to, the directory name against `name`, and one term per concept throughout.

## 5. Prose

An invoked body stays in context for the rest of the conversation, so every line is a recurring cost.

- **Explain why instead of stacking MUST, ALWAYS and NEVER.** A reader who knows the reason handles the case the rules do not cover.
- **State standing guidance as standing guidance.** Advice meant to hold for a whole task reads better as a rule than as a step in a list.
- **No changelog, no ticket ids.** A skill describes its current shape.
- Watch the density of bold; when every paragraph has some, none of it reads as emphasis.

## Reporting

Order by damage: a skill that cannot run, then material in the wrong file, then structure, headings, prose. Give the reason each one matters — without it the user cannot judge whether to fix it.

| Where | What | Why | Fix |
|---|---|---|---|
| frontmatter | `allowed-tools` omits `Edit` | The skill offers to apply fixes it cannot write | Add `Edit` |
| `SKILL.md` 46-86 | 41 lines of editor keystrokes in the body | Only some invocations edit a file; every one reads this | Move into `references/`, point from the situation table |

When the shape itself is off, show the proposed heading tree as well — a table of findings does not convey the whole.

Close by asking which items to apply, and apply only those.
