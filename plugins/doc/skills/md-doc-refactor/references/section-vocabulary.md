# doc 種別ごとの標準セクション列

`corpus.md` の 117 件（英語 80 / 日本語 37）から抽出した、doc 種別ごとの
実際の並び。頻度は「その種別としてコーパスに入っている件数のうち何件か」。
**census ではなく sample** なので、比率ではなく「この形が実在する / しない」を読む。

使い方: 新しい節を足すとき・既存の節を名前ごと直すときは、まず doc の種別を
決め、その種別の**正規スロット**のどれに当たるかを言えるようにする。どのスロット
にも当たらない節は、名前が悪いのではなく **その doc に属していない**可能性が高い。

---

## README (8件)

```
Installation / Getting Started
  → Usage / Examples / Your first <X>
  → Documentation / More information
  → Contributing
  → License
```

- `Contributing` 系が 5/8（react, vuejs/core, deno, prometheus, ohmyzsh）
- `License` が最後 4/8（vuejs/core, prometheus, fastapi, ohmyzsh）
- 導入が `Installation` / `Install` / `Getting Started` 5/8
- コミュニティ系（Sponsors / Stay In Touch / Community Meetings / Governance /
  Roadmap）は本題の**後ろ**に固まる。前に来る例は fastapi の `Sponsors` のみ
- 例: kubernetes/kubernetes は `To start using K8s | To start developing K8s |
  Support | Community Meetings | Adopters | Governance | Roadmap` ——
  **読者の役割**で切っており、機能で切っていない

## getting-started / installation (27件, 英日)

```
Try it online (任意)
  → Prerequisites / 前提条件 / 始める前に
  → Install / Create the project
  → Run / 動作確認
  → 環境ごとの差分・任意設定
  → Next steps / 次のステップ
```

- 締めの `Next steps` 系が 16/27。日本語は `次のステップ` `次の項目`
  `次に行うこと` `今後のステップ` `次は何をしますか？`
- 冒頭の「オンラインで試す」が 5 件（React `Try React`, Vue `Try Vue Online`,
  Angular / Nuxt `Play Online`, Vite ja `Vite をオンラインで試す`）
- 前提の節が 8 件（Angular / Astro / Spring Boot / Nuxt / Rails `Prerequisites`,
  k8s ja `始める前に`, Spring pleiades `必要なもの`, GitHub Docs ja `前提条件`）
- **OS / パッケージマネージャ / 環境の差は H3 に落ちる**。Groonga は
  `2. インストール` の下に `2.1. Windows | 2.2. macOS | 2.3. Debian GNU/Linux`。
  Deno は `Download and install` の下に `Cross-platform package managers`。
  環境名を H2 に昇格させた doc はコーパスに 1 件も無い

## configuration (11件)

```
何を設定するものか（概要）
  → 設定ファイルの場所
  → 記法 / 構文
  → 設定項目（キーごとの reference）
  → 上書き手段（環境変数など）
  → 廃止された設定
```

- 「ファイルの場所」を独立節にするのが 4/11（Grafana
  `Configuration file location`, Terraform `Locations`, etcd
  `Configuration file`, containerd `Base Configuration`）
- 設定項目はキー名そのものを見出しにする 5/11（Grafana `[paths]` `[server]`,
  Prometheus `<scrape_config>` `<tls_config>`, PostgreSQL
  `19.3.1. Connection Settings`, Docker Compose ja `version トップレベル要素`）
- Terraform は `Removed Settings` を最後に置く。**廃止の記録は末尾**

## troubleshooting (13件)

3 つの型しかない。混ぜない。

| 型 | 見出しの作り方 | 実例 |
|---|---|---|
| 症状列挙型 | 症状を述べた**文**が H2 | Istio: `Requests are rejected by Envoy` / `503 errors after setting destination rule` / `Envoy is crashing under load` |
| 部位分割型 | サブシステム名の名詞句が H2 | Docker: `Daemon \| Networking \| Volumes` / Elasticsearch: `General \| Data \| Management \| Capacity \| Snapshot and restore \| Other issues` |
| 手段分割型 | 調べ方が H2（動名詞） | k8s: `Examining pod logs \| Debugging with container exec \| Debugging with an ephemeral debug container` |

