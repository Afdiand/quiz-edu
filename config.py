"""
Konfigurasi aplikasi kuis
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG = {
    "mapel_path": os.path.join(BASE_DIR, "assets", "mapel.json"),
    "soal_path": os.path.join(BASE_DIR, "assets", "soal"),
    "users_path": os.path.join(BASE_DIR, "assets", "users.json"),
    "riwayat_path": os.path.join(BASE_DIR, "assets", "riwayat.json"),
    "assets_dir": os.path.join(BASE_DIR, "assets")
}


TINGKAT_KESULITAN = ["mudah", "sedang", "sulit"]


VALIDATION = {
    "min_username_length": 3,
    "min_password_length": 6
}