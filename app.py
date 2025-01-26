
from flask import Flask, jsonify, render_template
from threading import Thread
from utils.proxy_updater import start_proxy_updater
from utils.proxy_storage import get_proxies, get_raw_proxies, clean_old_proxies

app = Flask(__name__)

@app.route('/')
def index():
    clean_old_proxies()
    stats = get_stats()
    return render_template('index.html', stats=stats)

@app.route('/proxies/<protocol>')
def get_protocol_proxies(protocol):
    proxies = get_proxies(protocol)
    return jsonify(proxies)

@app.route('/raw')
def raw_proxies():
    proxies = get_raw_proxies()
    return jsonify(proxies)

def get_stats():
    # Simplified for demo
    return {
        'total_tested': 100,
        'total_working': 50,
        'http_count': 30,
        'socks4_count': 10,
        'socks5_count': 10
    }

if __name__ == "__main__":
    # Start proxy updater in a separate thread
    Thread(target=start_proxy_updater, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
