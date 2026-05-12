# =============================================================================
# SCRIPT 05 — Proyecto: Generador Automático de Informes
# =============================================================================
# El proyecto integrador del Nivel 5. Cada vez que lo ejecutas:
#   1. Lee los datos de estudiantes del CSV (Nivel 4)
#   2. Consulta el clima actual via API (Nivel 5)
#   3. Hace backup de los datos antes de procesar (Nivel 5)
#   4. Genera un informe completo en TXT con fecha automática (Nivel 5)
#   5. Guarda un resumen en JSON para futuras comparaciones (Nivel 4)
#   6. Todo organizado con funciones limpias (Nivel 3)
#
# Es un ejemplo real de automatización: un script que podrías programar
# para que se ejecute cada semana y genere el informe solo.
# =============================================================================

import csv
import json
import os
import shutil
from datetime import datetime

# Intentamos usar requests para el clima (opcional)
try:
    import requests
    REQUESTS_OK = True
except ImportError:
    REQUESTS_OK = False

# ─────────────────────────────────────────────
#  CONFIGURACIÓN
# ─────────────────────────────────────────────

BASE        = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATOS       = os.path.join(BASE, "datos")
INFORMES    = os.path.join(BASE, "datos", "informes")
BACKUPS     = os.path.join(BASE, "datos", "backups")

CSV_ORIGEN  = os.path.join(DATOS, "estudiantes.csv")
JSON_HISTORIAL = os.path.join(DATOS, "historial_informes.json")

CIUDAD      = "Sevilla"
LAT, LON    = 37.39, -5.99


# ─────────────────────────────────────────────
#  MÓDULO 1: DATOS
# ─────────────────────────────────────────────

def cargar_estudiantes(ruta_csv):
    """Lee el CSV de estudiantes y devuelve lista de diccionarios."""
    estudiantes = []
    with open(ruta_csv, "r", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            estudiantes.append({
                "nombre": fila["nombre"],
                "edad":   int(fila["edad"]),
                "ciudad": fila["ciudad"],
                "nota":   float(fila["nota"])
            })
    return estudiantes


def calcular_estadisticas(estudiantes):
    """Calcula estadísticas completas de la lista de estudiantes."""
    notas = [e["nota"] for e in estudiantes]
    aprobados = [e for e in estudiantes if e["nota"] >= 5]
    suspensos  = [e for e in estudiantes if e["nota"] < 5]

    return {
        "total":         len(estudiantes),
        "aprobados":     len(aprobados),
        "suspensos":     len(suspensos),
        "tasa_aprobado": round(len(aprobados) / len(estudiantes) * 100, 1),
        "media":         round(sum(notas) / len(notas), 2),
        "nota_maxima":   max(notas),
        "nota_minima":   min(notas),
        "mejor":         max(estudiantes, key=lambda e: e["nota"])["nombre"],
        "peor":          min(estudiantes, key=lambda e: e["nota"])["nombre"],
    }


def agrupar_por_calificacion(estudiantes):
    """Agrupa estudiantes por calificación en letra."""
    grupos = {"Sobresaliente": [], "Notable": [], "Aprobado": [], "Suspenso": []}
    for e in estudiantes:
        if e["nota"] >= 9:   grupos["Sobresaliente"].append(e)
        elif e["nota"] >= 7: grupos["Notable"].append(e)
        elif e["nota"] >= 5: grupos["Aprobado"].append(e)
        else:                grupos["Suspenso"].append(e)
    return grupos


# ─────────────────────────────────────────────
#  MÓDULO 2: CLIMA (opcional via API)
# ─────────────────────────────────────────────

def obtener_clima_actual(lat, lon):
    """Consulta el clima actual. Devuelve dict con datos o valores por defecto."""
    if not REQUESTS_OK:
        return {"temperatura": "N/A", "descripcion": "Sin conexión (instala requests)"}

    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat, "longitude": lon,
            "current": "temperature_2m,weather_code",
            "timezone": "Europe/Madrid"
        }
        r = requests.get(url, params=params, timeout=8)
        r.raise_for_status()
        datos = r.json()["current"]

        codigos = {0: "Despejado", 1: "Casi despejado", 2: "Parcialmente nublado",
                   3: "Nublado", 45: "Niebla", 51: "Llovizna", 61: "Lluvia", 80: "Chubascos"}

        return {
            "temperatura": f"{datos['temperature_2m']}°C",
            "descripcion": codigos.get(datos.get("weather_code", 0), "Variable")
        }
    except Exception:
        return {"temperatura": "N/A", "descripcion": "Error al consultar API"}


