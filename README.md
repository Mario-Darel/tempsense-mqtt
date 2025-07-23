# tempsense-mqtt
# 🌡️ TempSense-MQTT

Un petit projet IoT réalisé en Python, visant à simuler un capteur de température qui envoie ses données via le protocole MQTT. Les données sont ensuite reçues et visualisées dans une interface simple.

## 🎯 Objectifs

- Simuler un capteur de température virtuel
- Envoyer les données via MQTT (publisher)
- Recevoir les données dans un autre script (subscriber)
- Visualiser les données en console ou avec une interface graphique

## 🧰 Technologies utilisées

- Python 3
- Paho-MQTT (client MQTT en Python)
- Mosquitto (broker MQTT local ou cloud)
- Tkinter / Matplotlib / Streamlit (à tester pour la visualisation)

## ⚙️ Installation rapide

```bash
git clone https://github.com/ton-pseudo/tempsense-mqtt.git
cd tempsense-mqtt
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
