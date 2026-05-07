# =============================================================================
# SCRIPT 04 — Entrada del Usuario
# =============================================================================
# Los scripts útiles necesitan interactuar con el usuario.
# input() pausa el programa y espera a que el usuario escriba algo.
# Conceptos: input(), conversión de tipos, f-strings avanzadas
# =============================================================================

# Separador visual para que la salida sea más limpia
def separador():
    print("-" * 40)

# =============================================================================
# EJEMPLO 1: Saludo personalizado
# =============================================================================
print("=== EJEMPLO 1: Saludo personalizado ===")
separador()

# input() muestra el mensaje entre paréntesis y espera a que el usuario escriba
nombre = input("¿Cómo te llamas? ")

# El usuario escribe su nombre y pulsa Enter → se guarda en la variable 'nombre'
print(f"¡Encantado de conocerte, {nombre}!")
print(f"Tu nombre tiene {len(nombre)} letras.")

separador()
print()

# =============================================================================
# EJEMPLO 2: Calculadora de edad futura
# =============================================================================
print("=== EJEMPLO 2: ¿Qué edad tendrás en el futuro? ===")
separador()

# input() siempre devuelve str, así que convertimos a int con int()
edad_actual = int(input("¿Cuántos años tienes ahora? "))
anos_futuro = int(input("¿En cuántos años quieres saber tu edad? "))

edad_futura = edad_actual + anos_futuro

print(f"\nAhora tienes {edad_actual} años.")
print(f"En {anos_futuro} años, tendrás {edad_futura} años.")

separador()
print()

# =============================================================================
# EJEMPLO 3: Calculadora de propina
# =============================================================================
# Un ejemplo útil en la vida real: calcular la propina en un restaurante
print("=== EJEMPLO 3: Calculadora de propina ===")
separador()

# float() para admitir decimales (el ticket puede ser 23.50€)
total_cuenta = float(input("¿Cuánto fue la cuenta? (€) "))
porcentaje_propina = float(input("¿Qué porcentaje de propina quieres dejar? (%) "))

# Calculamos la propina y el total
propina = total_cuenta * (porcentaje_propina / 100)
total_con_propina = total_cuenta + propina

# Mostramos el resultado con formato de 2 decimales usando :.2f
print(f"\n📋 RESUMEN:")
print(f"   Cuenta:  {total_cuenta:.2f}€")
print(f"   Propina: {propina:.2f}€  ({porcentaje_propina}%)")
print(f"   TOTAL:   {total_con_propina:.2f}€")

separador()
print()

# =============================================================================
# EJEMPLO 4: Información completa del usuario
# =============================================================================
print("=== EJEMPLO 4: Ficha de usuario ===")
separador()

print("Vamos a crear tu ficha. Responde las siguientes preguntas:\n")

# Recogemos varios datos
nombre_completo = input("Nombre completo: ")
ciudad = input("Ciudad donde vives: ")
profesion = input("¿A qué te dedicas? ")
anio_nacimiento = int(input("Año de nacimiento: "))

# Calculamos la edad aproximada
anio_actual = 2025
edad_aproximada = anio_actual - anio_nacimiento

# Mostramos la ficha formateada
print()
print("=" * 40)
print("           📄 TU FICHA")
print("=" * 40)
print(f"  Nombre:     {nombre_completo}")
print(f"  Ciudad:     {ciudad}")
print(f"  Profesión:  {profesion}")
print(f"  Edad aprox: {edad_aproximada} años")
print("=" * 40)

# =============================================================================
# ¿Qué has aprendido?
# - input("mensaje") muestra el mensaje y espera la respuesta del usuario
# - El resultado de input() siempre es str
# - int(input(...)) convierte directamente la entrada a entero
# - float(input(...)) convierte la entrada a decimal
# - {variable:.2f} en una f-string muestra exactamente 2 decimales
# - Puedes construir interfaces de texto simples con print() e input()
# =============================================================================
