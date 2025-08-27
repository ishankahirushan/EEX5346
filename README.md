# 🌐 IoT Edge-Fog-Cloud System
### *Real-time Sensor Data Collection & Control with ESP32, Flask, and Django*

<div align="center">

![IoT](https://img.shields.io/badge/IoT-ESP32-0052CC?style=for-the-badge&logo=espressif)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket-Real--time-FF6B35?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## Overview

This project implements a **full-stack IoT Edge-Fog-Cloud system**:

- **Edge (ESP32)**: Reads temperature and humidity using DHT11/DHT22 sensors and sends data via WebSocket. Receives control commands from Fog/Cloud.
- **Fog (Raspberry Pi with Flask WebSocket)**: Acts as an intermediate server, receives real-time data from ESP32 nodes, forwards it to Django Cloud, and sends back control commands.
- **Cloud (Django Dashboard)**: Provides web interface for monitoring, controlling devices, and storing historical data in SQLite.

**Key Features:**

- Real-time sensor data collection from multiple ESP32 nodes.
- WebSocket communication between Edge (ESP32) and Fog (Flask on Raspberry Pi).
- Django dashboard for data visualization and device control.
- Control modes: `AUTO`, `MANUAL`, `OFF`.
- SQLite database for historical sensor logs.

---

## Architecture

```
           ┌────────────┐
           │   ESP32    │   <-- Edge
           │ (Sensors)  │
           └─────┬──────┘
                 │ WebSocket
                 ▼
           ┌────────────┐
           │  Raspberry │   <-- Fog
           │  Pi + Flask│
           └─────┬──────┘
                 │ REST API
                 ▼
           ┌────────────┐
           │   Django   │   <-- Cloud
           │  Dashboard │
           └────────────┘
                 │
             SQLite Database
```

---

## Requirements

- ESP32 board with DHT11/DHT22 sensor
- 2 Raspberry Pi Devices
- Django 5.2+
- Flask 2.3+
- Flask WebSocket / WebSocketsClient library
- SQLite
- Wi-Fi network

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/ishankahirushan/EEX5346.git
cd iot-edge-fog-cloud
```

---

### 2. Setup Python Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
Django==5.2
Flask==2.3
requests
websockets
```

---

### 3. Setup Django Cloud

```bash
cd fogcloud
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

- Control dashboard: `http://<Cloud_IP>:8000/control/`
- Admin panel: `http://<Cloud_IP>:8000/admin/`

> Add your IP to `ALLOWED_HOSTS` in `settings.py`.

---

### 4. Setup Flask Fog Server

```bash
cd flask_server
python app.py
```

- Listens on port `8765` for WebSocket connections from ESP32 Edge nodes.

---

### 5. Setup ESP32 Edge Node

1. Open `DHT_ESP32.ino` in Arduino IDE.
2. Update:

```cpp
const char* ssid = "Your_WiFi_SSID";
const char* password = "Your_WiFi_Password";
const char* websocket_server = "Raspberry_Pi_IP";
```

3. Upload to ESP32.
4. Open Serial Monitor to see real-time sensor data:

```
Connected to WebSocket server
Humidite: 72.21%  Temperature: 44.72°C
Command receive: AUTO
Humidite: 74.32%  Temperature: 45.10°C
Command receive: MANUAL
```

---

## Database

- **Type:** SQLite
- **Tables:**
  - `SensorData`: `NodeID`, `Humidity`, `TemperatureC`, `TemperatureF`, `Timestamp`
  - `ControlLogs`: `NodeID`, `Command`, `Timestamp`

> Take a screenshot from SQLiteStudio for observations.

---

## Django Control Dashboard

- Real-time display of temperature & humidity.
- Device control: `AUTO`, `MANUAL`, `OFF`.
- Historical data visualization.
- REST API endpoint `/api/fan` receives sensor data from Flask.
- PUT `/control/` endpoint sends control commands to ESP32 via Flask.

---

## Example ESP32 Serial Output

```
Connected to WebSocket server
Humidite: 72.21%  Temperature: 44.72°C
Command receive: AUTO
Humidite: 74.32%  Temperature: 45.10°C
Command receive: MANUAL
Humidite: 70.58%  Temperature: 43.90°C
Command receive: OFF
```

---

## Contributing

1. Fork repository
2. Create a branch: `git checkout -b feature-name`
3. Commit: `git commit -am 'Add new feature'`
4. Push: `git push origin feature-name`
5. Open Pull Request

---

## License

MIT License © 2025 Ishanka Hirushan

---
<div align="center">

### 🌟 Star this repo if it helped you!

**Built with ❤️ by [Ishanka Hirushan](https://github.com/ishankahirushan)**

*IoT Edge-Fog-Cloud System | 2025*

[![GitHub stars](https://img.shields.io/github/stars/ishankahirushan/EEX5346?style=social)](https://github.com/ishankahirushan/EEX5346/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ishankahirushan/EEX5346?style=social)](https://github.com/ishankahirushan/EEX5346/network)

</div>
