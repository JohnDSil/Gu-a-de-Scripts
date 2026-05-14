# config.py — Configuración y constantes del proyecto Agenda
import os

BASE_DIR   = os.path.dirname(__file__)
DATOS_DIR  = os.path.join(BASE_DIR, "datos")
RUTA_JSON  = os.path.join(DATOS_DIR, "contactos.json")
RUTA_CSV   = os.path.join(DATOS_DIR, "contactos_exportados.csv")

GRUPOS_VALIDOS = ["amigos", "familia", "trabajo", "otros"]
VERSION        = "1.0.0"
