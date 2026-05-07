# =============================================================================
# SCRIPT 01 — Condicionales: if / elif / else
# =============================================================================
# Las condicionales permiten que tu programa tome decisiones.
# El código dentro de un bloque if SOLO se ejecuta si la condición es True.
# Conceptos: if, elif, else, operadores de comparación, indentación
# =============================================================================

# --- ESTRUCTURA BÁSICA ---
# if condicion:
#     código que se ejecuta si la condición es True
# elif otra_condicion:
#     código si la segunda condición es True
# else:
#     código si ninguna condición fue True

print("=" * 45)
print("  EJEMPLO 1: Clasificador de notas")
print("=" * 45)

nota = float(input("Introduce tu nota (0-10): "))

# Comprobamos la nota de mayor a menor para atrapar primero los casos extremos
if nota > 10 or nota < 0:
    print("❌ Nota inválida. Debe estar entre 0 y 10.")
elif nota >= 9:
    print("🏆 SOBRESALIENTE — ¡Excelente trabajo!")
elif nota >= 7:
    print("⭐ NOTABLE — Muy bien hecho.")
elif nota >= 5:
    print("✅ APROBADO — Lo has conseguido.")
elif nota >= 3:
    print("⚠️  SUSPENSO — Necesitas repasar más.")
else:
    print("❌ MUY DEFICIENTE — Hay mucho que mejorar.")

print()

# --- CONDICIONALES SIN elif ---
# A veces solo necesitas un if simple (sin alternativas)

print("=" * 45)
print("  EJEMPLO 2: Descuento por edad")
print("=" * 45)

edad = int(input("¿Cuántos años tienes? "))
precio_base = 15.00

descuento = 0   # Por defecto, sin descuento

# Varios if independientes (todos se evalúan, no son excluyentes)
if edad < 12:
    descuento = 0.50       # 50% descuento para niños
if edad >= 65:
    descuento = 0.30       # 30% descuento para jubilados
if edad >= 18 and edad < 26:
    descuento = 0.10       # 10% descuento para jóvenes

precio_final = precio_base * (1 - descuento)

print(f"\nPrecio base: {precio_base:.2f}€")
if descuento > 0:
    print(f"Descuento aplicado: {int(descuento * 100)}%")
    print(f"Precio final: {precio_final:.2f}€")
else:
    print("Sin descuento aplicable.")
    print(f"Precio final: {precio_final:.2f}€")

print()

# --- CONDICIONALES ANIDADAS ---
# Un if dentro de otro if. Úsalas con moderación, pueden volverse confusas.

print("=" * 45)
print("  EJEMPLO 3: Sistema de acceso")
print("=" * 45)

usuario = input("Usuario: ")
password = input("Contraseña: ")

# Primero comprobamos el usuario, luego la contraseña
if usuario == "admin":
    if password == "1234":
        print("✅ Acceso concedido. Bienvenido, administrador.")
    else:
        print("❌ Contraseña incorrecta.")
elif usuario == "invitado":
    print("👤 Acceso como invitado (permisos limitados).")
else:
    print(f"❌ Usuario '{usuario}' no encontrado.")

print()

# --- COMPARAR STRINGS ---
# Los strings se comparan con == exactamente como los números
# Pero cuidado: "Hola" != "hola" (mayúsculas importan)

print("=" * 45)
print("  EJEMPLO 4: Clasificador de días")
print("=" * 45)

dia = input("Escribe el día de la semana: ").lower()   # .lower() pasa a minúsculas
                                                        # así "Lunes" y "lunes" son iguales

if dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
    print(f"📅 {dia.capitalize()} es un día laborable.")
elif dia in ["sábado", "domingo"]:
    print(f"🎉 {dia.capitalize()} es fin de semana. ¡A descansar!")
else:
    print(f"'{dia}' no es un día de la semana válido.")

# =============================================================================
# ¿Qué has aprendido?
# - if condicion: ejecuta código solo si la condición es True
# - elif: añade condiciones alternativas (se evalúan en orden)
# - else: captura todos los casos no cubiertos por if/elif
# - La indentación (4 espacios) define qué código pertenece a cada bloque
# - .lower() convierte texto a minúsculas para comparar sin problemas
# - 'valor' in [lista] comprueba si el valor está en una lista
# =============================================================================
