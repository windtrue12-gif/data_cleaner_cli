def main() -> None:
    filename = "file_read_test.py"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
            print(text)

    except FileNotFoundError:
        print(f"ファイルが見つからんかったで: {filename}")

    except Exception as e:
        print("予期せぬエラー:", e)


if __name__ == "__main__":
    main()
