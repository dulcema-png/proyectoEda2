from operaciones import (
    cargar_clientes,
    leer_entero,
    renovar_membresia_en_operaciones,
)
from mostrar import mostrar_clientes
from ordenar_id import quick_sort
from ordenar_vencimiento import merge_sort
from buscar import busqueda_binaria
from membresias import revisar_membresias
from agregar import agregar_cliente
from eliminar import eliminar_cliente


def menu():
    clientes, carga_exitosa = cargar_clientes()
    if carga_exitosa:
        print("\n[Sistema GYM Manager]: Archivo cargado exitosamente.")
    else:
        print("\n[Sistema GYM Manager]: Archivo cargado con advertencias o vacío (guardado deshabilitado).")

    while True:
        print("\n========================================")
        print("          GYM MANAGER - MENÚ          ")
        print("========================================")
        print("1. Mostrar todos los clientes")
        print("2. Ordenar clientes por ID (QuickSort)")
        print("3. Ordenar por vencimiento (MergeSort)")
        print("4. Buscar cliente por ID (Búsqueda Binaria)")
        print("5. Revisar membresías (Tercera Funcionalidad)")
        print("6. Agregar nuevo cliente (Con precios fijos)")
        print("7. Eliminar cliente por ID")
        print("8. Renovar membresía por ID")
        print("9. Salir")

        opcion = leer_entero("Selecciona una opción: ")

        if opcion == 1:
            mostrar_clientes(clientes)
        elif opcion == 2:
            clientes = quick_sort(clientes)
            print("\nClientes ordenados por ID:")
            mostrar_clientes(clientes)
        elif opcion == 3:
            clientes = merge_sort(clientes)
            print("\nClientes ordenados por fecha de vencimiento:")
            mostrar_clientes(clientes)
        elif opcion == 4:
            clientes_ordenados = quick_sort(clientes)
            id_buscado = leer_entero("Ingresa el ID del cliente a buscar: ")
            resultado = busqueda_binaria(clientes_ordenados, id_buscado)
            if resultado:
                print("\n¡Cliente encontrado!")
                mostrar_clientes([resultado])
            else:
                print("No se encontró ningún cliente con ese ID.")
        elif opcion == 5:
            revisar_membresias(clientes)
        elif opcion == 6:
            agregar_cliente(clientes)
        elif opcion == 7:
            eliminar_cliente(clientes)
        elif opcion == 8:
            renovar_membresia_en_operaciones(clientes)
        elif opcion == 9:
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()
