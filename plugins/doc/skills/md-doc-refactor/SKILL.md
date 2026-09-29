---
name: md-doc-refactor
description: Use this skill when refactoring existing Markdown documentation to improve organization, navigation, and information architecture without adding, deleting, or changing technical meaning. Suitable for structural cleanup of SKILL.md, README.md, AGENTS.md, CLAUDE.md, operations docs, architecture docs, and runbooks.
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# MD Document Refactor

## Purpose

Refactor an existing Markdown document without changing its meaning.

This skill reorganizes documentation in the same way source code can be refactored.

The objective is:

> Better organization with equivalent semantics.

This skill should improve structure, navigation, and information ownership while preserving all technical content.

Optimize for, in this order: semantic preservation, information ownership,
navigation clarity, structural consistency, low duplication, and small,
reviewable diffs (never at the cost of a parallel structure — step 5).

Use this skill when the user asks to reorganize, clean up, restructure, refactor, or improve the architecture of an existing Markdown document without changing its content.

Examples:

- Reorganize a messy README.
- Refactor a long operations doc.
- Split or merge sections for clarity.
- Move generated content away from conceptual explanation.
- Normalize heading hierarchy.
- Reduce duplicated explanations.
- Make a document easier to maintain after many incremental updates.

Do not use this skill to add new information. Use `md-doc-update` for content changes.

## Hard Constraints

### Allowed

- Move sections
- Rename headings
- Merge sections
- Split sections
- Reorder sections
- Extract duplicated explanations into a single owner section
- Replace repeated explanations with references
- Improve heading hierarchy
- Correct heading wording so it obeys the naming rules (noun-phrase default,
  no sentences, no filler-word containers). **This is structural, not style** —
  see `### Heading naming` below. Do not skip it as "purely style".
- Improve navigation
- Separate generated/reference content from authored explanation
- Update links affected by moved or renamed headings
- Reword minimally when necessary to preserve flow after moving content
- Reshape a passage into a numbered list, a table or a decision flowchart,
  and separate steps from their reasons, when the facts stay the same
  (`### 4. Shape inside sections`)

### Not Allowed

- Add new technical information
- Delete technical information
- Change requirements
- Change behavior
- Change examples
- Change commands
- Change configuration values
- Change warnings
- Rewrite body prose purely for style (heading wording is exempt — see Allowed)
- Invent new architecture
- Hide uncertainty by removing content

If meaningful refactoring requires deleting or adding content, stop and report that the requested change is not a pure refactor.

## Refactoring Workflow

Steps 0–3 each produce a **written artifact**. Write it down before moving on;
the final report carries them. A step whose artifact you cannot write is not
done, and editing before step 3 is finished is the most common failure of this
skill: it produces a shuffle of the old sections instead of a structure.

### 0. Repository state and constraints

A refactor rewrites the whole shape of a file, so a concurrent change is not a
mergeable conflict — it is a rewrite of someone else's work.

- **Concurrent work.** The base is `origin/main` (or whatever the user or
  environment declares as the latest main). Open PRs:
  `gh pr list --repo <owner>/<name> --state open --json number,title,files`.
  Unmerged commits: `git log --oneline --all ^<base> -- <file>`. Stop and
  confirm only when an open PR touches the file, or a listed commit is on a
  branch whose change is not in the base. The report states exactly one of:
  `確認済み（該当なし）` / `確認済み（<PR or branch>）` /
  `省略（<given premise or constraint>）` / `実行できず（<reason>）`.
- **Repo-enforced structure.** Look for checkers, templates and rules that fix
  the doc's headings or placement: grep the file name and the doc directory in
  `scripts/`, lint / pre-commit config, the docs index, and the repo's agent
  rules (`CLAUDE.md`, `AGENTS.md`, `.claude/rules/`). Headings they require are
  immovable; refactor under them. Run those checkers after editing.
