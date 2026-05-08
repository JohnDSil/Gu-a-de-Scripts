# =============================================================================
# SCRIPT 04 — Archivos JSON
# =============================================================================
# JSON es el formato estándar para guardar datos estructurados y complejos.
# APIs, configuraciones, bases de datos ligeras: todo usa JSON.
# Conceptos: json.load(), json.dump(), json.loads(), json.dumps()
# =============================================================================

import json
import os
from datetime import datetime

CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "..", "datos")
CARPETA_DATOS = os.path.abspath(CARPETA_DATOS)
RUTA_PUNTUACIONES = os.path.join(CARPETA_DATOS, "puntuaciones.json")


# ─────────────────────────────────────────────
#  PARTE 1: LEER UN ARCHIVO JSON
# ─────────────────────────────────────────────

print("=" * 55)
print("  PARTE 1: LEER JSON")
print("=" * 55)
print()

with open(RUTA_PUNTUACIONES, "r", encoding="utf-8") as f:
    datos = json.load(f)       # Convierte JSON → diccionario/lista Python

# La estructura ya la conocemos (la definimos en datos/puntuaciones.json)
config    = datos["configuracion"]
partidas  = datos["partidas"]

print(f"⚙️  Configuración del juego:")
print(f"   Rango:    {config['numero_min']} al {config['numero_max']}")
print(f"   Intentos: {config['max_intentos']}")
print()

print(f"🎮 Partidas registradas: {len(partidas)}")
print()

for p in partidas:
    estado = "✅ Ganó" if p["gano"] else "❌ Perdió"
    print(f"  {p['fecha']} | {p['jugador']:<10} | {estado} | {p['intentos']} intentos")

print()

# Análisis rápido
ganadas  = [p for p in partidas if p["gano"]]
promedio = sum(p["intentos"] for p in partidas) / len(partidas)

print(f"📊 Estadísticas:")
print(f"   Tasa de victoria: {len(ganadas)}/{len(partidas)} ({len(ganadas)/len(partidas)*100:.0f}%)")
print(f"   Media de intentos: {promedio:.1f}")

print()


# ─────────────────────────────────────────────
#  PARTE 2: ESCRIBIR Y ACTUALIZAR JSON
# ─────────────────────────────────────────────

print("=" * 55)
print("  PARTE 2: ACTUALIZAR JSON")
print("=" * 55)
print()

def cargar_puntuaciones(ruta):
    """Carga las puntuaciones desde JSON. Crea el archivo si no existe."""
    if not os.path.exists(ruta):
        estructura_inicial = {
            "partidas": [],
            "configuracion": {
                "numero_min": 1,
                "numero_max": 100,
                "max_intentos": 7
            }
        }
        guardar_puntuaciones(ruta, estructura_inicial)
        return estructura_inicial

    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_puntuaciones(ruta, datos):
    """Guarda las puntuaciones en JSON con formato legible."""
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(
            datos,
            f,
            indent=4,              # Sangría de 4 espacios (legible)
            ensure_ascii=False     # Permite ñ, tildes, etc.
        )

def registrar_partida(ruta, jugador, intentos, gano):
    """
    Añade una nueva partida al historial JSON.

    Args:
        ruta (str): Ruta al archivo JSON.
        jugador (str): Nombre del jugador.
        intentos (int): Número de intentos usados.
        gano (bool): Si el jugador ganó.
    """
    datos = cargar_puntuaciones(ruta)

    nueva_partida = {
        "jugador": jugador,
        "intentos": intentos,
        "gano": gano,
        "fecha": datetime.now().strftime("%Y-%m-%d")
    }

    datos["partidas"].append(nueva_partida)
    guardar_puntuaciones(ruta, datos)
    print(f"  ✅ Partida registrada para '{jugador}'")

# Añadimos nuevas partidas al historial
ruta_historial = os.path.join(CARPETA_DATOS, "puntuaciones_actualizado.json")

# Primero copiamos el original para no modificarlo
import shutil
shutil.copy(RUTA_PUNTUACIONES, ruta_historial)

registrar_partida(ruta_historial, "María", intentos=3, gano=True)
registrar_partida(ruta_historial, "Pedro", intentos=7, gano=False)
registrar_partida(ruta_historial, "Laura", intentos=1, gano=True)

