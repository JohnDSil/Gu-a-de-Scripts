# logica.py — Motor del quiz: evaluar respuestas, calcular puntos
import time
from config import PUNTOS_POR_CORRECTA, BONUS_RAPIDO, SEGUNDOS_POR_PREGUNTA


def evaluar_respuesta(pregunta, indice_respuesta, tiempo_tardado):
    """
    Evalúa si la respuesta es correcta y calcula los puntos.

    Returns:
        tuple: (es_correcta: bool, puntos: int, bonus: bool)
    """
    es_correcta = indice_respuesta == pregunta["correcta"]
    if not es_correcta:
        return False, 0, False

    bonus = tiempo_tardado < BONUS_RAPIDO
    puntos = PUNTOS_POR_CORRECTA + (BONUS_RAPIDO if bonus else 0)
    return True, puntos, bonus


def calcular_resultados(historial):
    """
    Calcula los resultados finales de una partida.

    Args:
        historial: lista de dicts por pregunta con correcta, puntos, tiempo

    Returns:
        dict con correctas, total, puntos, tiempo_medio, porcentaje
    """
    correctas    = sum(1 for h in historial if h["correcta"])
    puntos       = sum(h["puntos"] for h in historial)
    tiempo_medio = sum(h["tiempo"] for h in historial) / len(historial) if historial else 0

    return {
        "correctas":    correctas,
        "total":        len(historial),
        "puntos":       puntos,
        "tiempo_medio": tiempo_medio,
        "porcentaje":   round(correctas / len(historial) * 100) if historial else 0,
    }


def posicion_en_ranking(ranking, puntos):
    """Devuelve en qué posición quedaría esta puntuación."""
    for i, entrada in enumerate(ranking):
        if puntos >= entrada["puntos"]:
            return i + 1
    return len(ranking) + 1


def medir_tiempo_respuesta(pregunta_fn):
    """
    Ejecuta pregunta_fn y mide cuánto tiempo tardó el usuario.

    Returns:
        tuple: (resultado_de_fn, segundos_tardados)
    """
    inicio    = time.time()
    resultado = pregunta_fn()
    tardado   = time.time() - inicio
    return resultado, tardado
