"""
File Handler - Fungsi untuk membaca dan menulis file JSON
"""

import json
import os
from typing import List, Dict, Any, Optional


def get_json(path: str) -> List[Dict]:
    """
    Load JSON file dengan error handling
    
    Args:
        path: Path ke file JSON
        
    Returns:
        List dictionary dari file JSON, atau list kosong jika gagal
    """
    try:
        if not os.path.exists(path):
            print(f"   Warning: File '{path}' tidak ditemukan.")
            return []
            
        with open(path, "r", encoding="utf-8") as file:
            file_json = json.load(file)
        return file_json
        
    except json.JSONDecodeError as e:
        print(f"  Error: File '{path}' bukan format JSON yang valid. Detail: {e}")
        return []
    except PermissionError:
        print(f"  Error: Tidak memiliki izin untuk membaca file '{path}'.")
        return []
    except Exception as e:
        print(f"  Error tidak terduga saat membaca file: {e}")
        return []


def save_json(path: str, data: Any) -> bool:
    """
    Simpan data ke JSON file dengan error handling
    
    Args:
        path: Path tujuan file
        data: Data yang akan disimpan
        
    Returns:
        True jika berhasil, False jika gagal
    """
    try:
        dir_path = os.path.dirname(path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False, default=str)
        return True
        
    except PermissionError:
        print(f"  Error: Tidak memiliki izin untuk menulis ke '{path}'.")
        return False
    except Exception as e:
        print(f"  Error saat menyimpan file: {e}")
        return False


def file_exists(path: str) -> bool:
    """Cek apakah file ada"""
    return os.path.exists(path)


def create_directory(path: str) -> bool:
    """Buat direktori jika belum ada"""
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        print(f"  Error membuat direktori: {e}")
        return False