# Verificar el archivo actualizado
datos_actualizados = cargar_puntuaciones(ruta_historial)
print(f"\n📈 Total de partidas ahora: {len(datos_actualizados['partidas'])}")

print()


# ─────────────────────────────────────────────
#  PARTE 3: JSON COMO CONFIGURACIÓN
# ─────────────────────────────────────────────

print("=" * 55)
print("  PARTE 3: JSON COMO ARCHIVO DE CONFIGURACIÓN")
print("=" * 55)
print()

CONFIG_PREDETERMINADA = {
    "app": {
        "nombre": "Mi App",
        "version": "1.0.0",
        "idioma": "es"
    },
    "interfaz": {
        "tema": "claro",
        "fuente_tamanio": 14,
        "mostrar_ayuda": True
    },
    "juego": {
        "dificultad": "normal",
        "sonido": True,
        "volumen": 75
    }
}

ruta_config = os.path.join(CARPETA_DATOS, "config_app.json")

def obtener_config(ruta, predeterminada):
    """Carga config desde JSON, creando el archivo con valores por defecto si no existe."""
    if not os.path.exists(ruta):
        print("  ⚙️  Config no encontrada. Creando con valores por defecto...")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(predeterminada, f, indent=4, ensure_ascii=False)
        return predeterminada

    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def modificar_config(ruta, seccion, clave, valor):
    """Modifica un valor específico de la configuración."""
    with open(ruta, "r", encoding="utf-8") as f:
        config = json.load(f)

    config[seccion][clave] = valor

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    print(f"  ✅ Actualizado: config['{seccion}']['{clave}'] = {valor!r}")

# Cargar o crear configuración
config = obtener_config(ruta_config, CONFIG_PREDETERMINADA)
print(f"📋 Configuración cargada:")
print(f"   App: {config['app']['nombre']} v{config['app']['version']}")
print(f"   Tema: {config['interfaz']['tema']}")
print(f"   Volumen: {config['juego']['volumen']}%")

print()
print("Modificando configuración...")
modificar_config(ruta_config, "interfaz", "tema", "oscuro")
modificar_config(ruta_config, "juego", "volumen", 50)
modificar_config(ruta_config, "app", "idioma", "en")

# Verificar los cambios
config_nueva = obtener_config(ruta_config, {})
print(f"\n📋 Config actualizada:")
print(f"   Tema: {config_nueva['interfaz']['tema']}")
print(f"   Volumen: {config_nueva['juego']['volumen']}%")
print(f"   Idioma: {config_nueva['app']['idioma']}")

print()


# ─────────────────────────────────────────────
#  PARTE 4: JSON VS STRING (json.loads / json.dumps)
# ─────────────────────────────────────────────

print("=" * 55)
print("  PARTE 4: JSON ↔ STRING")
print("=" * 55)
print()

# json.dumps() convierte Python → string JSON (sin archivo)
datos_python = {"nombre": "Ana", "nota": 9.5, "aprobado": True}
texto_json   = json.dumps(datos_python, ensure_ascii=False)
print(f"Python → JSON string: {texto_json}")
print(f"Tipo: {type(texto_json)}")

# json.loads() convierte string JSON → Python (sin archivo)
texto_recibido = '{"ciudad": "Sevilla", "temperatura": 28, "llueve": false}'
datos_recibidos = json.loads(texto_recibido)
print(f"\nJSON string → Python: {datos_recibidos}")
print(f"Tipo: {type(datos_recibidos)}")
print(f"Ciudad: {datos_recibidos['ciudad']}, Temp: {datos_recibidos['temperatura']}°C")

# =============================================================================
# ¿Qué has aprendido?
# - json.load(f)          → archivo JSON → objeto Python
# - json.dump(datos, f)   → objeto Python → archivo JSON
# - json.loads(string)    → string JSON → objeto Python
# - json.dumps(datos)     → objeto Python → string JSON
# - indent=4              → formateado con sangría (más legible)
# - ensure_ascii=False    → permite caracteres españoles
# - JSON es perfecto para: configs, historiales, datos anidados
# - CSV es mejor para: datos tabulares simples (filas y columnas)
# =============================================================================
