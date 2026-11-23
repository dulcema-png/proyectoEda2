"""
Módulo: ordenar_vencimiento.py
Requisito: Algoritmo de Ordenamiento 2 (MergeSort) basado en fecha de vencimiento.
"""

def mezclar(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i]["fecha_vencimiento"] <= derecha[j]["fecha_vencimiento"]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def merge_sort(clientes):
    if len(clientes) <= 1:
        return clientes
    mitad = len(clientes) // 2
    izquierda = merge_sort(clientes[:mitad])
    derecha = merge_sort(clientes[mitad:])
    return mezclar(izquierda, derecha)
