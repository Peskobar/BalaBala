import logging
import subprocess
import time
from pathlib import Path

# Konfiguracja logowania
LOG_FILE = Path('/var/log/pirout-health.log')
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Definicje modułów do monitorowania
MODULY = {
    'openvpn': {
        'proces': 'openvpn',
        'restart': ['./backend/bash-scripts/openvpn_manager.sh', 'start'],
    },
    'wireguard': {
        'proces': 'wg-quick',
        'restart': ['./backend/bash-scripts/wireguard_manager.sh', 'start'],
    },
    'zapora': {
        'proces': 'nft',
        'restart': ['./backend/bash-scripts/firewall.sh', 'start'],
    },
}


def sprawdz_modul(nazwa: str, dane: dict) -> None:
    if subprocess.run(['pgrep', dane['proces']], capture_output=True).returncode != 0:
        logging.warning('Moduł %s nie działa, restart...', nazwa)
        subprocess.run(dane['restart'], check=False)
    else:
        logging.info('Moduł %s działa prawidłowo', nazwa)


def main() -> None:
    logging.info('Uruchomiono daemon zdrowotny')
    while True:
        for nazwa, dane in MODULY.items():
            sprawdz_modul(nazwa, dane)
        time.sleep(30)


if __name__ == '__main__':
    main()
