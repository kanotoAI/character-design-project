# Character Design Project — キャラクターデザイン資産

このリポジトリは、**あや・玲奈などのキャラクターデザインの正式資料・制作履歴・採否を管理する専用リポジトリ**です。AI画像生成全般を学ぶプロジェクトそのものではありません。

## 最初に読む
- [作業の対象と適用規則](docs/CHANGE_SCOPE.md)
- [構造整理と復元手順](docs/restructure-2026-11-17.md)
- 正式なキャラクター制作時のみ：[統合運用規則](rules/current_rules.md)、[絶対禁止](rules/absolute_prohibitions.md)
- 既存画像の局所編集時のみ：[画像編集規則](rules/image_editing_rules.md)
- [共通ロードマップ](planning/roadmap.md)

## 構成
- `characters/<id>/`：キャラクターごとの外見正本、正式画像、制作試行、manifest、履歴、ToDo
- `rules/`：正式デザイン制作に適用する詳細ルール
- `planning/`：キャラクター制作分野の作業予定
- `migration/`、`incoming/`：資料移管・アップロード・原記録（現行正本に自動昇格しない）
- `docs/`：分野の役割・運用移行メモ

## 学習プロジェクトとの関係
[AI-Image-Generation-Notes](https://github.com/kanotoAI/AI-Image-Generation-Notes) が、ComfyUIの学習・ツール開発およびChatGPT画像生成**技術検証**の入口です。キャラクターを題材にする技術実験でも、正式採用・正本更新を伴わなければこのリポジトリの全制作工程を必須としません。

## 守ること
- ユーザーの最新明示指示を尊重し、正式な外見・MASTER／APPROVED_REFERENCE・採否を無断変更しない。
- TRIAL／WORKINGを承認なしに正本扱いしない。
- 詳細の参照先・状態は個別のmanifest・正本と履歴を確認する。READMEを正本のコピーにしない。

## 安全な改編
2026-11-17の構造整理以前の状態は `backup/pre-restructure-2026-11-17` に保持。変更履歴と復元手順は [構造整理の記録](docs/restructure-2026-11-17.md) を参照。正式画像・承認履歴は維持する。
