# GymManager — Sistema de Gestión de Gimnasio

**Facultad de Ingeniería — UNAM**  
**Asignatura:** Estructuras de Datos y Algoritmos II  
**Grupo:** 8  
**Profesor:** Ing. Manuel Ivan Salgado Garduño  
**Instancia:** Segundo Avance  

### Integrantes del Equipo
* González Alcántara Gabriel Uriel
* Soto Montes Vanessa
* Yañez Guerrero Dulce Maria

---

## 1. Información General y Cambios del Proyecto

* **Nombre del Proyecto:** `GymManager`
* **Problema que resuelve:** Sistema de recepción para registrar, consultar, actualizar, renovar, dar de baja y analizar clientes y membresías de un gimnasio a partir de persistencia en archivo de texto (`clientes.txt`).
* **Cambios realizados para el Segundo Avance:**
  * Se consolidó la arquitectura modular en Python (`main.py`, `operaciones.py`, `mostrar.py`, `ordenar_id.py`, `ordenar_vencimiento.py`, `buscar.py`, `membresias.py`, `agregar.py`, `eliminar.py` y `renovar.py`).
  * Se integraron **QuickSort** (por ID), **MergeSort** (por fecha de vencimiento), **Búsqueda Binaria** (por ID) y el **Reporte y Clasificación de Membresías** (tercera funcionalidad algorítmica, sin necesidad de agregar un grafo artificial).
  * Se incorporó el alta de nuevos clientes con precios fijos por plan (*Diaria* $80, *Mensual* $500, *Anual* $4500), baja por ID (`.pop()`) y renovación de membresía por ID con actualización persistente en `clientes.txt`.
  * Se amplió el catálogo inicial automático de 10 a **100 registros** (`_generar_datos_iniciales(100)`) cuando `clientes.txt` no existe, superando el mínimo requerido de 15 registros.
  * Se implementó detección de archivos vacíos o malformados con **bloqueo de guardado** (`ARCHIVO_VALIDO`) para evitar sobrescribir o vaciar datos válidos.
  * Se añadieron validaciones estrictas de entrada (`leer_entero`, `leer_nombre`, `leer_fecha` con formato `AAAA-MM-DD` y bloqueo de fechas pasadas al registrar).

---

## 2. Estructuras de Datos y Arquitectura Modular

Se utiliza una **lista de diccionarios** en memoria (`clientes`), donde cada diccionario representa a un cliente con las siguientes claves:

* `id` (`int`): Identificador único del cliente.
* `nombre` (`str`): Nombre completo del cliente.
* `tipo_membresia` (`str`): Plan contratado (`Diaria`, `Mensual` o `Anual`).
* `fecha_inicio` (`str`): Fecha de inicio en formato `AAAA-MM-DD`.
* `fecha_vencimiento` (`str`): Fecha de vencimiento en formato `AAAA-MM-DD`.
* `cantidad_pagada` (`float`): Monto pagado por la membresía.

**Justificación:** Una lista dinámica permite recorrer, insertar, eliminar (`.pop()`) y aplicar algoritmos de ordenamiento y búsqueda indexada de forma directa, mientras que cada diccionario agrupa con claridad los atributos de cada socio.

### Módulos del proyecto
* `main.py`: Menú principal e integración de todas las opciones.
* `operaciones.py`: Carga inicial, generación de 100 registros si no existe el archivo, validación de integridad, bloqueo de guardado, renovación por ID y validaciones de entrada.
* `mostrar.py`: Impresión en consola de los registros de clientes.
* `ordenar_id.py`: Ordenamiento por `id` mediante **QuickSort**.
* `ordenar_vencimiento.py`: Ordenamiento por `fecha_vencimiento` mediante **MergeSort**.
* `buscar.py`: Localización por `id` mediante **Búsqueda Binaria**.
* `membresias.py`: Clasificación de vigencia respecto a la fecha actual.
* `agregar.py`: Alta de clientes con validación de campos y precios fijos.
* `eliminar.py`: Eliminación de clientes por `id` y sincronización con el archivo.
* `renovar.py`: Módulo de renovación de membresías con cálculo automático o manual de fechas.

---

## 3. Algoritmos Implementados y Complejidad

### 1. QuickSort (Ordenamiento por ID)
* **Propósito:** Ordenar la lista de clientes de menor a mayor según su `id`.
* **Funcionamiento:** Elige un pivote central, separa los elementos en menores, iguales y mayores al pivote, y ordena recursivamente las sublistas.
* **Complejidad temporal:** $O(n \log n)$ en caso promedio; $O(n^2)$ en el peor caso.

### 2. MergeSort (Ordenamiento por Fecha de Vencimiento)
* **Propósito:** Ordenar a los clientes cronológicamente según `fecha_vencimiento` (`AAAA-MM-DD`).
* **Funcionamiento:** Divide recursivamente la lista en mitades hasta llegar a sublistas unitarias y las fusiona de forma ordenada mediante la función `mezclar`.
* **Complejidad temporal:** $O(n \log n)$ en el mejor, promedio y peor caso.

### 3. Búsqueda Binaria (Localización por ID)
* **Propósito:** Buscar un cliente específico a partir de su `id`.
* **Funcionamiento:** Ordena previamente la lista por `id` con `quick_sort`, compara el ID buscado con el elemento central y descarta en cada paso la mitad donde no puede encontrarse.
* **Complejidad temporal:** $O(\log n)$.

### 4. Reporte y Clasificación de Membresías (Tercera Funcionalidad)
* **Propósito:** Evaluar la vigencia de cada membresía respecto a `date.today()`.
* **Funcionamiento:** Calcula `dias = (fecha_vencimiento - fecha_hoy).days` para cada registro y clasifica en:
  * **Vencidas:** `dias < 0`
  * **Próximas a vencer (alerta):** `0 <= dias <= 7` (incluye hoy y hasta en 7 días)
  * **Vigentes:** `dias > 7`
* **Complejidad temporal:** $O(n)$ (recorrido lineal).

---

## 4. Requisitos y Instrucciones de Ejecución

* **Lenguaje:** Python 3.8 o superior.
* **Dependencias externas:** Ninguna (usa únicamente módulos de la biblioteca estándar de Python: `os`, `datetime`).

### Pasos para ejecutar
1. Verifica que Python 3 esté instalado en tu equipo (`python --version` o `python3 --version`).
2. Descarga o clona la carpeta del proyecto en tu equipo y abre una terminal dentro de ella.
3. Ejecuta el programa principal:
   ```bash
   python main.py
