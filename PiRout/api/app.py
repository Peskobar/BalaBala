from flask import Flask, jsonify
from backend.python.pirout.firewall_manager import MenedzerZapory


app = Flask(__name__)
zapora = MenedzerZapory()


@app.route("/status")
def status() -> tuple:
    return jsonify({"status": "ok"})


@app.route("/firewall/start", methods=["POST"])
def firewall_start() -> tuple:
    zapora.wlacz()
    return jsonify({"firewall": "wlaczona"})


@app.route("/firewall/stop", methods=["POST"])
def firewall_stop() -> tuple:
    zapora.wylacz()
    return jsonify({"firewall": "wylaczona"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
