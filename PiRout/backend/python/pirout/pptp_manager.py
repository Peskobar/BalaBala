"""Menedżer PPTP."""
from .vpn_manager import MenedzerVPN

class MenedzerPptp(MenedzerVPN):
    def __init__(self) -> None:
        super().__init__("./backend/bash-scripts/pptp_manager.sh")
