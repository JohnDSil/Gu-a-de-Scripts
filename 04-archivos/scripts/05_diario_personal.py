# =============================================================================
# SCRIPT 05 — Proyecto: Diario Personal
# =============================================================================
# Un diario que guarda entradas en JSON y persiste entre sesiones.
# Cada vez que ejecutas el script, tus entradas anteriores siguen ahí.
#
# Integra todo el Nivel 4:
#   ✅ Leer y escribir archivos JSON
#   ✅ Manejo de errores (archivo no existe, datos corruptos)
#   ✅ Funciones bien organizadas (Nivel 3)
#   ✅ Menú interactivo con while (Nivel 2)
# =============================================================================

import json
import os
from datetime import datetime

# ─────────────────────────────────────────────
#  CONFIGURACIÓN
# ─────────────────────────────────────────────

CARPETA_DATOS  = os.path.join(os.path.dirname(__file__), "..", "datos")
RUTA_DIARIO    = os.path.join(os.path.abspath(CARPETA_DATOS), "mi_diario.json")
FORMATO_FECHA  = "%Y-%m-%d"
FORMATO_HORA   = "%H:%M"
FORMATO_DISPLAY = "%d de %B de %Y"   # "15 de enero de 2025"

# Categorías disponibles para las entradas
CATEGORIAS = ["📔 General", "😊 Emociones", "🎯 Metas", "💡 Ideas", "📚 Aprendizaje"]


# ─────────────────────────────────────────────
#  FUNCIONES DE DATOS (cargar / guardar)
# ─────────────────────────────────────────────

