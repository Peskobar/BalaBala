"""Menedżer tras."""
import subprocess

class MenedzerTrasy:
    def dodaj_trase(self, siec: str, brama: str) -> None:
        subprocess.run(["./backend/bash-scripts/routing.sh", siec, brama], check=True)
