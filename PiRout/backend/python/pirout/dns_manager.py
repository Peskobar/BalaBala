"""Menedżer DNS."""
import subprocess

class MenedzerDns:
    def ustaw_dns(self, adres: str) -> None:
        subprocess.run(["resolvectl", "dns", "eth0", adres], check=True)
