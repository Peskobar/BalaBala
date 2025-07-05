"""Menedżer bezpieczeństwa."""
import subprocess

class MenedzerBezpieczenstwa:
    def wylacz_icmp(self) -> None:
        subprocess.run(["sysctl", "-w", "net.ipv4.icmp_echo_ignore_all=1"], check=True)

    def wlacz_icmp(self) -> None:
        subprocess.run(["sysctl", "-w", "net.ipv4.icmp_echo_ignore_all=0"], check=True)
