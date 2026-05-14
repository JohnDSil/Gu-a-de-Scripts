# datos.py — Persistencia: leer y escribir contactos en JSON y CSV
import json
import csv
import os
from config import RUTA_JSON, RUTA_CSV, DATOS_DIR


def cargar_contactos():
    """Carga todos los contactos desde el JSON. Devuelve lista vacía si no existe."""
    if not os.path.exists(RUTA_JSON):
        return []
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def guardar_contactos(contactos):
    """Guarda la lista completa de contactos en el JSON."""
    os.makedirs(DATOS_DIR, exist_ok=True)
    with open(RUTA_JSON, "w", encoding="utf-8") as f:
        json.dump(contactos, f, indent=4, ensure_ascii=False)


def exportar_csv(contactos):
    """Exporta todos los contactos a un CSV compatible con Gmail/Outlook."""
    if not contactos:
        return False

    campos = ["id", "nombre", "apellido", "telefono", "email", "grupo", "fecha_creacion"]
    os.makedirs(DATOS_DIR, exist_ok=True)

    with open(RUTA_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(contactos)

    return True


def importar_csv(ruta_csv):
    """
    Importa contactos desde un CSV externo.
    Devuelve (nuevos, duplicados) según el email.
    """
    contactos_actuales = cargar_contactos()
    emails_existentes  = {c.get("email", "").lower() for c in contactos_actuales}

    nuevos     = []
    duplicados = 0

    with open(ruta_csv, "r", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            email = fila.get("email", "").lower()
            if email and email in emails_existentes:
                duplicados += 1
            else:
                nuevos.append(fila)
                if email:
                    emails_existentes.add(email)

    return nuevos, duplicados
