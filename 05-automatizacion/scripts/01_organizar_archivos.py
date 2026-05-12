# =============================================================================
# SCRIPT 01 — Organizador Automático de Archivos
# =============================================================================
# Un script muy útil en la vida real: tomas una carpeta caótica llena de
# archivos mezclados y Python los ordena en subcarpetas por tipo.
# Conceptos: os.walk(), shutil.move(), os.path, organización automática
# =============================================================================

import os
import shutil
from datetime import datetime

# ─────────────────────────────────────────────
#  CONFIGURACIÓN: qué extensiones van a qué carpeta
# ─────────────────────────────────────────────

CATEGORIAS = {
    "📄 Documentos":   [".pdf", ".doc", ".docx", ".txt", ".odt", ".md", ".rtf"],
    "🖼️  Imágenes":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "🎵 Audio":        [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "🎬 Vídeo":        [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"],
    "📦 Comprimidos":  [".zip", ".rar", ".7z", ".tar", ".gz"],
    "💻 Scripts":      [".py", ".js", ".sh", ".bat", ".rb", ".php"],
    "📊 Datos":        [".csv", ".json", ".xml", ".xlsx", ".xls", ".sql"],
    "🔧 Otros":        []   # Todo lo que no encaje en ninguna categoría
}

# Construimos el mapa inverso: extensión → nombre de carpeta
EXTENSION_A_CARPETA = {}
for carpeta, extensiones in CATEGORIAS.items():
    for ext in extensiones:
        EXTENSION_A_CARPETA[ext] = carpeta


def obtener_categoria(nombre_archivo):
    """Devuelve la categoría (nombre de carpeta) para un archivo dado."""
    _, extension = os.path.splitext(nombre_archivo)
    return EXTENSION_A_CARPETA.get(extension.lower(), "🔧 Otros")


def escanear_carpeta(ruta_carpeta):
    """
    Escanea una carpeta y devuelve un resumen de lo que contiene.

    Returns:
        dict: {categoria: [lista de archivos]}
    """
    if not os.path.isdir(ruta_carpeta):
        print(f"  ❌ '{ruta_carpeta}' no es una carpeta válida.")
        return {}

    resumen = {cat: [] for cat in CATEGORIAS}

    for archivo in os.listdir(ruta_carpeta):
        ruta_completa = os.path.join(ruta_carpeta, archivo)
        # Solo archivos, no subcarpetas
        if os.path.isfile(ruta_completa):
            categoria = obtener_categoria(archivo)
            resumen[categoria].append(archivo)

    return resumen


def mostrar_prevista(resumen):
    """Muestra lo que se va a organizar antes de hacerlo."""
    total = sum(len(archivos) for archivos in resumen.values())

    if total == 0:
        print("  📭 La carpeta ya está vacía o no tiene archivos.")
        return False

    print(f"  Se encontraron {total} archivo(s) para organizar:\n")
    for categoria, archivos in resumen.items():
        if archivos:
            print(f"  {categoria} ({len(archivos)} archivo(s)):")
            for archivo in archivos[:5]:   # Mostramos máx 5 por categoría
                tamanio = os.path.getsize
                print(f"    • {archivo}")
            if len(archivos) > 5:
                print(f"    • ... y {len(archivos) - 5} más")
            print()
    return True


def organizar_carpeta(ruta_carpeta, modo_simulacion=True):
    """
    Organiza los archivos de una carpeta en subcarpetas por categoría.

    Args:
        ruta_carpeta (str): Ruta a la carpeta a organizar.
        modo_simulacion (bool): Si True, solo muestra lo que haría sin mover nada.

    Returns:
        dict: Estadísticas de lo que se movió (o movería).
    """
    resumen = escanear_carpeta(ruta_carpeta)
    if not resumen:
        return {}

    estadisticas = {"movidos": 0, "errores": 0, "omitidos": 0}
    log = []

    for categoria, archivos in resumen.items():
        if not archivos:
            continue

        # Nombre de carpeta sin emoji para el sistema de archivos
        nombre_carpeta_limpio = categoria.split(" ", 1)[-1].strip()
        destino_carpeta = os.path.join(ruta_carpeta, nombre_carpeta_limpio)

        for archivo in archivos:
            origen = os.path.join(ruta_carpeta, archivo)
            destino = os.path.join(destino_carpeta, archivo)

            entrada_log = {
                "archivo": archivo,
                "categoria": categoria,
                "origen": origen,
                "destino": destino,
            }

            if modo_simulacion:
                print(f"  [SIMULACIÓN] {archivo}  →  {nombre_carpeta_limpio}/")
                estadisticas["movidos"] += 1
            else:
                try:
                    os.makedirs(destino_carpeta, exist_ok=True)

                    # Si ya existe un archivo con ese nombre en destino, renombrar
                    if os.path.exists(destino):
                        base, ext = os.path.splitext(archivo)
                        timestamp = datetime.now().strftime("%H%M%S")
                        nuevo_nombre = f"{base}_{timestamp}{ext}"
                        destino = os.path.join(destino_carpeta, nuevo_nombre)
                        entrada_log["renombrado"] = nuevo_nombre

                    shutil.move(origen, destino)
                    print(f"  ✅ {archivo}  →  {nombre_carpeta_limpio}/")
                    estadisticas["movidos"] += 1
                    entrada_log["estado"] = "movido"

                except Exception as e:
                    print(f"  ❌ Error con '{archivo}': {e}")
                    estadisticas["errores"] += 1
                    entrada_log["estado"] = f"error: {e}"

            log.append(entrada_log)

    return estadisticas, log


def guardar_log(ruta_carpeta, log):
    """Guarda un registro de lo que se organizó en un archivo .log."""
    import json
    ruta_log = os.path.join(ruta_carpeta, f"organizacion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    with open(ruta_log, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)
    print(f"\n  📝 Log guardado en: {os.path.basename(ruta_log)}")


# ─────────────────────────────────────────────
#  DEMO: organiza la carpeta de datos de práctica
# ─────────────────────────────────────────────

def crear_carpeta_demo():
    """Crea una carpeta con archivos de ejemplo para demostrar el organizador."""
    carpeta = os.path.join(os.path.dirname(__file__), "..", "datos", "carpeta_demo")
    os.makedirs(carpeta, exist_ok=True)

    archivos_demo = [
        "informe_enero.pdf", "foto_vacaciones.jpg", "cancion_favorita.mp3",
        "presupuesto.xlsx", "script_backup.py", "video_tutorial.mp4",
        "notas.txt", "datos_ventas.csv", "foto_perfil.png", "proyecto.zip",
        "config.json", "presentacion.pdf", "musica2.mp3", "apuntes.md",
        "archivo_raro.xyz"
    ]

    for nombre in archivos_demo:
        ruta = os.path.join(carpeta, nombre)
        if not os.path.exists(ruta):
            with open(ruta, "w") as f:
                f.write(f"Archivo de demo: {nombre}\n")

    return carpeta


if __name__ == "__main__":
    print("=" * 55)
    print("  🗂️  ORGANIZADOR AUTOMÁTICO DE ARCHIVOS")
    print("=" * 55)
    print()

    # Crear carpeta de demo
    carpeta_demo = crear_carpeta_demo()
    print(f"📁 Carpeta a organizar: {carpeta_demo}")
    print()

    # Escanear y mostrar previsualización
    resumen = escanear_carpeta(carpeta_demo)
    hay_archivos = mostrar_prevista(resumen)

    if hay_archivos:
        print("─" * 55)
        confirmar = input("  ¿Organizar ahora? (si = mover real / no = solo simulación): ").strip().lower()
        print()

        if confirmar in ["si", "sí", "s"]:
            print("  🚀 Organizando archivos...\n")
            stats, log = organizar_carpeta(carpeta_demo, modo_simulacion=False)
            guardar_log(carpeta_demo, log)
        else:
            print("  🔍 MODO SIMULACIÓN — No se mueve nada:\n")
            stats, log = organizar_carpeta(carpeta_demo, modo_simulacion=True)

        print()
        print("─" * 55)
        print(f"  ✅ Movidos:  {stats['movidos']}")
        print(f"  ❌ Errores:  {stats['errores']}")
        print("─" * 55)

# =============================================================================
# ¿Qué has aprendido?
# - os.listdir()         → lista archivos de una carpeta
# - os.path.isfile()     → comprueba si es archivo (no carpeta)
# - os.path.splitext()   → separa nombre y extensión: ("doc", ".pdf")
# - os.makedirs(exist_ok=True) → crea carpetas sin error si ya existen
# - shutil.move()        → mueve un archivo a otra ubicación
# - El patrón simulación/real: mostrar primero lo que harías, luego ejecutar
# =============================================================================