def cargar_diario():
    """Carga el diario desde JSON. Devuelve lista vacía si no existe."""
    if not os.path.exists(RUTA_DIARIO):
        return []
    try:
        with open(RUTA_DIARIO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("  ⚠️  Error al leer el diario. Empezando desde cero.")
        return []

def guardar_diario(entradas):
    """Guarda todas las entradas del diario en JSON."""
    os.makedirs(os.path.dirname(RUTA_DIARIO), exist_ok=True)
    with open(RUTA_DIARIO, "w", encoding="utf-8") as f:
        json.dump(entradas, f, indent=4, ensure_ascii=False)

def nueva_entrada(titulo, texto, categoria):
    """Crea y devuelve un diccionario con una nueva entrada de diario."""
    ahora = datetime.now()
    return {
        "id":        len(cargar_diario()) + 1,
        "titulo":    titulo,
        "texto":     texto,
        "categoria": categoria,
        "fecha":     ahora.strftime(FORMATO_FECHA),
        "hora":      ahora.strftime(FORMATO_HORA),
    }


# ─────────────────────────────────────────────
#  FUNCIONES DE PRESENTACIÓN
# ─────────────────────────────────────────────

def limpiar():
    """Limpia la pantalla (compatible con Windows y Unix)."""
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_cabecera():
    """Muestra la cabecera del diario."""
    hoy = datetime.now().strftime(FORMATO_DISPLAY)
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║            📖  MI DIARIO PERSONAL            ║")
    print(f"║         {hoy:^36}║")
    print("╚══════════════════════════════════════════════╝")
    print()

def mostrar_menu(num_entradas):
    """Muestra el menú principal."""
    print(f"  Entradas guardadas: {num_entradas}")
    print()
    print("  ┌──────────────────────────────┐")
    print("  │  1. ✏️   Nueva entrada       │")
    print("  │  2. 📋  Ver todas            │")
    print("  │  3. 🔍  Buscar entrada       │")
    print("  │  4. 🗑️   Eliminar entrada    │")
    print("  │  5. 📊  Estadísticas         │")
    print("  │  0. 🚪  Salir                │")
    print("  └──────────────────────────────┘")
    print()

def mostrar_entrada(entrada, detalle=False):
    """Muestra una entrada del diario en formato compacto o detallado."""
    fecha_obj = datetime.strptime(entrada["fecha"], FORMATO_FECHA)
    fecha_fmt = fecha_obj.strftime(FORMATO_DISPLAY)

    if detalle:
        print(f"  ┌─ #{entrada['id']:03d} ─────────────────────────────────────────┐")
        print(f"  │  📅 {fecha_fmt} a las {entrada['hora']}")
        print(f"  │  🏷️  {entrada['categoria']}")
        print(f"  │  📝 {entrada['titulo']}")
        print(f"  ├────────────────────────────────────────────────")
        # Mostramos el texto partido en líneas de máx 48 chars
        palabras = entrada["texto"].split()
        linea = "  │  "
        for palabra in palabras:
            if len(linea) + len(palabra) > 52:
                print(linea)
                linea = "  │  " + palabra + " "
            else:
                linea += palabra + " "
        if linea.strip() != "│":
            print(linea)
        print(f"  └────────────────────────────────────────────────")
    else:
        texto_corto = entrada["texto"][:45] + "..." if len(entrada["texto"]) > 45 else entrada["texto"]
        print(f"  #{entrada['id']:03d}  [{entrada['fecha']}]  {entrada['titulo']:<22}  {texto_corto}")


# ─────────────────────────────────────────────
#  FUNCIONES DE ACCIONES
# ─────────────────────────────────────────────

def accion_nueva_entrada(entradas):
    """Guía al usuario para escribir una nueva entrada."""
    print("\n  ✏️  NUEVA ENTRADA")
    print("  " + "─" * 40)

    titulo = input("  Título: ").strip()
    if not titulo:
        print("  ⚠️  El título no puede estar vacío.")
        return entradas

    print("  Categoría:")
    for i, cat in enumerate(CATEGORIAS, 1):
        print(f"    {i}. {cat}")

    try:
        opcion_cat = int(input("  Elige categoría (1-5): "))
        categoria = CATEGORIAS[opcion_cat - 1] if 1 <= opcion_cat <= 5 else CATEGORIAS[0]
    except (ValueError, IndexError):
        categoria = CATEGORIAS[0]

    print("  Escribe tu entrada (pulsa Enter dos veces para terminar):")
    lineas = []
    while True:
        linea = input("  > ")
        if linea == "" and lineas and lineas[-1] == "":
            break
        lineas.append(linea)

    texto = " ".join(l for l in lineas if l)
    if not texto:
        print("  ⚠️  La entrada está vacía.")
        return entradas

    entrada = nueva_entrada(titulo, texto, categoria)
    entradas.append(entrada)
    guardar_diario(entradas)
    print(f"\n  ✅ Entrada #{entrada['id']} guardada correctamente.")
    return entradas

def accion_ver_todas(entradas):
    """Muestra todas las entradas del diario."""
    if not entradas:
        print("\n  📭 No hay entradas todavía. ¡Escribe la primera!")
        return

    print(f"\n  📋 TODAS LAS ENTRADAS ({len(entradas)})")
    print("  " + "─" * 40)

    for entrada in reversed(entradas):   # Más recientes primero
        mostrar_entrada(entrada)

    # Preguntar si quiere ver alguna en detalle
    print()
    id_ver = input("  ¿Ver alguna en detalle? (número o Enter para volver): ").strip()
    if id_ver.isdigit():
        encontrada = next((e for e in entradas if e["id"] == int(id_ver)), None)
        if encontrada:
            print()
            mostrar_entrada(encontrada, detalle=True)
        else:
            print("  ⚠️  Entrada no encontrada.")

def accion_buscar(entradas):
    """Busca entradas por palabra clave."""
    termino = input("\n  🔍 Buscar: ").strip().lower()
    if not termino:
        return

    resultados = [
        e for e in entradas
        if termino in e["titulo"].lower()
        or termino in e["texto"].lower()
        or termino in e["categoria"].lower()
    ]

    if not resultados:
        print(f"  ❌ No se encontraron entradas con '{termino}'.")
    else:
        print(f"\n  Encontradas {len(resultados)} entrada(s):")
        for e in resultados:
            mostrar_entrada(e)

def accion_eliminar(entradas):
    """Elimina una entrada por su ID."""
    if not entradas:
        print("\n  📭 No hay entradas para eliminar.")
        return entradas

    id_str = input("\n  🗑️  ID de la entrada a eliminar: ").strip()
    if not id_str.isdigit():
        print("  ⚠️  Introduce un número válido.")
        return entradas

    id_eliminar = int(id_str)
    encontrada = next((e for e in entradas if e["id"] == id_eliminar), None)

    if not encontrada:
        print(f"  ❌ No existe la entrada #{id_eliminar}.")
        return entradas

    mostrar_entrada(encontrada, detalle=True)
    confirmar = input("\n  ¿Eliminar esta entrada? (si/no): ").strip().lower()

    if confirmar in ["si", "sí", "s"]:
        entradas = [e for e in entradas if e["id"] != id_eliminar]
        guardar_diario(entradas)
        print(f"  ✅ Entrada #{id_eliminar} eliminada.")
    else:
        print("  ↩️  Eliminación cancelada.")

    return entradas

def accion_estadisticas(entradas):
    """Muestra estadísticas del diario."""
    if not entradas:
        print("\n  📭 Sin datos todavía.")
        return

    print(f"\n  📊 ESTADÍSTICAS")
    print("  " + "─" * 40)
    print(f"  Total de entradas:  {len(entradas)}")

    # Por categoría
    por_categoria = {}
    for e in entradas:
        cat = e["categoria"]
        por_categoria[cat] = por_categoria.get(cat, 0) + 1

    print("\n  Por categoría:")
    for cat, n in sorted(por_categoria.items(), key=lambda x: -x[1]):
        barra = "█" * n + "░" * (10 - min(n, 10))
        print(f"    {cat:<22} {barra} {n}")

    # Racha de días
    fechas = sorted(set(e["fecha"] for e in entradas))
    print(f"\n  Primera entrada: {fechas[0]}")
    print(f"  Última entrada:  {fechas[-1]}")
    print(f"  Días distintos:  {len(fechas)}")


# ─────────────────────────────────────────────
#  PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────

def main():
    entradas = cargar_diario()

    while True:
        mostrar_cabecera()
        mostrar_menu(len(entradas))

        opcion = input("  Elige una opción: ").strip()
        print()

        if opcion == "1":
            entradas = accion_nueva_entrada(entradas)
        elif opcion == "2":
            accion_ver_todas(entradas)
        elif opcion == "3":
            accion_buscar(entradas)
        elif opcion == "4":
            entradas = accion_eliminar(entradas)
        elif opcion == "5":
            accion_estadisticas(entradas)
        elif opcion == "0":
            print("  👋 ¡Hasta pronto! Tus entradas están guardadas.")
            break
        else:
            print("  ⚠️  Opción no válida.")

        input("\n  [Pulsa Enter para continuar]")

if __name__ == "__main__":
    main()

# =============================================================================
# ¿Qué integra este proyecto?
# - Persistencia real: los datos sobreviven al cierre del programa
# - json.load() y json.dump() para leer/guardar el estado completo
# - Manejo de errores: archivo no existe, JSON corrupto
# - Funciones bien separadas por responsabilidad (Nivel 3)
# - Menú interactivo con while True + break (Nivel 2)
# - os.makedirs(exist_ok=True) para crear carpetas si no existen
#
# Próximo paso: Nivel 5 → Automatización
#   Aprenderás a hacer que Python trabaje por ti: mover archivos,
#   enviar emails, scrapear webs y programar tareas.
# =============================================================================
