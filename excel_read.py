import pandas as pd
from logger_setup import setup_logger
logger = setup_logger()

logger.info("Excel 読み込み開始")
df = pd.read_excel("data/sample.xlsx", engine="openpyxl")
print(df)
logger.info(f"読み込み行数: {len(df)}")