import json
import os
from modelos.vehiculo import Vehiculo


class GarajeServicio:

    def __init__(self):
        self.archivo = "vehiculos.json"
        self.vehiculos = []
        self.cargar_vehiculos()

    def cargar_vehiculos(self):

        if os.path.exists(self.archivo):

            with open(self.archivo, "r") as f:
                datos = json.load(f)

                for v in datos:
                    vehiculo = Vehiculo(v["placa"], v["marca"], v["propietario"])
                    self.vehiculos.append(vehiculo)

    def guardar_vehiculos(self):

        datos = []

        for v in self.vehiculos:
            datos.append({
                "placa": v.placa,
                "marca": v.marca,
                "propietario": v.propietario
            })

        with open(self.archivo, "w") as f:
            json.dump(datos, f, indent=4)

    def agregar_vehiculo(self, placa, marca, propietario):

        vehiculo = Vehiculo(placa, marca, propietario)
        self.vehiculos.append(vehiculo)

        self.guardar_vehiculos()

    def obtener_vehiculos(self):
        return self.vehiculos