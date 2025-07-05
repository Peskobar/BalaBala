"""Menedżer tras."""

import subprocess


class MenedzerTrasy:
    """Zarządzanie trasami sieci."""

    def dodaj_trase(self, siec: str, brama: str) -> None:
        subprocess.run(
            ["./backend/bash-scripts/routing.sh", siec, brama],
            check=True,
        )
