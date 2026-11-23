"""
Módulo: operaciones.py
Requisito: Manejo de archivos, persistencia (100 registros iniciales),
detección de archivos vacíos/corruptos con bloqueo de guardado,
renovación automática de membresía por ID y validaciones estrictas.
"""

from datetime import datetime, date, timedelta
import os

NOMBRE_ARCHIVO = "clientes.txt"

# Bandera global: solo se permite guardar si la carga fue íntegra
# o si el archivo no existía y se creó el catálogo inicial válido.
ARCHIVO_VALIDO = False


def _generar_datos_iniciales(total_registros=100):
    nombres_base = [
        "Armando Solis", "Carlos Ruiz", "Ana Lopez", "Luis Perez", "Maria Torres",
        "Pedro Garcia", "Sofia Hernandez", "Diego Flores", "Daniela Cruz", "Jorge Morales",
        "Carmen Gomez", "Javier Ramirez", "Lucia Fernandez", "Miguel Angel", "Elena Rojas",
        "Fernando Torres", "Gabriela Diaz", "Ricardo Morales", "Valeria Castro", "Alejandro Ortiz",
        "Rosa Martinez", "Mario Jimenez", "Beatriz Mendoza", "Raul Castillo", "Patricia Silva",
        "Gabriel Uriel", "Vanessa Soto", "Dulce Maria", "Esteban Quito", "Gloria Trevi",
        "Hugo Sanchez", "Irene Castillo", "Joaquin Sabina", "Karla Panini", "Leonardo Davinci",
        "Monica Naranjo", "Nicolas Maduro", "Olivia Wilde", "Pablo Picasso", "Quintin Tarantino",
        "Rocio Durcal", "Sergio Ramos", "Tatiana Palacios", "Ulises Eyra", "Vicente Fernandez",
        "Wendy Sulca", "Ximena Sarinana", "Yahir Olea", "Zoe Saldana", "Alan Brito",
        "Alberto Navarro", "Andrea Reyes", "Arturo Mendoza", "Brenda Vargas", "Cesar Delgado",
        "Claudia Ortiz", "David Romero", "Diana Herrera", "Eduardo Guzman", "Erika Sandoval",
        "Francisco Vega", "Gisela Campos", "Hector Maldonado", "Ilse Fuentes", "Ivan Rios",
        "Jessica Ponce", "Josefa Lara", "Karina Lozano", "Lorenzo Ibarra", "Mariana Guerrero",
        "Martin Solorzano", "Natalia Contreras", "Oscar Salazar", "Paola Dominguez", "Ramiro Escobar",
        "Rebeca Montoya", "Rodrigo Nunez", "Sandra Cabrera", "Sebastian Rios", "Silvia Villalobos",
        "Tomas Cisneros", "Veronica Meza", "Victor Alcaraz", "Xochitl Pineda", "Yolanda Espinoza",
        "Adrian Pacheco", "Alejandra Luna", "Alfonso Tellez", "Alicia Cordero", "Andres Benitez",
        "Angela Galvan", "Antonio Barrios", "Araceli Camacho", "Bruno Santamaria", "Camila Valdes",
        "Cristian Trejo", "Deborah Rosales", "Emilio Quintero", "Esmeralda Pech", "Fabian Zuniga"
    ]
    tipos = ["Mensual", "Anual", "Diaria"]
    precios = {"Mensual": 500.0, "Anual": 4500.0, "Diaria": 80.0}

    datos_iniciales = []
    for i in range(total_registros):
        id_val = 1000 + i
        nombre = nombres_base[i % len(nombres_base)]
        tipo = tipos[i % 3]
        precio = precios[tipo]
        mes = (i % 12) + 1
        dia = (i % 28) + 1
        fecha_inicio = f"2026-{mes:02d}-{dia:02d}"

        if tipo == "Anual":
            fecha_vencimiento = f"2027-{mes:02d}-{dia:02d}"
        elif tipo == "Mensual":
            s_mes = mes + 1 if mes < 12 else 1
            s_anio = 2026 if mes < 12 else 2027
            fecha_vencimiento = f"{s_anio}-{s_mes:02d}-{dia:02d}"
        else:
            fecha_vencimiento = fecha_inicio

        datos_iniciales.append({
            "id": id_val,
            "nombre": nombre,
            "tipo_membresia": tipo,
            "fecha_inicio": fecha_inicio,
            "fecha_vencimiento": fecha_vencimiento,
            "cantidad_pagada": precio
        })
    return datos_iniciales