# ─────────────────────────────────────────────
#  MÓDULO 3: BACKUP
# ─────────────────────────────────────────────

def hacer_backup(ruta_archivo, carpeta_backups):
    """Crea copia de seguridad con timestamp. Devuelve ruta del backup."""
    os.makedirs(carpeta_backups, exist_ok=True)
    nombre   = os.path.basename(ruta_archivo)
    base, ext = os.path.splitext(nombre)
    ts       = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino  = os.path.join(carpeta_backups, f"{base}_{ts}{ext}")
    shutil.copy2(ruta_archivo, destino)
    return destino


# ─────────────────────────────────────────────
#  MÓDULO 4: GENERACIÓN DEL INFORME TXT
# ─────────────────────────────────────────────

def generar_informe_txt(estudiantes, stats, grupos, clima, fecha, ciudad):
    """
    Genera el texto completo del informe.

    Returns:
        str: Informe formateado listo para escribir a archivo.
    """
    sep   = "═" * 60
    sep2  = "─" * 60
    lineas = []

    def L(texto=""):
        lineas.append(texto)

    # ── Cabecera ────────────────────────────
    L(sep)
    L(f"  INFORME DE NOTAS — {ciudad.upper()}")
    L(f"  Generado el {fecha.strftime('%d de %B de %Y a las %H:%M')}")
    L(f"  Clima: {clima['descripcion']} · {clima['temperatura']}")
    L(sep)
    L()

    # ── Resumen ejecutivo ───────────────────
    L("  RESUMEN EJECUTIVO")
    L(sep2)
    L(f"  Total de estudiantes:  {stats['total']}")
    L(f"  Aprobados:             {stats['aprobados']}  ({stats['tasa_aprobado']}%)")
    L(f"  Suspensos:             {stats['suspensos']}")
    L(f"  Nota media:            {stats['media']}")
    L(f"  Nota más alta:         {stats['nota_maxima']}  ({stats['mejor']})")
    L(f"  Nota más baja:         {stats['nota_minima']}  ({stats['peor']})")
    L()

    # ── Distribución por calificación ───────
    L("  DISTRIBUCIÓN POR CALIFICACIÓN")
    L(sep2)
    emojis = {"Sobresaliente": "🏆", "Notable": "⭐", "Aprobado": "✅", "Suspenso": "❌"}
    for calificacion, grupo in grupos.items():
        if grupo:
            pct = len(grupo) / stats["total"] * 100
            barra = "█" * len(grupo) + "░" * (stats["total"] - len(grupo))
            L(f"  {emojis[calificacion]} {calificacion:<16} {len(grupo):>2}  [{barra}]  {pct:.0f}%")
    L()

    # ── Listado completo ─────────────────────
    L("  LISTADO COMPLETO DE ESTUDIANTES")
    L(sep2)
    L(f"  {'NOMBRE':<22} {'CIUDAD':<12} {'NOTA':>5}  {'CALIF.'}")
    L(f"  {'─'*22} {'─'*12} {'─'*5}  {'─'*14}")

    for e in sorted(estudiantes, key=lambda x: x["nota"], reverse=True):
        if e["nota"] >= 9:     cal = "Sobresaliente"
        elif e["nota"] >= 7:   cal = "Notable"
        elif e["nota"] >= 5:   cal = "Aprobado"
        else:                  cal = "Suspenso"
        aprobado = "✅" if e["nota"] >= 5 else "❌"
        L(f"  {e['nombre']:<22} {e['ciudad']:<12} {e['nota']:>5.1f}  {aprobado} {cal}")

    L()

    # ── Pie ─────────────────────────────────
    L(sep)
    L(f"  Informe generado automáticamente con Python")
    L(f"  Scripts Roadmap — Nivel 5: Automatización")
    L(sep)

    return "\n".join(lineas)


