"""
Model Soal - Mengelola data soal kuis
"""

from typing import List


class Soal:
    """Class untuk merepresentasikan satu soal kuis"""
    
    def __init__(self, pertanyaan: str, opsiJawaban: List[str], kunciJawaban: int):
        """
        Inisialisasi soal
        
        Args:
            pertanyaan: Teks pertanyaan
            opsiJawaban: List pilihan jawaban
            kunciJawaban: Index jawaban yang benar (0-based)
        """
        self.__pertanyaan = pertanyaan
        self.__opsiJawaban = opsiJawaban
        self.__kunciJawaban = kunciJawaban

    def validasiJawaban(self, jawabanUser: int) -> bool:
        """
        Memeriksa apakah jawaban user benar
        
        Args:
            jawabanUser: Index jawaban yang dipilih user
            
        Returns:
            True jika benar, False jika salah
        """
        try:
            return jawabanUser == self.__kunciJawaban
        except Exception:
            return False

    def get_pertanyaan(self) -> str:
        """Mendapatkan teks pertanyaan"""
        return self.__pertanyaan

    def get_opsi(self) -> List[str]:
        """Mendapatkan daftar pilihan jawaban (copy)"""
        return self.__opsiJawaban.copy()
    
    def get_jumlah_opsi(self) -> int:
        """Mendapatkan jumlah pilihan jawaban"""
        return len(self.__opsiJawaban)
    
    def get_kunci(self) -> int:
        """Mendapatkan index kunci jawaban"""
        return self.__kunciJawaban
    
    def to_dict(self) -> dict:
        """Convert soal ke dictionary"""
        return {
            "pertanyaan": self.__pertanyaan,
            "opsiJawaban": self.__opsiJawaban,
            "kunciJawaban": self.__kunciJawaban
        }
    
    def __str__(self) -> str:
        return f"Soal: {self.__pertanyaan[:50]}..."
    
    def __repr__(self) -> str:
        return f"Soal(pertanyaan='{self.__pertanyaan[:30]}...', jumlah_opsi={len(self.__opsiJawaban)})"