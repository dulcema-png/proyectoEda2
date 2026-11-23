"""
Módulo: agregar.py
Requisito: Pide los datos por separado campo por campo, aplica precios fijos,
regresa al menú si hay un error de validación y respeta el bloqueo de guardado.
"""

from operaciones import guardar_archivo, leer_entero, leer_nombre, leer_fecha


def agregar_cliente(clientes):
    print("\n--- REGISTRAR NUEVO CLIENTE ---")

    # Valida que el ID sea estrictamente numérico
    id_cliente = leer_entero("Ingrese el ID: ")
    for c in clientes:
        if c["id"] == id_cliente:
            print("Error: Ya existe un cliente con ese ID. Regresando al menú...")
            return

    # Valida que el nombre no contenga números
    nombre = leer_nombre("Ingrese el nombre: ")

    print("\nSeleccione el tipo de membresía:")
    print("1. Diaria ($80)")
    print("2. Mensual ($500)")
    print("3. Anual ($4500)")
    opcion = leer_entero("Ingrese la opción (1-3): ")

    if opcion == 1:
        tipo = "Diaria"
        precio = 80.0
    elif opcion == 2:
        tipo = "Mensual"
        precio = 500.0
    elif opcion == 3:
        tipo = "Anual"
        precio = 4500.0
    else:
        print("Opción inválida. Se asigna Mensual ($500) por defecto.")
        tipo = "Mensual"
        precio = 500.0

    # Pide las fechas por separado con formato estructurado
    fecha_inicio = leer_fecha("Ingrese la fecha de inicio (AAAA-MM-DD): ")
    fecha_vencimiento = leer_fecha("Ingrese la fecha de vencimiento (AAAA-MM-DD): ")

    nuevo = {
        "id": id_cliente,
        "nombre": nombre,
        "tipo_membresia": tipo,
        "fecha_inicio": fecha_inicio,
        "fecha_vencimiento": fecha_vencimiento,
        "cantidad_pagada": precio
    }

    clientes.append(nuevo)
    if guardar_archivo(clientes):
        print("¡Cliente agregado exitosamente!")
    else:
        clientes.pop()
        print("No se agregó el cliente porque el guardado está bloqueado.")
