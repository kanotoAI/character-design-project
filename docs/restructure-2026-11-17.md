# 2026-11-17 構造整理と復元手順

## 整理の目的
このリポジトリは**キャラクターデザインの制作資産と採否を管理する専用領域**。親の学習プロジェクト自体をキャラクターデザイン専用にしない。ComfyUI学習・ChatGPT画像生成の技術実験は原則として [AI-Image-Generation-Notes](https://github.com/kanotoAI/AI-Image-Generation-Notes) 側で管理。

### 変更しない保護対象
- 承認済みPNG、MASTER、manifestに記録された画像の識別子、人格設定の置き場
- 正式外見設定の意味、既存の承認・不採用記録
- 旧ルール、履歴、試行画像（削除・一括移動しない）

### 既存ファイルの位置づけ
- `rules/current_rules.md`：**キャラクターデザイン制作時に限定**して適用する詳細規則。汎用画像生成の実験には自動適用しない。
- `rules/absolute_prohibitions.md`：制作時の既存の明示禁止。内容は緩和しない。
- `rules/image_editing_rules.md`：正式素材の既存画像修正など、対象領域を保護すべき作業に使用。
- `characters/<id>/01_settings/` と `05_history/manifest.md`：各キャラクターの正本と参照状態。
- `05_history/todo.md`：キャラクター制作の進捗。技術実験の原簿ではない。

### 読み込み手順
1. 単純なComfyUI/ChatGPT生成技術の質問→学習リポジトリを参照。
2. キャラクターを題材にした技術試験→学習側の実験設計＋必要な正式参照資料だけを取得。
3. キャラクターの正式設定変更／素材編集／MASTER採用→本リポジトリの詳細規則・禁止・対象manifestと履歴を参照。
4. レーンをまたぐ依頼は作業と採否を分離する。

### 復元可能性の境界
整理作業開始前のmainコミットを `backup/pre-restructure-2026-11-17` ブランチに固定。
編集は `restructure/learning-first-2026-11-17` 上で提案・レビューし、mainへの統合はPRの履歴により追跡する。
元の状態は `backup/pre-restructure-2026-11-17` を閲覧・再チェックアウトして復元できる。mainの破壊的resetや強制pushは不要。
ChatGPTのプロジェクトソースはGitHubブランチと連動しないため、別途ファイルを保存して手動差し替えが必要。
