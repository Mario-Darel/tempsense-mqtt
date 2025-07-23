import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import datetime

# Configuation du MQTT
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "tempsense/temperature"

# Stockage des données
window_size = 20  # nombre de points visibles
temps = deque(maxlen=window_size)
dates = deque(maxlen=window_size)

# Gestion des Callbacks MQTT
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connecte au broker MQTT avec le code {rc}")
    client.subscribe(TOPIC)
    print("Abonne au topic : {TOPIC}")
def on_message(client, userdata, msg):
    try :
         payload = msg.payload.decode()
         horodatage, valeur = payload.split(" | ")
         valeur  = float(valeur.replace("degres Celcius", " ").strip())
         date_obj = datetime.datetime.strptime(horodatage, "%Y-%m-%d %H:%M:%S")

         # Ajout des données dans les listes
         dates.append(date_obj)
         temps .append(valeur)
    except Exception as e:
         print(f"Erreur du parsing du message : {e}")

# Graphique
def animate(i):
    if len(dates)>0:
       ax.clear()
       ax.plot(dates, temps, color='tab:red', marker='o')
       ax.set_title("Temperature en temps reel")
       ax.set_xlabel("Heure")
       ax.set_ylabel("Temperature(en degré Celcius")
       ax.tick_params(axis='x', rotation=45)
       ax.grid(True)
# Setup du matplotlib
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, interval=1000)

# Le client MQTT
client = mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect(BROKER, PORT, 60)
client.loop_start()  # execute MQTT en fond

# Lancement du graphique
plt.tight_layout()
plt.show()

# Apres la fermeture du graphe on aura un arrêt propre
client.loop_stop()
client.disconnect()