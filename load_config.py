import json
from pathlib import Path

CONFIG_PATH = Path("config.json")

def load_config() -> dict:
    """config.json を読み込んで dict で返す"""
    text = CONFIG_PATH.read_text(encoding="utf-8")
    config = json.loads(text)
    return config

def main():
    config = load_config()
    print("設定を読み込みました：")
    print(f"  input_path : {config['input_path']}")
    print(f"  output_path: {config['output_path']}")
    print(f"  min_age    : {config['min_age']}")

if __name__ == "__main__":
    main()
