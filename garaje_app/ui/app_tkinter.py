import tkinter as tk
from tkinter import ttk
from servicios.garaje_servicio import GarajeServicio


class AppGaraje:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Garaje")

        self.servicio = GarajeServicio()

        # ---- FORMULARIO ----

        tk.Label(root, text="Placa").grid(row=0, column=0, padx=10, pady=5)
        self.entry_placa = tk.Entry(root)
        self.entry_placa.grid(row=0, column=1)

        tk.Label(root, text="Marca").grid(row=1, column=0, padx=10, pady=5)
        self.entry_marca = tk.Entry(root)
        self.entry_marca.grid(row=1, column=1)

        tk.Label(root, text="Propietario").grid(row=2, column=0, padx=10, pady=5)
        self.entry_propietario = tk.Entry(root)
        self.entry_propietario.grid(row=2, column=1)

        # ---- BOTONES ----

        btn_agregar = tk.Button(root, text="Agregar Vehículo", command=self.agregar_vehiculo)
        btn_agregar.grid(row=3, column=0, pady=10)

        btn_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_campos)
        btn_limpiar.grid(row=3, column=1)

        # ---- TABLA ----

        self.tabla = ttk.Treeview(root, columns=("Placa", "Marca", "Propietario"), show="headings")

        self.tabla.heading("Placa", text="Placa")
        self.tabla.heading("Marca", text="Marca")
        self.tabla.heading("Propietario", text="Propietario")

        self.tabla.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def agregar_vehiculo(self):

        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        propietario = self.entry_propietario.get()

        if placa and marca and propietario:

            self.servicio.agregar_vehiculo(placa, marca, propietario)

            self.tabla.insert("", "end", values=(placa, marca, propietario))

            self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)