import tkinter as tk
from tkinter import ttk
from servicios.garaje_servicio import GarajeServicio


class AppGaraje:

    def __init__(self, root):

        self.root = root
        self.root.title("Sistema de Gestión de Garaje")
        self.root.geometry("600x400")
        self.root.configure(bg="#2C3E50")

        self.servicio = GarajeServicio()

        # TITULO
        titulo = tk.Label(
            root,
            text="🚗 Sistema de Gestión de Garaje",
            font=("Arial", 18, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        titulo.pack(pady=10)

        # FRAME FORMULARIO
        frame_form = tk.Frame(root, bg="#34495E")
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Placa", bg="#34495E", fg="white").grid(row=0, column=0, padx=10, pady=5)
        self.entry_placa = tk.Entry(frame_form)
        self.entry_placa.grid(row=0, column=1)

        tk.Label(frame_form, text="Marca", bg="#34495E", fg="white").grid(row=1, column=0, padx=10, pady=5)
        self.entry_marca = tk.Entry(frame_form)
        self.entry_marca.grid(row=1, column=1)

        tk.Label(frame_form, text="Propietario", bg="#34495E", fg="white").grid(row=2, column=0, padx=10, pady=5)
        self.entry_propietario = tk.Entry(frame_form)
        self.entry_propietario.grid(row=2, column=1)

        # BOTONES
        frame_botones = tk.Frame(root, bg="#2C3E50")
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(
            frame_botones,
            text="Agregar Vehículo",
            command=self.agregar_vehiculo,
            bg="#27AE60",
            fg="white",
            width=15
        )
        btn_agregar.grid(row=0, column=0, padx=10)

        btn_limpiar = tk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar_campos,
            bg="#E67E22",
            fg="white",
            width=15
        )
        btn_limpiar.grid(row=0, column=1, padx=10)

        # TABLA
        frame_tabla = tk.Frame(root)
        frame_tabla.pack(pady=10)

        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=("Placa", "Marca", "Propietario"),
            show="headings",
            height=8
        )

        self.tabla.heading("Placa", text="Placa")
        self.tabla.heading("Marca", text="Marca")
        self.tabla.heading("Propietario", text="Propietario")

        self.tabla.column("Placa", width=120)
        self.tabla.column("Marca", width=150)
        self.tabla.column("Propietario", width=180)

        self.tabla.pack()

        # cargar datos guardados
        self.cargar_tabla()

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

    def cargar_tabla(self):

        for v in self.servicio.obtener_vehiculos():
            self.tabla.insert("", "end", values=(v.placa, v.marca, v.propietario))