- **症状を文にしてよいのは troubleshooting の症状列挙型だけ。** 他の doc 種別で
  断定文の見出しを使う例はコーパスに無い
- 締めに `Additional resources` / `What's next` / `次の項目` 5/13
- 前提チェックの節名は `始める前に`（k8s ja）。`触る前に` のような言い換えは
  コーパスに存在しない

## ADR (3件)

```
Context → Decision → (Alternatives Considered) → Consequences
        → (Implementation Notes) → References → Notes
```

3/3 が `Context` `Decision` `Consequences` `References` を持ち、**順序も同一**。
この種別だけは定型が完全に固まっている。勝手な言い換えをしない。

## SECURITY.md (3件)

`Supported versions` / `Threat model` / `Reporting a vulnerability` /
`Reporting process` / `Disclosure policy` / `Security updates`。
axios と nodejs はほぼ同じ語彙。electron だけ 3 節と短い。

## CONTRIBUTING.md (4件)

共通なのは「PR をどう出すか」だけ（4/4）。開発環境構築が 3/4。
それ以外はプロジェクトの統治スタイル次第で、**標準列は存在しない**
（vuejs は 9 節で H3 も深い、rust は 5 節でフラット）。
標準列が無い種別に無理やり型を当てないこと。

## migration / upgrade (5件)

2 つの型がある。

- **手順型**: Django `Required Reading | Dependencies | Resolving deprecation
  warnings | Installation | Testing | Deployment`、React 19 `Installing |
  Codemods | Breaking changes | New deprecations | Notable changes |
  TypeScript changes | Changelog`
- **版列挙型**: Rails `Upgrading from Rails 7.2 to Rails 8.0` を版の数だけ、
  Terraform `Upgrading to Terraform v1.16`

いずれも**版や変更点**を名前にする。「これまでに何をしたか」という
書き手の経緯を名前にした doc はコーパスに 1 件も無い。

## api-reference / cli-reference (8件)

- man 型は語彙が固定: git `NAME | SYNOPSIS | DESCRIPTION | OPTIONS |
  CONFIGURATION`、AWS CLI `Description | Synopsis | Options | Global Options |
  Examples`
- Web 型: MDN `Syntax | Description | Examples | Specifications |
  Browser compatibility | See also`
- メンバごとに H2 を切る型もある（Node.js `fs` は 313 個の H2）。
  **reference は例外的に「均一な粒度の大量の見出し」が正しい**

## security ガイド (3件)

脅威名 / 防御名の名詞句を H2 に並べる。
Django: `Cross site scripting (XSS) protection | Cross site request forgery
(CSRF) protection | SQL injection protection | Clickjacking protection |
SSL/HTTPS | Host header validation`。
Rails ja: `セッション | クロスサイトリクエストフォージェリ（CSRF） |
インジェクション | HTTPセキュリティヘッダー`。
唯一の命令形が Django `Always sanitize user input` で、これは**規範**であって
節の器ではない。

## FAQ (3件)

質問文をそのまま見出しにする。Ansible FAQ は H2 が全部疑問文
（`How do I disable cowsay?` 等）、Docker Desktop / WordPress ja / curl は
H3 が疑問文で H2 は分類名詞（`Philosophy | Install | Usage | Running`）。
**疑問文を見出しにしてよいのは FAQ と「なぜ〜か」の導入節だけ。**

## runbook (3件)

小さい。`Alerts | Escalation`（i-dot-ai）、`Releasing | Release
authentication`（cdp-use）。番号付き手順を H2 にする例が zoom/skills
（`1) Confirm Integration Surface` … `8) Source Checkpoints`）。
**番号は手順であることの明示であり、器の名前の代用ではない。**
