"""
Soal Service - Service untuk mengambil dan mengelola soal
"""

import os
import json
from typing import List, TYPE_CHECKING
from config import CONFIG
if TYPE_CHECKING:
    from models.soal import Soal


class SoalService:
    """Service class untuk mengelola soal"""
    
    @staticmethod
    def get_soal(tingkat: str, mapel: str) -> List['Soal']:
        """
        Mengambil soal berdasarkan tingkat kesulitan dan mata pelajaran
        
        Args:
            tingkat: Tingkat kesulitan (mudah/sedang/sulit)
            mapel: Nama mata pelajaran
            
        Returns:
            List objek Soal
        """
        from models.soal import Soal
        
        path = CONFIG["soal_path"]
        list_soal: List[Soal] = []
        file_path = os.path.join(path, f"{mapel}.json")
        
        try:
            if not os.path.exists(file_path):
                print(f"  Error: File soal untuk '{mapel}' tidak ditemukan di '{file_path}'")
                return []
                
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            if tingkat not in data:
                available_levels = list(data.keys())
                print(f"  Tingkat kesulitan '{tingkat}' tidak ditemukan.")
                print(f"   Tingkat yang tersedia: {available_levels}")
                return []
            
            for idx, soal in enumerate(data[tingkat]):
                try:
                    required_keys = ["pertanyaan", "opsiJawaban", "kunciJawaban"]
                    for key in required_keys:
                        if key not in soal:
                            raise KeyError(f"Key '{key}' tidak ditemukan pada soal ke-{idx+1}")
                    
                    list_soal.append(Soal(
                        soal["pertanyaan"],
                        soal["opsiJawaban"],
                        soal["kunciJawaban"]
                    ))
                except KeyError as e:
                    print(f"   Warning: Soal ke-{idx+1} dilewati - {e}")
                    continue
            
            if not list_soal:
                print(f"   Warning: Tidak ada soal valid untuk tingkat '{tingkat}'")
            
            return list_soal
            
        except json.JSONDecodeError as e:
            print(f"  Error: File soal untuk '{mapel}' bukan format JSON yang valid.")
            return []
        except Exception as e:
            print(f"  Error tidak terduga: {e}")
            return []
    
    @staticmethod
    def get_available_mapel() -> List[str]:
        """
        Mendapatkan daftar mata pelajaran yang memiliki file soal
        
        Returns:
            List nama mata pelajaran
        """
        path = CONFIG["soal_path"]
        mapel_list = []
        
        try:
            if os.path.exists(path):
                for file in os.listdir(path):
                    if file.endswith(".json"):
                        mapel_list.append(file.replace(".json", ""))
        except Exception as e:
            print(f"  Error membaca direktori soal: {e}")
        
        return mapel_list
    
    @staticmethod
    def get_tingkat_tersedia(mapel: str) -> List[str]:
        """
        Mendapatkan tingkat kesulitan yang tersedia untuk suatu mapel
        
        Args:
            mapel: Nama mata pelajaran
            
        Returns:
            List tingkat kesulitan
        """
        file_path = os.path.join(CONFIG["soal_path"], f"{mapel}.json")
        
        try:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                return list(data.keys())
        except Exception:
            pass
        
        return []
    
    @staticmethod
    def count_soal(mapel: str, tingkat: str) -> int:
        """
        Menghitung jumlah soal untuk mapel dan tingkat tertentu
        
        Args:
            mapel: Nama mata pelajaran
            tingkat: Tingkat kesulitan
            
        Returns:
            Jumlah soal
        """
        file_path = os.path.join(CONFIG["soal_path"], f"{mapel}.json")
        
        try:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                if tingkat in data:
                    return len(data[tingkat])
        except Exception:
            pass
        
        return 0