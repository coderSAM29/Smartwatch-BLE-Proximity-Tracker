import asyncio
import sys
from bleak import BleakScanner

if sys.platform == "Win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def scan_devices():
    print("scanning for nearby bluetoothdevices and smartwatch...")

    devices = await BleakScanner.discover(timeout=5.0, return_adv=True)

    for address, (device, adv_data) in devices.items():
        name = device.name if device.name else "unknown device"
        print(f"Name: {name}  Address: {address} Signal: {adv_data.rssi} dBm")

asyncio.run(scan_devices())        
