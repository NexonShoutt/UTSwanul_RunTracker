from fastapi import FastAPI
from database import engine, Base
from models import run as models
from routers import pelari
from routers import sesi_lari

# Ini command buat nge-generate tabel SQLite otomatis berdasarkan models/run.py
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RunTracker LITE API",
    description="API untuk merekam statistik sesi lari (Project UTS Web Lanjutan)",
    version="1.0.0"
)

app.include_router(pelari.router)
app.include_router(sesi_lari.router)

@app.get("/")
def root_check():
    return {"message": "Server RunTracker LITE nyala bos! Cek /docs buat Swagger UI."}