import pandas as pd

# CSVを読む
df = pd.read_csv("data/test.csv", encoding="utf-8")
print("読み込んだデータ：")
print(df)

# CSVに書き出す
df.to_csv("data/out_test.csv", index=False, encoding="utf-8")
print("書き出し完了！ → data/out_test.csv")
