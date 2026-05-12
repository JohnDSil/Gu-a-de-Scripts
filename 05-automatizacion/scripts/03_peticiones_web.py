# =============================================================================
# SCRIPT 03 — Peticiones Web y APIs Reales
# =============================================================================
# Python puede hablar con internet: consultar el tiempo, cambiar divisas,
# obtener datos de cualquier API pública. Todo con el módulo requests.
#
# ⚠️  Requisito: pip install requests
#
# APIs usadas (todas GRATUITAS, sin registro):
#   - open-meteo.com   → clima actual
#   - exchangerate-api → divisas
#   - official-joke-api → chistes en inglés
#   - catfact.ninja    → datos curiosos sobre gatos 🐱
# =============================================================================

import json
import os

# Intentamos importar requests; si no está, damos instrucciones claras
try:
    import requests
    REQUESTS_DISPONIBLE = True
except ImportError:
    REQUESTS_DISPONIBLE = False
    print("⚠️  'requests' no está instalado.")
    print("   Ejecuta: pip install requests")
    print("   Luego vuelve a correr este script.\n")


def hacer_peticion(url, params=None, timeout=10):
    """
    Realiza una petición GET con manejo de errores centralizado.

    Args:
        url (str): URL de la API.
        params (dict): Parámetros de la URL (?clave=valor).
        timeout (int): Segundos máximos de espera.

    Returns:
        dict | None: Datos JSON o None si falló.
    """
    if not REQUESTS_DISPONIBLE:
        return None
    try:
        respuesta = requests.get(url, params=params, timeout=timeout)
        respuesta.raise_for_status()   # Lanza excepción si status != 200
        return respuesta.json()
    except requests.exceptions.ConnectionError:
        print("  ❌ Sin conexión a internet.")
    except requests.exceptions.Timeout:
        print("  ❌ La petición tardó demasiado (timeout).")
    except requests.exceptions.HTTPError as e:
        print(f"  ❌ Error HTTP: {e}")
    except requests.exceptions.JSONDecodeError:
        print("  ❌ La respuesta no es JSON válido.")
    return None


# ─────────────────────────────────────────────
#  API 1: CLIMA ACTUAL (open-meteo.com)
#  Sin API key, completamente gratuita
# ─────────────────────────────────────────────

def obtener_clima(ciudad="Sevilla", latitud=37.39, longitud=-5.99):
    """
    Consulta el clima actual de una ciudad usando Open-Meteo.

    La API necesita coordenadas (lat/lon) en lugar del nombre de la ciudad.
    Coordenadas predeterminadas: Sevilla, España.
    """
    print("=" * 55)
    print(f"  ☀️  CLIMA EN {ciudad.upper()}")
    print("=" * 55)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":   latitud,
        "longitude":  longitud,
        "current":    "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "timezone":   "Europe/Madrid"
    }

    datos = hacer_peticion(url, params)
    if not datos:
        # Datos de ejemplo si no hay conexión
        print("  (Mostrando datos de ejemplo sin conexión)\n")
        print(f"  📍 Ciudad:      {ciudad}")
        print(f"  🌡️  Temperatura: 22°C")
        print(f"  💧 Humedad:     65%")
        print(f"  💨 Viento:      15 km/h")
        return

    actual = datos.get("current", {})
    temp   = actual.get("temperature_2m", "N/A")
    hum    = actual.get("relative_humidity_2m", "N/A")
    viento = actual.get("wind_speed_10m", "N/A")
    codigo = actual.get("weather_code", 0)

    # Códigos WMO de clima → descripción
    descripciones = {
        0: "☀️  Despejado",  1: "🌤️  Mayormente despejado",
        2: "⛅ Parcialmente nublado", 3: "☁️  Nublado",
        45: "🌫️  Niebla", 51: "🌦️  Llovizna ligera",
        61: "🌧️  Lluvia", 71: "🌨️  Nieve", 80: "🌦️  Chubascos",
        95: "⛈️  Tormenta"
    }
    descripcion = descripciones.get(codigo, f"Código {codigo}")

    print(f"  📍 Ciudad:      {ciudad}")
    print(f"  {descripcion}")
    print(f"  🌡️  Temperatura: {temp}°C")
    print(f"  💧 Humedad:     {hum}%")
    print(f"  💨 Viento:      {viento} km/h")
    print()


# ─────────────────────────────────────────────
#  API 2: TIPO DE CAMBIO (frankfurter.app)
#  Sin API key, gratuita
# ─────────────────────────────────────────────

