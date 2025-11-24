import argparse
import os
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="pandasでCSVを高速結合するCLI")

    parser.add_argument("input_dir", type=str, help="結合したいCSVが入ったフォルダ")
    parser.add_argument("output_file", type=str, help="出力するCSVファイル名")
    parser.add_argument("--verbose", action="store_true", help="読み込むファイル一覧を表示する")

    args = parser.parse_args()

    input_dir = args.input_dir
    output_file = args.output_file

    # フォルダ内のCSVを列挙
    files = [
        os.path.join(input_dir, f)
        for f in os.listdir(input_dir)
        if f.lower().endswith(".csv")
    ]

    if len(files) == 0:
        print("CSVが見つかりませんでした。")
        return

    if args.verbose:
        print("読み込むCSV：")
        for f in files:
            print("  -", f)

    # すべてのCSVをDataFrame化してまとめる
    dfs = []
    for file in files:
        try:
            df = pd.read_csv(file, encoding="cp932")
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding="utf-8-sig")
        dfs.append(df)

    merged = pd.concat(dfs, ignore_index=True)

    # 出力（UTF-8でOK）
    merged.to_csv(output_file, index=False, encoding="utf-8")

    print(f"結合完了！ → {output_file}")

if __name__ == "__main__":
    main()
