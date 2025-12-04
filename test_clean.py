import pandas as pd

df = pd.read_csv("data/test2.csv", encoding="utf-8")
print("初期データ：")
print(df)

# ① dropna → 欠損値のある行を消す
df = df.dropna()
print("\n欠損を消した：")
print(df)

# ② rename → 列名変更
df = df.rename(columns={"名前": "name", "年齢": "age", "身長": "height"})
print("\n列名を変更した：")
print(df)

# ③ astype → 数値変換
# 身長が "abc" のように数値じゃないとエラーになる（後で例外処理に進む）
df["age"] = df["age"].astype(int)
print("\nage を整数に変換した：")
print(df)
