"""
Model Skor - Mengelola perhitungan dan tampilan skor
"""


class Skor:
    """Class untuk mengelola skor kuis"""
    
    def __init__(self):
        self.__totalBenar: int = 0
        self.__totalSalah: int = 0
        self.__persentaseNilai: float = 0.0

    def set_skor_mentah(self, benar: int, salah: int):
        """
        Memasukkan data benar dan salah
        
        Args:
            benar: Jumlah jawaban benar
            salah: Jumlah jawaban salah
        """
        if benar < 0 or salah < 0:
            print("   Warning: Skor tidak boleh negatif, diset ke 0.")
            benar = max(0, benar)
            salah = max(0, salah)
            
        self.__totalBenar = benar
        self.__totalSalah = salah

    def hitungNilai(self):
        """Menghitung persentase nilai berdasarkan total benar dan salah"""
        total_soal = self.__totalBenar + self.__totalSalah
        
        if total_soal > 0:
            self.__persentaseNilai = (self.__totalBenar / total_soal) * 100
        else:
            self.__persentaseNilai = 0.0

    def tampilHasil(self):
        """Menampilkan hasil skor ke layar"""
        total = self.__totalBenar + self.__totalSalah
        
        print("\n" + "=" * 35)
        print("             HASIL KUIS")
        print("=" * 35)
        print(f"  ✓ Benar       : {self.__totalBenar}")
        print(f"  ✗ Salah       : {self.__totalSalah}")
        print(f"    Total Soal : {total}")
        print("-" * 35)
        print(f"    Nilai Akhir: {self.__persentaseNilai:.2f}%")
        print("=" * 35)
        
        self._tampil_feedback()

    def _tampil_feedback(self):
        """Menampilkan feedback berdasarkan nilai"""
        if self.__persentaseNilai >= 90:
            print("    LUAR BIASA! Sempurna!")
        elif self.__persentaseNilai >= 75:
            print("    BAGUS! Pertahankan!")
        elif self.__persentaseNilai >= 60:
            print("    CUKUP. Terus belajar!")
        else:
            print("    Jangan menyerah, terus berlatih!")

    def get_nilai_akhir(self) -> float:
        """Mendapatkan nilai akhir dalam persentase"""
        return self.__persentaseNilai
    
    def get_total_benar(self) -> int:
        """Mendapatkan total jawaban benar"""
        return self.__totalBenar
    
    def get_total_salah(self) -> int:
        """Mendapatkan total jawaban salah"""
        return self.__totalSalah
    
    def get_total_soal(self) -> int:
        """Mendapatkan total soal yang dijawab"""
        return self.__totalBenar + self.__totalSalah
    
    def reset(self):
        """Reset semua skor"""
        self.__totalBenar = 0
        self.__totalSalah = 0
        self.__persentaseNilai = 0.0
    
    def to_dict(self) -> dict:
        """Convert skor ke dictionary"""
        return {
            "totalBenar": self.__totalBenar,
            "totalSalah": self.__totalSalah,
            "persentaseNilai": self.__persentaseNilai
        }