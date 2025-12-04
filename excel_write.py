import pandas as pd

df = pd.read_excel("data/sample.xlsx")

df["bmi"] = df["height"] / (df["age"] * 0.1)  # 適当な計算してみる

df.to_excel("data/out_sample.xlsx", index=False, sheet_name="結果")
print("Excel に書き出したよ → data/out_sample.xlsx")
