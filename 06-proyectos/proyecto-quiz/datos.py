# datos.py — Ranking persistente y preguntas desde API
import json
import os
import random
from config import RUTA_RANKING, DATOS_DIR, PREGUNTAS_OFFLINE, PREGUNTAS_POR_PARTIDA

try:
    import requests
    REQUESTS_OK = True
except ImportError:
    REQUESTS_OK = False


def cargar_ranking():
    if not os.path.exists(RUTA_RANKING):
        return []
    try:
        with open(RUTA_RANKING, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def guardar_ranking(ranking):
    os.makedirs(DATOS_DIR, exist_ok=True)
    with open(RUTA_RANKING, "w", encoding="utf-8") as f:
        json.dump(ranking, f, indent=4, ensure_ascii=False)


def registrar_resultado(ranking, jugador, puntos, correctas, total, tiempo_medio):
    from datetime import datetime
    entrada = {
        "jugador":      jugador,
        "puntos":       puntos,
        "correctas":    correctas,
        "total":        total,
        "pct":          round(correctas / total * 100),
        "tiempo_medio": round(tiempo_medio, 1),
        "fecha":        datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    ranking.append(entrada)
    # Ordenar por puntos descendente
    ranking.sort(key=lambda x: x["puntos"], reverse=True)
    # Conservar solo el top 20
    del ranking[20:]
    guardar_ranking(ranking)
    return ranking


def obtener_preguntas_api(cantidad=PREGUNTAS_POR_PARTIDA):
    """
    Descarga preguntas de la Open Trivia DB (gratuita, sin API key).
    Devuelve lista de dicts con: pregunta, opciones, correcta (índice).
    """
    if not REQUESTS_OK:
        return None

    try:
        url = "https://opentdb.com/api.php"
        params = {"amount": cantidad, "type": "multiple", "lang": "es"}
        r = requests.get(url, params=params, timeout=8)
        r.raise_for_status()
        datos = r.json()

        if datos.get("response_code") != 0:
            return None

        preguntas = []
        for item in datos["results"]:
            # Limpiamos entidades HTML básicas
            def limpiar(texto):
                return (texto.replace("&quot;", '"').replace("&#039;", "'")
                        .replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">"))

            incorrectas = [limpiar(o) for o in item["incorrect_answers"]]
            correcta_txt = limpiar(item["correct_answer"])
            opciones     = incorrectas + [correcta_txt]
            random.shuffle(opciones)
            idx_correcta = opciones.index(correcta_txt)

            preguntas.append({
                "pregunta": limpiar(item["question"]),
                "opciones": opciones,
                "correcta": idx_correcta,
            })
        return preguntas

    except Exception:
        return None


def obtener_preguntas(cantidad=PREGUNTAS_POR_PARTIDA):
    """Intenta API; si falla, usa preguntas offline."""
    preguntas = obtener_preguntas_api(cantidad)
    if preguntas:
        return preguntas, "online"
    muestra = random.sample(PREGUNTAS_OFFLINE, min(cantidad, len(PREGUNTAS_OFFLINE)))
    return muestra, "offline"
