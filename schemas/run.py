from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date

# SCHEMAS BUAT SESI LARI
class SesiLariBase(BaseModel):
    tanggal: date
    rute: str
    jarak_km: float
    total_waktu_menit: float

class SesiLariCreate(SesiLariBase):
    pass

class SesiLariResponse(SesiLariBase):
    id: int
    pelari_id: int

    model_config = ConfigDict(from_attributes=True)


# SCHEMAS BUAT PELARI
class PelariBase(BaseModel):
    username: str
    email: str

class PelariCreate(PelariBase):
    password: str

class PelariResponse(PelariBase):
    id: int
    # relasi One-to-Many nya ditarik ke sini
    sesi_lari: List[SesiLariResponse] = []

    model_config = ConfigDict(from_attributes=True)