- **Inbound references.** `grep -rn "<file name>"` across the repo. Collect
  anchor links **and** prose references to a heading (`§ <heading>`). Note which
  referencing files you may not edit (frozen / historical records).
- State the document's **type** (README / getting-started / configuration /
  troubleshooting / ADR / SECURITY / CONTRIBUTING / migration / api-reference /
  FAQ / runbook).

### 1. Subject and ownership

- **Subject sentence.** Write what this doc covers, for whom, in one sentence.
  Content outside it belongs to another doc; whether to recommend splitting
  this doc follows `### Document split`.
- **Ownership across the repo.** For each topic in the doc, search the other
  docs (the docs index, architecture docs, sibling runbooks) for the same
  topic. Record `topic → other doc § → which should own it`. Do not move
  content across files: a cross-file move or a replacement by a link is a
  **proposal in the report**, applied only after the user answers it.
- **Undefined concepts.** Record the concepts the doc relies on but that no doc
  defines — for example two terms used as if interchangeable, or a resource
  named but never explained. Report them as gaps; do not write definitions.
- **Contradictions.** When a statement disagrees with the code or another doc
  you read along the way, record both sides. Report it; do not correct it.

### 2. Reader-question inventory

Go paragraph by paragraph. For each, write the reader question it answers and
its **kind**:

| Kind | The reader wants to… |
|---|---|
| decision | decide what to do in their case |
| prerequisite | know what must exist / who may act |
| procedure | do something |
| mechanism | understand how it works and why it is built that way |
| reference | look a value up |
| symptom | fix a failure they are seeing |
| record | read a dated past event |

### 3. Section tree

Design the tree from the inventory, not from the old section list.

1. **Gather entry points and operations first.** The old H2 list often
   files one thing under several headings; fix that before ordering.
   - **Entry points.** When the inventory holds several ways to start the
     same process (a merge, a manual dispatch, a local command; a CLI and a
     UI), make them siblings under one parent named for starting it
     (`実行方法`), even when the old doc spreads them over several H2s or
     files one under the kind of change that needs it.
   - **One owner per operation.** For each operation the doc explains (for
     example re-creating a resource), collect every paragraph about it. Its
     mechanism goes to exactly one section and its manual procedure to
     exactly one section (usually a child of the entry-point parent); each
     links to the other. Two sections explaining the same mechanism merge.
2. **Order the H2s by reader purpose.** A common order is decision →
   prerequisite → mechanism → procedure → Troubleshooting, but derive it from
   the inventory (see `### Section placement` § Anti-patterns). The H2s are the one
   level whose kinds differ by design; record their axis as `読み手の目的の順`.
3. **Write one axis per parent below H2.** For every H2 or deeper section
   with two or more children,
   write `children split by <axis>` in one phrase and the kind of each child.
   All children must be the same kind and answer the same question along that
   axis. If one phrase cannot cover them, the grouping is wrong — regroup
   before naming anything. None may sit one abstraction level above or below
   the rest; an odd one out almost always belongs under a different parent.
   One exception: a steps / reasons pair made in
   step 4 is a single unit; record its axis as `手順とその理由`.
   When the repo fixes every H2 (step 0), run steps 2–3 on the children of
   each fixed H2 instead, and say so in the report's 概要.
   Go no deeper than H4; below that, use a bold lead-in inside the body.
   A lone child section is folded into its parent unless something outside
   the file links to it; if its title named a scope the body does not state,
   keep that scope as a bold lead-in.
