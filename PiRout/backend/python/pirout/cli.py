import datetime
import os
from pathlib import Path
import subprocess

import psutil
import typer

from .firewall_manager import MenedzerZapory

app = typer.Typer(help="Narzędzie CLI PiRout")


@app.callback()
def main() -> None:
    """Główne polecenie."""
    pass


@app.command()
def doctor(zapisz: Path = typer.Option(None, help="Plik na raport")) -> None:
    """Diagnostyka łączności i obciążenia."""
    raport = [f"# Raport PiRout {datetime.datetime.now().isoformat()}\n"]
    wynik = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True)
    if wynik.returncode == 0:
        raport.append("## Łączność: OK\n")
    else:
        raport.append("## Łączność: BŁĄD\n")
        raport.append("``\n" + wynik.stderr.decode() + "\n``\n")
    cpu = psutil.cpu_percent(interval=1)
    raport.append(f"## Użycie CPU: {cpu}%\n")
    tresc = "\n".join(raport)
    if zapisz:
        Path(zapisz).write_text(tresc)
        typer.echo(f"Raport zapisano w {zapisz}")
    else:
        typer.echo(tresc)


@app.command("snapshot-list")
def snapshot_list() -> None:
    """Wyświetla historię migawek konfiguracji."""
    repo = Path(os.getenv("PIR_OUT_SNAPSHOTS", "/var/lib/pirout/snapshots"))
    if not (repo / ".git").exists():
        typer.echo("Brak migawek")
        raise typer.Exit()
    wynik = subprocess.run(
        ["git", "-C", str(repo), "log", "--oneline"],
        capture_output=True,
        text=True,
        check=True,
    )
    typer.echo(wynik.stdout)


@app.command("firewall-status")
def firewall_status() -> None:
    """Sprawdza stan zapory."""
    menedzer = MenedzerZapory()
    aktywna = menedzer.status()
    stan = "aktywna" if aktywna else "wylaczona"
    typer.echo(f"Zapora {stan}")


if __name__ == "__main__":
    app()
