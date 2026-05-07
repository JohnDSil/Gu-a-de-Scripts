# =============================================================================
# SCRIPT 04 — Bucle while
# =============================================================================
# El bucle while repite mientras una condición sea verdadera.
# Úsalo cuando NO sabes de antemano cuántas veces hay que repetir.
# Conceptos: while, break, bucle infinito controlado, validación de entrada
# =============================================================================

print("=" * 50)
print("  EL BUCLE WHILE")
print("=" * 50)
print()

# --- WHILE BÁSICO ---
# "Mientras esta condición sea True, sigue ejecutando este código"
# ⚠️ IMPORTANTE: la condición debe cambiar en algún momento, si no → bucle infinito

print("--- While básico: cuenta atrás ---")

cuenta = 10
while cuenta > 0:
    print(f"  {cuenta}...", end=" ")
    cuenta -= 1          # CRUCIAL: reducimos cuenta en cada ciclo
                         # Si olvidamos esto, el bucle nunca para

print("\n  ¡Feliz Año Nuevo! 🎆")
print()

# --- VALIDACIÓN DE ENTRADA CON WHILE ---
# El uso más útil de while: repetir hasta que el usuario dé una respuesta válida

print("--- Validación de entrada ---")

# Pedimos un número entre 1 y 100 y repetimos hasta que sea válido
numero_valido = False
while not numero_valido:
    try:
        numero = int(input("Escribe un número entre 1 y 100: "))
        if 1 <= numero <= 100:
            numero_valido = True   # Condición de salida: el número es válido
        else:
            print("  ⚠️  El número debe estar entre 1 y 100. Inténtalo de nuevo.")
    except ValueError:
        print("  ⚠️  Eso no es un número entero. Inténtalo de nuevo.")

print(f"  ✅ Has introducido: {numero}")
print()

# --- WHILE CON BREAK ---
# Otra forma de salir del bucle: usando break desde dentro
# Útil para el patrón "bucle infinito controlado"

print("--- Menú interactivo con while True ---")
print("(Escribe 'salir' para terminar)")
print()

historial = []   # Guardamos lo que escribe el usuario

# while True crea un bucle que solo termina con break
while True:
    entrada = input("Escribe algo (o 'salir'): ").strip()   # .strip() quita espacios

    if entrada.lower() == "salir":
        print("  👋 Saliendo del bucle.")
        break                           # Sale del while True

    if entrada == "":
        print("  ⚠️  No has escrito nada.")
        continue                        # Vuelve al inicio sin añadir nada

    historial.append(entrada)           # Guardamos en la lista (append = añadir)
    print(f"  ✅ Guardado. Total guardado: {len(historial)} elemento(s).")

print()
if historial:
    print("📋 Historial de entradas:")
    for i, elemento in enumerate(historial, 1):
        print(f"  {i}. {elemento}")
else:
    print("No guardaste ninguna entrada.")

print()

# --- CONTADOR DE INTENTOS ---
# While con límite de intentos: muy útil para sistemas de login, juegos, etc.

print("--- Sistema de contraseña con intentos limitados ---")

CONTRASENA_CORRECTA = "python123"   # En mayúsculas = constante (convención)
MAX_INTENTOS = 3
intentos = 0

while intentos < MAX_INTENTOS:
    intento = input(f"Contraseña (intento {intentos + 1}/{MAX_INTENTOS}): ")

    if intento == CONTRASENA_CORRECTA:
        print("✅ Contraseña correcta. Acceso concedido.")
        break
    else:
        intentos += 1
        restantes = MAX_INTENTOS - intentos
        if restantes > 0:
            print(f"  ❌ Contraseña incorrecta. Te quedan {restantes} intento(s).")
else:
    # El bloque else de un while se ejecuta si el bucle termina SIN break
    # Es decir, si se agotaron todos los intentos sin acertar
    print("🔒 Demasiados intentos fallidos. Cuenta bloqueada.")

# =============================================================================
# ¿Qué has aprendido?
# - while condicion: repite mientras la condición sea True
# - ⚠️ Siempre debes cambiar algo para que la condición eventualmente sea False
# - while True + break: patrón de "bucle infinito controlado"
# - .strip() elimina espacios al inicio y al final de un string
# - .append() añade un elemento al final de una lista
# - El else de un while se ejecuta si el bucle termina SIN usar break
# - Úsalo para validar entradas de usuario o repetir hasta acertar
# =============================================================================
