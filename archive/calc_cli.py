import argparse

def main() -> None:
    # メインのパーサー
    parser = argparse.ArgumentParser(description="四則演算をするCLIツール")

    # 共通オプション（どのコマンドでも使える）
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="計算の式も表示する",
    )

    # サブコマンド(add, sub, mul, div)を登録するための器
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,  # 何かしらサブコマンドを必須にする
    )

    # ---------- add コマンド ----------
    add_parser = subparsers.add_parser("add", help="足し算をする")
    add_parser.add_argument("a", type=float, help="1つ目の数字")
    add_parser.add_argument("b", type=float, help="2つ目の数字")

    # ---------- sub コマンド ----------
    sub_parser = subparsers.add_parser("sub", help="引き算をする")
    sub_parser.add_argument("a", type=float, help="1つ目の数字")
    sub_parser.add_argument("b", type=float, help="2つ目の数字")

    # ---------- mul コマンド ----------
    mul_parser = subparsers.add_parser("mul", help="掛け算をする")
    mul_parser.add_argument("a", type=float, help="1つ目の数字")
    mul_parser.add_argument("b", type=float, help="2つ目の数字")

    # ---------- div コマンド ----------
    div_parser = subparsers.add_parser("div", help="割り算をする")
    div_parser.add_argument("a", type=float, help="1つ目の数字")
    div_parser.add_argument("b", type=float, help="2つ目の数字")

    # ここで全部の引数をまとめて解析
    args = parser.parse_args()

    # サブコマンドごとに処理を分岐
    if args.command == "add":
        result = args.a + args.b
        op = "+"
    elif args.command == "sub":
        result = args.a - args.b
        op = "-"
    elif args.command == "mul":
        result = args.a * args.b
        op = "*"
    elif args.command == "div":
        result = args.a / args.b
        op = "/"
    else:
        parser.error("未知のコマンドです")

    # verbose フラグが付いてたら式も出す
    if args.verbose:
        print(f"{args.a} {op} {args.b} = {result}")
    else:
        print(result)

if __name__ == "__main__":
    main()
