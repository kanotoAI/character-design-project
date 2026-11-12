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
- upload_status: VERIFIED_IN_GITHUB
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
  - GitHub上の画像実在確認済み。表情制作の現行限定参照として有効。
  - 直前の旧表情サンプルは旧試作として扱い、通常の制作参照には使わない。GitHubに旧画像の登録はない。

### OUTFIT WORKING REFERENCES（GitHub登録確認済み）
- status: WORKING（5点すべて）
- use_as_reference: limited（衣装の方向性・服と小物の候補に限る）
- upload_status: VERIFIED_IN_GITHUB（5点のファイル実在確認）
- location: `02_design_trials/`
- notes: ユーザーが「とりあえずの衣装イメージとしてこの5点採用」と判断。衣装のイメージ資料として採用したもので、完成衣装・正式透過素材・顔や体型の正本ではない。画像のデザイン枠や説明文字は参照対象外。

#### `02_design_trials/reina_outfit_smart_chic_working_v1.png`
- status: WORKING
- use_as_reference: limited（衣装案）
- upload_status: VERIFIED_IN_GITHUB
- label: スマートシック
- scope: 前回C：黒系ジャケット・トップスと明るいパンツによる知的なきれいめスタイル
- ignore: 顔・髪・目・体型の変更、資料装飾・ラベル・レイアウト、衣装細部の最終確定扱い

#### `02_design_trials/reina_outfit_relaxed_casual_working_v1.png`
- status: WORKING
- use_as_reference: limited（衣装案）
- upload_status: VERIFIED_IN_GITHUB
- label: リラックスカジュアル
- scope: 前回D：淡色ゆったりニットとショートパンツの休日スタイル
- ignore: 顔・髪・目・体型の変更、資料装飾・ラベル・レイアウト、衣装細部の最終確定扱い

#### `02_design_trials/reina_outfit_office_working_v1.png`
- status: WORKING
- use_as_reference: limited（衣装案）
- upload_status: VERIFIED_IN_GITHUB
- label: オフィススタイル
- scope: 白シャツ・黒タイトスカート・タイツ・パンプスとバッグ等の小物
- ignore: 顔・髪・目・体型の変更、資料装飾・ラベル・レイアウト、衣装細部の最終確定扱い

#### `02_design_trials/reina_outfit_lavender_cardigan_working_v1.png`
- status: WORKING
- use_as_reference: limited（衣装案）
- upload_status: VERIFIED_IN_GITHUB
- label: ラベンダーカーディガン
- scope: 淡い紫のカーディガン・キャミソール・明るいショートパンツ
- ignore: 顔・髪・目・体型の変更、資料装飾・ラベル・レイアウト、衣装細部の最終確定扱い

#### `02_design_trials/reina_outfit_black_knit_white_cargo_working_v1.png`
- status: WORKING
- use_as_reference: limited（衣装案）
- upload_status: VERIFIED_IN_GITHUB
- label: 黒ニット＋白カーゴ
- scope: 黒のゆったりトップス・白ワイドカーゴパンツ・スニーカー・バッグ
- ignore: 顔・髪・目・体型の変更、資料装飾・ラベル・レイアウト、衣装細部の最終確定扱い

### Bポーズ衣装比較6枚（GitHub登録確認済み）
- status: WORKING（採用済みの衣装比較用作業参照。正式素材ではない）
- use_as_reference: limited（Bポーズの立ち姿、5着の着用時イメージ、黒下着の比較基準に限定）
- upload_status: VERIFIED_IN_GITHUB（6点）
- location: `02_design_trials/`
- source: 5着は「Bポーズ・5着比較」画像を5等分して上部タイトルを下部に移動したもの。下着は既存のBポーズ黒下着立ち絵を非生成的に整形したもの。
- notes: ユーザーが6点を採用。全6枚を600×1480pxに統一。白背景、枠線・装飾なし。名称・イメージは下部のみ。原画の人物や服を描き直さない。
- ignore: 顔・髪・目・体型の承認済み基準を上書きすること、完成衣装・MASTERとみなすこと、ポーズ以外の細部を最終確定とみなすこと。

