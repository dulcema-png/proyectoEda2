"""
Módulo: mostrar.py
Requisito: Consulta general de registros almacenados en la lista.
"""

def mostrar_clientes(clientes):
    if not clientes:
        print("No hay clientes registrados.")
        return
    for cliente in clientes:
        print("--------------------------------------------------")
        print(f"ID: {cliente['id']} | Nombre: {cliente['nombre']}")
        print(f"Membresía: {cliente['tipo_membresia']} | Pagado: ${cliente['cantidad_pagada']}")
        print(f"Inicio: {cliente['fecha_inicio']} | Vencimiento: {cliente['fecha_vencimiento']}")
