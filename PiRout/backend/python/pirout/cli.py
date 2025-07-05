import datetime
from pathlib import Path
import subprocess

import psutil
import typer

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


if __name__ == "__main__":
    app()