#### `02_design_trials/reina_pose_b_smart_chic_working_v1.png`
- status: WORKING
- use_as_reference: limited（Bポーズ衣装比較）
- upload_status: VERIFIED_IN_GITHUB
- label: スマートシック

#### `02_design_trials/reina_pose_b_relaxed_casual_working_v1.png`
- status: WORKING
- use_as_reference: limited（Bポーズ衣装比較）
- upload_status: VERIFIED_IN_GITHUB
- label: リラックスカジュアル

#### `02_design_trials/reina_pose_b_office_working_v1.png`
- status: WORKING
- use_as_reference: limited（Bポーズ衣装比較）
- upload_status: VERIFIED_IN_GITHUB
- label: オフィススタイル

#### `02_design_trials/reina_pose_b_lavender_cardigan_working_v1.png`
- status: WORKING
- use_as_reference: limited（Bポーズ衣装比較）
- upload_status: VERIFIED_IN_GITHUB
- label: ラベンダーカーディガン

#### `02_design_trials/reina_pose_b_black_knit_white_cargo_working_v1.png`
- status: WORKING
- use_as_reference: limited（Bポーズ衣装比較）
- upload_status: VERIFIED_IN_GITHUB
- label: 黒ニット＋白カーゴ

#### `02_design_trials/reina_pose_b_black_underwear_working_v1.png`
- status: WORKING
- use_as_reference: limited（Bポーズ衣装比較）
- upload_status: VERIFIED_IN_GITHUB
- label: 黒下着・Bポーズ

### ヘアアレンジ2案（GitHub登録確認済み）
- status: WORKING（2点とも）
- use_as_reference: limited（髪型の方向性・正面／背面のまとめ方に限定）
- upload_status: VERIFIED_IN_GITHUB（2点ともファイル実在とblob SHAを確認）
- location: `02_design_trials/`
- notes: ユーザーが2点をアップロード。お団子画像だけは、用意した2分割版とは異なる画像をユーザーが意図的にアップロードしたと明示。**GitHub上の画像を現行の作業参照とし、元のZIPとの差異は不整合・誤登録として扱わない。**
- ignore: 顔・目・体型・下着の既存基準の上書き、髪型の最終確定、正式透過素材・MASTERへの昇格。

#### `02_design_trials/reina_hair_half_up_front_back_working_v1.png`
- status: WORKING
- use_as_reference: limited（ハーフアップ正面・背面の髪型）
- upload_status: VERIFIED_IN_GITHUB
- provenance: 既存の4体比較画像から非生成的に左右分割した版。

#### `02_design_trials/reina_hair_low_bun_front_back_working_v1.png`
- status: WORKING
- use_as_reference: limited（お団子正面・背面の髪型）
- upload_status: VERIFIED_IN_GITHUB
- provenance: **ユーザーが意図的に別画像を選択してGitHubへアップロードした版**。ファイル名の `low_bun` や旧ZIPの内容だけで髪型の高さ・画像内容を断定しない。画像の具体的内容はGitHub登録版を基準に確認する。
- notes: 旧ZIPの画像とは同一バイナリではないが、ユーザー意図による差し替え。画素レベルの内容比較は未実施。

### MASTER
なし。正式透過素材は未制作。

### PENDING
- 全体デザインは再構築中。直近の体型調整案は次工程の作業基準として採用（ファイル登録確認済み）。
- 表情は控えめ表現版に方向性を移行。新画像のGitHub登録確認済み。
- 衣装イメージ5点をWORKINGの限定参照として採用。GitHub上の5ファイル実在確認済み。
- Bポーズ衣装比較6点は採用済み。画像本体のGitHub登録を確認済み。
- ヘアアレンジ2案（ハーフアップ／ユーザー選択のお団子画像）はGitHub登録確認済み。WORKINGの限定参照として扱う。
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
- G5 正式透過独立素材：未着手（正面基準立ち絵から開始し、必要な側面・背面を個別制作）
- G6 正式資料・三面図の組み立て：未着手（G5で承認済みの独立素材を使用）
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
