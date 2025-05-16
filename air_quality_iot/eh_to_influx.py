import json
from azure.eventhub import EventHubConsumerClient
from influxdb_client import InfluxDBClient, Point, WritePrecision

# ← paste your Event Hub–compatible conn str (minus EntityPath) here:
EH_COMPATIBLE_CONN_STR = "Endpoint=sb://ihsuprodsgres004dednamespace.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=n9nwqjfguY0akqi5MNQRmcMeaFXyBtIZKAIoTD6H5TU=;EntityPath=iothub-ehub-air-qualit-57169966-4db5c436e2"


# ← configure your InfluxDB instance here:
INFLUX_URL    = "http://localhost:8086"
INFLUX_TOKEN  = "ZISvxDZiswDdzxroxdoNIWgsUOffiYHUQWd8KhjVOOeAMA5tdeuuqA_S3zbg97oJr6xc55Wq7jNRCDthK0vJVQ=="
INFLUX_ORG    = "my-org"
INFLUX_BUCKET = "aqi_bucket"

eh_client = EventHubConsumerClient.from_connection_string(
    conn_str=EH_COMPATIBLE_CONN_STR,
    consumer_group="$Default",
   
)

influx_client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api     = influx_client.write_api()

def on_event(partition_context, event):
    body = event.body_as_str(encoding='UTF-8')
    data = json.loads(body)
    pm25 = data.get("pm25")
    no2  = data.get("no2")
    ts   = data.get("timestamp") 

    point = (
        Point("air_quality")
        .tag("device", partition_context.eventhub_name)
        .field("pm25", float(pm25))
        .field("no2",  float(no2))
        .time(ts, WritePrecision.S)
    )

    write_api.write(bucket=INFLUX_BUCKET, record=point)
    print(f"Written → pm2.5={pm25}, no2={no2} at ts={ts}")

    partition_context.update_checkpoint(event)

def main():
    with eh_client:
        print("Listening for events…")
        eh_client.receive(on_event=on_event)

if __name__ == "__main__":
    main()
