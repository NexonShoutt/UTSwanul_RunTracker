from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import run as models
from schemas import run as schemas

# Ini buat misahin endpoint khusus /pelari
router = APIRouter(
    prefix="/pelari",
    tags=["Pelari"]
)

# Endpoint buat CREATE pelari baru
@router.post("/", response_model=schemas.PelariResponse)
def create_pelari(pelari: schemas.PelariCreate, db: Session = Depends(get_db)):
    # Validasi: Cek email udah dipake apa belom
    db_pelari = db.query(models.Pelari).filter(models.Pelari.email == pelari.email).first()
    if db_pelari:
        raise HTTPException(status_code=400, detail="Email udah terdaftar bos!")

    # Bikin record baru (passwordnya kita simpen plain dulu sementara sebelum masuk materi JWT)
    new_pelari = models.Pelari(
        username=pelari.username,
        email=pelari.email,
        hashed_password=pelari.password 
    )
    db.add(new_pelari)
    db.commit()
    db.refresh(new_pelari)
    return new_pelari

# Endpoint buat READ semua data pelari
@router.get("/", response_model=list[schemas.PelariResponse])
def get_semua_pelari(db: Session = Depends(get_db)):
    return db.query(models.Pelari).all()