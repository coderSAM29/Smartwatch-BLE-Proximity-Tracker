# Smartwatch BLE Proximity Tracker

A lightweight Python toolkit for discovering Bluetooth Low Energy (BLE) smartwatches and tracking their real-time proximity using Received Signal Strength Indicator (RSSI) values.

## Overview

This repository provides two core scripts designed to work together:

1. **`watch_scanner.py`**: Scans the surrounding environment for nearby BLE devices, filtering and displaying device names, MAC addresses/UUIDs, and initial signal strengths to help you identify your smartwatch.
2. **`watch_tracker.py`**: Connects to or monitors a specific target smartwatch via its BLE address/UUID, continuously calculating signal strength (RSSI) and estimating proximity status (e.g., *Immediate*, *Near*, *Far*, or *Out of Range*).

---

## Features

- **Asynchronous BLE Scanning**: Fast, non-blocking device discovery using modern Python BLE libraries (such as `bleak`).
- **Real-Time RSSI Monitoring**: Continuous tracking of signal strength fluctuations to determine relative distance.
- **Proximity Threshold Alerts**: Configurable RSSI thresholds to trigger console alerts or custom actions when a watch moves out of range.
- **Cross-Platform Support**: Compatible with Windows, macOS, and Linux systems equipped with Bluetooth 4.0+ adapters.

---

## Prerequisites

- **Python**: Version 3.8 or higher
- **Hardware**: Built-in or USB Bluetooth Low Energy (BLE) adapter
- **Dependencies**:
  - `bleak` (Bluetooth Low Energy platform-agnostic client)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/coderSAM29/Smartwatch-BLE-Proximity-Tracker.git](https://github.com/coderSAM29/Smartwatch-BLE-Proximity-Tracker.git)
   cd Smartwatch-BLE-Proximity-Tracker
