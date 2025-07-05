import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import api.app as api_app  # noqa: E402

def test_status():
    klient = api_app.app.test_client()
    odp = klient.get('/status')
    dane = json.loads(odp.data)
    assert dane['status'] == 'ok'


def test_firewall_start(monkeypatch):
    akcje = []
    monkeypatch.setattr(api_app, 'zapora', api_app.zapora)
    monkeypatch.setattr(api_app.zapora, 'wlacz', lambda: akcje.append('start'))
    klient = api_app.app.test_client()
    odp = klient.post('/firewall/start')
    dane = json.loads(odp.data)
    assert dane['firewall'] == 'wlaczona'
    assert akcje == ['start']


def test_firewall_stop(monkeypatch):
    akcje = []
    monkeypatch.setattr(api_app, 'zapora', api_app.zapora)
    monkeypatch.setattr(api_app.zapora, 'wylacz', lambda: akcje.append('stop'))
    klient = api_app.app.test_client()
    odp = klient.post('/firewall/stop')
    dane = json.loads(odp.data)
    assert dane['firewall'] == 'wylaczona'
    assert akcje == ['stop']
