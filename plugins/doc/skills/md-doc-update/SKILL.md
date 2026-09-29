---
name: md-doc-update
description: This rule is used when updating md file (SKILL.md, README.md, AGENTS.md, CLAUDE.md, etc) to help make a beautiful document.
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# MD Doc update

## なぜこのSkillが必要か？

- AI はすぐに依頼されたことを追記するだけ
- 追記する場所と見出しの名前を、その場の語感で決めてしまう

## Doc更新時フロー

0. 着手前チェック

   - [ ] 同じファイルを触っている open PR / 未マージブランチが無いか
         (`gh pr list --repo <owner>/<name> --state open`、
         `gh pr view <n> --repo <owner>/<name> --json files`)。
         あれば、そちらに乗せるか着手前に方針を確認する
   - [ ] この doc の種別を言う (README / getting-started / configuration /
         troubleshooting / ADR / migration / api-reference / FAQ / runbook)

1. 全体Section構成を確認

   ```
   # MD Doc update
   ## なぜこのSkillが必要か？
   ## Doc更新時フロー
   ## Doc Validation
   ```

   - [ ] セクションが多すぎないか (10セクションや20セクションは結構多い)
         — ただし**減らすために複数の内容を 1 つの器に押し込まない**。
         器の名前 (`基本の〜` `〜について` `〜こと` `その他`) が生まれたら、
         それは統合ではなく粒度の破壊
   - [ ] サブセクションがある場合は、バランスが悪くなってないか。e.g. 一つのセクションだけが10個以上のサブセクションを持っていて、他のセクションにはサブセクションが一つものない
   - [ ] セクションのタイトルの**語形が揃っている**か (全部名詞句か、全部手順の
         動詞か)。「なんとなく統一されている」ではなく語形という一つの軸で判定する
   - [ ] 見出しが**文**になっていないか。主張は見出しではなく本文の 1 行目へ
   - [ ] セクションの切り方によって重複した内容が複数のセクションに入る構造になっていないか
1. Section構成の考え直し
2. Section構成がOKの場合は次にセクションないの内容を書く
3. それぞれのセクションに関して
    - [ ] セクションの中身がわかりやすく簡潔に書かれているか
    - [ ] ListやNumbered Listなどを使い並列関係を正しく表現出来ているか
    - [ ] 比較する場合にはテーブル表現などを使っているか
    - [ ] ArchitectureやInfrastructureに関しては全体のMermaid図を入れているか
    - [ ] 他のセクションの内容との重複や矛盾がないか
4. Diffのレビュー
    - [ ] コンテンツの追加だけになっていないか 既存のドキュメントの更新も少なからずあるはず (セクション再構成や参照 etc)
    - [ ] 単純なセクションの追加になっていないか
    - [ ] 重要な内容を削除していないか

## 節を足すときの判断基準

新しい節を作るのは**最後の手段**。既存 H2 の配下 (H3) や本文の一項目に
収まらないかを先に疑う。**仲間のうち 1 つだけを H2 に昇格させない** —
昇格候補を外して残りの兄弟が同じ器の名前で説明できるなら、それは章ではなく中身。

置く位置の既定:

```
Scope / 概要 → 仕組み・概念 → セットアップ・手順 → 既知の落とし穴
→ Troubleshooting → Related / 次のステップ
```

- 環境・platform 別の内容を**新しい H2 にしない**。親手順配下の H3 にし、
  動作の違いは仕組みへ、そこだけで起きる事故は落とし穴へ分配する
- 経緯・時系列を節にしない (`これまでに踏んだこと`)。doc は最新仕様の
  スナップショット。過去の事故を残すなら日付つき固有名で末尾に置く
- 一般テンプレ (`概念 → 設定 → 運用 → トラブル`) を中身を見ずに当てない。
  本文を段落単位で棚卸しし、読者の問いで束ねてから名前を選ぶ
- 締めの節 (`Related` / `次のステップ` / `See also`) は 1 つだけ、必ず最後

名前は**名詞句が既定**。手順の節とステップだけ動詞終止形・番号プレフィックスを
許し、兄弟の中で語形を揃える。日本語の語は実在 doc で使われている語から選び、
訳語を発明しない。

足したあとに兄弟を並べて読み、語形が揃っているか・全部が同じ問いの答えに
なっているか・1 つだけ抽象度が浮いていないかを確認する。

| 参照先 | 内容 |
|---|---|
| `references/section-placement.md` | 配置と命名の手順、兄弟テスト |
| `../md-doc-refactor/references/heading-forms.md` | 語形ルール、器語の禁止リスト、粒度、platform 別の置き場 |
| `../md-doc-refactor/references/section-vocabulary.md` | doc 種別ごとの標準セクション列 (頻度つき) |
| `../md-doc-refactor/references/ja-heading-glossary.md` | 英語見出し → 日本語の定訳表 (出典つき) |
| `../md-doc-refactor/references/corpus.md` | 実在 OSS doc 117 件の逐語見出し |

構造だけを直す (内容を足さない) 場合は `md-doc-refactor` を使う。

