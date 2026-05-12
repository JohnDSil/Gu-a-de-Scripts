# =============================================================================
# SCRIPT 02 — Fechas, Horas y Backups Automáticos
# =============================================================================
# Hacer copias de seguridad con fecha es una tarea que muchos hacen a mano.
# Python lo puede hacer solo en segundos, con nombres claros y limpieza automática.
# Conceptos: datetime, timedelta, strftime, shutil, backups con rotación
# =============================================================================

import os
import shutil
from datetime import datetime, timedelta

CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "..", "datos")
CARPETA_DATOS = os.path.abspath(CARPETA_DATOS)


# ─────────────────────────────────────────────
#  PARTE 1: TRABAJAR CON FECHAS Y HORAS
# ─────────────────────────────────────────────

print("=" * 55)
print("  PARTE 1: FECHAS Y HORAS CON DATETIME")
print("=" * 55)
print()

# Obtener la fecha y hora actual
ahora = datetime.now()
print(f"Fecha y hora actuales: {ahora}")
print()

# Formatear fechas con strftime (string format time)
# %Y = año 4 dígitos, %m = mes, %d = día
# %H = hora (24h), %M = minutos, %S = segundos
formatos = [
    ("%d/%m/%Y",              "Formato europeo"),
    ("%Y-%m-%d",              "Formato ISO (para archivos)"),
    ("%d de %B de %Y",        "Formato largo"),
    ("%H:%M:%S",              "Solo hora"),
    ("%Y%m%d_%H%M%S",         "Formato para nombres de archivo"),
    ("%A, %d de %B de %Y",    "Con día de la semana"),
]

print("Formatos de fecha:")
for formato, descripcion in formatos:
    print(f"  {descripcion:<35}: {ahora.strftime(formato)}")

print()

# Aritmética de fechas con timedelta
print("Aritmética de fechas:")
ayer        = ahora - timedelta(days=1)
manana      = ahora + timedelta(days=1)
semana_pasada = ahora - timedelta(weeks=1)
en_30_dias  = ahora + timedelta(days=30)
hace_2h     = ahora - timedelta(hours=2)

print(f"  Ayer:          {ayer.strftime('%d/%m/%Y')}")
print(f"  Mañana:        {manana.strftime('%d/%m/%Y')}")
print(f"  Hace 1 semana: {semana_pasada.strftime('%d/%m/%Y')}")
print(f"  En 30 días:    {en_30_dias.strftime('%d/%m/%Y')}")
print(f"  Hace 2 horas:  {hace_2h.strftime('%H:%M')}")

# Calcular diferencias entre fechas
inicio_curso = datetime(2025, 9, 15)   # Fecha fija
dias_para_inicio = (inicio_curso - ahora).days
print(f"\n  Días hasta el inicio del curso: {abs(dias_para_inicio)}")

# Comparar fechas
fecha_limite = datetime(2025, 12, 31)
if ahora < fecha_limite:
    print(f"  Quedan {(fecha_limite - ahora).days} días para fin de año")

print()


# ─────────────────────────────────────────────
#  PARTE 2: SISTEMA DE BACKUP CON FECHA
# ─────────────────────────────────────────────

print("=" * 55)
print("  PARTE 2: BACKUP AUTOMÁTICO")
print("=" * 55)
print()

CARPETA_BACKUPS = os.path.join(CARPETA_DATOS, "backups")
MAX_BACKUPS = 5   # Guardamos solo los últimos N backups


def crear_backup(archivo_origen, carpeta_backups=CARPETA_BACKUPS):
    """
    Crea una copia de seguridad de un archivo con la fecha en el nombre.

    Nombre del backup: nombrearchivo_YYYYMMDD_HHMMSS.extension

    Args:
        archivo_origen (str): Ruta al archivo del que hacer backup.
        carpeta_backups (str): Carpeta donde guardar los backups.

    Returns:
        str | None: Ruta al backup creado, o None si falló.
    """
    if not os.path.exists(archivo_origen):
        print(f"  ❌ No existe el archivo: {archivo_origen}")
        return None

    os.makedirs(carpeta_backups, exist_ok=True)

    # Construir nombre con timestamp
    nombre      = os.path.basename(archivo_origen)
    base, ext   = os.path.splitext(nombre)
    timestamp   = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_bkp  = f"{base}_{timestamp}{ext}"
    ruta_bkp    = os.path.join(carpeta_backups, nombre_bkp)

    shutil.copy2(archivo_origen, ruta_bkp)   # copy2 preserva metadatos
    tamanio = os.path.getsize(ruta_bkp)
    print(f"  ✅ Backup creado: {nombre_bkp}  ({tamanio} bytes)")
    return ruta_bkp


