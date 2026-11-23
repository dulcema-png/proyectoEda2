"""
Módulo: membresias.py
Requisito: Tercera funcionalidad algorítmica (Clasificación y análisis de vigencia).
"""

from datetime import date, datetime

def revisar_membresias(clientes):
    fecha_hoy = date.today()
    vencidas, por_vencer, vigentes = [], [], []
    for cliente in clientes:
        fecha = datetime.strptime(cliente["fecha_vencimiento"], "%Y-%m-%d").date()
        dias = (fecha - fecha_hoy).days
        if dias < 0:
            vencidas.append((cliente, abs(dias)))
        elif dias <= 7:
            por_vencer.append((cliente, dias))
        else:
            vigentes.append((cliente, dias))

    print("\n=== REPORTE DE MEMBRESÍAS ===")
    print(f"Total registros analizados: {len(clientes)}")
    print(f"Vencidas: {len(vencidas)} | Próximas a vencer (<=7 días): {len(por_vencer)} | Vigentes: {len(vigentes)}")
    
    print("\n--- PRÓXIMAS A VENCER (ALERTA) ---")
    if not por_vencer:
        print("No hay membresías próximas a vencer.")
    for c, d in por_vencer:
        print(f"-> {c['nombre']} (ID: {c['id']}) vence en {d} días.")
