"""
Model Riwayat - Mengelola riwayat kuis
"""

from datetime import date, datetime
from typing import Dict, List, Optional
from utils.file_handler import get_json, save_json
from config import CONFIG


class Riwayat:
    """Class untuk mengelola riwayat kuis"""
    
    def __init__(self, namaUser: str, mapel: str, nilaiAkhir: float, tanggalTes: date = None):
        """
        Inisialisasi riwayat
        
        Args:
            namaUser: Nama pengguna
            mapel: Nama mata pelajaran
            nilaiAkhir: Nilai akhir dalam persentase
            tanggalTes: Tanggal tes (default: hari ini)
        """
        self.__namaUser = namaUser
        self.__mapel = mapel
        self.__nilaiAkhir = nilaiAkhir
        self.__tanggalTes = tanggalTes or date.today()

    def simpanRiwayat(self) -> bool:
        """
        Menyimpan riwayat ke file JSON
        
        Returns:
            True jika berhasil, False jika gagal
        """
        try:
            riwayat_list = get_json(CONFIG["riwayat_path"])
            if riwayat_list is None:
                riwayat_list = []
            
            new_entry = {
                "namaUser": self.__namaUser,
                "mapel": self.__mapel,
                "nilaiAkhir": self.__nilaiAkhir,
                "tanggalTes": str(self.__tanggalTes),
                "timestamp": datetime.now().isoformat()
            }
            riwayat_list.append(new_entry)
            
            if save_json(CONFIG["riwayat_path"], riwayat_list):
                print(f"  Riwayat berhasil disimpan.")
                return True
            return False
            
        except Exception as e:
            print(f"  Error menyimpan riwayat: {e}")
            return False

    def bacaRiwayat(self):
        """Menampilkan detail riwayat ini ke layar"""
        print("\n" + "-" * 35)
        print("          DETAIL RIWAYAT")
        print("-" * 35)
        print(f"    Tanggal : {self.__tanggalTes}")
        print(f"    Nama    : {self.__namaUser}")
        print(f"    Mapel   : {self.__mapel}")
        print(f"    Nilai   : {self.__nilaiAkhir:.2f}%")
        print("-" * 35)

    @staticmethod
    def tampilSemuaRiwayat(username: str = None):
        """
        Menampilkan semua riwayat
        
        Args:
            username: Filter by username (opsional)
        """
        riwayat_list = get_json(CONFIG["riwayat_path"])
        
        if not riwayat_list:
            print("  Belum ada riwayat tersimpan.")
            return
        
        if username:
            riwayat_list = [r for r in riwayat_list if r.get("namaUser") == username]
            if not riwayat_list:
                print(f"  Tidak ada riwayat untuk user '{username}'.")
                return
        
        print("\n" + "=" * 50)
        print("                RIWAYAT KUIS")
        print("=" * 50)
        
        for idx, r in enumerate(riwayat_list, 1):
            try:
                print(f"\n  [{idx}] {r.get('tanggalTes', 'N/A')}")
                print(f"        {r.get('namaUser', 'Unknown')}")
                print(f"        {r.get('mapel', 'Unknown')}")
                print(f"        {r.get('nilaiAkhir', 0):.2f}%")
            except Exception:
                print(f"  [{idx}] Data tidak lengkap")
        
        print("\n" + "=" * 50)

    @staticmethod
    def getRiwayatByUser(username: str) -> List[Dict]:
        """
        Mendapatkan riwayat berdasarkan username
        
        Args:
            username: Username yang dicari
            
        Returns:
            List riwayat untuk user tersebut
        """
        riwayat_list = get_json(CONFIG["riwayat_path"]) or []
        return [r for r in riwayat_list if r.get("namaUser") == username]

    @staticmethod
    def hapusRiwayat(username: str = None) -> bool:
        """
        Menghapus riwayat
        
        Args:
            username: Hapus riwayat user tertentu, atau semua jika None
            
        Returns:
            True jika berhasil
        """
        try:
            if username:
                riwayat_list = get_json(CONFIG["riwayat_path"]) or []
                riwayat_list = [r for r in riwayat_list if r.get("namaUser") != username]
                save_json(CONFIG["riwayat_path"], riwayat_list)
            else:
                save_json(CONFIG["riwayat_path"], [])
            return True
        except Exception:
            return False

    def to_dict(self) -> Dict:
        """Convert riwayat ke dictionary"""
        return {
            "namaUser": self.__namaUser,
            "mapel": self.__mapel,
            "nilaiAkhir": self.__nilaiAkhir,
            "tanggalTes": str(self.__tanggalTes)
        }
    
    def get_nama_user(self) -> str:
        return self.__namaUser
    
    def get_mapel(self) -> str:
        return self.__mapel
    
    def get_nilai(self) -> float:
        return self.__nilaiAkhir
    
    def get_tanggal(self) -> date:
        return self.__tanggalTes