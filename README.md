# 🌫️ IoT Air Quality Monitoring System (InfluxDB + Docker)

This project is a complete IoT-based **Air Quality Monitoring System** that uses a **NodeMCU ESP8266** microcontroller to collect environmental data and stores it in **InfluxDB**. The system uses **Docker** for containerized deployment.

## 📦 Overview

- 📡 **ESP8266** collects sensor data.
- 🐍 **Python (`eh_to_influx.py`)** sends sensor data to InfluxDB.
- 🐳 **Docker** runs InfluxDB 2 at `http://localhost:8086`.
- 🧪 Optional: `azure_iot_simulator.py` used for testing/simulation.

## 🔧 How to Run the System

### 1. Start InfluxDB (v2) using Docker

```bash
docker run -p 8086:8086 \
  -v $PWD/influxdb2:/var/lib/influxdb2 \
  influxdb:2

## 🧪 Software Requirements

- Docker 
- InfluxDB (visulaing of data)
- Visual Studio Code
- Microsoft Azure


## 🚀 Setup Instructions

### 1. Flash NodeMCU
- Open `esp8266_air_sensor.ino` in Arduino IDE.
- Install necessary libraries: `DHT`, `ESP8266WiFi`, `ESP8266HTTPClient` or MQTT client.
- Modify WiFi credentials and server IP/port.
- Upload to ESP8266.

### 2. Start InfluxDB using Docker

```bash
docker-compose up -d
