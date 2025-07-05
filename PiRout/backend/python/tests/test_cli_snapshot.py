import os
import sys
import subprocess
from pathlib import Path
from typer.testing import CliRunner

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT / "backend" / "python"))

from pirout.cli import app  # noqa: E402
from pirout import config_manager  # noqa: E402

runner = CliRunner()


def test_doctor(monkeypatch) -> None:
    def fake_run(*args, **kwargs):
        class R:
            returncode = 0
            stderr = b""
        return R()
    monkeypatch.setattr(subprocess, "run", fake_run)
    wynik = runner.invoke(app, ["doctor"])
    assert "Raport PiRout" in wynik.stdout


def test_snapshot(tmp_path, monkeypatch) -> None:
    konf = tmp_path / "conf"
    snap = tmp_path / "snap"
    monkeypatch.setenv("PIR_OUT_CONF", str(konf))
    monkeypatch.setenv("PIR_OUT_SNAPSHOTS", str(snap))
    konf.mkdir()
    snap.mkdir()
    os.system(f"git init {snap}")
    config_manager.zapisz("test.conf", "dane", "inicjalny")
    log = os.popen(f"git -C {snap} log --oneline").read()
    assert "inicjalny" in log


def test_snapshot_list(tmp_path, monkeypatch) -> None:
    repo = tmp_path / "snap"
    monkeypatch.setenv("PIR_OUT_SNAPSHOTS", str(repo))
    repo.mkdir()
    os.system(f"git init {repo}")
    (repo / "plik").write_text("d")
    os.system(f"git -C {repo} add plik")
    os.system(f"git -C {repo} commit -m start")
    wynik = runner.invoke(app, ["snapshot-list"])
    assert "start" in wynik.stdout


def test_firewall_status_cli(monkeypatch) -> None:
    monkeypatch.setattr(
        "pirout.firewall_manager.MenedzerZapory.status",
        lambda self: True,
    )
    wynik = runner.invoke(app, ["firewall-status"])
    assert "aktywna" in wynik.stdout
