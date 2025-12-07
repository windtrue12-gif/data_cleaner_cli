from pathlib import Path
from loguru import logger
import datetime

def setup_logger():
    # logsフォルダ作成
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # 今日の日付ログファイル
    today = datetime.date.today().strftime("%Y-%m-%d")
    log_file = log_dir / f"{today}.log"

    logger.add(
        log_file,
        rotation="1 day",
        encoding="utf-8",
        retention="7 days",   # 7日で自動削除（お好み）
        level="INFO"
    )

    return logger
