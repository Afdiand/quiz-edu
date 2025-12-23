"""
Services package - berisi business logic dan services
"""

from .setup_service import SetupService

__all__ = [
    'SetupService'
]

def get_soal_service():
    from .soal_service import SoalService
    return SoalService