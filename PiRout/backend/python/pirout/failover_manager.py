"""Menedżer failover."""
import subprocess

class MenedzerFailover:
    def ustaw(self, brama: str) -> None:
        subprocess.run(["./backend/bash-scripts/failover.sh", brama], check=True)
