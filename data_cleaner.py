import pandas as pd
from logger_setup import setup_logger
import argparse

logger = setup_logger()

parser = argparse.ArgumentParser()
parser.add_argument("--src", required=True)
parser.add_argument("--dst", required=True)
parser.add_argument("--min-age", type=int, default=30)
args = parser.parse_args()

def clean_data(df, min_age):
    df = df.dropna()
    df = df[df["age"] >= min_age]
    df["age"] = df["age"].astype(int)
    df = df.sort_values("age", ascending=False)
    return df

def read_excel(path):
    logger.info("Excel 読み込み開始")
    df = pd.read_excel(path, engine="openpyxl")
    print(df)
    logger.info(f"読み込み行数: {len(df)}")
    return df

def write_excel(df, path):
    df.to_excel(path, index=False)

def main():
    try:
        logger.info("data_cleaner 開始")
        df = read_excel(args.src)
        df_clean = clean_data(df, args.min_age)
        write_excel(df_clean, args.dst)
        logger.info("data_cleaner 正常終了")

    except FileNotFoundError as e:
        logger.error(f"ファイルが見つかりません: {e.filename}")
        print(f"エラー: 入力ファイルが見つからんかったで → {e.filename}")

    except Exception as e:
        # ここでスタックトレース付きで全部ログに残す
        logger.exception("想定外のエラーが発生しました")
        print(f"想定外のエラーが起きたっぽい…: {e}")

if __name__ == "__main__":
    main()
