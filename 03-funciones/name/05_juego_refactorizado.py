# =============================================================================
# SCRIPT 05 — Proyecto: Adivina el Número (versión con funciones)
# =============================================================================
# El mismo juego del Nivel 2, completamente reescrito con funciones.
# Compara este archivo con el original (05_adivina_el_numero.py del Nivel 2)
# y verás la diferencia: mismo comportamiento, código mucho más organizado.
#
# Este es el patrón profesional: cada función hace UNA cosa, tiene un nombre
# claro, y el programa principal lee casi como prosa en inglés/español.
# =============================================================================

import random

# ─────────────────────────────────────────────
#  CONSTANTES
# ─────────────────────────────────────────────

NUMERO_MIN    = 1
NUMERO_MAX    = 100
MAX_INTENTOS  = 7

# ─────────────────────────────────────────────
#  FUNCIONES DE PRESENTACIÓN (mostrar pantallas)
# ─────────────────────────────────────────────

def mostrar_bienvenida():
    """Muestra la pantalla de título del juego."""
    print()
    print("╔══════════════════════════════════════════╗")
    print("║    🎯 ADIVINA EL NÚMERO  v2.0            ║")
    print("║       Ahora con funciones limpias 🧹     ║")
    print("╠══════════════════════════════════════════╣")
    print(f"║  Rango:    {NUMERO_MIN} al {NUMERO_MAX:<32}║")
    print(f"║  Intentos: {MAX_INTENTOS} máximo{' ' * 25}║")
    print("╚══════════════════════════════════════════╝")
    print()

def mostrar_barra_vidas(intentos_usados):
    """Muestra una barra visual de vidas restantes."""
    vidas_restantes = MAX_INTENTOS - intentos_usados + 1
    vidas_perdidas  = intentos_usados - 1
    barra = "❤️ " * vidas_restantes + "🖤 " * vidas_perdidas
    print(f"  Vidas: {barra}")

def mostrar_resultado_ganador(numero, intentos):
    """Muestra el mensaje de victoria con puntuación."""
    mensajes = {
        1: "¡¡INCREÍBLE!! ¡A la primera! 🏆🏆🏆",
        2: "¡Fantástico! Solo 2 intentos. 🥇",
        3: "¡Excelente! Muy pocos intentos. 🏆",
    }
    mensaje = mensajes.get(intentos, "¡Bien hecho! Lo conseguiste. ✅" if intentos <= 5
                           else "¡Lo lograste! Por los pelos. 😅")

    print()
    print("─" * 45)
    print(f"  🎉 ¡CORRECTO! El número era {numero}.")
    print(f"  {mensaje}")
    print(f"  Intentos usados: {intentos}/{MAX_INTENTOS}")
    print("─" * 45)

def mostrar_resultado_perdedor(numero):
    """Muestra el mensaje de derrota."""
    print()
    print("─" * 45)
    print(f"  😢 ¡Se acabaron los intentos!")
    print(f"  El número secreto era: {numero}")
    print("  ¡Más suerte la próxima vez!")
    print("─" * 45)

def mostrar_despedida(partidas, victorias):
    """Muestra estadísticas globales y mensaje de cierre."""
    ratio = round((victorias / partidas) * 100) if partidas > 0 else 0
    print()
    print("╔══════════════════════════════════════════╗")
    print("║          ESTADÍSTICAS FINALES            ║")
    print("╠══════════════════════════════════════════╣")
    print(f"║  Partidas jugadas: {partidas:<23}║")
    print(f"║  Victorias:        {victorias:<23}║")
    print(f"║  Ratio de éxito:   {ratio}%{' ' * (22 - len(str(ratio)))}║")
    print("╠══════════════════════════════════════════╣")
    print("║      ¡Gracias por jugar! 👋               ║")
    print("╚══════════════════════════════════════════╝")

# ─────────────────────────────────────────────
#  FUNCIONES DE LÓGICA (el cerebro del juego)
# ─────────────────────────────────────────────

def generar_numero_secreto():
    """Genera y devuelve un número aleatorio en el rango del juego."""
    return random.randint(NUMERO_MIN, NUMERO_MAX)

def pedir_intento(numero_intento):
    """
    Pide un número al usuario con validación completa.

    Args:
        numero_intento (int): Número de intento actual (para mostrar al usuario).

    Returns:
        int: El número válido introducido por el usuario.
    """
    while True:
        try:
            valor = int(input(f"  Intento {numero_intento}/{MAX_INTENTOS} → Tu número: "))
            if NUMERO_MIN <= valor <= NUMERO_MAX:
                return valor
            print(f"  ⚠️  Debe estar entre {NUMERO_MIN} y {NUMERO_MAX}.")
        except ValueError:
            print("  ⚠️  Por favor, escribe un número entero.")

