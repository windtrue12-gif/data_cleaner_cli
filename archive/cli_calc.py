import argparse

def main():
    parser = argparse.ArgumentParser(description="簡単な計算をするCLI")

    # 数字を2つ受け取る
    parser.add_argument("--a", type=float, required=True, help="1つ目の数字")
    parser.add_argument("--b", type=float, required=True, help="2つ目の数字")

    args = parser.parse_args()

    # 足し算
    result = args.a + args.b

    print(f"{args.a} + {args.b} = {result}")

if __name__ == "__main__":
    main()
