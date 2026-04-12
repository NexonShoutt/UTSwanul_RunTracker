from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Pelari(Base):
    __tablename__ = "pelari"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # relasi One-to-Many ke sesi lari
    sesi_lari = relationship("SesiLari", back_populates="pemilik")

class SesiLari(Base):
    __tablename__ = "sesi_lari"

    id = Column(Integer, primary_key=True, index=True)
    tanggal = Column(Date)
    rute = Column(String)
    jarak_km = Column(Float)
    total_waktu_menit = Column(Float)
    pelari_id = Column(Integer, ForeignKey("pelari.id"))

    # balikan relasi ke Pelari
    pemilik = relationship("Pelari", back_populates="sesi_lari")