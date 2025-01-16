import requests
import random
import time
from datetime import datetime
from random import uniform

def get_all_sensors_of_user(user_id=1):
    url = f"http://localhost:3000/sensores/getSensoresUser/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch sensors for user {user_id}: {response.text}")
        return []

def send_measurement(sensor_id, tipo_gas, latitud, longitud, valor):
    url = "http://localhost:3000/mediciones/mediciones"
    payload = {
        "id_sensor": sensor_id,
        "tipo_gas": tipo_gas,
        "valor": valor,
        "fecha": datetime.now().isoformat(),
        "latitud": latitud,
        "longitud": longitud
    }
    response = requests.post(url, json=payload)
    if response.status_code != 201:
        print(f"Failed to send measurement for sensor {sensor_id}: {response.text}")

def generate_random_measurements(sensors):
    gases = ["CO2", "O3", "NO2", "SO2"]
    while True:
        selected_sensors = random.sample(sensors, 5)
        used_sensors = set()
        for sensor in selected_sensors:
            if sensor['id_sensor'] in used_sensors:
                continue
            used_sensors.add(sensor['id_sensor'])
            tipo_gas = random.choice(gases)
            latitud = uniform(39.0, 40.0)  # Approximate latitude range for Comunidad Valenciana
            longitud = uniform(-1.5, 0.5)  # Approximate longitude range for Comunidad Valenciana
            valor = round(uniform(0, 500), 2)  # Random value for gas concentration
            send_measurement(sensor['id_sensor'], tipo_gas, latitud, longitud, valor)
        time.sleep(random.randint(20, 30))

# Example usage
if __name__ == "__main__":
    sensors = get_all_sensors_of_user()
    if sensors:
        generate_random_measurements(sensors)