def calcular_pista_temperatura(diferencia):
    """
    Devuelve un mensaje de pista según la cercanía al número secreto.

    Args:
        diferencia (int): Diferencia absoluta entre el intento y el número secreto.

    Returns:
        str: Mensaje de pista.
    """
    if diferencia <= 3:   return "🔥🔥 ¡ARDIENDO! Estás muy, muy cerca."
    if diferencia <= 8:   return "🔥 ¡Caliente!"
    if diferencia <= 20:  return "♨️  Tibio..."
    if diferencia <= 40:  return "😐 Frío."
    return "🧊 ¡Helado! Muy lejos."

def evaluar_intento(intento, numero_secreto):
    """
    Evalúa el intento del jugador y devuelve si acertó y el mensaje de pista.

    Args:
        intento (int): Número que adivinó el jugador.
        numero_secreto (int): El número que hay que adivinar.

    Returns:
        tuple: (acertado: bool, mensaje: str)
    """
    if intento == numero_secreto:
        return True, "¡Acertaste!"

    diferencia = abs(numero_secreto - intento)
    direccion  = "📈 Es MÁS ALTO" if intento < numero_secreto else "📉 Es MÁS BAJO"
    temperatura = calcular_pista_temperatura(diferencia)

    return False, f"{direccion}. {temperatura}"

def preguntar_jugar_de_nuevo():
    """Pregunta al jugador si quiere otra partida. Devuelve True/False."""
    respuesta = input("\n¿Quieres jugar otra vez? (si/no): ").strip().lower()
    return respuesta in ["si", "sí", "s", "yes", "y"]

# ─────────────────────────────────────────────
#  FUNCIÓN DE UNA PARTIDA
# ─────────────────────────────────────────────

def jugar_partida():
    """
    Gestiona una partida completa del juego.

    Returns:
        bool: True si el jugador ganó, False si perdió.
    """
    numero_secreto = generar_numero_secreto()
    intentos_usados = 0

    print(f"He pensado un número entre {NUMERO_MIN} y {NUMERO_MAX}.")
    print(f"Tienes {MAX_INTENTOS} intentos. ¡Buena suerte!")
    print()

    while intentos_usados < MAX_INTENTOS:
        intentos_usados += 1

        mostrar_barra_vidas(intentos_usados)
        intento = pedir_intento(intentos_usados)
        acertado, mensaje = evaluar_intento(intento, numero_secreto)

        if acertado:
            mostrar_resultado_ganador(numero_secreto, intentos_usados)
            return True

        print(f"  → {mensaje}")
        restantes = MAX_INTENTOS - intentos_usados
        if restantes > 0:
            print(f"  Te quedan {restantes} intento(s).\n")

    mostrar_resultado_perdedor(numero_secreto)
    return False

# ─────────────────────────────────────────────
#  PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────

def main():
    """
    Punto de entrada del juego. Gestiona el bucle de partidas
    y las estadísticas globales.
    """
    mostrar_bienvenida()

    partidas_jugadas = 0
    partidas_ganadas = 0

    while True:
        gano = jugar_partida()       # Juega una partida completa
        partidas_jugadas += 1
        if gano:
            partidas_ganadas += 1

        if not preguntar_jugar_de_nuevo():
            break
        print()                      # Espacio antes de la nueva partida

    mostrar_despedida(partidas_jugadas, partidas_ganadas)

if __name__ == "__main__":
    main()

# =============================================================================
# ¿Qué has aprendido comparando con el Nivel 2?
#
# NIVEL 2 (un solo bloque):          NIVEL 3 (con funciones):
# ─────────────────────────────────  ──────────────────────────────────
# ~80 líneas en un solo bloque       ~200 líneas, pero cada función < 20
# Difícil de depurar                 Fácil: puedes probar cada función sola
# Difícil de modificar               Cambias una función sin tocar el resto
# Difícil de reutilizar              puedes importar funciones en otros scripts
#
# La función main() lee casi como el pseudocódigo del juego:
#   mostrar_bienvenida()
#   mientras quiera jugar:
#       gano = jugar_partida()
#       contar estadísticas
#   mostrar_despedida()
#
# Próximo paso: Nivel 4 → Archivos
#   Guardaremos las puntuaciones en un archivo para que persistan entre sesiones.
# =============================================================================
