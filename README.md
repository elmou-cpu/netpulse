# NetPulse — Real-Time Network Monitoring Dashboard

NetPulse is a lightweight real-time system and network monitoring dashboard built with Python and Flask. It displays live CPU, RAM, disk usage, network speed, and connected device status in a clean dark-themed web interface.

> This project is actively being improved. New features will be added over time.

---

## Features

- Real-time CPU, RAM, and disk usage monitoring
- Live network upload and download speed tracking
- Total data sent and received
- Connected device status table
- Live traffic chart updated every 2 seconds
- Clean dark-mode UI

---

## Tech Stack

- Python 3
- Flask
- psutil
- JavaScript
- Chart.js
- HTML / CSS

---

## Installation

```bash
git clone https://github.com/moncef-bouchelaghem/netpulse.git
cd netpulse
pip install flask psutil --break-system-packages
python3 app.py
```

Then open your browser at `http://127.0.0.1:5000`

---

## Project Status

Work in progress. Planned improvements:
- Real ARP-based device scanning
- Telegram alert when a device goes offline
- User-configurable device list
- Deployment guide

---

## Author

**Moncef Bouchelaghem**
M1 Telecommunications Systems — Université Saad Dahlab Blida-1


