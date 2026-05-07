# =============================================================================
# SCRIPT 02 — Variables
# =============================================================================
# Las variables son la herramienta más fundamental de la programación.
# Sirven para guardar información y usarla más tarde.
# Conceptos: declarar variables, asignación, cambiar valores, f-strings
# =============================================================================

# --- DECLARAR UNA VARIABLE ---
# Formato: nombre_variable = valor
# El símbolo = significa "guarda esto en esta variable" (no es igualdad matemática)

nombre = "Laura"
edad = 22
ciudad = "Sevilla"

# Mostramos las variables con print()
print(nombre)   # Laura
print(edad)     # 22
print(ciudad)   # Sevilla

print()  # Línea en blanco para separar secciones

# --- F-STRINGS: mezclar texto y variables ---
# Pon una f antes de las comillas y escribe la variable entre llaves {}
print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")

print()

# --- CAMBIAR EL VALOR DE UNA VARIABLE ---
# Puedes reasignar una variable tantas veces como quieras
puntuacion = 0
print(f"Puntuación inicial: {puntuacion}")

puntuacion = 10
print(f"Después de ganar puntos: {puntuacion}")

puntuacion = puntuacion + 5   # Suma 5 a lo que ya tenía
print(f"Después de sumar 5 más: {puntuacion}")

# Atajo: += hace lo mismo que variable = variable + algo
puntuacion += 3
print(f"Después de += 3: {puntuacion}")

print()

# --- BUENAS PRÁCTICAS CON NOMBRES DE VARIABLES ---

# ❌ MAL: nombres poco descriptivos
x = "Juan"
n = 25
c = "Madrid"

# ✅ BIEN: nombres que explican qué contienen
nombre_usuario = "Juan"
edad_usuario = 25
ciudad_residencia = "Madrid"

# En Python se usa snake_case: palabras en minúsculas separadas por _
# nombre_de_la_variable  ← estilo Python
# nombreDeLaVariable     ← estilo Java/JavaScript (no recomendado en Python)

print("Variables con buenos nombres:")
print(f"Usuario: {nombre_usuario}, {edad_usuario} años, de {ciudad_residencia}")

print()

# --- VARIABLES QUE HACEN CÁLCULOS ---
# Puedes usar variables en operaciones y guardar el resultado en otra variable
precio_producto = 49.99
cantidad = 3
descuento = 0.10   # 10% de descuento

subtotal = precio_producto * cantidad
descuento_euros = subtotal * descuento
total = subtotal - descuento_euros

print(f"Precio unitario: {precio_producto}€")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: {subtotal}€")
print(f"Descuento (10%): -{descuento_euros}€")
print(f"TOTAL: {total}€")

# =============================================================================
# ¿Qué has aprendido?
# - variable = valor guarda información en memoria
# - Los nombres deben ser descriptivos y usar snake_case
# - f"texto {variable}" mezcla texto con variables fácilmente
# - Puedes cambiar el valor de una variable cuando quieras
# - += es un atajo para variable = variable + algo
# =============================================================================
