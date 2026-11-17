# 生成画像のGitHubバイナリアップロード検証（2026-11-18）

## 検証結果
- **成功**：ChatGPTの画像生成で作ったロボットイラストを縮小した **96×96ピクセルのPNG** をGitHubへ新規保存。
- 本検証で保存したファイル：`docs/connection-tests/2026-11-18_generated_robot_thumbnail_96.png`
- 作成元：同会話で生成したテスト用ロボットイラスト（オリジナル1254×1254 PNG）。
- GitHubでの登録方法：GitHub Blob API（base64転送）→Tree作成→Commit作成→main更新。
- 画像のコミット：`bd42d1cc6af5be69f9760d06c9f910223ab5577e`
- GitHubのtreeで対象ファイルが **2887 bytes**、blob SHA `a577a764eb56e854e72d7adc478a3e3b3eaf9cd2` として存在することを確認。
- ローカル96×96 PNGのGit blob SHAも `a577a764eb56e854e72d7adc478a3e3b3eaf9cd2` で一致：**画像バイト列の同一性確認済み**。
- 既存の正式画像・manifest・MASTERは変更していない。

## できたこと／残る制約
- テキスト以外の実バイナリ（PNG）をGitHubのリポジトリへ書き込めることを確認した。
- GitHub連携のテキスト取得ツールはPNGをUTF-8として読もうとしてエラーを返す。このエラーはアップロード失敗を意味せず、バイナリをテキスト専用取得で開けない制限を示す。
- **元の1254×1254画像は未アップロード**。今回の転送可能性のテストは96×96へ縮小したコピーで実施した。
- GitHub PNGの保存と、ChatGPT画像生成モデルがGitHub上のPNGを直接参照して生成できることは別機能。後者は未検証。
- 今後の大きなPNGの転送は別途、対応するファイル入力経路とサイズ制約を検証する。画像がGitHubへ登録済みとする際はpath、blob SHA、commit SHAを記録する。
