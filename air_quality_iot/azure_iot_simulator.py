import time, random, json
from azure.iot.device import IoTHubDeviceClient

CONNECTION_STRING = "HostName=Air-quality.azure-devices.net;DeviceId=sim-node-01;SharedAccessKey=Dd6oSnx/ADrMga9DeTiPUKL0OfSm4/FODfzMeb+cShE="

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def fake_pm25():
    base = random.uniform(5, 15)
    return round(base + random.uniform(0, 40) * random.choice([0,1]), 1)

def fake_no2():
    return round(random.uniform(5, 60) + random.uniform(0, 100) * random.choice([0,1]), 0)

try:
    print("Connecting to IoT Hub…")
    client.connect()
    while True:
        payload = {
            "pm25": fake_pm25(),
            "no2":  fake_no2(),
            "timestamp": int(time.time())
        }
        msg = json.dumps(payload)
        client.send_message(msg)
        print(f"→ Published: {msg}")
        time.sleep(10) 
finally:
    client.disconnect()
