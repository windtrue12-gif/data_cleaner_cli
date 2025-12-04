import pandas as pd

df = pd.read_csv("data/sample3.csv", encoding="utf-8")
print("元データ：")
print(df)

# 名前ごとの平均身長
grouped = df.groupby("name")["height"].mean()
print("\n名前ごとの平均身長：")
print(grouped)

# 年齢が高い順にソート
sorted_df = df.sort_values("age", ascending=False)
print("\n年齢が高い順：")
print(sorted_df)
