# =============================================================================
# SCRIPT 03 — Archivos CSV
# =============================================================================
# CSV (Comma-Separated Values) es el formato más universal para datos tabulares.
# Excel, Google Sheets, bases de datos: todos exportan e importan CSV.
# Conceptos: csv.reader, csv.DictReader, csv.writer, csv.DictWriter
# =============================================================================

import csv
import os

CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "..", "datos")
CARPETA_DATOS = os.path.abspath(CARPETA_DATOS)
RUTA_ESTUDIANTES = os.path.join(CARPETA_DATOS, "estudiantes.csv")


# ─────────────────────────────────────────────
#  PARTE 1: LEER UN CSV
# ─────────────────────────────────────────────

print("=" * 55)
print("  PARTE 1: LEER CSV")
print("=" * 55)
print()

# csv.DictReader: cada fila es un diccionario con los nombres de columna
# Es mucho más cómodo que csv.reader (que devuelve listas)

estudiantes = []

with open(RUTA_ESTUDIANTES, "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        # Cada fila es un dict: {"nombre": "Ana", "edad": "21", ...}
        # Los números vienen como strings → los convertimos
        estudiante = {
            "nombre": fila["nombre"],
            "edad":   int(fila["edad"]),
            "ciudad": fila["ciudad"],
            "nota":   float(fila["nota"])
        }
        estudiantes.append(estudiante)

print(f"📊 Leídos {len(estudiantes)} estudiantes del CSV:\n")

# Mostrar en formato tabla
print(f"  {'NOMBRE':<20} {'EDAD':>4}  {'CIUDAD':<12} {'NOTA':>5}")
print(f"  {'─'*20} {'─'*4}  {'─'*12} {'─'*5}")
for e in estudiantes:
    print(f"  {e['nombre']:<20} {e['edad']:>4}  {e['ciudad']:<12} {e['nota']:>5.1f}")

print()


# ─────────────────────────────────────────────
#  PARTE 2: ANALIZAR LOS DATOS LEÍDOS
# ─────────────────────────────────────────────

print("=" * 55)
print("  PARTE 2: ANÁLISIS DE DATOS")
print("=" * 55)
print()

notas      = [e["nota"] for e in estudiantes]
media      = sum(notas) / len(notas)
aprobados  = [e for e in estudiantes if e["nota"] >= 5]
suspensos  = [e for e in estudiantes if e["nota"] < 5]
mejor      = max(estudiantes, key=lambda e: e["nota"])
peor       = min(estudiantes, key=lambda e: e["nota"])

print(f"  Media de la clase:  {media:.2f}")
print(f"  Aprobados:          {len(aprobados)} ({len(aprobados)/len(estudiantes)*100:.0f}%)")
print(f"  Suspensos:          {len(suspensos)} ({len(suspensos)/len(estudiantes)*100:.0f}%)")
print(f"  Mejor nota:         {mejor['nombre']} ({mejor['nota']})")
print(f"  Peor nota:          {peor['nombre']} ({peor['nota']})")

# Agrupar por ciudad
ciudades = {}
for e in estudiantes:
    ciudad = e["ciudad"]
    if ciudad not in ciudades:
        ciudades[ciudad] = []
    ciudades[ciudad].append(e["nota"])

print(f"\n  Medias por ciudad:")
for ciudad, notas_ciudad in sorted(ciudades.items()):
    media_ciudad = sum(notas_ciudad) / len(notas_ciudad)
    print(f"    {ciudad:<12}: {media_ciudad:.2f}")

print()


# ─────────────────────────────────────────────
#  PARTE 3: ESCRIBIR UN CSV
# ─────────────────────────────────────────────

print("=" * 55)
print("  PARTE 3: ESCRIBIR CSV")
print("=" * 55)
print()

# Añadimos un campo calculado: calificación en letra
def nota_a_letra(nota):
    if nota >= 9: return "Sobresaliente"
    if nota >= 7: return "Notable"
    if nota >= 5: return "Aprobado"
    return "Suspenso"

estudiantes_con_letra = []
for e in estudiantes:
    nuevo = dict(e)                        # Copia del diccionario
    nuevo["calificacion"] = nota_a_letra(e["nota"])
    nuevo["aprobado"] = "Sí" if e["nota"] >= 5 else "No"
    estudiantes_con_letra.append(nuevo)

# Guardar el CSV con los nuevos campos
ruta_informe = os.path.join(CARPETA_DATOS, "informe_notas.csv")
campos = ["nombre", "edad", "ciudad", "nota", "calificacion", "aprobado"]

with open(ruta_informe, "w", newline="", encoding="utf-8") as f:
    # newline="" es OBLIGATORIO en Windows para evitar líneas en blanco extra
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()                 # Escribe la fila de cabecera
    escritor.writerows(estudiantes_con_letra)

print(f"✅ Informe guardado en: '{os.path.basename(ruta_informe)}'")

# Verificar leyendo el archivo recién creado
print(f"\n📄 Preview del informe generado:")
with open(ruta_informe, "r", encoding="utf-8") as f:
    for i, linea in enumerate(f):
        if i >= 4: break                   # Solo mostramos las primeras líneas
        print(f"  {linea.strip()}")
print("  ...")

print()


# ─────────────────────────────────────────────
#  PARTE 4: FILTRAR Y EXPORTAR SUBCONJUNTOS
# ─────────────────────────────────────────────

print("=" * 55)
print("  PARTE 4: FILTRAR Y EXPORTAR")
print("=" * 55)
print()

def exportar_subconjunto(estudiantes, filtro_fn, nombre_archivo):
    """
    Filtra estudiantes según un criterio y los exporta a CSV.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.
        filtro_fn (callable): Función que devuelve True para los que se incluyen.
        nombre_archivo (str): Nombre del archivo CSV de salida.
    """
    filtrados = [e for e in estudiantes if filtro_fn(e)]
    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)
    campos = list(filtrados[0].keys()) if filtrados else []

    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filtrados)

    print(f"  ✅ {nombre_archivo}: {len(filtrados)} registros")
    return filtrados

# Exportamos subconjuntos útiles
exportar_subconjunto(
    estudiantes_con_letra,
    lambda e: e["nota"] < 5,
    "suspensos.csv"
)

exportar_subconjunto(
    estudiantes_con_letra,
    lambda e: e["nota"] >= 7,
    "notables_sobresalientes.csv"
)

exportar_subconjunto(
    estudiantes_con_letra,
    lambda e: e["ciudad"] == "Sevilla",
    "estudiantes_sevilla.csv"
)

# =============================================================================
# ¿Qué has aprendido?
# - csv.DictReader → lee filas como diccionarios (usa nombres de columna)
# - csv.DictWriter → escribe filas desde diccionarios
# - Los números en CSV vienen como strings → convierte con int() o float()
# - newline="" es necesario al escribir CSV en Windows
# - Puedes analizar, filtrar y exportar datos en CSV fácilmente
# - lambda e: e["nota"] >= 5 → función anónima para filtrar listas
# =============================================================================
