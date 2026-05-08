# =============================================================================
# SCRIPT 02 — Manejo de Errores con Archivos
# =============================================================================
# Los archivos pueden fallar por muchas razones: no existen, no tienes permiso,
# están mal formateados... Un script robusto los gestiona sin romperse.
# Conceptos: try/except, FileNotFoundError, os.path, leer con seguridad
# =============================================================================

import os

CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "..", "datos")
CARPETA_DATOS = os.path.abspath(CARPETA_DATOS)


# ─────────────────────────────────────────────
#  PARTE 1: ERRORES COMUNES CON ARCHIVOS
# ─────────────────────────────────────────────

print("=" * 50)
print("  PARTE 1: ERRORES COMUNES")
print("=" * 50)
print()

# ─── Error 1: El archivo no existe ──────────

print("--- FileNotFoundError ---")
try:
    with open("archivo_fantasma.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError:
    print("  ❌ El archivo no existe.")
    print("  → Comprueba la ruta o créalo primero.")

print()

# ─── Error 2: Ruta incorrecta ────────────────

print("--- Ruta incorrecta ---")
try:
    with open("/carpeta/que/no/existe/archivo.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError as e:
    print(f"  ❌ Ruta no encontrada: {e}")

print()

# ─── Error 3: Datos mal formateados ──────────

print("--- Datos mal formateados ---")

# Simula leer un número desde un archivo donde hay texto no numérico
lineas_con_errores = ["42\n", "no_es_numero\n", "100\n", "\n", "77\n"]

numeros = []
errores = 0

for i, linea in enumerate(lineas_con_errores, 1):
    try:
        numero = int(linea.strip())
        numeros.append(numero)
    except ValueError:
        print(f"  ⚠️  Línea {i}: '{linea.strip()}' no es un número válido. Ignorada.")
        errores += 1

print(f"\n  ✅ Números leídos: {numeros}")
print(f"  ⚠️  Líneas con error: {errores}")

print()


# ─────────────────────────────────────────────
#  PARTE 2: COMPROBAR ANTES DE ABRIR
# ─────────────────────────────────────────────

print("=" * 50)
print("  PARTE 2: COMPROBAR ANTES DE ABRIR")
print("=" * 50)
print()

def leer_archivo_seguro(ruta):
    """
    Lee un archivo de forma segura. Devuelve el contenido o None si falla.

    Args:
        ruta (str): Ruta al archivo.

    Returns:
        str | None: Contenido del archivo, o None si no se pudo leer.
    """
    # os.path.exists() → True si el archivo existe
    if not os.path.exists(ruta):
        print(f"  ⚠️  No existe: {os.path.basename(ruta)}")
        return None

    # os.path.isfile() → True si es un archivo (no una carpeta)
    if not os.path.isfile(ruta):
        print(f"  ⚠️  No es un archivo: {ruta}")
        return None

    # os.path.getsize() → tamaño en bytes
    if os.path.getsize(ruta) == 0:
        print(f"  ⚠️  El archivo está vacío: {os.path.basename(ruta)}")
        return ""

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except PermissionError:
        print(f"  ❌ Sin permisos para leer: {os.path.basename(ruta)}")
        return None
    except UnicodeDecodeError:
        print(f"  ❌ Error de codificación en: {os.path.basename(ruta)}")
        return None

# Probamos con archivos que existen y otros que no
archivos_a_probar = [
    os.path.join(CARPETA_DATOS, "info_python.txt"),    # Existe ✅
    os.path.join(CARPETA_DATOS, "no_existe.txt"),      # No existe ❌
    os.path.join(CARPETA_DATOS, "estudiantes.csv"),    # Existe ✅
]

for ruta in archivos_a_probar:
    print(f"📂 {os.path.basename(ruta)}:")
    contenido = leer_archivo_seguro(ruta)
    if contenido:
        # Mostramos solo las primeras 60 letras
        preview = contenido[:60].replace("\n", " ")
        print(f"  ✅ Leído OK. Preview: '{preview}...'")
    print()


# ─────────────────────────────────────────────
#  PARTE 3: CREAR ARCHIVO SI NO EXISTE
# ─────────────────────────────────────────────

print("=" * 50)
print("  PARTE 3: CREAR SI NO EXISTE")
print("=" * 50)
print()

def asegurar_archivo(ruta, contenido_inicial=""):
    """
    Crea un archivo con contenido inicial si no existe.
    Si ya existe, lo deja como está.

    Returns:
        bool: True si el archivo existía, False si fue creado nuevo.
    """
    if os.path.exists(ruta):
        print(f"  📄 Ya existe: {os.path.basename(ruta)}")
        return True
    else:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)   # Crea carpetas si falta
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido_inicial)
        print(f"  ✨ Creado nuevo: {os.path.basename(ruta)}")
        return False

# Archivos que el programa necesita para funcionar
ruta_config = os.path.join(CARPETA_DATOS, "config.txt")
ruta_historial = os.path.join(CARPETA_DATOS, "historial.txt")

asegurar_archivo(ruta_config, "volumen=50\nidioma=es\ntema=claro\n")
asegurar_archivo(ruta_historial, "")    # Empieza vacío


# ─────────────────────────────────────────────
#  PARTE 4: INFORMACIÓN DE UN ARCHIVO
# ─────────────────────────────────────────────

print()
print("=" * 50)
print("  PARTE 4: INFORMACIÓN DE ARCHIVOS")
print("=" * 50)
print()

def info_archivo(ruta):
    """Muestra metadatos de un archivo."""
    if not os.path.exists(ruta):
        print(f"  '{ruta}' no existe")
        return

    nombre    = os.path.basename(ruta)
    tamanio   = os.path.getsize(ruta)
    extension = os.path.splitext(nombre)[1]   # '.txt', '.csv', etc.

    # Formatear tamaño de forma legible
    if tamanio < 1024:
        tam_legible = f"{tamanio} bytes"
    elif tamanio < 1024 ** 2:
        tam_legible = f"{tamanio/1024:.1f} KB"
    else:
        tam_legible = f"{tamanio/1024**2:.1f} MB"

    print(f"  📄 {nombre}")
    print(f"     Extensión: {extension}")
    print(f"     Tamaño:    {tam_legible}")
    print(f"     Ruta:      {ruta}")
    print()

archivos_info = [
    os.path.join(CARPETA_DATOS, "info_python.txt"),
    os.path.join(CARPETA_DATOS, "estudiantes.csv"),
    os.path.join(CARPETA_DATOS, "puntuaciones.json"),
]

for ruta in archivos_info:
    info_archivo(ruta)

# =============================================================================
# ¿Qué has aprendido?
# - FileNotFoundError → el archivo no existe
# - PermissionError   → no tienes permisos de lectura/escritura
# - ValueError        → el contenido no tiene el formato esperado
# - os.path.exists()  → comprueba si existe antes de abrir
# - os.path.isfile()  → distingue archivos de carpetas
# - os.path.getsize() → tamaño en bytes
# - os.makedirs(ruta, exist_ok=True) → crea carpetas si no existen
# - Devolver None cuando falla es mejor que dejar que el programa se rompa
# =============================================================================
