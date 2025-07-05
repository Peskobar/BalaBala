"""Zarządzanie migawkami konfiguracji."""
import os
import shutil
import subprocess
from pathlib import Path

from .config_manager import KATALOG_KONFIG

KATALOG_SNAP = Path(
    os.getenv('PIR_OUT_SNAPSHOTS', '/var/lib/pirout/snapshots')
)


def _inicjuj_repo() -> None:
    if not (KATALOG_SNAP / '.git').exists():
        KATALOG_SNAP.mkdir(parents=True, exist_ok=True)
        subprocess.run(['git', 'init'], cwd=KATALOG_SNAP, check=True)


def _skopiuj_konfiguracje() -> None:
    for element in KATALOG_SNAP.iterdir():
        if element.name == '.git':
            continue
        if element.is_file():
            element.unlink()
        else:
            shutil.rmtree(element)
    for src in KATALOG_KONFIG.iterdir():
        dest = KATALOG_SNAP / src.name
        if src.is_file():
            shutil.copy2(src, dest)
        else:
            shutil.copytree(src, dest)


def zapisz_snapshot(opis: str) -> None:
    _inicjuj_repo()
    _skopiuj_konfiguracje()
    subprocess.run(['git', 'add', '-A'], cwd=KATALOG_SNAP, check=True)
    subprocess.run(
        ['git', 'commit', '-m', opis],
        cwd=KATALOG_SNAP,
        check=True,
    )


def rollback(commit_id: str) -> None:
    subprocess.run(
        ['git', 'checkout', commit_id, '--', '.'],
        cwd=KATALOG_SNAP,
        check=True,
    )
    for src in KATALOG_SNAP.iterdir():
        if src.name == '.git':
            continue
        dest = KATALOG_KONFIG / src.name
        if src.is_file():
            shutil.copy2(src, dest)
        else:
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src, dest)
