from flask import Flask, render_template, jsonify
import psutil
import socket
import platform
import time

app = Flask(__name__)

BOOT_TIME = psutil.boot_time()

# ----------------------
# SYSTEM INFO
# ----------------------
def get_system_info():
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "os": platform.system() + " " + platform.release(),
        "cpu": psutil.cpu_percent(),
        "ram": mem.percent,
        "disk": disk.percent,
        "uptime": int(time.time() - BOOT_TIME)
    }


# ----------------------
# NETWORK STATS
# ----------------------
last_net = psutil.net_io_counters()
last_time = time.time()

def get_network_stats():
    global last_net, last_time

    now = psutil.net_io_counters()
    current_time = time.time()

    dt = current_time - last_time

    upload = (now.bytes_sent - last_net.bytes_sent) / dt
    download = (now.bytes_recv - last_net.bytes_recv) / dt

    last_net = now
    last_time = current_time

    return {
        "upload": round(upload / 1024, 2),
        "download": round(download / 1024, 2),
        "sent": round(now.bytes_sent / (1024**2), 2),
        "recv": round(now.bytes_recv / (1024**2), 2)
    }


# ----------------------
# MOCK DEVICE LIST (stable version)
# ----------------------
def get_devices():
    return [
        {"name": "Router", "ip": "192.168.1.1", "status": "Online"},
        {"name": "Laptop", "ip": "192.168.1.10", "status": "Online"},
        {"name": "Phone", "ip": "192.168.1.20", "status": "Online"},
    ]


# ----------------------
# ROUTES
# ----------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/stats")
def stats():
    return jsonify({
        "system": get_system_info(),
        "network": get_network_stats(),
        "devices": get_devices()
    })


# ----------------------
if __name__ == "__main__":
    app.run(debug=True)
