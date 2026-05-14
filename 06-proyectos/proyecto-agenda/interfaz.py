# interfaz.py — Todo lo que el usuario ve y escribe (print/input)
from config import GRUPOS_VALIDOS, VERSION
from logica import validar_contacto, estadisticas


SEP  = "─" * 52
SEP2 = "═" * 52
EMOJI_GRUPO = {"amigos": "👥", "familia": "👨‍👩‍👧", "trabajo": "💼", "otros": "📌"}


# ─────────────────────────────────────────────
#  PANTALLAS
# ─────────────────────────────────────────────

def pantalla_bienvenida():
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║           📒  AGENDA DE CONTACTOS               ║")
    print(f"║                   v{VERSION:<27}║")
    print("╚══════════════════════════════════════════════════╝")
    print()


def pantalla_menu(num_contactos):
    print(SEP2)
    print(f"  Contactos guardados: {num_contactos}")
    print(SEP)
    opciones = [
        ("1", "➕  Nuevo contacto"),
        ("2", "📋  Ver todos"),
        ("3", "🔍  Buscar"),
        ("4", "✏️   Editar contacto"),
        ("5", "🗑️   Eliminar contacto"),
        ("6", "📊  Estadísticas"),
        ("7", "💾  Exportar a CSV"),
        ("0", "🚪  Salir"),
    ]
    for clave, texto in opciones:
        print(f"    {clave}.  {texto}")
    print(SEP)


# ─────────────────────────────────────────────
#  MOSTRAR CONTACTOS
# ─────────────────────────────────────────────

def mostrar_contacto_linea(c):
    """Una línea compacta por contacto."""
    emoji = EMOJI_GRUPO.get(c.get("grupo", "otros"), "📌")
    tel   = c.get("telefono") or "—"
    email = c.get("email")    or "—"
    print(f"  #{c['id']:<4} {emoji} {c['nombre']} {c['apellido']:<20} {tel:<15} {email}")


def mostrar_contacto_detalle(c):
    """Vista detallada de un contacto."""
    emoji = EMOJI_GRUPO.get(c.get("grupo", "otros"), "📌")
    print()
    print(f"  ┌─ Contacto #{c['id']} {'─'*35}┐")
    print(f"  │  {emoji}  {c['nombre']} {c['apellido']}")
    print(f"  │  📞 {c.get('telefono') or '—'}")
    print(f"  │  📧 {c.get('email')    or '—'}")
    print(f"  │  🏷️  Grupo: {c.get('grupo', 'otros').capitalize()}")
    print(f"  │  📅 Creado: {c.get('fecha_creacion', '—')}")
    print(f"  └{'─'*48}┘")


def mostrar_lista(contactos, titulo="CONTACTOS"):
    if not contactos:
        print("\n  📭 No hay contactos que mostrar.\n")
        return
    print(f"\n  {titulo} ({len(contactos)})")
    print(f"  {'─'*52}")
    print(f"  {'ID':<6} {'NOMBRE':<26} {'TELÉFONO':<15} EMAIL")
    print(f"  {'─'*52}")
    for c in sorted(contactos, key=lambda x: x["apellido"].lower()):
        mostrar_contacto_linea(c)
    print()


# ─────────────────────────────────────────────
#  FORMULARIOS DE ENTRADA
# ─────────────────────────────────────────────

def pedir_contacto(contacto_existente=None):
    """
    Pide los datos de un contacto al usuario.
    Si se pasa un contacto existente, muestra los valores actuales como sugerencia.

    Returns:
        dict | None: Campos rellenados, o None si el usuario canceló.
    """
    print()
    if contacto_existente:
        print("  (Deja en blanco para conservar el valor actual)\n")

    def pedir(campo, etiqueta, actual="", requerido=False):
        sufijo = f" [{actual}]" if actual else ""
        while True:
            valor = input(f"  {etiqueta}{sufijo}: ").strip()
            if not valor and actual:
                return actual     # Conserva valor actual
            if not valor and requerido:
                print(f"  ⚠️  {etiqueta} es obligatorio.")
                continue
            return valor

    nombre   = pedir("nombre",   "Nombre",   contacto_existente and contacto_existente["nombre"],   True)
    if nombre.lower() == "cancelar":
        return None
    apellido = pedir("apellido", "Apellido", contacto_existente and contacto_existente["apellido"], True)
    telefono = pedir("telefono", "Teléfono", contacto_existente and contacto_existente.get("telefono", ""))
    email    = pedir("email",    "Email",    contacto_existente and contacto_existente.get("email", ""))

    print(f"  Grupos: {', '.join(GRUPOS_VALIDOS)}")
    grupo = pedir("grupo", "Grupo", contacto_existente and contacto_existente.get("grupo", "otros"))

    # Validar
    errores = validar_contacto(nombre, apellido, telefono, email, grupo or "otros")
    if errores:
        print("\n  ❌ Errores encontrados:")
        for e in errores:
            print(f"     • {e}")
        return None

    return {
        "nombre":   nombre,
        "apellido": apellido,
        "telefono": telefono,
        "email":    email,
        "grupo":    grupo or "otros",
    }


def pedir_id(mensaje="  ID del contacto: "):
    """Pide un ID numérico al usuario."""
    try:
        return int(input(mensaje))
    except ValueError:
        return None


def confirmar(mensaje):
    """Pide confirmación si/no. Devuelve True si el usuario dice sí."""
    r = input(f"  {mensaje} (si/no): ").strip().lower()
    return r in ["si", "sí", "s"]


# ─────────────────────────────────────────────
#  PANTALLA DE ESTADÍSTICAS
# ─────────────────────────────────────────────

def pantalla_estadisticas(contactos):
    stats = estadisticas(contactos)
    if stats["total"] == 0:
        print("\n  📭 La agenda está vacía.\n")
        return

    print(f"\n  📊 ESTADÍSTICAS DE LA AGENDA")
    print(f"  {SEP}")
    print(f"  Total de contactos:  {stats['total']}")
    print(f"  Con teléfono:        {stats['con_tel']}")
    print(f"  Con email:           {stats['con_email']}")
    print(f"\n  Por grupo:")
    for grupo, n in sorted(stats["por_grupo"].items(), key=lambda x: -x[1]):
        emoji = EMOJI_GRUPO.get(grupo, "📌")
        barra = "█" * n + "░" * (stats["total"] - n)
        print(f"    {emoji} {grupo.capitalize():<10} {n:>3}  {barra}")
    print()


# ─────────────────────────────────────────────
#  MENSAJES DE FEEDBACK
# ─────────────────────────────────────────────

def ok(mensaje):  print(f"\n  ✅ {mensaje}\n")
def error(mensaje): print(f"\n  ❌ {mensaje}\n")
def info(mensaje):  print(f"\n  ℹ️  {mensaje}\n")
def pausa():        input("  [Pulsa Enter para continuar]")
