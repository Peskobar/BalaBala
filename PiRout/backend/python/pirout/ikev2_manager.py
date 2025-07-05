"""Menedżer IKEv2."""

from .vpn_manager import MenedzerVPN


class MenedzerIkev2(MenedzerVPN):
    """Obsługa tunelu IKEv2."""

    def __init__(self) -> None:
        super().__init__("./backend/bash-scripts/ikev2_manager.sh")