def convertir_divisa(cantidad, moneda_origen="EUR", moneda_destino="USD"):
    """Convierte entre divisas usando la API de Frankfurter."""
    print("=" * 55)
    print("  💱 CONVERSOR DE DIVISAS")
    print("=" * 55)

    url = f"https://api.frankfurter.app/latest"
    params = {"from": moneda_origen, "to": moneda_destino}

    datos = hacer_peticion(url, params)
    if not datos:
        print("  (Sin conexión — usando tasa de ejemplo: 1 EUR = 1.08 USD)\n")
        tasa = 1.08
    else:
        tasa = datos["rates"].get(moneda_destino)
        if not tasa:
            print(f"  ❌ Divisa '{moneda_destino}' no encontrada.")
            return

    resultado = cantidad * tasa
    print(f"  {cantidad:,.2f} {moneda_origen}  =  {resultado:,.2f} {moneda_destino}")
    print(f"  Tasa: 1 {moneda_origen} = {tasa} {moneda_destino}")
    print()


def mostrar_tasas_multiples(moneda_base="EUR"):
    """Muestra las tasas de cambio de la moneda base contra varias divisas."""
    print(f"  Tasas de cambio para 1 {moneda_base}:")

    monedas = ["USD", "GBP", "JPY", "CHF", "CAD", "MXN"]
    url = "https://api.frankfurter.app/latest"
    params = {"from": moneda_base, "to": ",".join(monedas)}

    datos = hacer_peticion(url, params)
    if not datos:
        tasas_ejemplo = {"USD": 1.08, "GBP": 0.86, "JPY": 161.2, "CHF": 0.97, "CAD": 1.47, "MXN": 19.5}
        for moneda, tasa in tasas_ejemplo.items():
            print(f"    1 {moneda_base} = {tasa:>8.4f} {moneda}")
    else:
        for moneda, tasa in datos["rates"].items():
            print(f"    1 {moneda_base} = {tasa:>8.4f} {moneda}")
    print()


# ─────────────────────────────────────────────
#  API 3: DATO CURIOSO SOBRE GATOS 🐱
#  catfact.ninja — sin API key
# ─────────────────────────────────────────────

def dato_curioso_gato():
    """Obtiene un dato curioso aleatorio sobre gatos."""
    print("=" * 55)
    print("  🐱 DATO CURIOSO DEL DÍA")
    print("=" * 55)

    datos = hacer_peticion("https://catfact.ninja/fact")
    if datos:
        hecho = datos.get("fact", "Los gatos son increíbles.")
        print(f"  💡 {hecho}")
    else:
        print("  💡 Los gatos tienen 32 músculos en cada oreja.")
    print()


# ─────────────────────────────────────────────
#  PARTE 4: GUARDAR RESPUESTA DE API EN ARCHIVO
# ─────────────────────────────────────────────

def guardar_datos_api(datos, nombre_archivo):
    """Guarda los datos de una API en un archivo JSON local."""
    carpeta = os.path.join(os.path.dirname(__file__), "..", "datos")
    ruta = os.path.join(os.path.abspath(carpeta), nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(f"  💾 Datos guardados en: {nombre_archivo}")


# ─────────────────────────────────────────────
#  PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║     🌐 CONSULTANDO APIS EN TIEMPO REAL      ║")
    print("╚══════════════════════════════════════════════╝")
    print()

    # 1. Clima
    obtener_clima("Sevilla", latitud=37.39, longitud=-5.99)

    # 2. Divisas
    mostrar_tasas_multiples("EUR")
    convertir_divisa(100, "EUR", "USD")
    convertir_divisa(100, "EUR", "GBP")

    # 3. Dato curioso
    dato_curioso_gato()

    # 4. Guardar datos del clima en JSON
    print("=" * 55)
    print("  💾 GUARDAR RESPUESTA DE API")
    print("=" * 55)
    if REQUESTS_DISPONIBLE:
        datos_clima = hacer_peticion(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": 37.39, "longitude": -5.99,
                    "current": "temperature_2m,weather_code", "timezone": "Europe/Madrid"}
        )
        if datos_clima:
            from datetime import datetime
            datos_clima["consultado_en"] = datetime.now().isoformat()
            guardar_datos_api(datos_clima, "clima_sevilla.json")
            print("  ✅ Puedes abrir el JSON para ver la estructura completa.")
    else:
        print("  (Instala requests para guardar datos reales)")

# =============================================================================
# ¿Qué has aprendido?
# - requests.get(url, params=params) → petición HTTP GET con parámetros
# - respuesta.raise_for_status()      → lanza excepción si el servidor falla
# - respuesta.json()                  → convierte la respuesta JSON a dict Python
# - ConnectionError, Timeout, HTTPError → los tres errores más comunes de red
# - Las APIs públicas no necesitan registro y son perfectas para practicar
# - Siempre maneja el caso "sin conexión" para que el script no se rompa
# =============================================================================
