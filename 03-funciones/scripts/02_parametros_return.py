# =============================================================================
# SCRIPT 02 — Parámetros y Return
# =============================================================================
# Los parámetros son la información que le das a una función para que trabaje.
# Return es lo que la función te devuelve como resultado.
# Conceptos: parámetros, argumentos, valores por defecto, return, múltiples retornos
# =============================================================================

# --- PARÁMETROS BÁSICOS ---
# Los parámetros son variables que solo existen dentro de la función.
# Se les da valor cuando llamas a la función (eso se llama "argumento").

def saludar(nombre):
    """Saluda a una persona por su nombre."""
    print(f"¡Hola, {nombre}! Bienvenido.")

saludar("Ana")        # 'Ana' es el argumento → se asigna al parámetro 'nombre'
saludar("Carlos")
saludar("María")

print()

# Función con varios parámetros
def presentar(nombre, edad, ciudad):
    """Presenta a una persona con sus datos."""
    print(f"Me llamo {nombre}, tengo {edad} años y soy de {ciudad}.")

presentar("Luis", 25, "Madrid")
presentar("Sofía", 30, "Barcelona")

print()

# --- VALORES POR DEFECTO ---
# Si un parámetro tiene valor por defecto, no es obligatorio pasárselo.
# Los parámetros con valor por defecto van SIEMPRE al final.

def mostrar_precio(producto, precio, moneda="€", descuento=0):
    """Muestra el precio de un producto con descuento opcional."""
    precio_final = precio * (1 - descuento)
    print(f"  {producto}: {precio_final:.2f}{moneda}", end="")
    if descuento > 0:
        print(f"  (antes {precio:.2f}{moneda}, -{int(descuento*100)}%)", end="")
    print()

print("--- Precios en tienda ---")
mostrar_precio("Camiseta", 29.99)                          # Sin descuento, en €
mostrar_precio("Pantalón", 59.99, descuento=0.20)         # 20% descuento
mostrar_precio("Zapatos", 89.99, "$", 0.15)               # En dólares, 15% desc
mostrar_precio("Calcetines", 4.99, "€", 0.50)             # 50% descuento

print()

# --- RETURN: DEVOLVER UN RESULTADO ---
# return hace que la función "entregue" un valor al código que la llamó.
# Sin return (o con return vacío), la función devuelve None.

def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b       # La función entrega este valor y termina

def elevar_al_cuadrado(numero):
    """Devuelve el número elevado al cuadrado."""
    return numero ** 2

# El resultado de return lo podemos guardar en una variable
resultado = sumar(5, 3)
print(f"5 + 3 = {resultado}")

# O usarlo directamente en una expresión
print(f"El cuadrado de 7 es: {elevar_al_cuadrado(7)}")
print(f"La suma de cuadrados: {elevar_al_cuadrado(3) + elevar_al_cuadrado(4)}")

print()

# --- DIFERENCIA CLAVE: print vs return ---
# print() muestra algo en pantalla pero la función devuelve None
# return entrega el valor para que el código que llama lo pueda usar

def con_print(x):
    print(x * 2)      # Solo muestra, no devuelve nada útil

def con_return(x):
    return x * 2      # Devuelve el resultado para usarlo

# Con print: no puedes usar el resultado
valor_a = con_print(5)      # Muestra 10 en pantalla
# print(valor_a + 1)        # ¡ERROR! valor_a es None, no puedes sumarle 1

# Con return: sí puedes usar el resultado
valor_b = con_return(5)     # valor_b = 10
print(f"valor_b + 1 = {valor_b + 1}")   # 11 ✅

print()

# --- RETURN MÚLTIPLE ---
# Una función puede devolver varios valores a la vez (como tupla)

def analizar_texto(texto):
    """Analiza un texto y devuelve estadísticas básicas."""
    palabras    = len(texto.split())
    caracteres  = len(texto)
    sin_espacios = len(texto.replace(" ", ""))
    es_pregunta = texto.strip().endswith("?")

    return palabras, caracteres, sin_espacios, es_pregunta

# Desempaquetamos los valores devueltos en variables separadas
texto_ejemplo = "¿Cómo estás hoy?"
num_palabras, num_chars, num_sin_esp, pregunta = analizar_texto(texto_ejemplo)

print(f"Texto: '{texto_ejemplo}'")
print(f"  Palabras:              {num_palabras}")
print(f"  Caracteres totales:    {num_chars}")
print(f"  Caracteres sin spaces: {num_sin_esp}")
print(f"  ¿Es una pregunta?      {pregunta}")

print()

# --- FUNCIONES MATEMÁTICAS PERSONALIZADAS ---
# Ejemplo práctico: construir una mini librería de cálculo

def porcentaje(valor, total):
    """Calcula qué porcentaje representa valor sobre total."""
    if total == 0:
        return 0
    return round((valor / total) * 100, 2)

def aplicar_iva(precio, tasa_iva=0.21):
    """Devuelve el precio con IVA aplicado. IVA por defecto: 21%."""
    return round(precio * (1 + tasa_iva), 2)

def precio_con_descuento(precio, porcentaje_desc):
    """Calcula el precio final después de un descuento."""
    descuento = precio * (porcentaje_desc / 100)
    return round(precio - descuento, 2)

# Usamos las funciones encadenadas
precio_base = 100.00
precio_dto   = precio_con_descuento(precio_base, 15)    # -15%
precio_final = aplicar_iva(precio_dto)                  # +21% IVA

print("--- Cálculo de precio final ---")
print(f"Precio original:    {precio_base:.2f}€")
print(f"Después de -15%:    {precio_dto:.2f}€")
print(f"Después de +21% IVA: {precio_final:.2f}€")
print(f"Descuento total:    {porcentaje(precio_base - precio_final, precio_base)}%")

# =============================================================================
# ¿Qué has aprendido?
# - Los parámetros reciben información; los argumentos son los valores concretos
# - Los parámetros con valor por defecto son opcionales al llamar la función
# - return entrega un resultado que puedes usar; print solo lo muestra
# - Puedes devolver varios valores separados por comas (tupla)
# - Las funciones se pueden encadenar: resultado de una → entrada de otra
# =============================================================================
