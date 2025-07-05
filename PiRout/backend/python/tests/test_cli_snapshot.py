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


def test_snapshot_list(tmp_path, monkeypatch) -> None:
    repo = tmp_path / "snap"
    monkeypatch.setenv("PIR_OUT_SNAPSHOTS", str(repo))
    repo.mkdir()
    subprocess.run(["git", "init"], cwd=repo, check=True)
    (repo / "plik").write_text("d")
    subprocess.run(["git", "add", "plik"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-m", "start"], cwd=repo, check=True)
    wynik = subprocess.run([
        sys.executable,
        "-m",
        "pirout",
        "snapshot-list",
    ], capture_output=True, text=True)
    assert "start" in wynik.stdout
