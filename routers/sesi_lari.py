from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import run as models
from schemas import run as schemas

router = APIRouter(
    prefix="/sesi-lari",
    tags=["Sesi Lari"]
)

# endpoint buat tambah sesi lari ke pelari tertentu
@router.post("/{pelari_id}", response_model=schemas.SesiLariResponse)
def create_sesi_lari(pelari_id: int, sesi: schemas.SesiLariCreate, db: Session = Depends(get_db)):
    # Cek dulu, pelarinya ada beneran gak di database
    db_pelari = db.query(models.Pelari).filter(models.Pelari.id == pelari_id).first()
    if not db_pelari:
        raise HTTPException(status_code=404, detail="Waduh, pelari nggak ketemu bos!")

    # Kalo ada, kita masukin data larinya dan sambungin ke ID pelari
    # .model_dump() ini fitur Pydantic v2 buat ngekstrak dictionary
    new_sesi = models.SesiLari(**sesi.model_dump(), pelari_id=pelari_id)
    
    db.add(new_sesi)
    db.commit()
    db.refresh(new_sesi)
    return new_sesi

# Endpoint buat ngeliat semua sesi lari dari semua orang
@router.get("/", response_model=list[schemas.SesiLariResponse])
def get_semua_sesi(db: Session = Depends(get_db)):
    return db.query(models.SesiLari).all()

# Endpoint buat UPDATE sesi lari (PUT)
@router.put("/{sesi_id}", response_model=schemas.SesiLariResponse)
def update_sesi_lari(sesi_id: int, sesi_update: schemas.SesiLariCreate, db: Session = Depends(get_db)):
    # Cari dulu datanya ada apa nggak
    db_sesi = db.query(models.SesiLari).filter(models.SesiLari.id == sesi_id).first()
    if not db_sesi:
        raise HTTPException(status_code=404, detail="Data lari nggak ketemu bos!")
    
    # Kalo ada, kita timpa pake data baru dari user
    db_sesi.tanggal = sesi_update.tanggal
    db_sesi.rute = sesi_update.rute
    db_sesi.jarak_km = sesi_update.jarak_km
    db_sesi.total_waktu_menit = sesi_update.total_waktu_menit
    
    db.commit()
    db.refresh(db_sesi)
    return db_sesi

# Endpoint buat DELETE sesi lari
@router.delete("/{sesi_id}")
def delete_sesi_lari(sesi_id: int, db: Session = Depends(get_db)):
    db_sesi = db.query(models.SesiLari).filter(models.SesiLari.id == sesi_id).first()
    if not db_sesi:
        raise HTTPException(status_code=404, detail="Data lari nggak ketemu bos!")
    
    db.delete(db_sesi)
    db.commit()
    return {"message": "Sesi lari berhasil dihapus dari muka bumi"}