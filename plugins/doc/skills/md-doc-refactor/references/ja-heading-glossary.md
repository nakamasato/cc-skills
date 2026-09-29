# 日本語見出しの定訳表

英語見出し → 日本語圏で**実際に使われている**語。出典はすべて `corpus.md`
収録の実在ページ。直訳を作らず、この表の attested 語から選ぶ。

複数形が並ぶ列は、左ほど汎用・右ほど文脈限定。

| 英語 | 日本語（attested） | 出典 |
|---|---|---|
| Installation | **インストール** | Groonga `2. インストール` / Django ja `Django のインストール方法` / Redmine `Redmineのインストール` |
| Getting Started | **はじめよう** / **はじめに** / **〜を始めよう** | railsguides `Rails をはじめよう` `はじめに` / LINE `Messaging APIを始めよう` |
| Prerequisites / Before you begin | **前提条件** / **始める前に** / **必要なもの** | GitHub Docs ja `前提条件` / k8s ja `始める前に` / Spring pleiades `必要なもの` |
| Overview / Introduction | **概要** / **イントロダクション** / **はじめに** | Vite ja `概要` / Laravel ja `イントロダクション` / Rails ja security `はじめに` |
| What is X? / Why X? | **X とは？** / **X とは何か** / **なぜ X なのか？** | Vue ja `Vue とは？` / railsguides `Railsとは何か` / k8s ja `Podとは何か？` / Laravel ja `なぜLaravelなのか？` |
| Configuration / Setup | **設定** / **初期設定** / **セットアップ** | Laravel ja `初期設定` / Docker ja `セットアップ` / Redmine `とりあえずの設定` |
| Configuration options | **設定** + 項目名の名詞句 | Docker Compose ja `version トップレベル要素` `services トップレベル要素` |
| How it works / Architecture | **〜の仕組み**（本コーパスに直接の attestation 無し）。attested な代替: **〜とは何か** / **〜機構** / **〜の定義方法** | k8s ja `仮想IPアドレッシング機構` `Serviceの定義方法` / `Podとは何か？` |
| Usage | **使用** / **〜を使う** / **〜の使用** | Docker ja `ボリュームの使用` `ボリュームを使ってコンテナを起動` |
| Next steps | **次のステップ** / **次の項目** / **次に行うこと** / **今後のステップ** | Laravel ja / k8s ja / Mackerel / railsguides |
| Troubleshooting | **トラブルシューティング** / **問題の診断** / **困った時は** | k8s ja `問題の診断` / Mackerel `困った時は` |
| Known issues | **既知の問題** | k8s ja DNS デバッグ `既知の問題` |
| Debugging | **デバッグ** / **〜のデバッグ** | k8s ja `Podのデバッグ` |
| Caveats / Gotchas | **〜で気をつけるべきこと**（主語が固有名のときのみ） / **使用上の注意** | Git book ja `サブモジュール使用時に気をつけるべきこと` / Ruby ja `使用上の注意` |
| FAQ | **FAQ** / **よくある質問** | WordPress ja `FAQ/インストール` |
| Differences / X vs Y | **X と Y の違い** / **X 対 Y** | Docker ja `-v と --mount との挙動の違い` / Laravel ja `接続 対 キュー` / SvelteKit `SvelteKit vs Svelte` |
| Security | **セキュリティ** / **セキュリティチェック** | PHP ja `セキュリティ` / railsguides `セキュリティチェック` |
| Testing | **テスト** / **〜でテストを書く** / **単体テスト** | railsguides `Railsでテストを書く` / Vue ja `単体テスト` `E2E テスト` |
| Deployment | **デプロイ** / **production環境にデプロイする** | railsguides `Kamalでproduction環境にデプロイする` / Firebase `本番環境に関数をデプロイする` |
| Migration (DB) | **マイグレーション** | railsguides `データベースのマイグレーション` |
| Reference | **リファレンス** | MDN ja `リファレンス` |
| Guides / How-to | **ガイド** / **手引き** | MDN ja `ガイド` `手引き` |
| Concepts | **概念** / 概念名そのもの | k8s ja `Serviceタイプ` `キャッシュの種類` |
| Summary / Conclusion | **まとめ** / **要約** | Spring pleiades `要約` / Phoenix `Summary` |
| Related / See also | **関連リンク** / **関連事項** / **関連トピック** / **関連情報** | railsguides `関連リンク` / Spring pleiades `関連事項` / MDN ja `関連トピック` `関連情報` |
| Contributing | **〜に協力** / **コントリビュート** | MDN ja `MDN の改良に協力` |
| Step N | **手順 N: 〜** / **ステップ N：〜** / **N. 〜** | GitHub Docs ja `手順 1: リポジトリを作成する` / React ja `ステップ 1：レンダーのトリガ` / LINE `1. LINE公式アカウントを作成する` |
| Escalation / Alerts | （日本語 attestation 無し。英語のまま `Alerts` `Escalation` が実例） | i-dot-ai RUNBOOK |

## 使うときの注意

- **英語の見出しをそのまま残してよい語がある。** `Troubleshooting` `README`
  `FAQ` `Scope` `Related` は日本語 doc でもそのまま出る。無理に訳して
  `症状から探す` のような非 attested 語を作らない。
- **カタカナ + 日本語動詞の混成は自然。** `デプロイする` `マイグレーション`
  `オーガニゼーションに所属する` は attested。片仮名を避けて漢語に置き換える
  必要はない。
- **表の右側に無い語を発明しない。** 発明した語はレビューで必ず引っかかる。
  どうしても該当が無ければ、内容そのものの名詞（`設定ファイルの探索順`
  `Kubernetes でのデータ永続化`）を見出しにするほうが安全。
