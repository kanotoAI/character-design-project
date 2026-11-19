# 段階3記録（実際の画像入力）

GitHub保存について：この記録と試作は、段階4（新しい会話からGitHubの記録だけで再開できるかの確認）の前提として、試験用フォルダ docs/connection-tests/ へ次の名前で保存される。
- 試作画像：docs/connection-tests/2026-11-19_stage3_input_trial_01.webp（365,220 bytes、WebP 1600×1600、SHA-256 d6d5f94f5dcd83095503cae02612867422ce132641f77e3bdb1220308ea1b6ed、状態 TRIAL／入力確認用、正式採用ではない）
- 比較画像（非生成的配置、左＝入力・右＝出力）：docs/connection-tests/2026-11-19_stage3_comparison.png
- 本記録：docs/connection-tests/2026-11-19_stage3_record.md
- 入力に使った原本：characters/aya/03_trials/AYA_ROUND_02_source_candidate.jpeg（SHA-256 b345525922e339443b35ec949a65f3dd1022d490983b7585d462ed861f281924）
- 次の作業：段階4＝新しい会話でこの記録から原本・直近候補（上記試作）・採否（未採用・TRIALのまま）・次の作業（段階5の制作能力判定は未実施）を特定すること。段階5では局所補修か新規再現かをユーザーと決めてから行う。

実施：2026-11-19 22:04 JST
目的：段階2でGitHubから再取得した実ファイルを、生成ツールの画像入力へ実際に指定できるか確認する。入力できたことと、モデルが顔を再現できたかは別判定（後者は段階5）。

## 試行記録（引き継ぎ8章の最小記録形式）

- 試行ID：STAGE3-20261119-01
- 日時：2026-11-19 22:04 JST
- 目的：入力確認（新規作画TRIAL 1枚。局所編集ではない）
- 原本ID・GitHubパス・commit/blob・SHA-256・寸法：
  - 入力ファイル：workspace/character_handoff_check/stage2/reacquired/2026-11-19_stage2_round02_copy.jpeg
  - これは段階2で GitHub commit a90b14a75b6fce9260a1a62a89c3c89b3b1cb3aa（docs/connection-tests/2026-11-19_stage2_round02_copy.jpeg）から再取得した実ファイルで、ROUND 02原本とバイト同一。
  - 436,348 bytes、JPEG 1254×1254、SHA-256 b345525922e339443b35ec949a65f3dd1022d490983b7585d462ed861f281924、blob e6bd1e827f098df923d59fc219517cb80a780d30
- 実際に入力した画像：上記の再取得実ファイルを、生成ツールの prompt の画像入力（kind=image、ローカルファイルパス）として指定した。URLの文章記載ではない。
- 実行ツール・モデル・版・設定：Museの画像生成ツール（media.generate_image）。内部モデルの版は不明（ツール側から開示なし）。マスク入力欄はこのツールの入力仕様に存在しないことを確認（マスク付き編集はこの経路では未確認／不可と記録する。別経路の有無は未確認）。
- ユーザー指示と、ツールへ実際に渡した指示：
  - ユーザー承認済みの小規模試作範囲：入力確認用に1枚だけ、TRIAL、GitHubへは保存しない、局所編集の完成品としない。
  - ツールへ渡した文章（英語原文）：「Use the provided image as the reference image. Generate one new image of the same character with the same front-facing close-up composition: rose-brown short bob hair, red eyes, pink turtleneck sweater, and the same cherry blossom hairpins as in the reference image, plain light background, formal 2D anime style. No text.」
- 変更対象／維持対象／マスク：新規作画のため変更／維持の画素指定はなし。マスクなし（指定手段もなし）。
- 生成・非生成・合成等の実施順序：生成1回のみ。比較シートは生成後に PIL で左右に並べただけの非生成的配置（stage3_comparison_side_by_side.png、左＝入力、右＝出力、同じ高さ1024pxに揃えた表示用。精密比較の倍率条件としては段階5で再確認が必要）。
- 出力名・保存先・ハッシュ：
  - workspace/character_handoff_check/stage3/stage3_input_trial_01.webp（生成ツールの元ファイル名 media-generation-stage3-input-trial-01-0-8750b9d6-….webp のコピー）
  - 365,220 bytes、WebP 1600×1600、SHA-256 d6d5f94f5dcd83095503cae02612867422ce132641f77e3bdb1220308ea1b6ed
  - GitHubへは保存していない。
- 結果：
  - ①入力の受け付け：成功。ツールは実ファイルを入力として受け付け、エラーなく1枚を生成した。
  - ②入力の反映（大まかな確認）：反映あり。正面顔アップの構図、ローズブラウン系ボブ、赤い瞳、ピンクのタートルネック、画面右の桜ヘアピン大小2輪、無地の明るい背景が、入力と対応する形で出力に現れた。文章だけの指示では通常ここまで構図・小物配置が一致しないため、画像入力が実際に使われたと判断できる。
  - ③細部の差異（観察のみ、段階5の正式評価ではない）：髪色が原本より彩度低めで茶色寄り。髪の輪郭がやや長く・緩く広がる。目や顔の比率にもわずかな違いが見える。人体・周辺物の明らかな破綻や画像内テキストはなし。
  - 顔再現の合格・不合格：ここでは判定しない（段階5で、顔輪郭・頬・目口配置／髪／線と塗り／色彩に分けて正式に比較する）。
- ユーザー評価：未実施（報告後に確認）
- 状態：TRIAL（入力確認用）。正式素材・正式参照への昇格なし。制作参照には使わない。
- 失敗原因の観察と仮説：失敗なし。差異の原因分析は段階5の範囲。
- 次の一手と前回から変える点：段階4では、新しい会話でGitHubの記録だけから原本・直近候補（このTRIALを含む）・採否・次の作業を特定し、原画像と直近候補の取得と実ファイル入力まで再現できるか確認する。なお、このTRIALは現在ローカルのみにあり、GitHub未保存のため、段階4の「GitHubの記録だけから特定」では見つけられない点が論点になる（段階4の実施前に、このTRIALと段階3記録をGitHubの試験用保存先へ残すかどうかをユーザーと決める）。
- 未実施・未確認：段階4、段階5は未実施。マスク付き生成／編集の可否はこのツールでは確認できていない（入力欄なし）。

## 判定

段階3は合格（入力確認として）：再取得した実ファイルを生成ツールの画像入力へ実際に指定でき、出力への反映も確認できた。あわせて、この経路にはマスク入力がないことも確認できた。