4. **Take the axis from the real structure of the subject**, not from which
   paragraphs sound related: the execution order of a script or pipeline, the
   triggers that start it (a workflow's `on:`), its components, its inputs, the
   list of symptoms. An axis read off the artifact is parallel by construction
   and can be checked against the code. When the doc itself already
   enumerates the members (a table whose rows are the cases), use those rows.
5. **Name the children** with identifiers the reader actually sees (trigger,
   command, resource names) or plain reader vocabulary. Qualify the object
   (`pod 再作成後の起動確認`, not `再作成後の確認`). Never coin an umbrella word
   (`〜経路`, `〜系`) to make unlike children look parallel, and never use a bare
   implementation token (`render`, `prune`) as a whole title.
6. **Place dated incidents and migration history** as
   `### Section placement` § Dated incidents and history says.

### 4. Shape inside sections

These reshapes keep the same facts and are structural, so they are allowed:

- **A sequence** (processing steps, a procedure) becomes a numbered list: one
  step per item, stating only what the step does. Conditions and sub-steps
  nest under it.
- **Reasons, prohibitions and pitfalls** of those steps go to a separate
  sibling (for example `処理の流れ` / `各段階の理由`), one bullet per step,
  tagged with the step number. A long reason, or one with a code block, stays
  a bullet with the paragraphs and block indented under it. The step names
  the command or option and what it does; the reason does not repeat that.
- **How to read a step's result** (what `1/2` means, what a zero count means)
  stays with the step. Only the why and the prohibitions move.
- **Build steps only from facts already in the doc.** Do not import a fact
  from the code or another doc to complete a step, even a correct one; report
  the missing link as a gap instead. A step whose run condition the doc does
  not state (always, or only with a flag) stays out of the numbered list, in
  the section it came from — but the list itself is still made from the steps
  whose order the doc does state.
- **A split sentence keeps its language** and gains only the subject or
  demonstrative it needs to stand alone.
- **Branching already stated in prose or a table** becomes a decision table or
  a mermaid flowchart built only from the existing facts. Keep node labels
  short; put long file lists in a table under the chart.

### 5. Application and verification

- If no meaningful structural improvement exists, make no changes and explain
  why.
- Prefer the smallest change that makes every parent pass step 3. A small diff
  never outranks a parallel structure.
- Keep commands, examples, paths, IDs, configuration values and warnings
  unchanged unless only moved. Preserve generated blocks exactly unless moving
  the whole block.
- Update anchor links and prose `§` references in files you may edit. A
  rename still goes ahead when a file you may not edit (a frozen record)
  refers to the old title; list that broken reference under 確認したいこと.
  A reference that was already broken before your edit and points at a
  section you refactored is retargeted and listed under 確認したいこと too.
- Verify:
  - every code span of the original is still in the file (the first command
    prints nothing):

    ```bash
    git show HEAD:<file> > "$TMPDIR/orig.md"
    grep -o '`[^`]*`' "$TMPDIR/orig.md" | sort -u > "$TMPDIR/orig"
    grep -o '`[^`]*`' <file> | sort -u > "$TMPDIR/new"
    comm -23 "$TMPDIR/orig" "$TMPDIR/new"
    ```

  - the repo checkers found in step 0 pass;
  - every parent passes step 3 item 3, and every title obeys
    `### Heading naming`;
  - the result has one owner section per concept and one purpose per section,
    readers find things quickly, no unnecessary repetition is left,
    generated/reference content is isolated from authored explanation, the
    structural complexity is lower, and future updates are easier;
  - reader intents are separated where appropriate: concepts, architecture,
    operations, reference, troubleshooting, recovery, and migration history
    (`#### Dated incidents and history`);
  - the diff is structural and reviewable.

If semantic equivalence cannot be verified, report the uncertainty.

## Rules used by the workflow

### Heading naming

Renaming is where this skill most often goes wrong. These rules are derived
from 117 real OSS / published technical docs (English 80, Japanese 37) whose
verbatim headings are in `references/corpus.md`. **Do not invent a "typical"
heading — pick one that the corpus actually attests.**

#### Word form

- **Noun phrase is the default.** `Installation`, `Configuration options`,
  `Breaking changes`, `Threat model`, `既知の問題`, `テストの種類`.
- **Gerund / 「〜する」 for sections whose subject is an action**:
  `Getting Started`, `Reporting a vulnerability`, `Examining pod logs`,
  `プロジェクトを作成する`, `kubectlの設定を検証する`.
- **Imperative and numbered prefixes only for individual procedure steps**:
  `Run the development server`, `手順 1: リポジトリを作成する`,
  `ステップ 1：レンダーのトリガ`.
- **Question form only in FAQ and in a single "what is / why" opener**:
  `What is SvelteKit?`, `なぜLaravelなのか？`.
- **Declarative sentences only in the symptom list of a troubleshooting doc**
  (Istio: `Envoy is crashing under load`). Nowhere else. There are zero
  Japanese sentence headings in the corpus.

A claim belongs in the **first line of the body**, not in the heading:
`Ready は疎通を保証しない` → `Ready 状態の解釈`.

Whatever form you choose, **all siblings under one parent use the same form.**
A Japanese verb heading is not wrong; a verb heading among noun-phrase siblings
is.

#### Banned container headings

A heading whose head word does not restrict what may go under it becomes a
dumping ground and destroys granularity. Do not use:

`基本の〜` / `〜について` / `〜まわり` / `〜系` / `〜関連` / `〜こと`
(`気をつけること`, `踏んだこと`) / `その他` / `Tips` / `ポイント` / `補足`,
and a second `概要` anywhere below the opener.

The corpus permits a container word **only as the final section absorbing
residue** (Elasticsearch `Other issues`, HAProxy `Other sections`, git `NOTES`,
ADR `Notes`). Never mid-document.

Replacements: `基本の設定` → `セットアップ` / `設定ファイルの場所`;
`Kubernetes で気をつけること` → split into `Kubernetes での差分` (under the parent procedure)
and items absorbed by `既知の落とし穴`; `これまでに踏んだこと` → `既知の落とし穴`,
or, if it truly is history, as `#### Dated incidents and history` says; `症状から診断する` →
`Troubleshooting`; `直す` → not a section at all.

#### Attested Japanese terms

Use the attested term from `references/ja-heading-glossary.md`.
`触る前に` is invented; the attested form is `始める前に` / `前提条件`.
`Troubleshooting` / `Scope` / `Related` / `FAQ` stay in English in Japanese
docs — that is attested and normal.

### Section placement

#### Mixing rules

| Do not mix | Where each goes |
|---|---|
| Concept (why / how it works) and procedure (commands) | separate H2s — `仕組み` vs `セットアップ` |
| Procedure and troubleshooting | Troubleshooting is its own H2; only a failure closed over one step stays as its H3 |
| Steps and their reasons | a numbered list of steps, and a separate sibling with the reasons tagged by step |
| Current spec and history | see `#### Dated incidents and history` |
| General rule and platform/environment-specific difference | see below |
| Reference tables and explanation | explanation in the H2, per-key reference as H3s or a separate doc |
| Facts and prohibitions | a prohibition is one item under the pitfalls section, not its own H2 |

#### Dated incidents and history

A doc is a snapshot of the current spec.

A dated incident is a record, so it may not sit beside procedure or mechanism
siblings. Put it as a child of `Troubleshooting`, next to the table row of the
symptom it shows (add that row only if the doc already states the symptom and
its fix). If the doc has no such symptom, group the incidents under one parent
whose children are all dated records. Name each with its date, keeping code
spans from the body in backticks: ``2026-09-06 `v2.1` → `v2.2` の upgrade``. A
current rule written inside an incident ("so never mix X with Y") moves to the
section of that rule; the incident keeps only what was observed, and the rule
links to `#troubleshooting`. When one sentence holds both, the past-tense
observation stays and the present-tense rule moves. A dated incident is never
an H2 of its own.

Separating pure migration history means **getting it out of the current-spec
sections**, not giving it a section of its own. Keep history only as a dated
proper name at the end
(cert-manager `March 2020 Let's Encrypt CAA Rechecking Bug`), never as
`これまでに踏んだこと`.

#### Platform / environment content

**Never promote an environment name to H2.** Across all 117 docs, not one
uses an OS, cloud, or platform name as a top-level section; they are always
children of the procedure (Groonga `2. インストール` > `2.1. Windows`;
Laravel `Installation Using Herd` > `Herd on macOS`; Spring Boot
`Setting Up the Project With Maven` / `... With Gradle`).

Distribute environment-specific content three ways:
behavioral difference → the concept section; procedural difference → a final
child of the setup section; failure that only happens there → the pitfalls
section. If nothing is left over, no dedicated section is needed.

#### Anti-patterns

**Sibling promotion.** Do not raise one item out of a set because it feels
important. If removing the candidate leaves the remaining siblings describable
by the same parent name, it is a member, not a chapter. Emphasize in the body
instead.

**Template application.** Do not map the document onto a generic sequence (`concept → setup → operations
→ troubleshooting`) without reading it. The standard sequences in
`references/section-vocabulary.md` are a **vocabulary for naming and ordering**,
not a mold. Inventory the existing prose paragraph by paragraph, write down the
reader question each answers, group the questions, and only then name the
groups. A group that no slot fits usually belongs in a different document.

### Document split

Consider recommending a multi-document split when:

- The document serves multiple reader intents.
- Generated reference content is larger than authored guidance.
- Operational procedures obscure conceptual explanation.
- Troubleshooting and recovery dominate the main page.
- The document has more than around 8-10 major sections.
- Different readers need different entry points.

Possible split pattern:

- Overview
- Operations
- Schema/reference
- Generated catalog
- Troubleshooting/recovery

This list is an example of how documents get divided, **not a section list to
copy into a document.** Applying it (or `concept → setup → operations →
troubleshooting`) without inventorying the actual prose is the single most
common failure of this skill — see `### Section placement` § Anti-patterns.

Do not split automatically unless the user explicitly allows multi-file refactoring.

## Final Response Format

Report in the user's language. In Japanese, call the `##` line
**「sectionタイトル」** and a title together with its body **「セクション」**.
Do not use 「見出し」 or 「節」: readers cannot tell which of the two they mean.

Include, in this order:

1. **概要** — the subject sentence (step 1) and the document type.
2. **変更後の構成** — the full section tree of the result, as a code block.
   Mark changed sections with ★ and a few words on what changed. The reader
   must be able to see the final shape, not only a list of edits.
3. **親ごとの軸** — a table `親 | 子を分ける軸 | 子の種類` covering every
   parent with two or more children (step 3).
4. **変更内容** — a table `変換 | 対象 | 変更後`. Every table row, list item or
   sentence you composed from existing facts (step 4) is a row here, with the
   place its facts came from.
5. **意味を変えていないことの確認** — the code-span comparison result, the
   checkers that passed, and the concurrent-work result in the wording of
   step 0.
6. **他 doc との重複、欠けている概念、食い違い** — the step 1 records. Cross-file moves
   and link replacements appear here as proposals, not as done work.
7. **確認したいこと** — one question per item. An item the user does not answer
   explicitly is **not** approved: ask it again before acting on it, even if the
   user approved other items in the same reply.

Do not say only "refactored the document."

## References

Load these only when you need them.

| File | Contents |
|---|---|
| `references/section-vocabulary.md` | Standard section sequences per doc type, with counts and real examples |
| `references/heading-forms.md` | Full word-form tables (EN/JA), container-word ban list and replacements, mixing rules, platform placement, promotion rule, anti-template procedure |
| `references/ja-heading-glossary.md` | English heading → attested Japanese term, with sources |
| `references/corpus.md` | Verbatim H2/H3 of 117 real docs (EN 80 / JA 37), plus the URLs that could not be fetched |

To add new information rather than reorganize it, use `md-doc-update`.