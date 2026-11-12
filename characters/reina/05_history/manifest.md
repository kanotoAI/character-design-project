# 玲奈 — Manifest

**最終更新：2026-11-12**

## 参照ルール
作業開始時は、次の順で確認する。
1. `/rules/current_rules.md`
2. 本 `manifest.md`
3. `00_concept/concept.md`
4. `01_settings/personality.md`
5. `01_settings/appearance.md`
6. `01_settings/decisions.md`
7. 登録済み APPROVED_REFERENCE / MASTER 画像

## 正本ファイル
| path | role | version | status | use_as_reference |
|---|---|---:|---|---|
| 00_concept/concept.md | 基本構想 | 1.0 | MASTER | true |
| 01_settings/personality.md | 人格・関係性 | 1.0 | MASTER | true |
| 01_settings/appearance.md | 外見文章正本 | 1.0 | MASTER | true |
| 01_settings/decisions.md | 採否・保留 | 1.0 | MASTER | true |
| 05_history/manifest.md | 状態管理 | 1.1 | MASTER | true |
| 05_history/revisions.md | 変更履歴 | 1.0 | MASTER | true |

## 画像管理方針
- 画像は、ファイル名だけで用途を断定せず、必ず本manifestの `status` / `use_as_reference` / `scope` / `ignore` を併せて確認する。
- APPROVED_REFERENCE は指定された範囲だけ参照する。
- TRIAL は比較・判断補助専用であり、原則としてデザイン正本にはしない。
- ARCHIVE は履歴保管。通常制作では参照しない。
- REJECTED は参照禁止。

## 画像一覧

### APPROVED_REFERENCE

#### `01_settings/reference_images/reina_reference_face_style_v1.png`
- status: APPROVED_REFERENCE
- use_as_reference: true
- scope:
  - 顔立ち
  - 目の基本形
  - 髪型
  - 髪色
  - 描画タッチ
  - 全体の上品な雰囲気
- ignore:
  - ピンク系の枠線・花装飾
  - 資料レイアウトそのもの
  - 画像内の旧文章・旧数値
- notes:
  - 玲奈の顔・髪・絵柄・雰囲気の主要参照。
  - 画像内の文字情報よりGitHub上の現行正本を優先する。

### TRIAL / DECISION SUPPORT

#### `01_settings/reference_images/reina_trial_bust_fine_range_v1.png`
- status: TRIAL
- use_as_reference: limited
- scope:
  - バストサイズの細かな比較
  - 「2〜3の間」の調整幅確認
- ignore:
  - 顔・髪・目などの細部デザイン
  - バスト以外の微差
- notes:
  - 比較検討専用。
  - 現行採用値は「2〜3の間②」。
  - 採用されたのは比較結果であり、この画像全体が正本という意味ではない。

### SUPERSEDED / PREVIOUS BODY REFERENCE

#### `01_settings/reference_images/reina_reference_body_turnaround_v1.png`
- status: SUPERSEDED
- use_as_reference: false
- scope:
  - 旧体型・旧三面図の履歴比較
- ignore:
  - ピンク系の枠線・花装飾
  - 資料レイアウトそのもの
  - 画像内の旧文章・旧数値
  - 他パネルと不一致になっている目の詳細表現
- notes:
  - 現行作業基準へ移行済み。通常制作の直接参照から外す。
  - 目の詳細が顔・三面図・表情と不一致の場合、その目詳細部分は参照しない。
  - バストは `decisions.md` の D-001「2〜3の間②」を優先する。


### ARCHIVE / NON-REFERENCE

#### `01_settings/reference_images/reina_archive_bust_rough_range_v1.png`
- status: ARCHIVE
- use_as_reference: false
- scope:
  - 「まず大まかなレンジを分け、その範囲内で細かく調整する」という検討履歴
- ignore:
  - 現行制作への直接参照
  - 顔・髪・体型・バストの最終基準
- notes:
  - 大まかなサイズレンジを決めるために使用した履歴画像。
  - 通常の制作では参照しない。
  - 後から「どういう検討経路で2〜3の間に絞ったか」を確認する必要がある場合のみ履歴として見る。

### APPROVED_DETAIL

