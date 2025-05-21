import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    print(f"Received from MQTT: {data}")
    # Here you would push to Beam pipeline or MinIO

client = mqtt.Client()
client.on_message = on_message
client.connect('localhost', 1883, 60)
client.subscribe('sensors/#')

if __name__ == "__main__":
    print("Listening to MQTT...")
    client.loop_forever()