# ─────────────────────────────────────────────
#  MÓDULO 5: HISTORIAL DE INFORMES
# ─────────────────────────────────────────────

def actualizar_historial(ruta_historial, stats, fecha, ruta_informe):
    """Añade la entrada de este informe al historial JSON."""
    historial = []
    if os.path.exists(ruta_historial):
        with open(ruta_historial, "r", encoding="utf-8") as f:
            historial = json.load(f)

    entrada = {
        "fecha":         fecha.strftime("%Y-%m-%d %H:%M"),
        "total":         stats["total"],
        "media":         stats["media"],
        "tasa_aprobado": stats["tasa_aprobado"],
        "archivo":       os.path.basename(ruta_informe)
    }
    historial.append(entrada)

    with open(ruta_historial, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=4, ensure_ascii=False)

    return len(historial)


# ─────────────────────────────────────────────
#  PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────

def main():
    fecha = datetime.now()

    print()
    print("╔══════════════════════════════════════════════╗")
    print("║     📊 GENERADOR AUTOMÁTICO DE INFORMES     ║")
    print("╚══════════════════════════════════════════════╝")
    print()

    # PASO 1 — Backup de los datos originales
    print("  [1/6] 💾 Haciendo backup de datos...")
    ruta_backup = hacer_backup(CSV_ORIGEN, BACKUPS)
    print(f"        ✅ {os.path.basename(ruta_backup)}")

    # PASO 2 — Cargar estudiantes
    print("  [2/6] 📂 Cargando datos de estudiantes...")
    estudiantes = cargar_estudiantes(CSV_ORIGEN)
    print(f"        ✅ {len(estudiantes)} estudiantes cargados")

    # PASO 3 — Calcular estadísticas
    print("  [3/6] 🔢 Calculando estadísticas...")
    stats  = calcular_estadisticas(estudiantes)
    grupos = agrupar_por_calificacion(estudiantes)
    print(f"        ✅ Media: {stats['media']} | Aprobados: {stats['tasa_aprobado']}%")

    # PASO 4 — Consultar clima
    print(f"  [4/6] 🌤️  Consultando clima en {CIUDAD}...")
    clima = obtener_clima_actual(LAT, LON)
    print(f"        ✅ {clima['descripcion']} · {clima['temperatura']}")

    # PASO 5 — Generar y guardar informe TXT
    print("  [5/6] 📝 Generando informe...")
    os.makedirs(INFORMES, exist_ok=True)
    nombre_informe = f"informe_{fecha.strftime('%Y%m%d_%H%M%S')}.txt"
    ruta_informe   = os.path.join(INFORMES, nombre_informe)

    texto_informe = generar_informe_txt(estudiantes, stats, grupos, clima, fecha, CIUDAD)
    with open(ruta_informe, "w", encoding="utf-8") as f:
        f.write(texto_informe)
    print(f"        ✅ {nombre_informe}")

    # PASO 6 — Actualizar historial JSON
    print("  [6/6] 📈 Actualizando historial...")
    num_informes = actualizar_historial(JSON_HISTORIAL, stats, fecha, ruta_informe)
    print(f"        ✅ Informe #{num_informes} en el historial")

    # ── Resultado final ──────────────────────
    print()
    print("  ─" * 28)
    print()
    print(texto_informe)
    print()
    print(f"  📁 Informe guardado en: datos/informes/{nombre_informe}")
    print(f"  📁 Backup en:           datos/backups/{os.path.basename(ruta_backup)}")
    print()


if __name__ == "__main__":
    main()

# =============================================================================
# ¿Qué integra este proyecto?
# ─────────────────────────────────────────────────────────
# Nivel 1 → Variables, tipos, f-strings
# Nivel 2 → For loops, if/elif para clasificar notas
# Nivel 3 → Funciones con responsabilidad única, main()
# Nivel 4 → csv.DictReader, json.dump/load, manejo de archivos
# Nivel 5 → shutil.copy2 (backup), requests (clima), datetime (timestamp),
#            os.makedirs (crear carpetas automáticamente)
#
# Próxima parada: Nivel 6 → Proyectos
#   Integrarás todo en aplicaciones completas con estructura de proyecto real.
# =============================================================================
