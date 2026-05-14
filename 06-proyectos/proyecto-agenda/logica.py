# logica.py — Lógica de negocio: CRUD, búsqueda, validación
from datetime import datetime
from config import GRUPOS_VALIDOS


# ─────────────────────────────────────────────
#  GENERACIÓN DE IDs
# ─────────────────────────────────────────────

def siguiente_id(contactos):
    """Devuelve el siguiente ID disponible (máximo actual + 1)."""
    if not contactos:
        return 1
    return max(c["id"] for c in contactos) + 1


# ─────────────────────────────────────────────
#  VALIDACIÓN
# ─────────────────────────────────────────────

def validar_contacto(nombre, apellido, telefono, email, grupo):
    """
    Valida los campos de un contacto.

    Returns:
        list[str]: Lista de errores. Vacía si todo es válido.
    """
    errores = []

    if not nombre.strip():
        errores.append("El nombre no puede estar vacío.")
    if not apellido.strip():
        errores.append("El apellido no puede estar vacío.")
    if telefono and not telefono.replace(" ", "").replace("+", "").isdigit():
        errores.append("El teléfono solo puede contener dígitos, espacios y '+'.")
    if email and ("@" not in email or "." not in email.split("@")[-1]):
        errores.append("El email no tiene un formato válido.")
    if grupo not in GRUPOS_VALIDOS:
        errores.append(f"Grupo inválido. Opciones: {', '.join(GRUPOS_VALIDOS)}")

    return errores


# ─────────────────────────────────────────────
#  CRUD
# ─────────────────────────────────────────────

def crear_contacto(contactos, nombre, apellido, telefono="", email="", grupo="otros"):
    """Crea un nuevo contacto y lo añade a la lista. Devuelve el contacto creado."""
    contacto = {
        "id":             siguiente_id(contactos),
        "nombre":         nombre.strip(),
        "apellido":       apellido.strip(),
        "telefono":       telefono.strip(),
        "email":          email.strip().lower(),
        "grupo":          grupo.lower(),
        "fecha_creacion": datetime.now().strftime("%Y-%m-%d"),
    }
    contactos.append(contacto)
    return contacto


def buscar_contactos(contactos, termino):
    """
    Busca contactos por nombre, apellido, email o teléfono.
    La búsqueda es insensible a mayúsculas.
    """
    termino = termino.lower()
    return [
        c for c in contactos
        if termino in c["nombre"].lower()
        or termino in c["apellido"].lower()
        or termino in c.get("email", "").lower()
        or termino in c.get("telefono", "")
    ]


def obtener_por_id(contactos, id_buscado):
    """Devuelve el contacto con ese ID, o None si no existe."""
    return next((c for c in contactos if c["id"] == id_buscado), None)


def actualizar_contacto(contactos, id_contacto, cambios):
    """
    Actualiza los campos indicados de un contacto.

    Args:
        cambios (dict): Solo los campos que se quieren cambiar.

    Returns:
        bool: True si se encontró y actualizó, False si no existe.
    """
    contacto = obtener_por_id(contactos, id_contacto)
    if not contacto:
        return False
    campos_editables = ["nombre", "apellido", "telefono", "email", "grupo"]
    for campo, valor in cambios.items():
        if campo in campos_editables:
            contacto[campo] = valor.strip() if isinstance(valor, str) else valor
    return True


def eliminar_contacto(contactos, id_contacto):
    """Elimina el contacto con ese ID. Devuelve True si lo encontró."""
    original = len(contactos)
    contactos[:] = [c for c in contactos if c["id"] != id_contacto]
    return len(contactos) < original


# ─────────────────────────────────────────────
#  ESTADÍSTICAS
# ─────────────────────────────────────────────

def estadisticas(contactos):
    """Devuelve un dict con estadísticas de la agenda."""
    if not contactos:
        return {"total": 0}

    por_grupo = {}
    con_email = 0
    con_tel   = 0

    for c in contactos:
        g = c.get("grupo", "otros")
        por_grupo[g] = por_grupo.get(g, 0) + 1
        if c.get("email"):   con_email += 1
        if c.get("telefono"): con_tel  += 1

    return {
        "total":     len(contactos),
        "por_grupo": por_grupo,
        "con_email": con_email,
        "con_tel":   con_tel,
    }
