# datos.py
import json
import os
from config import RUTA_JSON, DATOS_DIR


def cargar_gastos():
    if not os.path.exists(RUTA_JSON):
        return []
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def guardar_gastos(gastos):
    os.makedirs(DATOS_DIR, exist_ok=True)
    with open(RUTA_JSON, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)
