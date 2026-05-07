# =============================================================================
# SCRIPT 03 — Bucle for
# =============================================================================
# El bucle for repite un bloque de código para cada elemento de una secuencia.
# "Haz esto PARA CADA elemento de esta colección."
# Conceptos: for, range(), enumerate(), listas básicas, break, continue
# =============================================================================

print("=" * 50)
print("  EL BUCLE FOR")
print("=" * 50)
print()

# --- FOR CON range() ---
# range(n) genera los números del 0 al n-1
# range(inicio, fin) genera de inicio hasta fin-1
# range(inicio, fin, paso) controla de cuánto en cuánto salta

print("--- Contando con range() ---")

print("Del 1 al 5:")
for numero in range(1, 6):          # range(1, 6) → 1, 2, 3, 4, 5
    print(f"  {numero}")

print()
print("Números pares del 2 al 10:")
for par in range(2, 11, 2):         # paso 2 → salta de dos en dos
    print(f"  {par}", end="  ")     # end="  " evita el salto de línea
print()

print()
print("Cuenta atrás:")
for i in range(5, 0, -1):          # paso -1 → cuenta hacia atrás
    print(f"  {i}...")
print("  ¡Despegue! 🚀")

print()

# --- FOR CON STRINGS ---
# Un string es una secuencia de caracteres, puedes recorrerla con for

print("--- Recorriendo un string ---")

palabra = "Python"
print(f"Las letras de '{palabra}' son:")
for letra in palabra:
    print(f"  {letra}")

print()

# Contar vocales en una palabra
texto = input("Escribe una palabra para contar sus vocales: ")
vocales = "aeiouáéíóúü"
contador_vocales = 0

for caracter in texto.lower():      # .lower() para no distinguir mayúsculas
    if caracter in vocales:
        contador_vocales += 1

print(f"'{texto}' tiene {contador_vocales} vocal(es).")

print()

# --- FOR CON LISTAS ---
# Las listas son colecciones ordenadas de elementos (las verás en detalle en el Nivel 3)
# Por ahora, solo aprende a recorrerlas con for

print("--- Recorriendo una lista ---")

asignaturas = ["Matemáticas", "Física", "Programación", "Historia", "Inglés"]

print("📚 Mis asignaturas:")
for asignatura in asignaturas:
    print(f"  • {asignatura}")

print()

# enumerate() da tanto el índice (posición) como el elemento
print("📚 Mis asignaturas numeradas:")
for indice, asignatura in enumerate(asignaturas, start=1):   # start=1 empieza desde 1
    print(f"  {indice}. {asignatura}")

print()

# --- ACUMULADORES CON FOR ---
# Un patrón muy común: acumular resultados dentro del bucle

print("--- Calculando la suma y media ---")

numeros = [85, 92, 78, 95, 88, 72, 91]
total = 0

for numero in numeros:
    total += numero              # Sumamos cada número al total

media = total / len(numeros)    # len() devuelve cuántos elementos hay

print(f"Notas: {numeros}")
print(f"Suma total: {total}")
print(f"Media: {media:.2f}")

print()

# --- BREAK Y CONTINUE ---

print("--- break: salir del bucle antes de tiempo ---")

# Buscar un elemento y parar cuando lo encuentres
lista_compra = ["leche", "pan", "huevos", "mantequilla", "café"]
buscar = "huevos"
encontrado = False

for producto in lista_compra:
    if producto == buscar:
        encontrado = True
        break                    # ¡Encontrado! No hace falta seguir buscando

if encontrado:
    print(f"✅ '{buscar}' está en la lista de la compra.")
else:
    print(f"❌ '{buscar}' NO está en la lista de la compra.")

print()
print("--- continue: saltar un elemento y seguir ---")

# Mostrar solo los números que NO son divisibles por 3
print("Números del 1 al 15 que NO son múltiplos de 3:")
for n in range(1, 16):
    if n % 3 == 0:
        continue                 # Salta este número y va al siguiente
    print(f"  {n}", end="  ")
print()

# =============================================================================
# Patrones clave para recordar:
# - for elemento in coleccion:       → recorre cada elemento
# - for i in range(n):               → repite n veces (i = 0 a n-1)
# - for i in range(a, b):            → desde a hasta b-1
# - for i, elemento in enumerate():  → con índice y elemento a la vez
# - total += elemento                → patrón acumulador
# - break                            → sale del bucle
# - continue                         → salta al siguiente ciclo
# =============================================================================
