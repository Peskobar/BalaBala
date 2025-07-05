import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT / "backend" / "python"))

from pirout import config_manager  # noqa: E402


def test_doctor() -> None:
    wynik = subprocess.run([
        sys.executable,
        "-m",
        "pirout",
        "doctor",
    ], capture_output=True, text=True)
    assert "Raport PiRout" in wynik.stdout


def test_snapshot(tmp_path, monkeypatch) -> None:
    konf = tmp_path / "conf"
    snap = tmp_path / "snap"
    monkeypatch.setenv("PIR_OUT_CONF", str(konf))
    monkeypatch.setenv("PIR_OUT_SNAPSHOTS", str(snap))
    konf.mkdir()
    snap.mkdir()
    subprocess.run(["git", "init"], cwd=snap, check=True)
    config_manager.zapisz("test.conf", "dane", "inicjalny")
    historia = subprocess.run(["git", "log", "--oneline"], cwd=snap, capture_output=True, text=True)
    assert "inicjalny" in historia.stdout
