
"""
Main Entry Point - Aplikasi Kuis Pembelajaran
"""

import sys

from services.setup_service import SetupService
from app.aplikasi_kuis import AplikasiKuis


def main():
    """Fungsi utama aplikasi"""
    try:
        SetupService.setup_assets()
        
        if not SetupService.verify_setup():
            print("   Beberapa file tidak ditemukan. Menjalankan setup ulang...")
            SetupService.setup_assets()
        
        app = AplikasiKuis()
        app.run()
        
    except KeyboardInterrupt:
        print("\n\n Program dihentikan oleh user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n  Error fatal: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()