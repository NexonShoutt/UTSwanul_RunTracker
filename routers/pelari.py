from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import run as models
from schemas import run as schemas
import auth 

router = APIRouter(prefix="/pelari", tags=["Pelari"])

@router.post("/register", response_model=schemas.PelariResponse)
def create_pelari(pelari: schemas.PelariCreate, db: Session = Depends(get_db)):
    db_pelari = db.query(models.Pelari).filter(models.Pelari.email == pelari.email).first()
    if db_pelari:
        raise HTTPException(status_code=400, detail="Email udah terdaftar bos!")

    # hash
    hashed_pwd = auth.get_password_hash(pelari.password)
    
    new_pelari = models.Pelari(
        username=pelari.username,
        email=pelari.email,
        hashed_password=hashed_pwd 
    )
    db.add(new_pelari)
    db.commit()
    db.refresh(new_pelari)
    return new_pelari

@router.get("/", response_model=list[schemas.PelariResponse])
def get_semua_pelari(db: Session = Depends(get_db)):
    return db.query(models.Pelari).all()

# ENDPOINT VVIP BJIR (TERPROTEKSI JWT)
@router.get("/me", response_model=schemas.PelariResponse)
def get_profil_sendiri(current_user: models.Pelari = Depends(auth.get_current_user)):
    # data user yg on
    return current_user