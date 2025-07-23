import paho.mqtt.client as mqtt

# Configuration MQTT
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "tempsense/temperature"

# Réception d'un message
def on_message(client, userdata, message):
    print(f"Message recu : {message.payload.decode()}")

# Création du client MQTT
client = mqtt.Client()

# Joindre le message de réception
client.on_message = on_message

# Connexion au broker MQTT
print("Connexion au broker MQTT...\n")
client.connect(BROKER, PORT, 60)
print(f"Abonne au topic:{TOPIC}")
client.subscribe(TOPIC)

# Boucle pour attendre les messages
client.loop_forever()