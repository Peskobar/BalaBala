"""Zarządzanie konfiguracją aplikacji."""
from pathlib import Path
import os


KATALOG_KONFIG = Path(os.getenv("PIR_OUT_CONF", "/etc/pirout"))


def pobierz_sciezke(plik: str) -> Path:
    """Zwraca pełną ścieżkę do pliku konfiguracyjnego."""
    return KATALOG_KONFIG / plik


def zapisz(plik: str, dane: str, opis: str) -> None:
    sciezka = pobierz_sciezke(plik)
    sciezka.parent.mkdir(parents=True, exist_ok=True)
    sciezka.write_text(dane)
    from . import snapshot_manager
    snapshot_manager.zapisz_snapshot(opis)
