"""Menedżer zapory sieciowej."""
import subprocess

class MenedzerZapory:
    """Klasa do zarządzania zaporą."""

    def wlacz(self) -> None:
        subprocess.run(["./backend/bash-scripts/firewall.sh", "start"], check=True)

    def wylacz(self) -> None:
        subprocess.run(["./backend/bash-scripts/firewall.sh", "stop"], check=True)
