import argparse
import csv
import os

def main():
    parser = argparse.ArgumentParser(description="フォルダ内のCSVを結合するCLIツール")

    parser.add_argument("input_dir", type=str, help="結合したいCSVが入ったフォルダ")
    parser.add_argument("output_file", type=str, help="出力するCSVファイル名")
    parser.add_argument("--verbose", action="store_true", help="詳細ログを表示する")

    args = parser.parse_args()

    input_dir = args.input_dir
    output_file = args.output_file

    # フォルダ内のCSVファイルを取得
    files = [
        f for f in os.listdir(input_dir)
        if f.lower().endswith(".csv")
    ]

    if args.verbose:
        print("読み込むファイル：")
        for f in files:
            print("  -", f)

    if not files:
        print("CSVが見つかりませんでした…")
        return

    merged_rows = []
    header = None

    # 1つずつCSVを読み込んで結合
    for csv_file in files:
        path = os.path.join(input_dir, csv_file)

        with open(path, "r", encoding="CP932", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)

            if header is None:
                header = rows[0]  # 最初のCSVのヘッダーだけ使う
                merged_rows.append(header)

            # 2行目以降（データ行）だけ追加
            merged_rows.extend(rows[1:])

    # 結合したCSVを書き込み
    with open(output_file, "w", encoding="CP932", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(merged_rows)

    print(f"結合完了！ → {output_file}")

if __name__ == "__main__":
    main()
