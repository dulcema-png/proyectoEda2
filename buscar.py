"""
Módulo: buscar.py
Requisito: Algoritmo de Búsqueda Binaria por ID (requiere previo ordenamiento).
"""

def busqueda_binaria(clientes_ordenados, id_buscado):
    izquierda = 0
    derecha = len(clientes_ordenados) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        id_actual = clientes_ordenados[medio]["id"]
        if id_actual == id_buscado:
            return clientes_ordenados[medio]
        elif id_actual < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None
