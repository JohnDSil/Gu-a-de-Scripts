# =============================================================================
# SCRIPT 02 — Operadores Lógicos: and, or, not
# =============================================================================
# Los operadores lógicos permiten combinar varias condiciones en una sola.
# Conceptos: and, or, not, tablas de verdad, situaciones reales
# =============================================================================

print("=" * 50)
print("  OPERADORES LÓGICOS EN ACCIÓN")
print("=" * 50)
print()

# --- OPERADOR AND ---
# AND: la condición completa es True SOLO si TODAS las partes son True
# "Necesito que se cumplan TODAS las condiciones"

print("--- AND: se necesitan TODAS las condiciones ---")

edad = int(input("¿Cuántos años tienes? "))
tiene_dni = input("¿Tienes DNI? (si/no): ").lower() == "si"

# Para votar necesitas ser mayor de edad Y tener DNI
puede_votar = edad >= 18 and tiene_dni

if puede_votar:
    print("✅ Puedes votar.")
else:
    # Averiguamos cuál condición falla para dar un mensaje útil
    if edad < 18:
        print("❌ No puedes votar: eres menor de edad.")
    if not tiene_dni:
        print("❌ No puedes votar: necesitas DNI.")

print()

# Tabla de verdad de AND (para entenderlo bien):
# True  AND True  = True   ← solo este caso es True
# True  AND False = False
# False AND True  = False
# False AND False = False

# --- OPERADOR OR ---
# OR: la condición completa es True si AL MENOS UNA parte es True
# "Me basta con que se cumpla cualquiera de las condiciones"

print("--- OR: basta con UNA condición ---")

medio_transporte = input("¿Qué medio de transporte usas? (coche/moto/bici/pie): ").lower()

# Un día lluvioso afecta a quien va en bici o a pie
es_dia_lluvioso = True   # Supongamos que llueve

if (medio_transporte == "bici" or medio_transporte == "pie") and es_dia_lluvioso:
    print("🌧️  Hoy llueve y vas en modo no cubierto. ¡Lleva paraguas!")
else:
    print("🚗 Tu medio de transporte te protege de la lluvia.")

print()

# Tabla de verdad de OR:
# True  OR True  = True
# True  OR False = True
# False OR True  = True
# False OR False = False  ← solo este caso es False

# --- OPERADOR NOT ---
# NOT: invierte el valor booleano (True → False, False → True)
# "Quiero que esta condición NO se cumpla"

print("--- NOT: invierte la condición ---")

esta_en_mantenimiento = False
usuario_logueado = True

# not False → True, así que se ejecuta
if not esta_en_mantenimiento:
    if usuario_logueado:
        print("✅ Bienvenido al sistema.")
    else:
        print("🔒 Por favor, inicia sesión.")
else:
    print("🔧 El sistema está en mantenimiento. Vuelve más tarde.")

print()

# --- COMBINACIÓN DE LOS TRES ---
# Puedes combinarlos libremente. Usa paréntesis para dejar claro el orden.

print("--- Combinando AND, OR y NOT ---")
print()

hora = int(input("¿Qué hora es? (0-23): "))
es_festivo = input("¿Es festivo hoy? (si/no): ").lower() == "si"
tiene_reserva = input("¿Tienes reserva? (si/no): ").lower() == "si"

# El restaurante abre de 13 a 16 y de 20 a 23
# En festivos abre todo el día (12-23)
# Sin reserva, no se puede entrar después de las 21

hora_comida = 13 <= hora <= 16
hora_cena   = 20 <= hora <= 23
hora_festivo = 12 <= hora <= 23

if es_festivo:
    esta_abierto = hora_festivo
else:
    esta_abierto = hora_comida or hora_cena

if esta_abierto:
    if hora >= 21 and not tiene_reserva:
        print("🍽️  El restaurante está abierto, pero a esta hora necesitas reserva.")
    else:
        print("🍽️  ¡El restaurante está abierto! Puedes entrar.")
else:
    print("🚫 El restaurante está cerrado a esta hora.")

# =============================================================================
# ¿Qué has aprendido?
# - and: True solo si TODAS las condiciones son True
# - or: True si AL MENOS UNA condición es True
# - not: invierte el resultado (True↔False)
# - Usa paréntesis para agrupar condiciones complejas y evitar ambigüedades
# - 13 <= hora <= 16 es una forma elegante de comprobar rangos en Python
# =============================================================================
