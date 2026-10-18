#  GymManager — Sistema de Gestión de Gimnasio

**Facultad de Ingeniería — UNAM**  
**Asignatura:** Estructuras de Datos y Algoritmos II  
**Grupo:** 8  
**Profesor:** Ing. Manuel Ivan Salgado Garduño  

---

##  Integrantes del Equipo
* González Alcántara Gabriel Uriel
* Soto Montes Vanessa
* Yañez Guerrero Dulce Maria

---

##  1. Información General y Cambios del Proyecto
* **Nombre del Proyecto:** GymManager
* **Problema que resuelve:** Sistema de recepción para registrar, administrar y consultar información de clientes y membresías de un gimnasio de forma eficiente.
* **Cambios desde el primer avance:** No se realizó ningún cambio significativo; se conserva la propuesta inicial del sistema de recepción. Para este segundo avance, se integraron oficialmente los algoritmos de ordenamiento **QuickSort** (por ID) y **MergeSort** (por fecha de vencimiento), así como la estrategia de **búsqueda binaria** por ID y el módulo de **reporte de membresías**.

---

## 2. Estructuras de Datos Utilizadas
Se implementó una **lista de diccionarios**, donde cada diccionario almacena los datos individuales de un cliente:
* `id`: Identificador único del cliente.
* `nombre`: Nombre completo.
* `tipo_membresia`: Categoría del pase.
* `fecha_inicio`: Fecha de alta en formato `YYYY-MM-DD`.
* `fecha_vencimiento`: Fecha límite del servicio en formato `YYYY-MM-DD`.
* `pago`: Estatus o monto del pago.

**Justificación:** Esta estructura es adecuada porque permite almacenar de manera dinámica a múltiples clientes, facilitando el acceso y la modificación de sus atributos. Además, una lista se adapta de forma natural para aplicar algoritmos de ordenamiento avanzados como *QuickSort* y *MergeSort* mediante índices.

---

## 3. Algoritmos Implementados y Complejidad

### 1. QuickSort (Ordenamiento por ID)
* **Propósito:** Ordena a los clientes de menor a mayor según su ID.
* **Funcionamiento:** Selecciona un elemento pivote y divide la lista en tres sublistas (menores, iguales y mayores al pivote), repitiendo el proceso recursivamente.
* **Complejidad temporal:** $O(n \log n)$ en promedio.

### 2. MergeSort (Ordenamiento por Vencimiento)
* **Propósito:** Ordena a los clientes según la fecha de vencimiento de su membresía.
* **Funcionamiento:** Divide la lista recursivamente en mitades hasta tener elementos individuales, y luego los recombina de forma ordenada comparando las fechas.
* **Complejidad temporal:** $O(n \log n)$ en el peor y mejor de los casos.

### 3. Búsqueda Binaria (Localización por ID)
* **Propósito:** Localiza de manera rápida a un cliente a partir de su ID.
* **Funcionamiento:** Requiere que la lista esté previamente ordenada por ID (utilizando QuickSort). Compara el ID buscado con el elemento central y descarta la mitad donde no puede encontrarse.
* **Complejidad temporal:** $O(\log n)$.

### 4. Reporte y Clasificación de Membresías (Tercera Funcionalidad)
* **Propósito:** Analiza las fechas de vencimiento en tiempo real respecto a la fecha actual y clasifica los registros.
* **Funcionamiento:** Calcula los días restantes para cada cliente y agrupa los resultados en tres categorías: 
  * Membresías vencidas ($dias < 0$)
  * Próximas a vencer ($dias \le 7$ días)
  * Vigentes ($dias > 7$ días)
* **Complejidad temporal:** $O(n)$ (recorrido lineal de la lista).

---

## 4. Requisitos y Instrucciones de Ejecución

* **Lenguaje:** Python 3.8 o superior.
* **Librerías externas:** Ninguna (utiliza módulos nativos de Python como `datetime`).

### Pasos para ejecutar:
1. Asegúrate de tener Python instalado en tu equipo.
2. Clona o descarga este repositorio en tu computadora.
3. Abre una terminal o consola en la carpeta del proyecto.
4. Ejecuta el programa principal con el siguiente comando:
   ```bash
   python main.py
