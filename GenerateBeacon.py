# generar 200 beacons

import uuid
from SensorAndMedicion import Sensor
import requests

def generate_beacons(num_beacons=200):
    beacons = []
    for i in range(num_beacons):
        beacon = Sensor(
            id=i,
            estado="activo",
            num_referencia=i,
            uuid=str(uuid.uuid4()),
            nombre=f"Beacon_{i}",
            conexion=False,
            bateria=100
        )
        beacons.append(beacon)
    return beacons

def register_beacons(beacons):
    url = "http://localhost:3000/usuarios/registrar-sensor"
    for beacon in beacons:
        payload = {
            "id_usuario": 1,  # Assuming a default user ID for this example
            "estado": beacon.estado,
            "num_referencia": beacon.num_referencia,
            "uuid": beacon.uuid,
            "nombre": beacon.nombre,
            "conexion": beacon.conexion,
            "bateria": beacon.bateria
        }
        response = requests.post(url, json=payload)
        if response.status_code != 201:
            print(f"Failed to register beacon {beacon.id}: {response.text}")

# Example usage
if __name__ == "__main__":
    beacons = generate_beacons()
    register_beacons(beacons)

