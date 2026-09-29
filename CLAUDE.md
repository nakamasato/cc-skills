# cc-skills

Claude Code の plugin marketplace (`nakamasato`)。構成とインストール手順は `README.md` を参照。

## Skill と plugin の追加

- skill は `plugins/<plugin>/skills/<skill>/SKILL.md` に置く
- plugin を新しく作ったら `.claude-plugin/marketplace.json` の `plugins` にも登録する
- skill から別の skill のファイルを参照するときは、`~/.claude/skills/...` ではなく参照元ファイルからの相対パスで書く。plugin としてインストールすると `~/.claude/skills/` には置かれない

## 検証

変更後に両方を通す:

```
claude plugin validate .
claude plugin validate plugins/<plugin>
```
