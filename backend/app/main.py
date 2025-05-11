from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware
from . import models


# テーブル作成
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB セッションを取得する Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# 例：画像レコード一覧取得
@app.get("/images/")
def list_images(db: Session = Depends(get_db)):
    return db.query(models.ImageRecord).all()