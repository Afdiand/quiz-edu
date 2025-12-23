"""
Model SesiKuis - Mengelola sesi kuis
"""

from typing import List, Optional, TYPE_CHECKING
from .mata_pelajaran import MataPelajaran
from .soal import Soal
from .skor import Skor
from .riwayat import Riwayat
from config import TINGKAT_KESULITAN

if TYPE_CHECKING:
    from services.soal_service import SoalService


class SesiKuis:
    """Class untuk mengelola sesi kuis"""
    
    TINGKAT_VALID = TINGKAT_KESULITAN
    
    def __init__(self, mapel_obj: MataPelajaran):
        """
        Inisialisasi sesi kuis
        
        Args:
            mapel_obj: Object MataPelajaran yang sudah dipilih
        """
        self.__tingkatKesulitan: str = ""
        self.__indeksSoalSaatIni: int = 0
        self.__daftarJawabanUser: List[int] = []
        self.__sedang_berjalan: bool = False

        self.mataPelajaran = mapel_obj
        self.daftarSoal: List[Soal] = []
        self.skor = Skor()

    def __dapatkan_soal(self, kesulitan: str) -> bool:
        """Mengambil soal dari service"""
        from services.soal_service import SoalService
        
        if not self.mataPelajaran.is_selected():
            print("  Mata pelajaran belum dipilih.")
            return False
        
        self.daftarSoal = SoalService.get_soal(kesulitan, self.mataPelajaran.get_info())
        return len(self.daftarSoal) > 0

    def setKesulitan(self, level: str) -> bool:
        """
        Set tingkat kesulitan kuis
        
        Args:
            level: Tingkat kesulitan (mudah/sedang/sulit)
            
        Returns:
            True jika berhasil, False jika gagal
        """
        level = level.lower().strip()
        
        if level not in self.TINGKAT_VALID:
            print(f"   Tingkat kesulitan tidak valid.")
            print(f"   Pilihan: {', '.join(self.TINGKAT_VALID)}")
            return False
        
        self.__tingkatKesulitan = level
        
        if self.__dapatkan_soal(self.__tingkatKesulitan):
            print(f"   Tingkat kesulitan '{level}' dipilih. ({len(self.daftarSoal)} soal)")
            return True
        else:
            print("   Gagal memuat soal.")
            return False

    def mulaiKuis(self) -> bool:
        """
        Memulai sesi kuis
        
        Returns:
            True jika berhasil dimulai
        """
        if not self.daftarSoal:
            print("   Tidak ada soal untuk dikerjakan.")
            return False
        
        self.__sedang_berjalan = True
        self.__indeksSoalSaatIni = 0
        self.__daftarJawabanUser = []
        
        print("\n" + "=" * 40)
        print("           KUIS DIMULAI!")
        print("=" * 40)
        print(f"     Mapel     : {self.mataPelajaran.get_info()}")
        print(f"     Kesulitan : {self.__tingkatKesulitan}")
        print(f"     Jumlah    : {len(self.daftarSoal)} soal")
        print("=" * 40)
        print("\nKetik nomor jawaban (0, 1, 2, ...) untuk menjawab")
        print("Ketik 'q' untuk keluar\n")
        
        return True

    def tampilSoal(self) -> bool:
        """
        Menampilkan soal saat ini
        
        Returns:
            True jika berhasil menampilkan soal
        """
        if not self.__sedang_berjalan:
            print("  Kuis belum dimulai.")
            return False
            
        if self.__indeksSoalSaatIni >= len(self.daftarSoal):
            print("    Tidak ada soal lagi.")
            return False
        
        try:
            soal_aktif = self.daftarSoal[self.__indeksSoalSaatIni]
            total = len(self.daftarSoal)
            
            print(f"\n╔{'═' * 48}╗")
            print(f"║    SOAL {self.__indeksSoalSaatIni + 1} dari {total}".ljust(50) + "║")
            print(f"╠{'═' * 48}╣")
            
            pertanyaan = soal_aktif.get_pertanyaan()
            if len(pertanyaan) > 46:
                print(f"║  {pertanyaan[:43]}...".ljust(50) + "║")
            else:
                print(f"║  {pertanyaan}".ljust(50) + "║")
            
            print(f"╠{'═' * 48}╣")
            
            opsi = soal_aktif.get_opsi()
            for idx, text in enumerate(opsi):
                huruf = chr(65 + idx) 
                opsi_text = f"    {idx}. ({huruf}) {text[:40]}"
                print(f"║{opsi_text}".ljust(50) + "║")
            
            print(f"╚{'═' * 48}╝")
            return True
            
        except Exception as e:
            print(f"  Error menampilkan soal: {e}")
            return False

    def inputJawaban(self, jawaban_idx: int) -> bool:
        """
        Menyimpan jawaban user
        
        Args:
            jawaban_idx: Index jawaban yang dipilih
            
        Returns:
            True jika valid, False jika tidak
        """
        if not self.__sedang_berjalan:
            print("  Kuis belum dimulai.")
            return False
            
        if self.__indeksSoalSaatIni >= len(self.daftarSoal):
            print("  Tidak ada soal aktif.")
            return False
        
        soal_aktif = self.daftarSoal[self.__indeksSoalSaatIni]
        max_idx = soal_aktif.get_jumlah_opsi() - 1
        
        if not (0 <= jawaban_idx <= max_idx):
            print(f"  Jawaban tidak valid. Pilih antara 0-{max_idx}")
            return False
        
        self.__daftarJawabanUser.append(jawaban_idx)
        return True

    def nextSoal(self) -> bool:
        """
        Pindah ke soal berikutnya
        
        Returns:
            True jika masih ada soal, False jika sudah selesai
        """
        if not self.__sedang_berjalan:
            return False
            
        self.__indeksSoalSaatIni += 1
        
        if self.__indeksSoalSaatIni >= len(self.daftarSoal):
            self.__selesaikanSesi()
            return False
        else:
            self.tampilSoal()
            return True

    def __selesaikanSesi(self):
        """Menyelesaikan sesi kuis dan hitung skor"""
        self.__sedang_berjalan = False
        
        print("\n" + "=" * 20)
        print("\n         KUIS SELESAI!")
        
        benar = 0
        salah = 0
        
        for i, soal in enumerate(self.daftarSoal):
            if i < len(self.__daftarJawabanUser):
                user_ans = self.__daftarJawabanUser[i]
                if soal.validasiJawaban(user_ans):
                    benar += 1
                else:
                    salah += 1
            else:
                salah += 1
        
        self.skor.set_skor_mentah(benar, salah)
        self.skor.hitungNilai()
        self.skor.tampilHasil()

    def jalankan_kuis_interaktif(self, username: str) -> Optional[float]:
        """
        Menjalankan kuis secara interaktif
        
        Args:
            username: Nama user yang mengerjakan
            
        Returns:
            Nilai akhir atau None jika dibatalkan
        """
        if not self.mulaiKuis():
            return None
        
        while self.__sedang_berjalan:
            self.tampilSoal()
            
            while True:
                jawaban = input("\n  Jawaban Anda (atau 'q' untuk keluar): ").strip()
                
                if jawaban.lower() == 'q':
                    confirm = input("   Yakin ingin keluar? (y/n): ").strip().lower()
                    if confirm == 'y':
                        print("  Kuis dibatalkan.")
                        self.__sedang_berjalan = False
                        return None
                    continue
                
                try:
                    jawaban_idx = int(jawaban)
                    if self.inputJawaban(jawaban_idx):
                        break
                except ValueError:
                    print("  Masukkan angka yang valid.")
            
            if self.__sedang_berjalan:
                self.nextSoal()
        
        nilai = self.skor.get_nilai_akhir()
        riwayat = Riwayat(username, self.mataPelajaran.get_info(), nilai)
        riwayat.simpanRiwayat()
        
        return nilai
    
    def is_running(self) -> bool:
        """Cek apakah kuis sedang berjalan"""
        return self.__sedang_berjalan
    
    def get_progress(self) -> tuple:
        """Mendapatkan progress kuis (current, total)"""
        return (self.__indeksSoalSaatIni + 1, len(self.daftarSoal))
    
    def get_tingkat_kesulitan(self) -> str:
        """Mendapatkan tingkat kesulitan yang dipilih"""
        return self.__tingkatKesulitan