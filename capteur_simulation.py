import random
import time
from datetime import datetime
def lire_temperature():
     """On va ici simuler la lecture d'une température entre 20 et 30 degrés.""" 
     return round(random.uniform(20.0, 30.0), 2)
def simuler_capteur(intervalle=6):
       """On va générer une température toutes les x secondes."""
       print("Simulation du capteur de température en cours(Ctrl+C pour arrêter)...\n")
       try:
          while True:
               temp=lire_temperature()
               horodatage=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
               print(f"[{horodatage}]  Temperature:{temp} degres Celsius.")
               time.sleep(intervalle)
       except KeyboardInterrupt:
               print("\nArret de la simulation du capteur.")

if __name__== "__main__":
        simuler_capteur()