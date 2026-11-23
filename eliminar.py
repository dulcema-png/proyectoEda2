"""
Módulo: eliminar.py
Requisito: Baja de registros por ID usando operaciones de lista (.pop()),
actualización en txt y respeto al bloqueo de guardado.
"""

from operaciones import guardar_archivo, leer_entero


def eliminar_cliente(clientes):
    print("\n--- ELIMINAR CLIENTE ---")
    if not clientes:
        print("No hay clientes registrados.")
        return

    id_buscado = leer_entero("Ingresa el ID del cliente a eliminar: ")

    for i in range(len(clientes)):
        if clientes[i]["id"] == id_buscado:
            cliente_eliminado = clientes.pop(i)  # Operación de eliminación en lista
            if guardar_archivo(clientes):
                print("¡Cliente eliminado correctamente de la lista y del archivo!")
            else:
                clientes.insert(i, cliente_eliminado)
                print("No se eliminó el cliente porque el guardado está bloqueado.")
            return

    print("No se encontró ningún cliente con ese ID.")
