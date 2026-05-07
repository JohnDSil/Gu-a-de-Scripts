# =============================================================================
# SCRIPT 04 — Scope y Buenas Prácticas
# =============================================================================
# Scope = "alcance" → dónde puede verse y usarse una variable.
# Este script también muestra cómo organizar un programa grande con funciones.
# Conceptos: scope local/global, constantes, organización de código, main()
# =============================================================================

# ─────────────────────────────────────────────
#  PARTE 1: SCOPE (ALCANCE)
# ─────────────────────────────────────────────

print("=== PARTE 1: SCOPE ===")
print()

# Variable GLOBAL: definida fuera de cualquier función
# Accesible desde cualquier parte del programa
contador_global = 0
nombre_app = "Mi Programa"

def scope_local():
    """Demuestra que las variables locales no salen de la función."""
    variable_local = "Solo existo aquí dentro"
    print(f"  Dentro de la función: '{variable_local}'")

scope_local()

# Intentar usar variable_local fuera da NameError:
# print(variable_local)  # ← NameError: name 'variable_local' is not defined

print(f"  Fuera de la función: la variable local NO existe")

print()

# ─────────────────────────────────────────────
# ¿Cómo pasar datos entre funciones correctamente?
# La respuesta: parámetros y return. NO variables globales.
# ─────────────────────────────────────────────

# ❌ FORMA INCORRECTA: modificar una variable global
puntos = 0

def ganar_puntos_mal(cantidad):
    global puntos          # Accede y modifica la variable global
    puntos += cantidad     # Esto funciona pero es mala práctica

ganar_puntos_mal(10)
print(f"  [MAL] Puntos con global: {puntos}")

# ✅ FORMA CORRECTA: pasar el valor como parámetro y retornar el nuevo valor
def ganar_puntos_bien(puntos_actuales, cantidad):
    """Devuelve los nuevos puntos sin tocar variables globales."""
    return puntos_actuales + cantidad

mis_puntos = 0
mis_puntos = ganar_puntos_bien(mis_puntos, 10)
mis_puntos = ganar_puntos_bien(mis_puntos, 25)
print(f"  [BIEN] Puntos con return: {mis_puntos}")

print()

# ─────────────────────────────────────────────
# Variables que SÍ deben ser globales: las CONSTANTES
# Las constantes son valores que nunca cambian.
# Por convención se escriben en MAYÚSCULAS.
# ─────────────────────────────────────────────

# Constantes del programa (se definen al inicio del archivo)
VERSION          = "1.0.0"
MAX_USUARIOS     = 100
TASA_IVA         = 0.21
NOMBRE_EMPRESA   = "TechSchool S.L."

def mostrar_info_app():
    """Muestra la info de la aplicación usando constantes globales."""
    print(f"  Aplicación: {NOMBRE_EMPRESA}")
    print(f"  Versión:    {VERSION}")
    print(f"  IVA:        {int(TASA_IVA * 100)}%")

print("=== Información de la app ===")
mostrar_info_app()

print()

# ─────────────────────────────────────────────
#  PARTE 2: ORGANIZAR UN PROGRAMA CON FUNCIONES
# ─────────────────────────────────────────────

print("=== PARTE 2: PROGRAMA BIEN ORGANIZADO ===")
print()

# Un programa bien organizado sigue esta estructura:
#
#  1. Importaciones (import ...)
#  2. Constantes
#  3. Funciones auxiliares (pequeñas, hacen UNA cosa)
#  4. Funciones principales (orquestan las auxiliares)
#  5. Punto de entrada: if __name__ == "__main__":

# ─── Funciones auxiliares ───────────────────

def validar_nota(nota):
    """Devuelve True si la nota está en rango válido (0-10)."""
    return 0 <= nota <= 10

def nota_a_letra(nota):
    """Convierte nota numérica a calificación en letra."""
    if nota >= 9:   return "A"
    if nota >= 7:   return "B"
    if nota >= 5:   return "C"
    if nota >= 3:   return "D"
    return "F"

def calcular_media(notas):
    """Calcula la media de una lista de notas válidas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)

def mostrar_informe(nombre, notas):
    """
    Genera y muestra el informe completo de un estudiante.

    Args:
        nombre (str): Nombre del estudiante.
        notas (list): Lista de notas numéricas.
    """
    notas_validas = [n for n in notas if validar_nota(n)]
    invalidas     = len(notas) - len(notas_validas)

    media  = calcular_media(notas_validas)
    letra  = nota_a_letra(media)
    aprueba = media >= 5

    print(f"  ┌─ Informe de {nombre} {'─' * (25 - len(nombre))}┐")
    print(f"  │  Notas:      {notas_validas}")
    if invalidas:
        print(f"  │  ⚠️  {invalidas} nota(s) inválidas ignoradas")
    print(f"  │  Media:      {media:.2f}  →  {letra}")
    print(f"  │  Resultado:  {'✅ APROBADO' if aprueba else '❌ SUSPENSO'}")
    print(f"  └{'─' * 32}┘")

# ─── Función principal ──────────────────────

def procesar_clase(estudiantes):
    """
    Procesa los datos de toda una clase.

    Args:
        estudiantes (dict): Diccionario nombre → lista de notas.
    """
    print("  📋 BOLETÍN DE NOTAS")
    print()

    medias = []
    for nombre, notas in estudiantes.items():
        mostrar_informe(nombre, notas)
        medias.append(calcular_media([n for n in notas if validar_nota(n)]))
        print()

    media_clase = calcular_media(medias)
    aprobados   = sum(1 for m in medias if m >= 5)
    suspensos   = len(medias) - aprobados

    print(f"  ─── Resumen de clase ───────────────")
    print(f"  Media de la clase: {media_clase:.2f}  →  {nota_a_letra(media_clase)}")
    print(f"  Aprobados: {aprobados} | Suspensos: {suspensos}")

# ─── Punto de entrada ───────────────────────
# if __name__ == "__main__" es la forma estándar en Python de decir:
# "Ejecuta este bloque solo si corres este archivo directamente,
#  no si lo importas desde otro script."

if __name__ == "__main__":
    clase = {
        "Ana García":    [8.5, 7.0, 9.2, 6.8],
        "Luis Martín":   [5.5, 4.0, 6.1, 5.9],
        "Sofía López":   [9.8, 9.5, 10, 9.1],
        "Carlos Ruiz":   [3.2, 4.5, 2.8, 15],    # 15 es nota inválida
        "Elena Torres":  [6.0, 5.5, 7.2, 4.8],
    }

    procesar_clase(clase)

# =============================================================================
# ¿Qué has aprendido?
# - Las variables locales solo existen dentro de su función
# - Usa parámetros + return en lugar de modificar variables globales
# - Las CONSTANTES (en MAYÚSCULAS) sí son globales por convención
# - Un buen programa divide la lógica en funciones pequeñas y claras
# - if __name__ == "__main__": marca el punto de entrada del programa
# - Cada función debe hacer UNA sola cosa y hacerla bien
# =============================================================================
