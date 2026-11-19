# GitHub保存時の補足（このファイルの所在）

この記録と成果物は docs/connection-tests/ に次の名前で保存されている：
- 成果物（作業ベース候補・TRIAL）：docs/connection-tests/2026-11-20_local_repair_01_hairpinless.png（PNG 1254×1254、1,597,529 bytes、SHA-256 51436204f1f03f6da04b37c5d7acb956047d8476a39eee2badf7ccc8bd588069）
- 補修部の拡大比較：docs/connection-tests/2026-11-20_local_repair_01_comparison.png
- 本記録：docs/connection-tests/2026-11-20_local_repair_01_record.md
- 状態：ユーザーが「作業ベース候補」と評価（2026-11-20）。正式採用・MASTER・正式参照ではない。原本 characters/aya/03_trials/AYA_ROUND_02_source_candidate.jpeg は無変更。

---

# 局所補修 試行01記録（ROUND 02 ヘアピンなし髪ベース）

実施：2026-11-20（検証完了後の制作試行。ユーザーの「すすめてこ」を受けて実施）
目的：ROUND 02 の直近目標 ― 顔バランスを画素レベルで守ったまま、ヘアピンなしの自然な髪のベースを作る。

## 試行記録（引き継ぎ8章の最小記録形式）

- 試行ID：REPAIR-20261120-01
- 日時：2026-11-20 03:26〜03:28 JST
- 目的：局所編集（領域単位変更：ヘアピン領域のみ）
- 原本：characters/aya/03_trials/AYA_ROUND_02_source_candidate.jpeg（436,348 bytes、1254×1254、SHA-256 b345525922e339443b35ec949a65f3dd1022d490983b7585d462ed861f281924、blob e6bd1e82…）
- 実際に入力した画像：原本から切り出したヘアピン領域の正方形クロップ（座標 x770–1150, y170–550、380×380、crop_hairpin_region.png、SHA-256 67cc669b…6231）。原本全体は生成に入力していない。
  - 花の位置は画像の座標計測で特定：大花は正規化座標 x695–827, y205–342／小花 x750–851, y320–422（1254px換算で大花 x871–1037, y257–429／小花 x940–1067, y401–529）。
- 実行ツール：Museの画像生成ツール（media.generate_image）。マスク入力欄はないため、マスクは合成工程でこちらが定義した。
- ツールへ渡した指示（英語原文）：「Remove the two cherry blossom hairpin flowers from the hair in this image. Fill the area where the flowers were with natural hair that matches the surrounding hair exactly: same rose-red color, same strand direction flowing downward, same highlights and shading, same 2D anime painting style. Keep all other hair, the composition, colors and background in this crop unchanged. No flowers, no accessories, no text.」
- 変更対象／維持対象／マスク：
  - 変更対象：ヘアピン領域（領域単位）。マスクはクロップ座標で角丸矩形 x85–315, y70–372（半径40、ぼかし10px）＝原本座標 x855–1085, y240–542 相当の周辺を含む。
  - 維持対象：マスク外の全画素。
- 実施順序（生成→非生成合成）：（1）領域クロップ →（2）クロップだけを生成入力して髪パッチを生成（1600×1600 WebP）→（3）パッチを380×380へ非生成リサイズ →（4）マスクで原本へ合成（非生成）→（5）差分検証。
  - 過去の試行との違い：全体生成画像から部分を切り出して貼る方式（試行済み7）ではなく、原本の当該領域そのものを生成入力にしたため、色・毛流れ・ハイライトの文脈が領域内で完結する点が異なる。自動補完（telea）・移植・毛束線追加は使っていない。
- 出力：workspace/character_handoff_check/local_repair_01/round02_hairpinless_trial01.png（PNG 1254×1254、1,597,529 bytes、SHA-256 51436204f1f03f6da04b37c5d7acb956047d8476a39eee2badf7ccc8bd588069）。GitHub未保存。原本は無変更。
- 結果：
  - 領域外差分：変更画素 77,780 px（全体の約4.9%）はすべてマスク内に収まり、クロップ外の変更は0、マスク値0の場所の変更も0（最大差分0）。「完全維持」指定の基準（禁止領域の RGBA 差分ゼロ）を満たすことを実測で確認した。なお出力は PNG で保存しており、JPEG で再保存すると再圧縮で全体に差分が出る点に注意。
  - 顔／髪／画風：顔・目・口・頬・タートルネックは画素そのまま（差分ゼロ領域）。花とその影は消え、補修部は下向きの毛流れ・色・ツヤが周囲とつながっている。境界の段差や花の残骸は目視では確認できない。
  - 残る違和感（観察）：拡大すると、補修部中央の毛束は周囲よりやや滑らかで、細い毛束線の密度が少し低い（生成＋縮小の影響と思われる）。通常の表示サイズでは目立たない。
- ユーザー評価：2026-11-20、本チャットで「この出来でアリ、作業ベース候補にして」と評価された。
- 状態：TRIAL のまま、ユーザー指定の「作業ベース候補」（ヘアピンなし髪ベースの候補。ROUND 02 原本が「作業基準候補」であるのと同様、正式採用・MASTER・正式参照への昇格ではない）。今後の制作作業はこの候補を土台にできる。
- 次の一手：ユーザー評価次第。違和感を詰めるなら、毛束の細部密度を上げる方向の再試行（パッチ生成の条件変更）が候補。
