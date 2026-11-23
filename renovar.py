"""
Módulo: renovar.py
Requisito: Renovación de membresía por ID que actualiza el vencimiento
y se conserva al reiniciar.
"""

from datetime import date, timedelta
from operaciones import guardar_archivo, leer_entero, leer_fecha


def renovar_membresia(clientes):
    print("\n--- RENOVAR MEMBRESÍA POR ID ---")
    if not clientes:
        print("No hay clientes cargados en memoria para renovar.")
        return

    id_buscado = leer_entero("Ingresa el ID del cliente a renovar: ")

    cliente_objetivo = None
    for c in clientes:
        if c["id"] == id_buscado:
            cliente_objetivo = c
            break

    if not cliente_objetivo:
        print(f"No se encontró ningún cliente con el ID {id_buscado}.")
        return

    print(
        f"Cliente seleccionado: {cliente_objetivo['nombre']} "
        f"| Actual: {cliente_objetivo['tipo_membresia']} "
        f"| Vence: {cliente_objetivo['fecha_vencimiento']}"
    )

    print("\nSeleccione el nuevo tipo de membresía:")
    print("1. Diaria ($80)")
    print("2. Mensual ($500)")
    print("3. Anual ($4500)")
    opcion = leer_entero("Ingrese la opción (1-3): ")

    if opcion == 1:
        tipo = "Diaria"
        precio = 80.0
        dias_duracion = 1
    elif opcion == 2:
        tipo = "Mensual"
        precio = 500.0
        dias_duracion = 30
    elif opcion == 3:
        tipo = "Anual"
        precio = 4500.0
        dias_duracion = 365
    else:
        print("Opción inválida. Se asigna Mensual ($500) por defecto.")
        tipo = "Mensual"
        precio = 500.0
        dias_duracion = 30

    print("\n¿Cómo deseas definir la nueva vigencia?")
    print("1. Calcular automáticamente desde hoy")
    print("2. Ingresar fecha de inicio manual (AAAA-MM-DD) y calcular vencimiento")
    print("3. Ingresar fecha de inicio y fecha de vencimiento manualmente")
    modo_fecha = leer_entero("Selecciona una opción (1-3): ")

    if modo_fecha == 2:
        fecha_inicio = leer_fecha("Ingrese la nueva fecha de inicio (AAAA-MM-DD): ")
        inicio_dt = date.fromisoformat(fecha_inicio)
        fecha_vencimiento = (inicio_dt + timedelta(days=dias_duracion)).isoformat()
    elif modo_fecha == 3:
        fecha_inicio = leer_fecha("Ingrese la nueva fecha de inicio (AAAA-MM-DD): ")
        fecha_vencimiento = leer_fecha("Ingrese la nueva fecha de vencimiento (AAAA-MM-DD): ")
        if fecha_vencimiento < fecha_inicio:
            print("Error: La fecha de vencimiento no puede ser anterior a la fecha de inicio.")
            return
    else:
        inicio_dt = date.today()
        fecha_inicio = inicio_dt.isoformat()
        fecha_vencimiento = (inicio_dt + timedelta(days=dias_duracion)).isoformat()

    cliente_objetivo["tipo_membresia"] = tipo
    cliente_objetivo["fecha_inicio"] = fecha_inicio
    cliente_objetivo["fecha_vencimiento"] = fecha_vencimiento
    cliente_objetivo["cantidad_pagada"] = precio

    if guardar_archivo(clientes):
        print(
            f"¡Membresía renovada! Nuevo vencimiento para {cliente_objetivo['nombre']} "
            f"(ID: {cliente_objetivo['id']}): {fecha_vencimiento}."
        )
