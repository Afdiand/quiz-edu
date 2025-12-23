"""
Validators - Fungsi untuk validasi input user
"""

from typing import Optional
import re


def validasi_input_int(prompt: str, min_val: int = None, max_val: int = None) -> Optional[int]:
    """
    Validasi input integer dari user
    
    Args:
        prompt: Pesan prompt untuk user
        min_val: Nilai minimum (opsional)
        max_val: Nilai maksimum (opsional)
        
    Returns:
        Integer yang valid atau None jika gagal
    """
    try:
        value = input(prompt).strip()
        
        if not value:
            print("  Input tidak boleh kosong.")
            return None
        
        value = int(value)
        
        if min_val is not None and value < min_val:
            print(f"  Nilai harus minimal {min_val}.")
            return None
            
        if max_val is not None and value > max_val:
            print(f"  Nilai harus maksimal {max_val}.")
            return None
            
        return value
        
    except ValueError:
        print("  Input harus berupa angka.")
        return None


def validasi_input_str(prompt: str, min_length: int = 1) -> Optional[str]:
    """
    Validasi input string dari user
    
    Args:
        prompt: Pesan prompt untuk user
        min_length: Panjang minimum string
        
    Returns:
        String yang valid atau None jika gagal
    """
    try:
        value = input(prompt).strip()
        
        if len(value) < min_length:
            print(f"  Input minimal {min_length} karakter.")
            return None
            
        return value
        
    except Exception as e:
        print(f"  Error input: {e}")
        return None


def validasi_email(email: str) -> bool:
    """
    Validasi format email sederhana
    
    Args:
        email: String email yang akan divalidasi
        
    Returns:
        True jika valid, False jika tidak
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validasi_password(password: str, min_length: int = 6) -> tuple[bool, str]:
    """
    Validasi password
    
    Args:
        password: Password yang akan divalidasi
        min_length: Panjang minimum password
        
    Returns:
        Tuple (is_valid, message)
    """
    if len(password) < min_length:
        return False, f"Password minimal {min_length} karakter."
    
    return True, "Password valid."


def validasi_username(username: str, min_length: int = 3) -> tuple[bool, str]:
    """
    Validasi username
    
    Args:
        username: Username yang akan divalidasi
        min_length: Panjang minimum username
        
    Returns:
        Tuple (is_valid, message)
    """
    if len(username) < min_length:
        return False, f"Username minimal {min_length} karakter."
    
    if not username.isalnum() and '_' not in username:
        return False, "Username hanya boleh huruf, angka, dan underscore."
    
    return True, "Username valid."