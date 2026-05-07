# =============================================================================
# SCRIPT 03 — Tipos de Datos
# =============================================================================
# Python distingue qué tipo de información guardas en una variable.
# El tipo determina qué puedes hacer con esa información.
# Conceptos: str, int, float, bool, type(), conversión de tipos
# =============================================================================

# --- TIPO STR (string = cadena de texto) ---
# Todo lo que va entre comillas es texto (str)

saludo = "Buenos días"
nombre = 'Carlos'          # Comillas simples también funcionan
frase_larga = "Python es un lenguaje de programación muy popular"

print("=== STRINGS (texto) ===")
print(saludo)
print(f"Tipo de 'saludo': {type(saludo)}")   # <class 'str'>

# Operaciones con strings
print()
print("Operaciones con texto:")
print(f"Longitud del nombre: {len(nombre)} caracteres")   # len() cuenta caracteres
print(f"Todo en mayúsculas: {saludo.upper()}")
print(f"Todo en minúsculas: {saludo.lower()}")
print(f"¿Empieza por 'Buenos'? {saludo.startswith('Buenos')}")

# Concatenar (unir) strings con +
texto1 = "Hola"
texto2 = "mundo"
union = texto1 + " " + texto2
print(f"Unión de strings: {union}")

print()

# --- TIPO INT (integer = número entero) ---
# Números sin decimales: positivos, negativos o cero

edad = 25
temperatura_bajo_cero = -5
poblacion_espana = 47_400_000   # El _ ayuda a leer números grandes (Python lo ignora)

print("=== INTEGERS (enteros) ===")
print(f"Edad: {edad}")
print(f"Tipo de 'edad': {type(edad)}")   # <class 'int'>
print(f"Temperatura: {temperatura_bajo_cero}°C")
print(f"Población de España: {poblacion_espana:,} habitantes")   # :, añade separadores de miles

print()

# --- TIPO FLOAT (número decimal) ---
# Números con decimales (coma decimal se escribe como punto en Python)

precio = 9.99
pi = 3.14159
porcentaje = 0.75   # Representa 75%

print("=== FLOATS (decimales) ===")
print(f"Precio: {precio}€")
print(f"Tipo de 'precio': {type(precio)}")   # <class 'float'>
print(f"Pi aproximado: {pi}")

# Redondear decimales con round()
resultado = 10 / 3
print(f"10 / 3 = {resultado}")
print(f"10 / 3 redondeado a 2 decimales = {round(resultado, 2)}")

print()

# --- TIPO BOOL (boolean = booleano) ---
# Solo puede ser True (verdadero) o False (falso)
# Muy importante: True y False van en MAYÚSCULA

tiene_cuenta = True
esta_conectado = False
es_mayor_de_edad = True

print("=== BOOLEANS (verdadero/falso) ===")
print(f"¿Tiene cuenta? {tiene_cuenta}")
print(f"Tipo de 'tiene_cuenta': {type(tiene_cuenta)}")   # <class 'bool'>
print(f"¿Está conectado? {esta_conectado}")

# Los booleanos se pueden comparar
numero = 18
print(f"¿{numero} >= 18? {numero >= 18}")   # True
print(f"¿{numero} > 20? {numero > 20}")     # False

print()

# --- CONVERSIÓN ENTRE TIPOS ---
# A veces necesitas convertir un tipo a otro. Esto se llama "casting"

print("=== CONVERSIÓN DE TIPOS ===")

# str → int (convierte texto a entero)
texto_numero = "42"
numero_real = int(texto_numero)
print(f"'{texto_numero}' como entero: {numero_real + 8}")   # 50 (hace suma real)

# str → float
texto_decimal = "3.14"
numero_decimal = float(texto_decimal)
print(f"'{texto_decimal}' como float: {numero_decimal * 2}")   # 6.28

# int/float → str
edad = 25
edad_texto = str(edad)
print(f"Edad como texto: '{edad_texto}' (tipo: {type(edad_texto).__name__})")

# ⚠️ TRAMPA COMÚN: input() siempre devuelve str
# Si el usuario escribe "5", no puedes sumarle 3 directamente
# numero = input("Escribe un número: ")  ← esto devuelve "5" (str)
# print(numero + 3)  ← ¡ERROR! No puedes sumar str + int
# print(int(numero) + 3)  ← ✅ Primero conviertes, luego sumas

print()

# --- RESUMEN VISUAL ---
print("=== RESUMEN DE TIPOS ===")
print(f"str:   {'Hola mundo'!r}")
print(f"int:   {42}")
print(f"float: {3.14}")
print(f"bool:  {True}")

# =============================================================================
# ¿Qué has aprendido?
# - str = texto (entre comillas)
# - int = número entero (sin decimales)
# - float = número decimal (con punto, no coma)
# - bool = True o False (solo dos posibles valores)
# - type() te dice qué tipo es una variable
# - int(), float(), str() convierten entre tipos
# - input() SIEMPRE devuelve str → conviértelo si necesitas número
# =============================================================================
