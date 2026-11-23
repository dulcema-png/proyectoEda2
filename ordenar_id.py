"""
Módulo: ordenar_id.py
Requisito: Algoritmo de Ordenamiento 1 (QuickSort) basado en ID de clientes.
"""

def quick_sort(clientes):
    if len(clientes) <= 1:
        return clientes
    pivote = clientes[len(clientes) // 2]["id"]
    menores = [c for c in clientes if c["id"] < pivote]
    iguales = [c for c in clientes if c["id"] == pivote]
    mayores = [c for c in clientes if c["id"] > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)
