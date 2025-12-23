"""
Aplikasi Kuis - Controller utama aplikasi
"""

from typing import Optional
from models import MataPelajaran, SesiKuis, Pengguna, Riwayat
from utils.validators import validasi_input_int, validasi_input_str
from services.soal_service import SoalService


class AplikasiKuis:
    """Controller utama aplikasi kuis"""
    
    def __init__(self):
        """Inisialisasi aplikasi"""
        self.pengguna = Pengguna()
        self.mapel = MataPelajaran()
        self.sesi_kuis: Optional[SesiKuis] = None
    
    def tampil_header(self):
        """Menampilkan header aplikasi"""
        print("\n" + "=" * 50)
        print("        APLIKASI KUIS PEMBELAJARAN  ")
        print("=" * 50)
    
    def run(self):
        """Menjalankan aplikasi (alias untuk menu_utama)"""
        self.menu_utama()
    
    def menu_utama(self):
        """Menu utama aplikasi"""
        while True:
            self.tampil_header()
            
            if self.pengguna.is_logged_in():
                result = self._menu_logged_in()
            else:
                result = self._menu_guest()
            
            if result == "exit":
                print("\n  Terima kasih telah menggunakan aplikasi!")
                break
    
    def _menu_logged_in(self) -> Optional[str]:
        """Menu untuk user yang sudah login"""
        print(f"\n    Login sebagai: {self.pengguna.get_username()}")
        print("\n  MENU:")
        print("  1.   Mulai Kuis")
        print("  2.   Lihat Riwayat")
        print("  3.   Lihat Daftar Mapel")
        print("  4.   Ubah Password")
        print("  5.   Logout")
        print("  0.   Keluar")
        
        pilihan = validasi_input_int("\n  Pilihan Anda: ", 0, 5)
        
        if pilihan == 0:
            return "exit"
        elif pilihan == 1:
            self.menu_mulai_kuis()
        elif pilihan == 2:
            self.pengguna.lihat_riwayat()
            input("\nTekan Enter untuk melanjutkan...")
        elif pilihan == 3:
            self._tampil_info_mapel()
            input("\nTekan Enter untuk melanjutkan...")
        elif pilihan == 4:
            self.menu_ubah_password()
        elif pilihan == 5:
            self.pengguna.logOut()
        
        return None
    
    def _menu_guest(self) -> Optional[str]:
        """Menu untuk guest (belum login)"""
        print("\n  MENU:")
        print("  1.   Login")
        print("  2.   Daftar Akun")
        print("  3.   Lupa Password")
        print("  4.   Lihat Daftar Mapel")
        print("  0.   Keluar")
        
        pilihan = validasi_input_int("\n  Pilihan Anda: ", 0, 4)
        
        if pilihan == 0:
            return "exit"
        elif pilihan == 1:
            self.menu_login()
        elif pilihan == 2:
            self.menu_daftar()
        elif pilihan == 3:
            self.menu_lupa_password()
        elif pilihan == 4:
            self.mapel.tampilDaftarMapel()
            input("\nTekan Enter untuk melanjutkan...")
        
        return None
    
    def menu_login(self):
        """Menu login"""
        print("\n" + "-" * 30)
        print("        LOGIN")
        print("-" * 30)
        
        email = validasi_input_str("  Email    : ")
        if not email:
            return
        
        password = validasi_input_str("  Password : ")
        if not password:
            return
        
        self.pengguna.login(email, password)
    
    def menu_daftar(self):
        """Menu pendaftaran"""
        print("\n" + "-" * 30)
        print("        DAFTAR AKUN")
        print("-" * 30)
        
        username = validasi_input_str("  Username (min 3 char): ", 3)
        if not username:
            return
        
        email = validasi_input_str("  Email: ")
        if not email:
            return
        
        password = validasi_input_str("  Password (min 6 char): ", 6)
        if not password:
            return
        
        self.pengguna.signUp(username, email, password)
    
    def menu_lupa_password(self):
        """Menu lupa password"""
        print("\n" + "-" * 30)
        print("        LUPA PASSWORD")
        print("-" * 30)
        
        email = validasi_input_str("  Masukkan email terdaftar: ")
        if email:
            self.pengguna.forgetPassword(email)
    
    def menu_ubah_password(self):
        """Menu ubah password"""
        print("\n" + "-" * 30)
        print("        UBAH PASSWORD")
        print("-" * 30)
        
        old_pass = validasi_input_str("  Password lama: ")
        if not old_pass:
            return
        
        new_pass = validasi_input_str("  Password baru (min 6 char): ", 6)
        if not new_pass:
            return
        
        confirm_pass = validasi_input_str("  Konfirmasi password baru: ")
        if not confirm_pass:
            return
        
        if new_pass != confirm_pass:
            print("  Password baru tidak cocok.")
            return
        
        self.pengguna.changePassword(old_pass, new_pass)
    
    def _tampil_info_mapel(self):
        """Menampilkan info mata pelajaran dan soal yang tersedia"""
        self.mapel.tampilDaftarMapel()
        
        print("\n  SOAL YANG TERSEDIA:")
        print("-" * 40)
        
        available = SoalService.get_available_mapel()
        if not available:
            print("  Belum ada soal yang tersedia.")
            return
        
        for mapel_name in available:
            tingkat_list = SoalService.get_tingkat_tersedia(mapel_name)
            print(f"\n    {mapel_name}:")
            for tingkat in tingkat_list:
                count = SoalService.count_soal(mapel_name, tingkat)
                print(f"     - {tingkat.capitalize()}: {count} soal")
    
    def menu_mulai_kuis(self):
        """Menu untuk memulai kuis"""
        print("\n" + "-" * 40)
        print("            MULAI KUIS")
        print("-" * 40)
        
        self.mapel.reset()
        self.mapel.tampilDaftarMapel()
        daftar = self.mapel.getDaftarMapel()
        
        if not daftar:
            print("  Tidak ada mata pelajaran tersedia.")
            input("\nTekan Enter untuk kembali...")
            return
        
        idx = validasi_input_int(f"\n  Pilih mapel (0-{len(daftar)-1}): ", 0, len(daftar)-1)
        if idx is None:
            return
        
        if not self.mapel.pilihMapelByIndex(idx):
            input("\nTekan Enter untuk kembali...")
            return
        
        tingkat_tersedia = SoalService.get_tingkat_tersedia(self.mapel.get_info())
        if not tingkat_tersedia:
            print(f"  Tidak ada soal untuk mata pelajaran '{self.mapel.get_info()}'.")
            input("\nTekan Enter untuk kembali...")
            return
        
        print("\n    TINGKAT KESULITAN:")
        tingkat_map = {}
        for i, tingkat in enumerate(tingkat_tersedia, 1):
            count = SoalService.count_soal(self.mapel.get_info(), tingkat)
            emoji = {"mudah": "🟢", "sedang": "🟡", "sulit": "🔴"}.get(tingkat, "⚪")
            print(f"  {i}. {emoji} {tingkat.capitalize()} ({count} soal)")
            tingkat_map[i] = tingkat
        
        tingkat_idx = validasi_input_int(f"\n  Pilih tingkat (1-{len(tingkat_tersedia)}): ", 1, len(tingkat_tersedia))
        
        if tingkat_idx is None:
            return
        
        tingkat = tingkat_map[tingkat_idx]
        
        self.sesi_kuis = SesiKuis(self.mapel)
        
        if not self.sesi_kuis.setKesulitan(tingkat):
            input("\nTekan Enter untuk kembali...")
            return
        
        konfirmasi = input("\n  Siap memulai kuis? (y/n): ").strip().lower()
        if konfirmasi != 'y':
            print("  Kuis dibatalkan.")
            return
        
        self.sesi_kuis.jalankan_kuis_interaktif(self.pengguna.get_username())
        
        input("\nTekan Enter untuk kembali ke menu...")