# =============================================================================
# SCRIPT 05 — Proyecto: Adivina el Número
# =============================================================================
# Un juego completo que integra TODO lo aprendido en el Nivel 2:
#   ✅ if / elif / else para dar pistas
#   ✅ while para repetir hasta acertar o agotar intentos
#   ✅ Operadores lógicos y de comparación
#   ✅ break para salir cuando se acierta
#   ✅ Acumuladores (contar intentos)
#   ✅ Validación de entrada del usuario
#
# El ordenador elige un número secreto y el jugador debe adivinarlo.
# =============================================================================

import random   # Módulo de Python para generar números aleatorios
                # (lo verás más en profundidad en niveles superiores)

# --- CONFIGURACIÓN DEL JUEGO ---
NUMERO_MIN   = 1
NUMERO_MAX   = 100
MAX_INTENTOS = 7    # Con 7 intentos y búsqueda binaria siempre se puede ganar

# --- PANTALLA DE BIENVENIDA ---
print()
print("╔══════════════════════════════════════════╗")
print("║       🎯 ADIVINA EL NÚMERO               ║")
print("║          Nivel 2 — Scripts Roadmap       ║")
print("╠══════════════════════════════════════════╣")
print(f"║  Rango:    {NUMERO_MIN} al {NUMERO_MAX}                       ║")
print(f"║  Intentos: {MAX_INTENTOS} máximo                        ║")
print("╚══════════════════════════════════════════╝")
print()

# --- BUCLE PRINCIPAL: permite jugar varias partidas ---
jugar_de_nuevo = True

while jugar_de_nuevo:

    # Generamos un número aleatorio en cada partida
    numero_secreto = random.randint(NUMERO_MIN, NUMERO_MAX)
    intentos_usados = 0
    ha_ganado = False

    print(f"He pensado un número entre {NUMERO_MIN} y {NUMERO_MAX}.")
    print(f"Tienes {MAX_INTENTOS} intentos. ¡Buena suerte!")
    print()

    # --- BUCLE DE INTENTOS ---
    while intentos_usados < MAX_INTENTOS:

        intentos_usados += 1
        restantes = MAX_INTENTOS - intentos_usados

        # Mostramos barra de intentos visual
        barra = "❤️ " * (MAX_INTENTOS - intentos_usados + 1) + "🖤 " * (intentos_usados - 1)
        print(f"  Vidas: {barra}")

        # --- PEDIR NÚMERO CON VALIDACIÓN ---
        entrada_valida = False
        while not entrada_valida:
            try:
                intento = int(input(f"  Intento {intentos_usados}/{MAX_INTENTOS} → Tu número: "))
                if NUMERO_MIN <= intento <= NUMERO_MAX:
                    entrada_valida = True
                else:
                    print(f"  ⚠️  Debe estar entre {NUMERO_MIN} y {NUMERO_MAX}.")
            except ValueError:
                print("  ⚠️  Por favor, escribe un número entero.")

        # --- EVALUAR EL INTENTO ---
        diferencia = abs(numero_secreto - intento)   # abs() = valor absoluto

        if intento == numero_secreto:
            # ¡ACERTÓ!
            ha_ganado = True
            break   # Sale del bucle de intentos

        elif intento < numero_secreto:
            direccion = "📈 Es MÁS ALTO"
        else:
            direccion = "📉 Es MÁS BAJO"

        # Pista adicional según la cercanía
        if diferencia <= 5:
            calor = "🔥 ¡Estás ardiendo! Muy cerca."
        elif diferencia <= 15:
            calor = "♨️  Caliente."
        elif diferencia <= 30:
            calor = "😐 Tibio..."
        else:
            calor = "🧊 Frío, muy frío."

        print(f"  → {direccion}. {calor}")

        if restantes > 0:
            print(f"  Te quedan {restantes} intento(s).\n")
        else:
            print()

    # --- RESULTADO DE LA PARTIDA ---
    print()
    print("─" * 45)

    if ha_ganado:
        # Puntuación basada en intentos usados
        if intentos_usados == 1:
            mensaje = "¡¡INCREÍBLE!! ¡A la primera! 🏆🏆🏆"
        elif intentos_usados <= 3:
            mensaje = "¡Excelente! Muy pocos intentos. 🏆"
        elif intentos_usados <= 5:
            mensaje = "¡Bien hecho! Lo conseguiste. ✅"
        else:
            mensaje = "¡Lo lograste! Aunque por los pelos. 😅"

        print(f"  🎉 ¡CORRECTO! El número era {numero_secreto}.")
        print(f"  {mensaje}")
        print(f"  Intentos usados: {intentos_usados}/{MAX_INTENTOS}")
    else:
        print(f"  😢 ¡Se acabaron los intentos!")
        print(f"  El número secreto era: {numero_secreto}")
        print("  ¡Más suerte la próxima vez!")

    print("─" * 45)
    print()

    # --- ¿JUGAR OTRA VEZ? ---
    respuesta = input("¿Quieres jugar otra vez? (si/no): ").strip().lower()
    jugar_de_nuevo = respuesta in ["si", "sí", "s", "yes", "y"]
    print()

# --- DESPEDIDA ---
print("╔══════════════════════════════════════════╗")
print("║   ¡Gracias por jugar! Hasta pronto 👋    ║")
print("╚══════════════════════════════════════════╝")
print()

# =============================================================================
# ¿Qué has integrado en este proyecto?
# - random.randint(a, b): número aleatorio entre a y b (inclusive)
# - abs(): valor absoluto (diferencia sin signo)
# - while externo para múltiples partidas
# - while interno para los intentos de cada partida
# - Validación de entrada con try/except (captura errores de conversión)
# - if/elif/else para pistas y resultados
# - break para salir del bucle cuando se acierta
# - Acumuladores para contar intentos
# - Operadores de comparación para evaluar cercanía
#
# Próximo paso: Nivel 3 → Funciones
#   Aprenderás a empaquetar código en funciones reutilizables.
#   ¡Este mismo juego quedará mucho más limpio y organizado!
# =============================================================================
