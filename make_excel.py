import pandas as pd

data = {
    "name": ["Fuma", "Hana", "Kuro"],
    "age": [30, 22, 25],
    "height": [170, 160, 180],
}

df = pd.DataFrame(data)
df.to_excel("data/sample.xlsx", index=False, sheet_name="Sheet1")

print("data/sample.xlsx を作ったよ")
