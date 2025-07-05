"""Menedżer L2TP."""

from .vpn_manager import MenedzerVPN


class MenedzerL2tp(MenedzerVPN):
    """Obsługa tunelu L2TP."""

    def __init__(self) -> None:
        super().__init__("./backend/bash-scripts/l2tp_manager.sh")