def limpiar_backups_antiguos(carpeta_backups, nombre_base, max_backups=MAX_BACKUPS):
    """
    Elimina los backups más antiguos de un archivo, conservando solo los últimos N.

    Args:
        carpeta_backups (str): Carpeta con los backups.
        nombre_base (str): Nombre base del archivo (sin extensión ni timestamp).
        max_backups (int): Cuántos backups conservar.
    """
    if not os.path.exists(carpeta_backups):
        return

    # Filtrar solo los backups de este archivo (los que empiezan por nombre_base)
    todos = [
        f for f in os.listdir(carpeta_backups)
        if f.startswith(nombre_base) and os.path.isfile(os.path.join(carpeta_backups, f))
    ]
    todos.sort()   # Orden alfabético = orden cronológico (gracias al formato YYYYMMDD)

    # Si hay más de max_backups, eliminar los más antiguos
    a_eliminar = todos[:-max_backups] if len(todos) > max_backups else []
    for archivo in a_eliminar:
        os.remove(os.path.join(carpeta_backups, archivo))
        print(f"  🗑️  Eliminado backup antiguo: {archivo}")

    if a_eliminar:
        print(f"  → Conservando los {max_backups} más recientes.")


def listar_backups(carpeta_backups, nombre_base=None):
    """Muestra los backups disponibles con su fecha y tamaño."""
    if not os.path.exists(carpeta_backups):
        print("  📭 No hay backups todavía.")
        return

    archivos = os.listdir(carpeta_backups)
    if nombre_base:
        archivos = [f for f in archivos if f.startswith(nombre_base)]

    if not archivos:
        print("  📭 No se encontraron backups.")
        return

    archivos.sort(reverse=True)   # Más recientes primero
    print(f"  {'ARCHIVO':<45} {'TAMAÑO':>10}")
    print(f"  {'─'*45} {'─'*10}")
    for archivo in archivos:
        ruta = os.path.join(carpeta_backups, archivo)
        tamanio = os.path.getsize(ruta)
        tam_legible = f"{tamanio/1024:.1f} KB" if tamanio > 1024 else f"{tamanio} B"
        print(f"  {archivo:<45} {tam_legible:>10}")


# ─── Demo del sistema de backups ────────────

# Creamos un archivo de ejemplo para hacerle backup
archivo_demo = os.path.join(CARPETA_DATOS, "base_de_datos_demo.json")
if not os.path.exists(archivo_demo):
    import json
    with open(archivo_demo, "w", encoding="utf-8") as f:
        json.dump({"version": 1, "datos": [1, 2, 3]}, f)

print("Haciendo backups del archivo de demo:")
print()

# Simulamos 3 ejecuciones del backup (en producción lo harías desde cron/scheduler)
import time
for i in range(3):
    crear_backup(archivo_demo)
    if i < 2:
        time.sleep(1)   # Espera 1 seg para que el timestamp sea diferente

print()
print("Limpiando backups (máximo 2 conservados para la demo):")
limpiar_backups_antiguos(CARPETA_BACKUPS, "base_de_datos_demo", max_backups=2)

print()
print("Backups disponibles:")
listar_backups(CARPETA_BACKUPS)


# ─────────────────────────────────────────────
#  PARTE 3: DETECTAR ARCHIVOS MODIFICADOS RECIENTEMENTE
# ─────────────────────────────────────────────

print()
print("=" * 55)
print("  PARTE 3: ARCHIVOS MODIFICADOS RECIENTEMENTE")
print("=" * 55)
print()

def archivos_modificados_en(carpeta, dias=1):
    """
    Devuelve una lista de archivos modificados en los últimos N días.

    Args:
        carpeta (str): Carpeta a escanear.
        dias (int): Umbral de días.

    Returns:
        list: Lista de rutas de archivos recientes.
    """
    limite = datetime.now() - timedelta(days=dias)
    recientes = []

    for archivo in os.listdir(carpeta):
        ruta = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta):
            # os.path.getmtime() → timestamp de última modificación
            mtime = datetime.fromtimestamp(os.path.getmtime(ruta))
            if mtime > limite:
                recientes.append((archivo, mtime))

    recientes.sort(key=lambda x: x[1], reverse=True)   # Más recientes primero
    return recientes

recientes = archivos_modificados_en(CARPETA_DATOS, dias=1)
print(f"Archivos modificados en las últimas 24h en datos/:")
if recientes:
    for nombre, fecha in recientes:
        print(f"  📄 {nombre:<40} {fecha.strftime('%H:%M:%S')}")
else:
    print("  (ninguno)")

# =============================================================================
# ¿Qué has aprendido?
# - datetime.now()            → fecha y hora actual
# - ahora.strftime(formato)   → convertir fecha a string con formato
# - timedelta(days=N)         → sumar o restar tiempo a una fecha
# - (fecha2 - fecha1).days    → diferencia en días entre dos fechas
# - shutil.copy2()            → copia preservando metadatos (fecha modificación)
# - os.path.getmtime()        → timestamp de última modificación de un archivo
# - Patrón backup: nombre + timestamp → permite ordenar por nombre = por fecha
# =============================================================================
