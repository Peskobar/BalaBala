import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from api.app import app  # noqa: E402

def test_status():
    klient = app.test_client()
    odp = klient.get('/status')
    dane = json.loads(odp.data)
    assert dane['status'] == 'ok'
