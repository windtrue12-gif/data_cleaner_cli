def main() -> None:
    # メモ帳みたいなテキストファイルを作って書き込む
    with open("hello.txt", "w", encoding="utf-8") as f:
        f.write("こんにちは、ふうちゃん！\n")
        f.write("with 文でファイル書き込みテスト中。\n")

if __name__ == "__main__":
    main()
