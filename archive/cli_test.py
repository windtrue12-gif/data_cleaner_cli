import argparse

def main():
    # ① 引数を受け取るための“器”
    parser = argparse.ArgumentParser(description="最初のCLIテスト")

    # ② --name という引数を追加
    parser.add_argument("--name", type=str, required=True, help="名前を入力してね")

    # ③ コマンドラインから値を読み取る
    args = parser.parse_args()

    # ④ 受け取った引数を使う
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
