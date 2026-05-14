# config.py
import os

BASE_DIR  = os.path.dirname(__file__)
DATOS_DIR = os.path.join(BASE_DIR, "datos")
RUTA_JSON = os.path.join(DATOS_DIR, "gastos.json")

CATEGORIAS = [
    "🍔 Alimentación", "🏠 Vivienda", "🚗 Transporte",
    "💊 Salud",        "🎮 Ocio",     "👕 Ropa",
    "📚 Educación",    "💡 Servicios", "✈️  Viajes", "📦 Otros"
]

MONEDA  = "€"
VERSION = "1.0.0"
