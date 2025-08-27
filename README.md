# 🌐 Advanced IoT Edge-Fog-Cloud System v2.0
### *Professional-Grade Sensor Data Collection & Control with ESP32, Flask, and Django*

<div align="center">

![IoT](https://img.shields.io/badge/IoT-ESP32-0052CC?style=for-the-badge&logo=espressif)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket-Real--time-FF6B35?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📋 Project Overview

This project implements a **production-ready IoT Edge-Fog-Cloud system** with the following architecture:

- **Edge Layer (ESP32)**: DHT11/DHT22 sensor nodes with LED control, WebSocket communication, and automatic threshold-based operation
- **Fog Layer (Raspberry Pi + Flask)**: Intermediate processing server with WebSocket handling, data forwarding, and device command relay
- **Cloud Layer (Django)**: Web dashboard with REST API, SQLite database, real-time monitoring, and multi-mode device control

**Core Features:**
- ✅ Real-time sensor data collection from multiple ESP32 nodes
- ✅ Bi-directional WebSocket communication (ESP32 ↔ Raspberry Pi)
- ✅ REST API integration (Raspberry Pi ↔ Django Cloud)
- ✅ Three control modes: `AUTO`, `MANUAL`, `OFF`
- ✅ SQLite database with historical sensor logs and control records
- ✅ Web-based control interface with real-time updates
- ✅ Automatic LED control based on temperature thresholds
- ✅ Multi-device support with unique NodeID identification

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     ☁️ CLOUD LAYER                          │
│  ┌─────────────────────────────────────────────────────┐    │
│  │               Django Web Application                │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │    │
│  │  │   Control   │  │    REST     │  │   SQLite    │  │    │
│  │  │ Dashboard   │  │     API     │  │  Database   │  │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    🌫️ FOG LAYER                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │        Raspberry Pi + Flask WebSocket Server        │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │    │
│  │  │  WebSocket  │  │   Flask     │  │   Data      │  │    │
│  │  │   Handler   │  │  REST API   │  │ Forwarding  │  │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────┬───────────────────────────────────────┘
                      │ WebSocket Communication
                      ▼
┌────────────────────────────────────────────────────────────┐
│                    ⚡ EDGE LAYER                           │
│    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│    │ ESP32 Node1 │  │ ESP32 Node2 │  │ ESP32 NodeN │       │
│    │ DHT22 + LED │  │ DHT11 + LED │  │ DHT22 + LED │       │
│    └─────────────┘  └─────────────┘  └─────────────┘       │
│            │               │               │               │
│       ┌────┴────┐     ┌────┴────┐     ┌────┴────┐          │
│       │ Sensor  │     │ Sensor  │     │ Sensor  │          │
│       │ Reading │     │ Reading │     │ Reading │          │
│       │   +     │     │   +     │     │   +     │          │
│       │ Control │     │ Control │     │ Control │          │
│       └─────────┘     └─────────┘     └─────────┘          │
└────────────────────────────────────────────────────────────┘
```

---

## 🔧 Technical Specifications

### Hardware Requirements
- **ESP32 Development Board** (ESP32-WROOM-32 or ESP32-DevKit)
- **DHT11/DHT22** Temperature & Humidity Sensors
- **LED** with appropriate resistor (220Ω recommended)
- **Breadboard** and jumper wires
- **2x Raspberry Pi** (or equivalent Linux systems)
- **USB cables** for ESP32 programming
- **Stable Wi-Fi network** for device connectivity

### Software Stack
| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| **Edge** | Arduino IDE | 2.0+ | ESP32 development |
| **Edge** | WebSocketsClient | Latest | Real-time communication |
| **Fog** | Python | 3.11+ | Server runtime |
| **Fog** | Flask | 2.3+ | Web framework |
| **Fog** | WebSockets | Latest | Async communication |
| **Cloud** | Django | 5.2+ | Web application |
| **Cloud** | SQLite | 3.0+ | Database storage |
| **Cloud** | Requests | Latest | HTTP client |

---

## ⚙️ Installation & Setup

### 1. Environment Preparation

```bash
# Clone the repository
git clone https://github.com/ishankahirushan/EEX5346.git
cd EEX5346

# Create Python virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

### 2. Install Dependencies

```bash
# Install required Python packages
pip install Django==5.2
pip install Flask==2.3
pip install requests
pip install websockets
pip install asyncio
```

### 3. Cloud Layer Setup (Django)

```bash
# Navigate to cloud directory
cd fogcloud

# Run database migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Update ALLOWED_HOSTS in settings.py with your IP
# ALLOWED_HOSTS = ['your_cloud_ip', 'localhost', '127.0.0.1']

# Start Django server
python manage.py runserver 0.0.0.0:8000
```

**Access Points:**
- Control Dashboard: `http://<Cloud_IP>:8000/control/`
- Admin Interface: `http://<Cloud_IP>:8000/admin/`
- API Endpoint: `http://<Cloud_IP>:8000/api/fan`

### 4. Fog Layer Setup (Flask + WebSocket)

```bash
# Navigate to Flask server directory
cd flask_server

# Update IP addresses in WF_app.py:
# - Line 45: Django server IP (Cloud layer)
# - WebSocket server runs on 0.0.0.0:8765

# Start Flask WebSocket server
python WF_app.py
```

**Server Configuration:**
- WebSocket Server: `ws://0.0.0.0:8765`
- Flask REST API: `http://0.0.0.0:5000`
- Status Endpoint: `http://0.0.0.0:5000/status`

### 5. Edge Layer Setup (ESP32)

```cpp
// Update configuration in DHT_ESP32.ino
const char* ssid = "Your_WiFi_SSID";
const char* password = "Your_WiFi_Password";
const char* websocket_server = "Raspberry_Pi_Fog_IP";  // Fog layer IP
const int websocket_port = 8765;

// Hardware pin configuration
#define DHTPIN 14      // DHT sensor pin
#define ledPin 4       // LED control pin
#define DHTTYPE DHT11  // or DHT22
```

**Upload Process:**
1. Open Arduino IDE
2. Install ESP32 board package and WebSocketsClient library
3. Select correct COM port and ESP32 board
4. Compile and upload the code
5. Open Serial Monitor (115200 baud) to observe operation

---

## 📊 Database Schema

### SensorData Table
```sql
CREATE TABLE SensorData (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NodeId VARCHAR(50) NOT NULL,
    Humidity FLOAT NOT NULL,
    TemperatureC FLOAT NOT NULL,
    TemperatureF FLOAT NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### ControlLogs Table
```sql
CREATE TABLE ControlLogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NodeId VARCHAR(50) NOT NULL,
    Command VARCHAR(20) NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**Database Features:**
- Automatic timestamping for all records
- Multi-node support with NodeId tracking
- Historical data retention for analytics
- SQLite browser compatibility for data inspection

---

## 🎮 Control Interface

### Operation Modes

| Mode | Description | LED Behavior | Data Logging |
|------|-------------|--------------|--------------|
| **AUTO** | Temperature-based control | ON when T > threshold | Continuous |
| **MANUAL** | Web interface control | User-controlled | Continuous |
| **OFF** | System disabled | Always OFF | Stopped |

### Web Dashboard Features
- 📊 **Real-time Data Display**: Live temperature and humidity readings
- 🎛️ **Device Control Panel**: Mode selection and manual LED control
- 📈 **Historical Charts**: Sensor data visualization over time
- 🔍 **Device Status**: Connection status and last update time
- 📋 **Command History**: Log of all control actions

![Control Interface](https://raw.githubusercontent.com/ishankahirushan/EEX5346/main/UI/ControlPage.png)

### REST API Endpoints

```http
# Receive sensor data from Fog layer
POST /api/fan
Content-Type: application/json
{
    "NodeId": "node1",
    "h_level": 65.5,
    "c_level": 24.3,
    "f_level": 75.7
}

# Send control commands to devices
PUT /control/
Content-Type: application/json
{
    "command": "AUTO|MANUAL|OFF"
}
```

---

## 📡 Communication Protocol

### ESP32 ↔ Fog Layer (WebSocket)
```
Direction: Bidirectional
Protocol: WebSocket (ws://)
Port: 8765
Data Format: CSV string

Uplink (Sensor Data):
"node1,65.5,24.3,75.7"
Format: NodeId,Humidity,TemperatureC,TemperatureF

Downlink (Commands):
"AUTO" | "MANUAL" | "OFF"
```

### Fog ↔ Cloud Layer (HTTP REST)
```
Direction: Fog → Cloud (Data), Cloud → Fog (Commands)
Protocol: HTTP/1.1
Port: 8000 (Django), 5000 (Flask)

Data Transmission:
POST http://cloud-ip:8000/api/fan
{"NodeId": "node1", "h_level": 65.5, "c_level": 24.3, "f_level": 75.7}

Command Relay:
PUT http://fog-ip:5000/control
{"command": "AUTO"}
```

---

## 🔍 System Monitoring

### ESP32 Serial Output
```
Connected to Wi-Fi. IP: 192.168.1.100
Connected to WebSocket server
Humidity: 65.5% Temperature: 24.3°C, 75.7°F
Command received: AUTO
Humidity: 66.2% Temperature: 25.1°C, 77.2°F
Command received: MANUAL
LED Status: ON
```

### Fog Layer Console Output
```
WebSocket server running on ws://0.0.0.0:8765
Client connected
Received from client: node1,65.5,24.3,75.7
Response from Django server: 200 OK
Sent command AUTO to client
```

### Django Admin Monitoring
- Access via `/admin/` interface
- View all sensor data records
- Monitor control command logs  
- Export data for analysis
- User management and permissions

---

## 🚀 Future Implementation Roadmap

### 🌟 **Phase 1: Enhanced Connectivity** *(Community Welcome!)*

**Target Contributors:** Network & Protocol Developers

- **Multiple Protocol Support**
  - MQTT integration for industrial applications
  - LoRaWAN support for long-range deployments
  - Bluetooth mesh for local device networks
  - *Fork opportunity: Add protocol adapters*

- **Advanced WebSocket Features**
  - Connection recovery and retry logic
  - Message queuing for offline devices
  - Compression for bandwidth optimization
  - *Contribute: WebSocket middleware enhancements*

### 🔧 **Phase 2: Edge Intelligence** *(ML/AI Contributors)*

**Target Contributors:** Machine Learning Engineers

- **On-Device Processing**
  - Implement basic anomaly detection on ESP32
  - Local decision making without cloud dependency
  - Adaptive sampling based on data patterns
  - *Fork opportunity: TensorFlow Lite integration*

- **Predictive Analytics**
  - Sensor failure prediction models
  - Maintenance scheduling algorithms
  - Energy consumption optimization
  - *Contribute: ML model implementations*

### 🛡️ **Phase 3: Security & Reliability** *(Security Researchers)*

**Target Contributors:** Cybersecurity Specialists

- **Enhanced Security**
  - Device authentication and encryption
  - Secure boot for ESP32 devices
  - API rate limiting and DDoS protection
  - *Fork opportunity: Security module development*

- **System Reliability**
  - Automatic failover mechanisms
  - Health monitoring and alerting
  - Backup and disaster recovery
  - *Contribute: Monitoring and alerting systems*

### 📊 **Phase 4: Advanced Analytics** *(Data Scientists)*

**Target Contributors:** Data Scientists & Analysts

- **Real-time Analytics**
  - Stream processing with Apache Kafka
  - Time-series database integration (InfluxDB)
  - Advanced visualization dashboards
  - *Fork opportunity: Analytics pipeline development*

- **Business Intelligence**
  - Custom reporting and KPI tracking
  - Data export and integration APIs
  - Multi-tenant support for enterprises
  - *Contribute: BI dashboard implementations*

### 🌐 **Phase 5: Scalability & Cloud-Native** *(DevOps Engineers)*

**Target Contributors:** DevOps & Cloud Engineers

- **Container Orchestration**
  - Docker containerization for all components
  - Kubernetes deployment manifests
  - Helm charts for easy deployment
  - *Fork opportunity: Cloud-native architecture*

- **Multi-Cloud Support**
  - AWS IoT Core integration
  - Azure IoT Hub connectivity
  - Google Cloud IoT support
  - *Contribute: Cloud provider integrations*

---

## 🤝 Contributing Guidelines

### 🎯 **How to Get Involved**

**For Beginners:**
1. 🍴 **Fork the Repository**: Start with our comprehensive codebase
2. 🔍 **Pick an Issue**: Check GitHub Issues for beginner-friendly tasks
3. 🛠️ **Set Up Development**: Follow our detailed setup instructions
4. 📝 **Make Changes**: Implement features following our coding standards
5. 🔄 **Submit PR**: Create pull requests with detailed descriptions

**For Advanced Contributors:**
- 🏗️ **Architecture Improvements**: Propose system-wide enhancements
- 📚 **Documentation**: Help improve setup guides and API documentation
- 🧪 **Testing**: Add unit tests, integration tests, and performance benchmarks
- 🐛 **Bug Fixes**: Tackle complex issues and edge cases

### 📋 **Contribution Areas**

| Area | Skill Level | Technologies | Impact |
|------|-------------|--------------|--------|
| **Frontend Development** | Intermediate | HTML, CSS, JavaScript, React | High |
| **Backend APIs** | Intermediate | Python, Django, Flask | High |
| **IoT Development** | Advanced | C++, Arduino, ESP32 | Critical |
| **DevOps & Deployment** | Advanced | Docker, K8s, CI/CD | High |
| **Mobile Applications** | Intermediate | React Native, Flutter | Medium |
| **Data Analytics** | Advanced | Python, SQL, ML | Medium |
| **Documentation** | Beginner | Markdown, Technical Writing | High |
| **Testing & QA** | Intermediate | PyTest, Integration Testing | Critical |

### 🏆 **Recognition Program**

**🌟 Contributor Levels:**
- **⭐ Contributor**: First successful PR merge
- **🌟 Regular Contributor**: 5+ merged PRs
- **💫 Core Contributor**: 15+ PRs + code reviews
- **🏆 Maintainer**: Trusted with repository management

**🎁 Benefits:**
- GitHub profile recognition
- LinkedIn recommendation letters
- Conference speaking opportunities
- Direct mentorship from project maintainers
- Priority access to new features and beta testing

---

## 📞 Community & Support

### 💬 **Get Help**
- 📋 **GitHub Issues**: Technical problems and feature requests
- 📧 **Email Support**: ishankahirushan22@gmail.com
- 💭 **Discussions**: Use GitHub Discussions for questions
- 📖 **Documentation**: Comprehensive guides in `/docs` folder

### 🤖 **Development Resources**
- **Setup Scripts**: Automated environment configuration
- **Code Templates**: Starter code for new features  
- **Testing Framework**: Comprehensive test suites
- **CI/CD Pipeline**: Automated testing and deployment

**Ready to contribute?** 
1. ⭐ Star this repository
2. 🍴 Fork and explore the codebase  
3. 💡 Pick a feature from our roadmap
4. 🚀 Submit your first contribution!

---

<div align="center">

## 🌟 **Project Evolution Continues...**

**From Lab Project to Production System**

*This project started as EEX5346 Lab 02 and continues evolving with community contributions. Every fork, star, and contribution helps build something bigger than the sum of its parts.*

[![GitHub stars](https://img.shields.io/github/stars/ishankahirushan/EEX5346?style=social)](https://github.com/ishankahirushan/EEX5346/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ishankahirushan/EEX5346?style=social)](https://github.com/ishankahirushan/EEX5346/network)
[![GitHub issues](https://img.shields.io/github/issues/ishankahirushan/EEX5346)](https://github.com/ishankahirushan/EEX5346/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/ishankahirushan/EEX5346)](https://github.com/ishankahirushan/EEX5346/pulls)

**Built with 💙 by [Ishanka Hirushan](https://github.com/ishankahirushan) | Enhanced by the Community**

*© 2025 EEX5346 IoT Project | Open Source MIT License | Empowering IoT Innovation*

</div>