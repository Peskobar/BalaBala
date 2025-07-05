"""Menedżer zapory sieciowej."""

import subprocess


class MenedzerZapory:
    """Klasa do zarządzania zaporą."""

    SKRYPT = "./backend/bash-scripts/firewall.sh"

    def wlacz(self) -> None:
        subprocess.run([self.SKRYPT, "start"], check=True)

    def wylacz(self) -> None:
        subprocess.run([self.SKRYPT, "stop"], check=True)

    def status(self) -> bool:
        wynik = subprocess.run(["iptables", "-L"], capture_output=True)
        return wynik.returncode == 0
