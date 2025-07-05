"""Zarządzanie konfiguracją aplikacji."""
from pathlib import Path
import os

KATALOG_KONFIG = Path(os.getenv("PIR_OUT_CONF", "/etc/pirout"))

def pobierz_sciezke(plik: str) -> Path:
    """Zwraca pełną ścieżkę do pliku konfiguracyjnego."""
    return KATALOG_KONFIG / plik
