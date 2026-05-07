# =============================================================================
# SCRIPT 03 — Librería de Funciones Útiles
# =============================================================================
# El poder real de las funciones: construir herramientas que usas una y otra vez.
# Este script es una colección de funciones útiles para problemas del día a día.
# Conceptos: listas, funciones con listas, funciones auxiliares, composición
# =============================================================================

# ─────────────────────────────────────────────
#  SECCIÓN 1: Funciones de texto
# ─────────────────────────────────────────────

def titulo(texto, ancho=50, caracter="="):
    """Devuelve un título decorado centrado entre líneas."""
    linea = caracter * ancho
    return f"\n{linea}\n  {texto}\n{linea}"

def truncar(texto, max_chars, sufijo="..."):
    """Acorta un texto largo y añade '...' si supera el límite."""
    if len(texto) <= max_chars:
        return texto
    return texto[:max_chars - len(sufijo)] + sufijo

def contar_palabras(texto):
    """Devuelve el número de palabras en un texto."""
    return len(texto.split())

def capitalizar_titulo(frase):
    """Capitaliza cada palabra de una frase (estilo título de libro)."""
    palabras_excluidas = {"de", "la", "el", "en", "y", "a", "un", "una", "los", "las"}
    palabras = frase.lower().split()
    resultado = []
    for i, palabra in enumerate(palabras):
        if i == 0 or palabra not in palabras_excluidas:
            resultado.append(palabra.capitalize())
        else:
            resultado.append(palabra)
    return " ".join(resultado)

# Probamos las funciones de texto
print(titulo("FUNCIONES DE TEXTO"))

texto_largo = "Este es un texto muy largo que debería truncarse porque supera el límite establecido"
print(f"Original:  {texto_largo}")
print(f"Truncado:  {truncar(texto_largo, 40)}")
print(f"Palabras:  {contar_palabras(texto_largo)}")
print(f"Título:    {capitalizar_titulo('el señor de los anillos: las dos torres')}")


# ─────────────────────────────────────────────
#  SECCIÓN 2: Funciones matemáticas
# ─────────────────────────────────────────────

def es_primo(n):
    """Devuelve True si n es un número primo, False si no lo es."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):   # Solo necesitamos comprobar hasta √n
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Calcula el factorial de n (n! = n × n-1 × ... × 2 × 1)."""
    if n < 0:
        return None    # El factorial de negativos no existe
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def es_palindromo(texto):
    """Devuelve True si el texto se lee igual al derecho y al revés."""
    limpio = texto.lower().replace(" ", "")   # Ignoramos mayúsculas y espacios
    return limpio == limpio[::-1]              # [::-1] invierte el string

print(titulo("FUNCIONES MATEMÁTICAS"))

# Números primos del 1 al 30
primos = [n for n in range(2, 31) if es_primo(n)]
print(f"Primos del 1 al 30: {primos}")

# Factoriales
for num in [0, 1, 5, 10]:
    print(f"  {num}! = {factorial(num)}")

# Palíndromos
palabras = ["radar", "python", "reconocer", "hola", "ana"]
print("\nPalíndromos:")
for p in palabras:
    estado = "✅ ES palíndromo" if es_palindromo(p) else "❌ No es palíndromo"
    print(f"  '{p}': {estado}")


# ─────────────────────────────────────────────
#  SECCIÓN 3: Funciones con listas
# ─────────────────────────────────────────────

def estadisticas_lista(numeros):
    """
    Calcula estadísticas básicas de una lista de números.

    Args:
        numeros (list): Lista de números.

    Returns:
        dict: Diccionario con suma, media, mínimo, máximo y rango.
    """
    if not numeros:           # Si la lista está vacía
        return None

    return {
        "cantidad": len(numeros),
        "suma":     sum(numeros),
        "media":    round(sum(numeros) / len(numeros), 2),
        "minimo":   min(numeros),
        "maximo":   max(numeros),
        "rango":    max(numeros) - min(numeros)
    }

def filtrar_pares(numeros):
    """Devuelve solo los números pares de la lista."""
    return [n for n in numeros if n % 2 == 0]

def filtrar_mayores_que(numeros, umbral):
    """Devuelve los números mayores que el umbral dado."""
    return [n for n in numeros if n > umbral]

def eliminar_duplicados(lista):
    """Elimina elementos duplicados manteniendo el orden original."""
    vistos = []
    for elemento in lista:
        if elemento not in vistos:
            vistos.append(elemento)
    return vistos

print(titulo("FUNCIONES CON LISTAS"))

notas = [72, 85, 91, 68, 74, 88, 95, 61, 83, 79]
print(f"Notas: {notas}")

stats = estadisticas_lista(notas)
print(f"\nEstadísticas:")
for clave, valor in stats.items():
    print(f"  {clave.capitalize():<10}: {valor}")

print(f"\nNotas >= 80: {filtrar_mayores_que(notas, 79)}")

colores = ["rojo", "azul", "verde", "rojo", "azul", "amarillo", "verde"]
print(f"\nCon duplicados:    {colores}")
print(f"Sin duplicados:    {eliminar_duplicados(colores)}")


# ─────────────────────────────────────────────
#  SECCIÓN 4: Funciones de validación
# ─────────────────────────────────────────────

def es_email_valido(email):
    """Validación básica de formato de email."""
    return "@" in email and "." in email.split("@")[-1] and len(email) > 5

def es_telefono_valido(telefono):
    """Valida que el teléfono tenga 9 dígitos (formato España)."""
    limpio = telefono.replace(" ", "").replace("-", "")
    return limpio.isdigit() and len(limpio) == 9

def pedir_entero(mensaje, minimo=None, maximo=None):
    """
    Pide un entero al usuario con validación y rango opcional.
    Repite hasta obtener una entrada válida.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"  ⚠️  Debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ⚠️  Debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("  ⚠️  Por favor, escribe un número entero.")

print(titulo("FUNCIONES DE VALIDACIÓN"))

emails = ["usuario@gmail.com", "sinArroba.com", "a@b.c", "correcto@dominio.es"]
for email in emails:
    estado = "✅" if es_email_valido(email) else "❌"
    print(f"  {estado} {email}")

print()
telefonos = ["612345678", "6 1234 5678", "12345", "987-654-321"]
for tel in telefonos:
    estado = "✅" if es_telefono_valido(tel) else "❌"
    print(f"  {estado} {tel}")

print()
# pedir_entero en acción (entrada interactiva)
edad = pedir_entero("¿Cuántos años tienes? (1-120): ", minimo=1, maximo=120)
print(f"Edad registrada: {edad} años ✅")

# =============================================================================
# ¿Qué has aprendido?
# - Una "librería" es simplemente un conjunto de funciones relacionadas
# - Las funciones con listas procesan colecciones de datos de forma limpia
# - Puedes devolver diccionarios para agrupar varios resultados
# - Las funciones de validación centralizan la lógica de comprobación
# - pedir_entero() es un patrón muy útil: valida, pide de nuevo si hay error
# =============================================================================
