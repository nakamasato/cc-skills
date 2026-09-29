# Claude Code Skills

Claude Code の plugin marketplace。

## Plugins

| Plugin | Skills | 用途 |
|---|---|---|
| `doc` | `md-doc-update` / `md-doc-refactor` | Markdown doc の内容更新と、意味を変えない構造リファクタ |
| `skill` | `skill-reviewer` | skill の構造レビュー (SKILL.md と references/・scripts/ の振り分け) |

## Installation

```
/plugin marketplace add nakamasato/cc-skills
/plugin install doc@nakamasato
/plugin install skill@nakamasato
```

ローカルの clone から試す場合は `/plugin marketplace add ./` を使う。
