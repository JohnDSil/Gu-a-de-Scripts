# =============================================================================
# SCRIPT 01 — Tu primera función
# =============================================================================
# Una función es un bloque de código con nombre que puedes reutilizar.
# Define la función UNA vez, llámala MUCHAS veces.
# Conceptos: def, llamar funciones, funciones sin parámetros, print vs return
# =============================================================================

# --- DEFINIR UNA FUNCIÓN ---
# La función se define con 'def'. NO se ejecuta aquí, solo se "registra".

def mostrar_bienvenida():
    """Muestra una pantalla de bienvenida decorada."""
    print("=" * 40)
    print("    BIENVENIDO AL PROGRAMA")
    print("=" * 40)

def mostrar_separador():
    """Imprime una línea divisoria."""
    print("-" * 40)

def mostrar_despedida():
    """Muestra un mensaje de cierre."""
    print()
    print("=" * 40)
    print("    ¡Hasta la próxima!")
    print("=" * 40)


# --- LLAMAR UNA FUNCIÓN ---
# Ahora sí la ejecutamos: nombre_funcion()

mostrar_bienvenida()          # Primera llamada
print()

# Podemos llamarla tantas veces como queramos
print("Sección de resultados:")
mostrar_separador()
print("  Resultado 1: ✅")
print("  Resultado 2: ✅")
mostrar_separador()

print()
print("Otra sección:")
mostrar_separador()
print("  Item A")
print("  Item B")
mostrar_separador()

mostrar_despedida()

print()
print("─" * 40)
print()

# --- ¿POR QUÉ ES MEJOR CON FUNCIONES? ---
# Fíjate: usamos mostrar_separador() 4 veces.
# Si queremos cambiar el separador de '-' a '═', solo tocamos UN sitio.
# Sin funciones, tendríamos que cambiarlo en cada print("-" * 40).

# --- ORDEN DE DEFINICIÓN ---
# En Python puedes llamar a una función DESPUÉS de definirla en el archivo,
# pero NUNCA antes de que Python haya leído la definición.

# ❌ Esto daría error:
# saludar_mal()          # Error: 'saludar_mal' no está definida aún
# def saludar_mal():
#     print("Hola")

# ✅ Esto funciona:
def saludar_bien():
    print("¡Hola! Función definida correctamente.")

saludar_bien()            # La función ya está definida arriba

print()

# --- FUNCIONES QUE LLAMAN A OTRAS FUNCIONES ---
# Una función puede llamar a otras funciones dentro de sí misma.
# Es como construir con bloques: piezas pequeñas forman piezas grandes.

def dibujar_caja(texto):
    """Dibuja el texto dentro de una caja decorativa."""
    ancho = len(texto) + 4
    borde = "+" + "-" * ancho + "+"

    print(borde)
    print(f"|  {texto}  |")
    print(borde)

def mostrar_menu_principal():
    """Muestra el menú principal del programa."""
    print()
    dibujar_caja("MENÚ PRINCIPAL")          # Llama a otra función
    print("  1. Nueva partida")
    print("  2. Cargar partida")
    print("  3. Opciones")
    print("  4. Salir")
    mostrar_separador()                      # Llama a otra función definida arriba

mostrar_menu_principal()

# =============================================================================
# ¿Qué has aprendido?
# - def nombre(): define una función (no la ejecuta)
# - nombre()    llama y ejecuta la función
# - Las funciones evitan repetir código
# - Una función puede llamar a otras funciones
# - Define las funciones antes de llamarlas
# - Los docstrings (""" """) explican qué hace la función
# =============================================================================
