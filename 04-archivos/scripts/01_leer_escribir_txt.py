# =============================================================================
# SCRIPT 01 — Leer y Escribir Archivos de Texto
# =============================================================================
# Los archivos permiten que tus datos sobrevivan al cierre del programa.
# Sin archivos, cada vez que ejecutas el script, empiezas desde cero.
# Conceptos: open(), with, read(), write(), readlines(), append
# =============================================================================

import os   # Para trabajar con rutas y comprobar si existen archivos

# Definimos una carpeta de trabajo para todos los archivos que creemos
CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "..", "datos")
CARPETA_DATOS = os.path.abspath(CARPETA_DATOS)


# ─────────────────────────────────────────────
#  PARTE 1: LEER UN ARCHIVO EXISTENTE
# ─────────────────────────────────────────────

print("=" * 50)
print("  PARTE 1: LEER UN ARCHIVO")
print("=" * 50)

ruta_txt = os.path.join(CARPETA_DATOS, "info_python.txt")

# Forma correcta: with open() cierra el archivo automáticamente
with open(ruta_txt, "r", encoding="utf-8") as archivo:
    contenido_completo = archivo.read()    # Lee TODO el archivo como un string

print(f"📄 Contenido de '{os.path.basename(ruta_txt)}':")
print(contenido_completo)

# Contar líneas, palabras y caracteres
with open(ruta_txt, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()           # Lista de líneas (cada una con '\n')

num_lineas   = len(lineas)
num_palabras = sum(len(l.split()) for l in lineas)
num_chars    = sum(len(l) for l in lineas)

print(f"📊 Estadísticas del archivo:")
print(f"   Líneas:    {num_lineas}")
print(f"   Palabras:  {num_palabras}")
print(f"   Caracteres:{num_chars}")

print()

# Leer línea por línea (más eficiente para archivos grandes)
print("─ Primeras 3 líneas del archivo ─")
with open(ruta_txt, "r", encoding="utf-8") as archivo:
    for i, linea in enumerate(archivo):
        if i >= 3:
            break
        print(f"  {i+1}: {linea.strip()}")   # .strip() elimina el '\n' del final

print()


# ─────────────────────────────────────────────
#  PARTE 2: ESCRIBIR UN ARCHIVO NUEVO
# ─────────────────────────────────────────────

print("=" * 50)
print("  PARTE 2: ESCRIBIR UN ARCHIVO")
print("=" * 50)

ruta_nuevo = os.path.join(CARPETA_DATOS, "mi_primer_archivo.txt")

# Modo 'w': crea el archivo si no existe, lo sobreescribe si ya existe
with open(ruta_nuevo, "w", encoding="utf-8") as archivo:
    archivo.write("Hola, esto es mi primer archivo de texto.\n")
    archivo.write("Lo he creado con Python.\n")
    archivo.write("¡Es muy sencillo!\n")

print(f"✅ Archivo creado: '{os.path.basename(ruta_nuevo)}'")

# Verificamos leyéndolo
with open(ruta_nuevo, "r", encoding="utf-8") as archivo:
    print("📄 Contenido guardado:")
    print(archivo.read())


# ─────────────────────────────────────────────
#  PARTE 3: AÑADIR CONTENIDO SIN BORRAR (append)
# ─────────────────────────────────────────────

print("=" * 50)
print("  PARTE 3: AÑADIR AL FINAL (append)")
print("=" * 50)

ruta_log = os.path.join(CARPETA_DATOS, "registro.log")

from datetime import datetime

def registrar_evento(mensaje):
    """Añade una línea con timestamp al archivo de log."""
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{ahora}] {mensaje}\n"
    with open(ruta_log, "a", encoding="utf-8") as f:   # 'a' = append
        f.write(linea)
    print(f"  📝 Registrado: {linea.strip()}")

# Añadimos varios eventos (cada llamada añade al final, sin borrar lo anterior)
registrar_evento("Script iniciado")
registrar_evento("Usuario conectado: Ana")
registrar_evento("Operación completada con éxito")
registrar_evento("Script finalizado")

print()
print("📄 Contenido del log:")
with open(ruta_log, "r", encoding="utf-8") as f:
    print(f.read())


# ─────────────────────────────────────────────
#  PARTE 4: ESCRIBIR UNA LISTA DE LÍNEAS
# ─────────────────────────────────────────────

print("=" * 50)
print("  PARTE 4: GUARDAR UNA LISTA")
print("=" * 50)

frutas = ["manzana", "plátano", "naranja", "uva", "fresa", "melón"]
ruta_frutas = os.path.join(CARPETA_DATOS, "frutas.txt")

# writelines() escribe una lista de strings (tú añades el \n)
with open(ruta_frutas, "w", encoding="utf-8") as f:
    f.writelines(fruta + "\n" for fruta in frutas)

print(f"✅ Guardadas {len(frutas)} frutas en '{os.path.basename(ruta_frutas)}'")

# Leerlas de vuelta como lista limpia
with open(ruta_frutas, "r", encoding="utf-8") as f:
    frutas_leidas = [linea.strip() for linea in f]   # strip() quita el \n

print(f"📋 Frutas recuperadas: {frutas_leidas}")

# =============================================================================
# ¿Qué has aprendido?
# - with open("archivo", modo, encoding="utf-8") as f: → forma segura de abrir
# - Modos: 'r' (leer), 'w' (escribir/sobreescribir), 'a' (añadir al final)
# - f.read()      → todo el contenido como string
# - f.readlines() → lista de líneas (con \n)
# - f.write()     → escribe un string (tú pones el \n)
# - Usa siempre encoding="utf-8" para soportar caracteres españoles
# - .strip() en cada línea elimina el \n del final al leer
# =============================================================================
