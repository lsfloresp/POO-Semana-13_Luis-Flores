# Sistema Básico de Gestión de Garaje 🚗

Aplicación de escritorio desarrollada en **Python utilizando Tkinter** que permite registrar vehículos que ingresan a un garaje y visualizar la información desde una interfaz gráfica.

## Autor

**Luis Santiago Flores Piña**

## Descripción

Este proyecto implementa una aplicación GUI que permite registrar vehículos dentro de un garaje.
El sistema almacena información básica del vehículo y muestra los registros en una tabla dentro de la interfaz.

El programa está desarrollado siguiendo una **arquitectura modular**, separando el código en diferentes carpetas para mejorar la organización y mantenimiento.

## Funcionalidades

* Registrar vehículos ingresando:

  * Placa
  * Marca
  * Propietario
* Mostrar los vehículos registrados en una tabla.
* Limpiar los campos del formulario.
* Guardar los vehículos en un archivo para mantener los datos registrados.

## Tecnologías utilizadas

* **Python**
* **Tkinter** (interfaz gráfica)
* **JSON** para almacenamiento de datos (Adicional)

## Estructura del proyecto

```
garaje_app/
│
├── main.py
│
├── modelos/
│   └── vehiculo.py
│
├── servicios/
│   └── garaje_servicio.py
│
└── ui/
    └── app_tkinter.py
```

### Descripción de carpetas

**modelos/**
Contiene las clases que representan las entidades del sistema. En este caso la clase `Vehiculo`.

**servicios/**
Contiene la lógica del programa, como agregar vehículos y obtener la lista de vehículos registrados.

**ui/**
Contiene la interfaz gráfica desarrollada con Tkinter.

**main.py**
Archivo principal que inicia la aplicación.

## Ejecución del programa

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```
python main.py
```

Esto abrirá la ventana de la aplicación donde se podrán registrar los vehículos.

## Objetivo académico

Este proyecto fue desarrollado como parte de una práctica académica para aplicar conceptos de:

* Desarrollo de interfaces gráficas en Python.
* Arquitectura modular en aplicaciones.
* Organización del código en modelos, servicios y UI.
