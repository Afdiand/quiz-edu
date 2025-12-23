"""
Model Pengguna - Mengelola data dan autentikasi pengguna
"""

from typing import List, Dict, Optional
from datetime import datetime
from utils.file_handler import get_json, save_json
from utils.validators import validasi_email, validasi_password, validasi_username
from config import CONFIG, VALIDATION
from .riwayat import Riwayat


class Pengguna:
    """Class untuk mengelola pengguna"""
    
    def __init__(self, username: str = "", email: str = "", password: str = ""):
        """
        Inisialisasi pengguna
        
        Args:
            username: Nama pengguna
            email: Alamat email
            password: Password
        """
        self.__username = username
        self.__email = email
        self.__password = password
        self.__is_logged_in = False
        self.riwayat_user: List[Riwayat] = []

    @staticmethod
    def _load_users() -> List[Dict]:
        """Load semua user dari file"""
        return get_json(CONFIG["users_path"]) or []

    @staticmethod
    def _save_users(users: List[Dict]) -> bool:
        """Simpan semua user ke file"""
        return save_json(CONFIG["users_path"], users)

    def signUp(self, username: str, email: str, password: str) -> bool:
        """
        Mendaftarkan akun baru
        
        Args:
            username: Nama pengguna
            email: Alamat email
            password: Password
            
        Returns:
            True jika berhasil, False jika gagal
        """
        
        is_valid, msg = validasi_username(username, VALIDATION["min_username_length"])
        if not is_valid:
            print(f"  {msg}")
            return False
        
        if not validasi_email(email):
            print("  Format email tidak valid.")
            return False
        
        is_valid, msg = validasi_password(password, VALIDATION["min_password_length"])
        if not is_valid:
            print(f"  {msg}")
            return False
        
        users = self._load_users()
        for user in users:
            if user.get("email") == email:
                print("  Email sudah terdaftar.")
                return False
            if user.get("username") == username:
                print("  Username sudah digunakan.")
                return False
        
        new_user = {
            "username": username,
            "email": email,
            "password": password,  
            "created_at": datetime.now().isoformat()
        }
        users.append(new_user)
        
        if self._save_users(users):
            self.__username = username
            self.__email = email
            self.__password = password
            print(f"  Akun '{username}' berhasil didaftarkan!")
            return True
        
        return False

    def login(self, email: str, password: str) -> bool:
        """
        Login ke akun
        
        Args:
            email: Alamat email
            password: Password
            
        Returns:
            True jika berhasil, False jika gagal
        """
        if not email or not password:
            print("  Email dan password harus diisi.")
            return False
        
        users = self._load_users()
        
        for user in users:
            if user.get("email") == email and user.get("password") == password:
                self.__username = user.get("username", "")
                self.__email = email
                self.__password = password
                self.__is_logged_in = True
                print(f"  Login berhasil! Selamat datang, {self.__username}!")
                return True
        
        print("  Email atau password salah.")
        return False

    def forgetPassword(self, email: str) -> bool:
        """
        Simulasi reset password
        
        Args:
            email: Alamat email yang terdaftar
            
        Returns:
            True jika email ditemukan
        """
        users = self._load_users()
        
        for user in users:
            if user.get("email") == email:
                print(f"   Link reset password telah dikirim ke {email}")
                return True
        
        print("  Email tidak terdaftar.")
        return False

    def logOut(self):
        """Logout dari akun"""
        if self.__is_logged_in:
            print(f"  Sampai jumpa, {self.__username}!")
            self.__is_logged_in = False
            self.__username = ""
            self.__email = ""
            self.__password = ""
        else:
            print("    Tidak ada user yang login.")

    def changePassword(self, old_password: str, new_password: str) -> bool:
        """
        Mengubah password
        
        Args:
            old_password: Password lama
            new_password: Password baru
            
        Returns:
            True jika berhasil
        """
        if not self.__is_logged_in:
            print("  Silakan login terlebih dahulu.")
            return False
        
        if old_password != self.__password:
            print("  Password lama salah.")
            return False
        
        is_valid, msg = validasi_password(new_password, VALIDATION["min_password_length"])
        if not is_valid:
            print(f"  {msg}")
            return False
        
        users = self._load_users()
        for user in users:
            if user.get("email") == self.__email:
                user["password"] = new_password
                break
        
        if self._save_users(users):
            self.__password = new_password
            print("  Password berhasil diubah.")
            return True
        
        return False

    def is_logged_in(self) -> bool:
        """Cek apakah user sudah login"""
        return self.__is_logged_in
    
    def get_username(self) -> str:
        """Mendapatkan username"""
        return self.__username
    
    def get_email(self) -> str:
        """Mendapatkan email"""
        return self.__email

    def lihat_riwayat(self):
        """Melihat riwayat kuis user ini"""
        if not self.__is_logged_in:
            print("  Silakan login terlebih dahulu.")
            return
        Riwayat.tampilSemuaRiwayat(self.__username)
    
    def to_dict(self) -> Dict:
        """Convert user ke dictionary (tanpa password)"""
        return {
            "username": self.__username,
            "email": self.__email,
            "is_logged_in": self.__is_logged_in
        }