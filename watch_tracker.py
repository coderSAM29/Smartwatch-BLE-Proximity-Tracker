import asyncio 
from bleak import BleakScanner


WATCH_ADDRESS = "YOUR_WATCH_ADDRESS"  # Replace with your smartwatch's Bluetooth address

async def track_watch():
    print(f"Tracking smartwatch({WATCH_ADDRESS}) LIVE...")
    print("Press ctrl + c to stop")

    while True:
        devices = await BleakScanner.discover(timeout=4.0, return_adv=True)

        found = False
        for address, (devices, adv_data)in devices.items():
            if address.upper() == WATCH_ADDRESS.upper():
                found = True
                rssi = adv_data.rssi
                distance = "unknown"

                if rssi > -60:
                    distance = "very close (within 1-2 meters)"
                elif rssi > -80:
                    distanse = "nearby (inside the room)"  
                else:
                    distance = "far away (weak signal)" 

                print(f"[TRACKED] signal: {rssi} dBm status: {distance}")   
                break

            if not found:
                print("[LOST] smartwatch is out of range or turned off...")      

asyncio.run(track_watch())                                      
