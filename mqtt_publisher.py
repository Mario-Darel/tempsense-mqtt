import random
import time
import paho.mqtt.client as mqtt
from datetime import datetime

# Fonction capteur simule
def lire_temperature():
        return round(random.uniform(20.0,30.0), 2)
# Configuration MQTT
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "tempsense/temperature"

# Creation client MQTT
client = mqtt.Client()

# Connexion client au broker
print("Connexion au broker MQTT.../n")
client.connect(BROKER, PORT, 60)
print(f"Connecte au broker {BROKER}:{PORT}")
try:
   while True:
        temperature = lire_temperature()
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"{horodatage} | {temperature} degres Celcius"
        print(f"-Publication : {message}")
        client.publish(TOPIC, message)
        time.sleep(6)
except KeyboardInterrupt:
        print("\n Arret de l'envoi MQTT.")
        client.disconnect()