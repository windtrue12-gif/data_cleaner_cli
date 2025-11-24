from pathlib import Path
data_dir = Path("data")
files = list(data_dir.glob("*.csv"))
print(files)