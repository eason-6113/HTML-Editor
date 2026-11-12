# 貢獻指南

修復問題時，請附瀏覽器版本、重現步驟與預期結果。報表範例請使用虛構資料。

1. Fork 本庫，從 `main` 建立分支。
2. 編輯 `index.html`。若操作有變更，同步更新 `guide.html`。
3. 用 Chrome 或 Edge 開啟編輯器，確認報表匯入、修改與匯出流程。另可執行 `python scripts/check_html.py` 檢查 HTML 入口與內嵌 JavaScript，需有 Python 3 和 Node.js。
4. 提交指向本庫 `main` 的 PR，說明修改、驗證結果與已知限制。

編輯器和手冊各自是一個可離線開啟的 HTML 檔。請保留直接開檔使用的方式。涉及存檔或批次同步時，請核對修改範圍、原檔備份與跳過衝突的結果。
