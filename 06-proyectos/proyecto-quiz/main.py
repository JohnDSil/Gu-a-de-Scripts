# main.py — Quiz con ranking persistente
# La interfaz está aquí directamente porque el juego es muy interactivo
# y separarlo en otro archivo añadiría complejidad sin beneficio claro.

import time
import datos
import logica
from config import SEGUNDOS_POR_PREGUNTA, PREGUNTAS_POR_PARTIDA


# ─────────────────────────────────────────────
#  PANTALLAS
# ─────────────────────────────────────────────

def pantalla_bienvenida():
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║           🎮  QUIZ — DESAFÍO TOTAL           ║")
    print("║     ¿Cuánto sabes? Demuéstralo.              ║")
    print("╚══════════════════════════════════════════════╝")
    print()
    print(f"  📌 {PREGUNTAS_POR_PARTIDA} preguntas por partida")
    print(f"  ⏱️  {SEGUNDOS_POR_PREGUNTA} segundos por pregunta")
    print(f"  ⭐ +{10} puntos por respuesta correcta")
    print(f"  ⚡ +5 bonus si respondes en menos de 5 segundos")
    print()


def mostrar_menu():
    print("  ═" * 26)
    print("    1.  🎯  Jugar partida")
    print("    2.  🏆  Ver ranking")
    print("    0.  🚪  Salir")
    print("  ─" * 26)


def mostrar_ranking(ranking):
    print()
    if not ranking:
        print("  📭 El ranking está vacío. ¡Sé el primero!\n")
        return

    print("  🏆 RANKING — TOP JUGADORES")
    print(f"  {'─'*52}")
    print(f"  {'POS':<5} {'JUGADOR':<18} {'PUNTOS':>7} {'%ACIERTO':>9} {'TIEMPO':>7}  FECHA")
    print(f"  {'─'*52}")
    medallas = {1: "🥇", 2: "🥈", 3: "🥉"}
    for i, e in enumerate(ranking, 1):
        medalla = medallas.get(i, f"#{i:<2}")
        print(f"  {medalla:<5} {e['jugador']:<18} {e['puntos']:>7} "
              f"{e['pct']:>8}%  {e['tiempo_medio']:>5.1f}s  {e['fecha']}")
    print()


def mostrar_pregunta(numero, total, pregunta, puntos_acumulados):
    """Muestra la pregunta y devuelve el índice elegido (0-3) y el tiempo."""
    print()
    print(f"  ─── Pregunta {numero}/{total}  │  Puntos: {puntos_acumulados} ───")
    print()
    # Texto de pregunta partido en líneas de 50 chars
    texto = pregunta["pregunta"]
    while len(texto) > 50:
        corte = texto[:50].rfind(" ")
        print(f"  {texto[:corte]}")
        texto = texto[corte+1:]
    print(f"  {texto}")
    print()

    letras = ["A", "B", "C", "D"]
    for i, opcion in enumerate(pregunta["opciones"]):
        print(f"    {letras[i]}.  {opcion}")
    print()

    # Pedir respuesta con tiempo
    inicio = time.time()
    while True:
        raw = input(f"  Tu respuesta (A/B/C/D) [⏱️ {SEGUNDOS_POR_PREGUNTA}s]: ").strip().upper()
        tiempo = time.time() - inicio

        if tiempo > SEGUNDOS_POR_PREGUNTA:
            print("  ⏰ ¡Tiempo agotado!")
            return -1, tiempo   # -1 = sin respuesta

        if raw in letras:
            return letras.index(raw), tiempo

        print("  ⚠️  Escribe A, B, C o D.")


def mostrar_feedback(es_correcta, puntos, bonus, respuesta_correcta, pregunta):
    correcta_txt = pregunta["opciones"][pregunta["correcta"]]
    if es_correcta:
        msg = f"  ✅ ¡CORRECTO!  +{puntos} puntos"
        if bonus:
            msg += "  ⚡ ¡Bonus de velocidad!"
        print(msg)
    else:
        print(f"  ❌ Incorrecto. La respuesta era: {correcta_txt}")
    time.sleep(1.2)


def pantalla_fin_partida(resultados, posicion):
    print()
    print("  ══════════════════════════════════════════")
    print("                 FIN DE PARTIDA")
    print("  ══════════════════════════════════════════")
    print(f"  🎯 Correctas:    {resultados['correctas']}/{resultados['total']} ({resultados['porcentaje']}%)")
    print(f"  ⭐ Puntuación:   {resultados['puntos']} puntos")
    print(f"  ⏱️  Tiempo medio: {resultados['tiempo_medio']:.1f}s por pregunta")
    print(f"  🏆 Posición:     #{posicion} en el ranking")

    if resultados["porcentaje"] == 100:
        print("\n  🎉 ¡PERFECTO! ¡Todo correcto! ¡Increíble!")
    elif resultados["porcentaje"] >= 80:
        print("\n  🌟 ¡Muy bien! Gran resultado.")
    elif resultados["porcentaje"] >= 60:
        print("\n  👍 Bien. ¡Sigue practicando!")
    else:
        print("\n  💪 Aún hay margen de mejora. ¡Inténtalo de nuevo!")
    print()


# ─────────────────────────────────────────────
#  FLUJO DE UNA PARTIDA
# ─────────────────────────────────────────────

def jugar_partida(ranking):
    jugador = input("\n  Tu nombre: ").strip()
    if not jugador:
        jugador = "Anónimo"

    print(f"\n  Cargando preguntas...")
    preguntas, fuente = datos.obtener_preguntas(PREGUNTAS_POR_PARTIDA)

    if fuente == "offline":
        print("  ⚠️  Sin conexión — usando preguntas locales.")
    else:
        print(f"  ✅ {len(preguntas)} preguntas cargadas desde internet.")

    input("\n  ¡Preparado? Pulsa Enter para empezar...")

    historial      = []
    puntos_totales = 0

    for i, pregunta in enumerate(preguntas, 1):
        idx, tiempo = mostrar_pregunta(i, len(preguntas), pregunta, puntos_totales)

        if idx == -1:   # Tiempo agotado
            es_correcta, puntos, bonus = False, 0, False
        else:
            es_correcta, puntos, bonus = logica.evaluar_respuesta(pregunta, idx, tiempo)

        mostrar_feedback(es_correcta, puntos, bonus, idx, pregunta)
        puntos_totales += puntos

        historial.append({
            "correcta": es_correcta,
            "puntos":   puntos,
            "tiempo":   min(tiempo, SEGUNDOS_POR_PREGUNTA),
        })

    resultados = logica.calcular_resultados(historial)
    posicion   = logica.posicion_en_ranking(ranking, resultados["puntos"])

    pantalla_fin_partida(resultados, posicion)

    ranking = datos.registrar_resultado(
        ranking, jugador,
        resultados["puntos"], resultados["correctas"],
        resultados["total"],  resultados["tiempo_medio"]
    )
    return ranking


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    pantalla_bienvenida()
    ranking = datos.cargar_ranking()

    while True:
        mostrar_menu()
        opcion = input("  Opción: ").strip()

        if opcion == "1":
            ranking = jugar_partida(ranking)
            mostrar_ranking(ranking)
            input("  [Pulsa Enter para continuar]")
        elif opcion == "2":
            mostrar_ranking(ranking)
            input("  [Pulsa Enter para continuar]")
        elif opcion == "0":
            print("\n  👋 ¡Hasta la próxima!\n")
            break
        else:
            print("  ⚠️  Opción no válida.")


if __name__ == "__main__":
    main()
