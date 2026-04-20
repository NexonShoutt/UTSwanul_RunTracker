# RunTracker LITE API

RunTracker LITE adalah RESTful API berbasis FastAPI yang dirancang untuk mencatat dan mengelola statistik aktivitas lari. Proyek ini dibangun sebagai tugas Ujian Tengah Semester (UTS) mata kuliah Pemrograman Web Lanjutan.

## Fitur Utama

* **Manajemen Pelari (CRUD):** Pendaftaran akun pelari dan pengambilan data profil.
* **Manajemen Sesi Lari (CRUD):** Pencatatan riwayat lari yang mencakup tanggal, rute, jarak, dan waktu.
* **Relasi Database:** Implementasi relasi *One-to-Many* antara Pelari dan Sesi Lari menggunakan SQLAlchemy.
* **Autentikasi JWT:** Pengamanan endpoint menggunakan JSON Web Token untuk pendaftaran dan login pengguna.
* **Dokumentasi Interaktif:** Dokumentasi API otomatis menggunakan Swagger UI.

## Stack Teknologi

* **Framework:** FastAPI
* **Bahasa Pemrograman:** Python 3.9+
* **ORM:** SQLAlchemy
* **Database:** SQLite
* **Autentikasi:** Jose (JWT) & Passlib (Bcrypt)
* **Validasi Data:** Pydantic v2

## Struktur Proyek

```text
RunTracker_MID/
├── models/             # Model database SQLAlchemy
├── routers/            # Endpoint API modular
├── schemas/            # Skema validasi Pydantic
├── auth.py             # Logika keamanan dan JWT
├── database.py         # Konfigurasi koneksi database
├── main.py             # Entry point aplikasi
├── requirements.txt    # Daftar dependensi Python
└── README.md           # Dokumentasi proyek