#### `01_settings/reference_images/reina_approved_eye_detail_v1.png`
- status: APPROVED_REFERENCE
- use_as_reference: true
- scope:
  - 目の形
  - 上下まつ毛
  - まぶた線
  - 虹彩
  - 瞳孔
  - ハイライト
  - 目の表情変化
- ignore:
  - 資料の装飾的な背景・外周デザイン
  - 文章のレイアウト自体
- notes:
  - ユーザー承認済みの「目の詳細」基準。
  - 元の玲奈顔デザインを一次原本として詳細化したもの。
  - 目のデザイン内容を参照し、資料装飾をキャラクター正本としない。

### CURRENT WORKING REFERENCE（登録確認済み）
#### `02_design_trials/reina_body_proportion_working_v1.png`
- status: WORKING
- use_as_reference: limited（次工程の体型比率・脚長・頭身の作業基準）
- upload_status: VERIFIED_IN_GITHUB
- source: 直近の「玲奈_体型比率調整_局所版_v1.png」
- scope: 三面図制作へ進むための体型・頭身・脚長の暫定方向
- ignore: 正式な最終比率とみなすこと、顔・目・髪の承認済み個別基準を上書きすること
- notes: ユーザーのOKは作業継続の承認であり、決定稿承認ではない。三面図制作中の調整を許可。GitHub上の画像実在確認済み。次工程の作業参照として有効。

#### `02_design_trials/reina_expression_restrained_working_v1.png`
- status: WORKING
- use_as_reference: limited（表情の方向性・感情表現の強さに限定）
- upload_status: PENDING_UPLOAD
- source: 2026-11-12の最新「玲奈 表情サンプル（控えめ表現版）」8表情シート
- scope:
  - 玲奈らしい落ち着いた表情の方向性
  - 笑顔と驚きを控えめにする表現幅
  - 通常・微笑み・控えめ笑顔・控えめ驚き・困惑・控えめ怒り・照れ・控えめ悲しみの探索基準
- ignore:
  - 最終表情セットとしての確定扱い
  - 顔・髪・目の承認済み個別デザイン基準を上書きすること
  - シートのラベルや配置を正式資料デザインとみなすこと
- notes:
  - ユーザーが「これで移行」として採用した現行の表情探索案。
  - 画像のGitHubアップロード確認後、表情制作の現行限定参照として有効化。
  - 直前の旧表情サンプルは旧試作として扱い、通常の制作参照には使わない。GitHubに旧画像の登録はない。

### MASTER
なし。正式透過素材は未制作。

### PENDING
- 全体デザインは再構築中。直近の体型調整案は次工程の作業基準として採用（ファイル登録確認済み）。
- 表情は控えめ表現版に方向性を移行。新画像のアップロード確認待ち。
- 再構築後、残る APPROVED_REFERENCE 画像について、新デザインとの一致範囲を再確認し、必要に応じて以下のいずれかへ状態更新する：
  - APPROVED_REFERENCE 維持
  - scope限定
  - SUPERSEDED
  - ARCHIVE
- 状態変更は無断で行わず、ユーザー確認後に反映する。

### REJECTED
- R-001：①〜⑤の5体比較のうち、ユーザーが明示的にボツ指定した生成版
- R-002：巨大な左正面拡大＋目詳細不一致＋デザイン変更版
いずれも use_as_reference: false。

## 現在のゲート
- G1 基本構想：概ね通過
- G2 人格：概ね通過
- G3 外見方向性：通過
- G4 基準ビジュアル：進行中（目の詳細は承認済み。全体デザイン調整中）
- G5 正式素材：未着手
- G6 正式資料：未着手
- G7 最終登録：未着手

## 絶対維持事項
- 部分変更は指定箇所以外を変えない。
- 変更しない部分は再生成・再貼付しない。
- REJECTEDを参照しない。
- ARCHIVEを通常制作の参照に使わない。
- 他キャラの資料装飾を玲奈へ流用しない。


## 表記ルール
- キャラクター名は「玲奈」を正本表記とする。
- 英字・ローマ字・英語副題を自動追加しない。


## 追加REJECTED
- 誤生成の学生風キャラ設定シート：玲奈の現行デザインと無関係。use_as_reference: false。
