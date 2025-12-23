"""
Setup Service - Service untuk inisialisasi dan setup aplikasi
"""

import os
from utils.file_handler import save_json, file_exists, create_directory
from config import CONFIG


class SetupService:
    """Service class untuk setup aplikasi"""
    
    @staticmethod
    def setup_assets():
        """Membuat file asset contoh jika belum ada"""
        print("\n🔧 Memeriksa dan menyiapkan file konfigurasi...")
        
        create_directory(CONFIG["assets_dir"])
        create_directory(CONFIG["soal_path"])
        
        SetupService._setup_mapel()
        SetupService._setup_users()
        SetupService._setup_riwayat()
        
        print("  Konfigurasi selesai!\n")
    
    @staticmethod
    def _setup_mapel():
        """Setup file mapel.json"""
        if not file_exists(CONFIG["mapel_path"]):
            mapel_contoh = [
                {"id": "MTK", "nama": "Matematika"},
                {"id": "IPA", "nama": "IPA"},
                {"id": "IPS", "nama": "IPS"},
                {"id": "BIN", "nama": "Bahasa Indonesia"},
                {"id": "BIG", "nama": "Bahasa Inggris"}
            ]
            if save_json(CONFIG["mapel_path"], mapel_contoh):
                print("    File mapel.json contoh telah dibuat.")
    
    
        
    
    @staticmethod
    def _setup_users():
        """Setup file users.json"""
        if not file_exists(CONFIG["users_path"]):
            if save_json(CONFIG["users_path"], []):
                print("    File users.json telah dibuat.")
    
    @staticmethod
    def _setup_riwayat():
        """Setup file riwayat.json"""
        if not file_exists(CONFIG["riwayat_path"]):
            if save_json(CONFIG["riwayat_path"], []):
                print("    File riwayat.json telah dibuat.")
    
    @staticmethod
    def verify_setup() -> bool:
        """
        Verifikasi apakah semua file yang diperlukan ada
        
        Returns:
            True jika semua file ada
        """
        required_files = [
            CONFIG["mapel_path"],
            CONFIG["users_path"],
            CONFIG["riwayat_path"]
        ]
        
        all_exists = True
        for file_path in required_files:
            if not file_exists(file_path):
                print(f"   Missing: {file_path}")
                all_exists = False
        
        return all_exists