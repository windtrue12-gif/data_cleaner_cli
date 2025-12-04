# data_cleaner_cli

簡単なデータクレンジング用の CLI ツール。  
Excel / CSV からデータを読み込み、条件で抽出して整形し、別ファイルに出力します。

---

## 必要環境

- Python 3.13
- 仮想環境（uv / venv どちらでも）
- インストールしているライブラリ
  - pandas
  - openpyxl
  - loguru

※ `uv` を使っている場合は以下のコマンドでインストール済み：

```bash
uv add pandas openpyxl loguru
