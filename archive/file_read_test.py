def main() -> None:
    with open("hello.txt", "r", encoding="utf-8") as f:
        text = f.read()

    print("=== ファイルの中身 ===")
    print(text)

if __name__ == "__main__":
    main()
