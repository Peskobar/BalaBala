"""Menedżer WireGuarda."""

from .vpn_manager import MenedzerVPN


class MenedzerWireguard(MenedzerVPN):
    """Obsługa tunelu WireGuard."""

    def __init__(self) -> None:
        super().__init__("./backend/bash-scripts/wireguard_manager.sh")
