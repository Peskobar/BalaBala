"""Menedżer failover."""

import subprocess


class MenedzerFailover:
    """Ustawia zapasową bramę."""

    def ustaw(self, brama: str) -> None:
        subprocess.run(
            ["./backend/bash-scripts/failover.sh", brama],
            check=True,
        )
