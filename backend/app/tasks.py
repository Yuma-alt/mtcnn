from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery("tasks", broker=REDIS_URL, backend=REDIS_URL)

@celery_app.task
def preprocess_image(record_id: int):
    # TODO: DB からレコード取得 → 顔検出／アライメント → TSV 更新 など
    return {"id": record_id, "status": "done"}