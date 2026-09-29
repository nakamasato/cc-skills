# 見出しの語形・器の名前・粒度

判断基準の本体。実例はすべて `corpus.md`（実在 doc 117 件）から。

---

## 1. 語形（英語）

| 語形 | 使ってよい場所 | 実例 |
|---|---|---|
| 名詞句 | **既定。** 概念 / reference / 設定項目 / 脅威名 / 分類 | `Installation`, `Configuration options`, `Command-line flags`, `Breaking changes`, `Threat model`, `Cluster failure modes`, `Context` `Decision` `Consequences` |
| 動名詞 (-ing) | 手順・作業を主題にする節 | `Getting Started`, `Creating a Vue Application`, `Reporting a vulnerability`, `Examining pod logs`, `Debugging with container exec`, `Upgrading from Rails 7.2 to Rails 8.0` |
| 命令形 | 手順の**個々のステップ**、チェックリスト、規範 | `Run the development server`, `Set up TypeScript`, `Try React`, `Always sanitize user input`, `Switch away from manage.py runserver` |
| 疑問文 | FAQ、および「なぜ / とは」の導入節のみ | `What is SvelteKit?`, `Why Laravel?`, `How do I disable cowsay?`, `Should I use Create React App?` |
| 断定文 | **troubleshooting の症状列挙のみ** | Istio `Envoy is crashing under load`, `Route rules don't seem to affect traffic flow` |
| ALL CAPS | man page のみ | git `NAME` `SYNOPSIS` `OPTIONS` |

締めの節は `Next steps` / `What's next` / `More information` /
`Additional resources` / `See also` / `Related` のいずれか 1 つを最後に置く。
複数置かない。

## 2. 語形（日本語）

日本語 37 件で実際に使われている形。

| 語形 | 使ってよい場所 | 実例 |
|---|---|---|
| 名詞句（体言止め） | **既定。** 概念 / reference / 分類 / 設定項目 | `概要`, `初期設定`, `ルーティング`, `セッション`, `既知の問題`, `テストの種類`, `Serviceタイプ`, `キャッシュの種類`, `関連リンク` |
| 「〜する」動詞終止形 | **手順の節・手順のステップ。** ここでは名詞句より普通 | `プロジェクトを作成する`, `kubectlの設定を検証する`, `オーガニゼーションに所属する`, `関数の実行をエミュレートする`, `レコードを更新する`, `Railsアプリを新規作成する` |
| 「〜とは」「なぜ〜か」 | 導入・概念の冒頭 1 節だけ | `Vue とは？`, `Railsとは何か`, `Podとは何か？`, `なぜテストをするのか？`, `なぜLaravelなのか？` |
| 番号プレフィックス | 順序が本質の手順 | `手順 1: リポジトリを作成する`, `1. LINE公式アカウントを作成する`, `ステップ 1：レンダーのトリガ`, `2.1. Windows` |
| 断定文 | **使わない。**コーパスに日本語の断定文見出しは 0 件 | — |

**重要**: 日本語で動詞終止形の見出しが悪いのではない。悪いのは
**兄弟見出しと語形が揃っていないこと**と、**手順でない節に動詞を使うこと**。
`セットアップ` の下に `1. ログイン` `2. 設定の確認` と並べるなら名詞句で
揃え、`ログインする` `設定を確認する` と並べるなら全部動詞で揃える。
混ぜない。

口語・体言でない言い切りは避ける。`認証を通す` `直す` `API key を使わない`
はいずれもコーパスに類例が無い。同じ内容の attested な形は
`認証`（名詞句）/ `認証を設定する`（手順）/ `API key の使用禁止`（名詞句）。

## 3. 器の名前（禁止リスト）

**中身を制限しない語を見出しの主語にしない。** 何でも入る器は、後から何でも
入れられてしまい、粒度不一致の温床になる。

禁止する語形:

- `基本の〜` / `基本設定` — 「基本」は中身を言っていない
- `〜について` / `〜まわり` / `〜系` / `〜関連`
- `〜こと`（`気をつけること` `やること` `踏んだこと`）
- `その他` / `Tips` / `ポイント` / `補足` / `メモ` を**中間**に置く
- `触る前に` のような言い換え。attested な形は `始める前に` / `前提条件`
- `概要` の濫用。導入 1 節だけに許す。2 箇所目の `概要` は器になっている

**例外は末尾だけ。** コーパスで器語が現れるのは常に最後の節:
Elasticsearch `Other issues`（最終節）、HAProxy `Other sections`（最終節）、
git-rebase `NOTES`、ADR `Notes`。**残余を受ける最終節としてだけ許す。**

置き換え方:

| 器の名前 | 中身を見て付け直す |
|---|---|
| `基本の設定` | `セットアップ` / `初期設定` / `設定ファイルの場所` |
| `Kubernetes で気をつけること` | 中身が差分なら `Kubernetes での差分`、落とし穴なら `既知の落とし穴` へ**吸収** |
| `これまでに踏んだこと` | 現行仕様なら `既知の落とし穴`。過去の事故なら日付つきの固有名（cert-manager `March 2020 Let's Encrypt CAA Rechecking Bug`）にして末尾へ |
| `症状から診断する` | `Troubleshooting` |
| `直す` | 直し方は Troubleshooting の中身。節にしない |

## 4. 見出しは文にしない

主張は**本文の 1 行目**に置き、見出しは名詞句にする。

| 悪い | 良い |
|---|---|
| `同じポートで 2 つ起動すると後の方が落ちる` | `ポートの競合` |
| `Ready は疎通を保証しない` | `Ready 状態の解釈` |
| `--force は削除が先に走る` | `--force オプション` |

唯一の例外は troubleshooting の症状列挙型（Istio 型）。そこでは症状が
検索キーなので文でよい。それ以外で断定文を見出しにした doc はコーパスに無い。

## 5. 1 つの H2 の下に混ぜてよいもの / いけないもの

**判定**: その H2 の下の各ブロックに「読者はこれを**いつ**読むか」を聞く。
答えが違うものは同居させない。

| 混ぜてはいけない組 | 分け先 |
|---|---|
| 概念（なぜ / どう動くか）と 手順（コマンド列） | `仕組み` と `セットアップ` に分ける。Vue ja は `なぜテストをするのか？` `いつテストをするか？` `テストの種類` `単体テスト` を全部別 H2 にしている |
| 手順 と トラブルシューティング | Troubleshooting は独立 H2。Rust Book は `Installation` の下に H3 `Troubleshooting` を置く（親手順に閉じた失敗のみ） |
| 現行仕様 と 経緯・履歴 | 履歴は書かない。残すなら日付つき固有名で末尾 |
| 一般則 と 環境・platform 固有の差分 | §6 |
| reference 表 と 説明 | 説明を H2、キーごとの表を配下の H3 か別 doc（Grafana / Prometheus 型） |
| 事実（何がそうなっているか）と 禁止事項（何をしてはいけないか） | 禁止事項は落とし穴の 1 項目として H3 に置く。単独 H2 に昇格させない |

**兄弟テスト**: ある H2 の直下の H3 群を並べて読み、
(a) 語形が揃っているか、(b) 同じ問いの答えになっているか、
(c) 1 つだけ抽象度が高い / 低いものが無いか、を確認する。
1 つだけ浮いているものは、たいてい**別の H2 の配下に属する**。

## 6. platform 別・環境別の置き場

**環境名を H2 に昇格させない。** コーパス 117 件に、環境名・OS 名・
クラウド名を H2 にした doc は 1 件も無い。常に親手順の配下の H3。

- Groonga: `2. インストール` > `2.1. Windows` `2.2. macOS` `2.3. Debian GNU/Linux`
- Deno: `Download and install` > `Cross-platform package managers`、
  別 H2 に `Docker` `Installation location`
- Laravel: `Creating a Laravel Application` > `Installation Using Herd` >
  `Herd on macOS` `Herd on Windows`
- Spring Boot: `Setting Up the Project With Maven` / `... With Gradle`
  （ビルドツール差を**手順の中で**分岐）

やり方: 環境固有の内容を 3 つに分配する。

1. **動作の違い** → `仕組み` の H3（例: `Kubernetes でのデータ永続化`）
2. **手順の違い** → `セットアップ` の最後の H3（例: `Kubernetes での差分`）
3. **そこだけで起きる事故** → `既知の落とし穴` の H3

分配してなお残るものが無ければ、環境専用の H2 は要らない。

## 7. 昇格の禁止

**仲間のうち 1 つだけを H2 に昇格させない。** `API key を使わない` は
「落とし穴」の一項目であって章ではない。昇格させてよいのは、
その項目が他の兄弟と**種類が違う**ときだけで、強調したいときではない。
強調は本文（警告文・太字）でやる。

判定: 昇格候補を外したとき、残りの兄弟が同じ器の名前で説明できるなら、
それは同じ器の中身であって章ではない。

## 8. テンプレの当てはめ禁止

`概念 → 設定 → 運用 → Troubleshooting` のような一般テンプレを、
中身を見ずに当てるのは失敗する。`section-vocabulary.md` の標準列は
**当てはめる型ではなく、名前と順序を選ぶときの語彙集**として使う。

手順:

1. 既存の本文を段落単位で棚卸しし、各段落が答えている**読者の問い**を書き出す
2. 問いを種類（概念 / 手順 / 事実 / 禁止 / 症状）で束ねる
3. 束ごとに、その doc 種別の標準列（`section-vocabulary.md`）から名前を選ぶ
4. 選べない束があれば、その doc の外に属するか、既存の束に吸収されるべき

「テンプレのどれに当たるか」ではなく「棚卸しの束がどう名乗るか」の順で考える。
