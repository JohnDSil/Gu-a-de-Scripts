# =============================================================================
# SCRIPT 05 — Calculadora Simple
# =============================================================================
# Tu primer "proyecto" real: una calculadora interactiva.
# Este script integra todo lo aprendido en el nivel 1.
#
# ¿Qué hace este script?
#   → Pide dos números al usuario
#   → Muestra el resultado de sumar, restar, multiplicar y dividir
#   → Maneja el caso especial de dividir entre cero
#
# Conceptos: input(), conversión de tipos, operadores, f-strings, condición simple
# =============================================================================

# --- CABECERA DEL PROGRAMA ---
# Es buena práctica mostrar una pantalla de bienvenida clara

print("=" * 45)
print("         🧮 CALCULADORA BÁSICA")
print("         Nivel 1 - Scripts Roadmap")
print("=" * 45)
print()

# --- PEDIR LOS NÚMEROS AL USUARIO ---
# Usamos float para admitir tanto enteros como decimales (3, 7.5, -2, etc.)

print("Introduce dos números para operar con ellos.")
print()

numero1 = float(input("Primer número:  "))
numero2 = float(input("Segundo número: "))

print()

# --- CALCULAR LOS RESULTADOS ---

resultado_suma       = numero1 + numero2
resultado_resta      = numero1 - numero2
resultado_multi      = numero1 * numero2

# La división necesita cuidado especial: no se puede dividir entre 0
# Usamos una condición simple (aprenderás más en el Nivel 2)
if numero2 != 0:
    resultado_division = numero1 / numero2
    division_texto = f"{resultado_division:.4f}"   # 4 decimales para mayor precisión
else:
    division_texto = "⚠️  Imposible (no se puede dividir entre 0)"

# También calculamos potencia y módulo como extras
resultado_potencia   = numero1 ** numero2
resultado_modulo     = numero1 % numero2 if numero2 != 0 else "N/A"

# --- MOSTRAR LOS RESULTADOS ---

print("-" * 45)
print(f"  Operaciones con {numero1} y {numero2}:")
print("-" * 45)
print(f"  ➕  Suma:            {numero1} + {numero2} = {resultado_suma:.4f}")
print(f"  ➖  Resta:           {numero1} - {numero2} = {resultado_resta:.4f}")
print(f"  ✖️   Multiplicación:  {numero1} × {numero2} = {resultado_multi:.4f}")
print(f"  ➗  División:        {numero1} ÷ {numero2} = {division_texto}")
print(f"  🔢  Potencia:        {numero1} ^ {numero2} = {resultado_potencia:.4f}")
print(f"  🔁  Módulo (resto):  {numero1} % {numero2} = {resultado_modulo}")
print("-" * 45)

# --- DATO EXTRA: análisis rápido ---
print()
print("📊 Análisis rápido:")

# Mostramos cuál es el mayor
if numero1 > numero2:
    print(f"  • {numero1} es mayor que {numero2}")
elif numero1 < numero2:
    print(f"  • {numero2} es mayor que {numero1}")
else:
    print(f"  • {numero1} y {numero2} son iguales")

# Indicamos si los números son pares o impares (solo si son enteros)
if numero1 == int(numero1):   # Comprobamos que es un entero "disfrazado" de float
    tipo1 = "par" if int(numero1) % 2 == 0 else "impar"
    print(f"  • {int(numero1)} es {tipo1}")

if numero2 == int(numero2):
    tipo2 = "par" if int(numero2) % 2 == 0 else "impar"
    print(f"  • {int(numero2)} es {tipo2}")

print()
print("=" * 45)
print("  ✅ Cálculo completado. ¡Hasta luego!")
print("=" * 45)

# =============================================================================
# ¿Qué has aprendido con este script?
# - Integrar input(), conversión de tipos y operadores en un programa real
# - Manejar casos especiales (división entre cero)
# - Formatear la salida de forma clara y profesional con print()
# - Usar :.4f en f-strings para controlar los decimales mostrados
#
# Próximo paso: Nivel 2 → Control de flujo
#   Aprenderás a usar if/elif/else de forma completa y bucles (for, while)
#   para repetir operaciones automáticamente.
# =============================================================================
