"""Podstawowa klasa zarządzająca usługami VPN."""
import subprocess

class MenedzerVPN:
    """Bazowy menedżer VPN."""

    def __init__(self, skrypt: str) -> None:
        self.skrypt = skrypt

    def start(self) -> None:
        subprocess.run([self.skrypt, "start"], check=True)

    def stop(self) -> None:
        subprocess.run([self.skrypt, "stop"], check=True)