def cargar_clientes():
    """
    Carga clientes desde clientes.txt.
    Retorna una tupla: (lista_clientes, carga_exitosa).
    Si el archivo no existe, crea 100 registros iniciales válidos.
    Si el archivo está vacío o tiene líneas inválidas, marca carga_exitosa = False
    y bloquea el guardado hasta que se recupere un archivo válido.
    """
    global ARCHIVO_VALIDO
    ARCHIVO_VALIDO = False

    if not os.path.exists(NOMBRE_ARCHIVO):
        datos_iniciales = _generar_datos_iniciales(100)
        try:
            with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
                for c in datos_iniciales:
                    f.write(
                        f"{c['id']},{c['nombre']},{c['tipo_membresia']},"
                        f"{c['fecha_inicio']},{c['fecha_vencimiento']},{c['cantidad_pagada']}\n"
                    )
            ARCHIVO_VALIDO = True
            return datos_iniciales, True
        except Exception as e:
            print(f"\n[Error]: No se pudo crear '{NOMBRE_ARCHIVO}': {e}")
            return [], False

    clientes = []
    lineas_no_vacias = 0
    errores_formato = []

    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
            for num_linea, linea in enumerate(f, start=1):
                contenido = linea.strip()
                if not contenido:
                    continue
                lineas_no_vacias += 1
                partes = contenido.split(",")

                if len(partes) != 6:
                    errores_formato.append(
                        f"Línea {num_linea}: se esperaban 6 campos, se encontraron {len(partes)}."
                    )
                    continue

                try:
                    id_val = int(partes[0].strip())
                    nombre = partes[1].strip()
                    tipo = partes[2].strip()
                    f_inicio = datetime.strptime(partes[3].strip(), "%Y-%m-%d").date().strftime("%Y-%m-%d")
                    f_venc = datetime.strptime(partes[4].strip(), "%Y-%m-%d").date().strftime("%Y-%m-%d")
                    monto = float(partes[5].strip())

                    if not nombre or not tipo or monto < 0:
                        errores_formato.append(f"Línea {num_linea}: datos de negocio inválidos.")
                        continue

                    clientes.append({
                        "id": id_val,
                        "nombre": nombre,
                        "tipo_membresia": tipo,
                        "fecha_inicio": f_inicio,
                        "fecha_vencimiento": f_venc,
                        "cantidad_pagada": monto
                    })
                except ValueError as ve:
                    errores_formato.append(f"Línea {num_linea}: error de tipo/fecha ({ve}).")

    except Exception as e:
        print(f"\n[Error crítico]: No se pudo leer '{NOMBRE_ARCHIVO}': {e}")
        print("[Guardado bloqueado]: Repara o restaura el archivo antes de guardar cambios.")
        return [], False

    if lineas_no_vacias == 0:
        print(f"\n[Alerta]: El archivo '{NOMBRE_ARCHIVO}' está vacío.")
        print("[Guardado bloqueado]: No se pueden guardar cambios hasta recuperar datos válidos.")
        return [], False

    if errores_formato:
        print(f"\n[Alerta]: Se detectaron filas malformadas o inválidas en '{NOMBRE_ARCHIVO}':")
        for err in errores_formato:
            print(f"  - {err}")
        print("[Guardado bloqueado]: Corrige el archivo o restaura una copia válida antes de guardar.")
        return [], False

    ARCHIVO_VALIDO = True
    return clientes, True


def guardar_archivo(clientes):
    """
    Guarda los cambios en clientes.txt solo si ARCHIVO_VALIDO es True.
    Impide sobrescribir o vaciar el archivo cuando hubo error de carga o archivo vacío.
    """
    if not ARCHIVO_VALIDO:
        print("\n[Guardado bloqueado]: El archivo actual presentó errores o estaba vacío al cargarse.")
        print("Recupera/corrige 'clientes.txt' y reinicia el programa para habilitar el guardado.")
        return False

    try:
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
            for c in clientes:
                f.write(
                    f"{c['id']},{c['nombre']},{c['tipo_membresia']},"
                    f"{c['fecha_inicio']},{c['fecha_vencimiento']},{c['cantidad_pagada']}\n"
                )
        print("¡Cambios guardados en el archivo permanentemente!")
        return True
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False


def renovar_membresia_en_operaciones(clientes):
    """
    Busca un cliente por ID, solicita el plan (Diaria, Mensual o Anual),
    calcula el vencimiento automáticamente desde hoy y guarda el cambio.
    """
    print("\n--- RENOVAR MEMBRESÍA POR ID ---")
    if not clientes:
        print("No hay clientes cargados en memoria para renovar.")
        return False

    id_buscado = leer_entero("Ingresa el ID del cliente a renovar: ")

    cliente_objetivo = None
    for c in clientes:
        if c["id"] == id_buscado:
            cliente_objetivo = c
            break

    if not cliente_objetivo:
        print(f"No se encontró ningún cliente con el ID {id_buscado}.")
        return False

    print(
        f"Cliente seleccionado: {cliente_objetivo['nombre']} "
        f"| Actual: {cliente_objetivo['tipo_membresia']} "
        f"| Vence: {cliente_objetivo['fecha_vencimiento']}"
    )

    print("\nSeleccione el tipo de membresía:")
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

    inicio_dt = date.today()
    fecha_inicio = inicio_dt.isoformat()
    fecha_vencimiento = (inicio_dt + timedelta(days=dias_duracion)).isoformat()

    cliente_objetivo["tipo_membresia"] = tipo
    cliente_objetivo["fecha_inicio"] = fecha_inicio
    cliente_objetivo["fecha_vencimiento"] = fecha_vencimiento
    cliente_objetivo["cantidad_pagada"] = precio

    if guardar_archivo(clientes):
        print(
            f"La membresía se renovó automáticamente ({tipo}). "
            f"Nuevo vencimiento para {cliente_objetivo['nombre']} "
            f"(ID: {cliente_objetivo['id']}): {fecha_vencimiento}."
        )
        return True

    return False


def leer_entero(mensaje):
    """Valida estrictamente que la entrada sea un número entero (evita letras en el ID)."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número entero válido (no se permiten letras).")


def leer_nombre(mensaje):
    """Valida que el nombre contenga únicamente letras y espacios (evita números en el nombre)."""
    while True:
        nombre = input(mensaje).strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            continue
        if all(c.isalpha() or c.isspace() for c in nombre):
            return nombre
        print("Error: El nombre solo debe contener letras (sin números ni caracteres extraños).")


def leer_fecha(mensaje):
    """Valida estrictamente el formato AAAA-MM-DD y evita que se ingresen fechas pasadas."""
    fecha_actual = date.today()

    while True:
        fecha_str = input(mensaje).strip()
        try:
            fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            if fecha_obj < fecha_actual:
                print(f"Error: No puedes registrar fechas pasadas (la fecha actual es {fecha_actual}).")
                continue
            return fecha_str
        except ValueError:
            print("Error: Formato inválido. Usa estrictamente AAAA-MM-DD (Ej. 2026-11-15).")
