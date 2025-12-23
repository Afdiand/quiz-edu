"""
Model MataPelajaran - Mengelola data mata pelajaran
"""

from typing import List, Dict, Optional
from utils.file_handler import get_json
from config import CONFIG


class MataPelajaran:
    """Class untuk mengelola mata pelajaran"""
    
    __data_mapel: Optional[List[Dict]] = None  
    
    @classmethod
    def _load_mapel(cls) -> List[Dict]:
        """Lazy loading untuk data mapel"""
        if cls.__data_mapel is None:
            cls.__data_mapel = get_json(CONFIG["mapel_path"])
        return cls.__data_mapel
    
    @classmethod
    def reload_mapel(cls):
        """Reload data mapel dari file"""
        cls.__data_mapel = None
        return cls._load_mapel()

    def __init__(self):
        self.__namaMapel: str = ""
        self.__kategoriID: str = ""

    def pilihMapel(self, nama_dicari: str) -> bool:
        """
        Memilih mata pelajaran berdasarkan nama
        
        Args:
            nama_dicari: Nama mata pelajaran yang dicari
            
        Returns:
            True jika berhasil, False jika gagal
        """
        data = self._load_mapel()
        
        if not data:
            print("  Data mata pelajaran kosong atau tidak dapat dimuat.")
            return False
        
        for mp in data:
            try:
                if mp["nama"].lower() == nama_dicari.lower():
                    self.__namaMapel = mp["nama"]
                    self.__kategoriID = mp["id"]
                    print(f"  Mata pelajaran '{self.__namaMapel}' terpilih.")
                    return True
            except KeyError:
                continue
                
        print(f"  Mata pelajaran '{nama_dicari}' tidak ditemukan.")
        return False

    def pilihMapelByIndex(self, index: int) -> bool:
        """
        Memilih mata pelajaran berdasarkan index
        
        Args:
            index: Index mata pelajaran dalam daftar
            
        Returns:
            True jika berhasil, False jika gagal
        """
        data = self._load_mapel()
        
        if not data:
            print("  Data mata pelajaran kosong atau tidak dapat dimuat.")
            return False
        
        if 0 <= index < len(data):
            try:
                self.__namaMapel = data[index]["nama"]
                self.__kategoriID = data[index]["id"]
                print(f"  Mata pelajaran '{self.__namaMapel}' terpilih.")
                return True
            except KeyError as e:
                print(f"  Error: Data mapel tidak lengkap - {e}")
                return False
        else:
            print(f"  Index tidak valid. Pilih antara 0-{len(data)-1}")
            return False

    def getDaftarMapel(self) -> List[Dict]:
        """Mendapatkan daftar semua mata pelajaran"""
        return self._load_mapel()

    def tampilDaftarMapel(self):
        """Menampilkan daftar mata pelajaran ke layar"""
        data = self._load_mapel()
        
        if not data:
            print("  Tidak ada mata pelajaran yang tersedia.")
            return
        
        print("\n  DAFTAR MATA PELAJARAN:")
        print("-" * 30)
        for idx, mp in enumerate(data):
            try:
                print(f"  {idx}. {mp['nama']} ({mp['id']})")
            except KeyError:
                print(f"  {idx}. [Data tidak lengkap]")
        print("-" * 30)

    def get_info(self) -> str:
        """Mendapatkan nama mata pelajaran yang dipilih"""
        return self.__namaMapel
    
    def get_id(self) -> str:
        """Mendapatkan ID mata pelajaran yang dipilih"""
        return self.__kategoriID
    
    def is_selected(self) -> bool:
        """Cek apakah mata pelajaran sudah dipilih"""
        return bool(self.__namaMapel)
    
    def reset(self):
        """Reset pilihan mata pelajaran"""
        self.__namaMapel = ""
        self.__kategoriID = ""