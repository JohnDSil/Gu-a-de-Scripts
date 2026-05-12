# =============================================================================
# SCRIPT 04 — Argumentos de Línea de Comandos
# =============================================================================
# Los scripts profesionales se usan desde la terminal pasando argumentos,
# no solo ejecutándolos sin más. Así un mismo script sirve para muchos casos.
#
# Ejemplos de uso:
#   python 04_argumentos_cli.py --ayuda
#   python 04_argumentos_cli.py saludar --nombre Ana
#   python 04_argumentos_cli.py calcular --operacion suma --a 15 --b 27
#   python 04_argumentos_cli.py info --archivo estudiantes.csv
#
# Conceptos: sys.argv, argparse, subcomandos, scripts de terminal
# =============================================================================

import sys
import os

CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "..", "datos")
CARPETA_DATOS = os.path.abspath(CARPETA_DATOS)


# ─────────────────────────────────────────────
#  PARTE 1: sys.argv — la forma manual (básica)
# ─────────────────────────────────────────────

# sys.argv es una lista con todos los argumentos que recibió el script:
# sys.argv[0] → nombre del script
# sys.argv[1] → primer argumento
# sys.argv[2] → segundo argumento...

print("=" * 55)
print("  PARTE 1: sys.argv — argumentos raw")
print("=" * 55)
print()
print(f"  Este script se llamó como:")
print(f"  $ python {' '.join(sys.argv)}")
print()
print(f"  sys.argv tiene {len(sys.argv)} elemento(s):")
for i, arg in enumerate(sys.argv):
    etiqueta = "(nombre del script)" if i == 0 else f"(argumento {i})"
    print(f"    [{i}] = '{arg}'  {etiqueta}")

print()


# ─────────────────────────────────────────────
#  PARTE 2: argparse — la forma profesional
# ─────────────────────────────────────────────

# argparse es el módulo estándar de Python para CLIs.
# Genera ayuda automática, valida tipos y maneja errores.

import argparse

print("=" * 55)
print("  PARTE 2: Construyendo una CLI con argparse")
print("=" * 55)
print()


def construir_parser():
    """Construye y devuelve el parser de argumentos de la CLI."""

    parser = argparse.ArgumentParser(
        prog="mi_herramienta",
        description="🛠️  Herramienta de ejemplo — Scripts Roadmap Nivel 5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python 04_argumentos_cli.py saludar --nombre Ana
  python 04_argumentos_cli.py calcular --op suma --a 10 --b 5
  python 04_argumentos_cli.py info --archivo estudiantes.csv
  python 04_argumentos_cli.py convertir --cantidad 100 --de EUR --a USD
        """
    )

    # Subcomandos: cada "comando" tiene sus propios argumentos
    subparsers = parser.add_subparsers(dest="comando", help="Comandos disponibles")

    # ── Subcomando: saludar ──────────────────
    p_saludar = subparsers.add_parser("saludar", help="Genera un saludo personalizado")
    p_saludar.add_argument("--nombre", "-n", required=True,  help="Nombre de la persona")
    p_saludar.add_argument("--idioma", "-i", default="es",   help="Idioma: es, en, fr (default: es)")
    p_saludar.add_argument("--formal",       action="store_true", help="Usar tono formal")

    # ── Subcomando: calcular ─────────────────
    p_calc = subparsers.add_parser("calcular", help="Realiza una operación matemática")
    p_calc.add_argument("--op",  choices=["suma", "resta", "multi", "div"], required=True)
    p_calc.add_argument("--a",   type=float, required=True, help="Primer número")
    p_calc.add_argument("--b",   type=float, required=True, help="Segundo número")

    # ── Subcomando: info ─────────────────────
    p_info = subparsers.add_parser("info", help="Muestra info de un archivo")
    p_info.add_argument("--archivo", "-f", required=True, help="Nombre del archivo en datos/")

    # ── Subcomando: convertir ────────────────
    p_conv = subparsers.add_parser("convertir", help="Convierte temperatura o longitud")
    p_conv.add_argument("--tipo",     choices=["temp", "longitud"], default="temp")
    p_conv.add_argument("--cantidad", type=float, required=True)
    p_conv.add_argument("--de",       required=True, help="Unidad origen (C, F, K, m, km, mi)")
    p_conv.add_argument("--a",        required=True, help="Unidad destino")

    return parser


# ─────────────────────────────────────────────
#  FUNCIONES DE CADA SUBCOMANDO
# ─────────────────────────────────────────────

def cmd_saludar(args):
    """Ejecuta el subcomando 'saludar'."""
    saludos = {
        "es": ("Hola",       "Buenos días",      "¿Cómo estás?"),
        "en": ("Hello",      "Good morning",     "How are you?"),
        "fr": ("Bonjour",    "Bonjour",          "Comment allez-vous?"),
        "de": ("Hallo",      "Guten Morgen",     "Wie geht es Ihnen?"),
    }

    idioma = args.idioma if args.idioma in saludos else "es"
    informal, formal_sal, pregunta = saludos[idioma]

    if args.formal:
        saludo = f"{formal_sal}, {args.nombre}. {pregunta}"
    else:
        saludo = f"{informal}, {args.nombre}! 👋"

    print(f"\n  💬 {saludo}\n")


def cmd_calcular(args):
    """Ejecuta el subcomando 'calcular'."""
    a, b = args.a, args.b
    operaciones = {
        "suma":  (a + b,      f"{a} + {b}"),
        "resta": (a - b,      f"{a} - {b}"),
        "multi": (a * b,      f"{a} × {b}"),
        "div":   (a / b if b != 0 else None, f"{a} ÷ {b}"),
    }

    resultado, expresion = operaciones[args.op]
    print()
    if resultado is None:
        print(f"  ❌ Error: División entre cero.")
    else:
        print(f"  🧮 {expresion} = {resultado:.4f}".rstrip("0").rstrip(".") + "\n")


def cmd_info(args):
    """Ejecuta el subcomando 'info': muestra info de un archivo."""
    ruta = os.path.join(CARPETA_DATOS, args.archivo)

    print()
    if not os.path.exists(ruta):
        print(f"  ❌ No encontrado: {args.archivo}")
        print(f"  → Buscado en: {CARPETA_DATOS}")
        archivos = os.listdir(CARPETA_DATOS)
        print(f"  → Archivos disponibles: {', '.join(archivos)}")
        return

    tamanio  = os.path.getsize(ruta)
    ext      = os.path.splitext(args.archivo)[1]
    tam_kb   = tamanio / 1024

    print(f"  📄 Archivo: {args.archivo}")
    print(f"     Tamaño:    {tam_kb:.2f} KB ({tamanio} bytes)")
    print(f"     Extensión: {ext}")

    # Para CSV: contar filas
    if ext == ".csv":
        with open(ruta, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        print(f"     Filas (sin cabecera): {len(lineas) - 1}")
        print(f"     Cabecera: {lineas[0].strip()}")

    # Para JSON: mostrar claves
    elif ext == ".json":
        import json
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        if isinstance(datos, dict):
            print(f"     Claves: {', '.join(datos.keys())}")
        elif isinstance(datos, list):
            print(f"     Elementos en lista: {len(datos)}")

    # Para TXT: contar líneas y palabras
    elif ext == ".txt":
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
        lineas = contenido.splitlines()
        palabras = contenido.split()
        print(f"     Líneas:  {len(lineas)}")
        print(f"     Palabras: {len(palabras)}")

    print()


def cmd_convertir(args):
    """Ejecuta el subcomando 'convertir'."""
    print()
    v = args.cantidad
    origen = args.de.upper()
    destino = args.a.upper()

    if args.tipo == "temp":
        conversiones_temp = {
            ("C", "F"): lambda c: c * 9/5 + 32,
            ("F", "C"): lambda f: (f - 32) * 5/9,
            ("C", "K"): lambda c: c + 273.15,
            ("K", "C"): lambda k: k - 273.15,
            ("F", "K"): lambda f: (f - 32) * 5/9 + 273.15,
            ("K", "F"): lambda k: (k - 273.15) * 9/5 + 32,
        }
        fn = conversiones_temp.get((origen, destino))
        if fn:
            print(f"  🌡️  {v} °{origen}  =  {fn(v):.2f} °{destino}\n")
        else:
            print(f"  ❌ Conversión {origen} → {destino} no soportada.\n")

    elif args.tipo == "longitud":
        conversiones_long = {
            ("M",  "KM"): lambda x: x / 1000,
            ("KM", "M"):  lambda x: x * 1000,
            ("M",  "MI"): lambda x: x / 1609.34,
            ("MI", "M"):  lambda x: x * 1609.34,
            ("KM", "MI"): lambda x: x / 1.60934,
            ("MI", "KM"): lambda x: x * 1.60934,
        }
        fn = conversiones_long.get((origen, destino))
        if fn:
            print(f"  📏 {v} {origen}  =  {fn(v):.4f} {destino}\n")
        else:
            print(f"  ❌ Conversión {origen} → {destino} no soportada.\n")


# ─────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────

def main():
    parser = construir_parser()
    args = parser.parse_args()

    if not args.comando:
        # Si no se dio ningún comando, mostramos la ayuda
        print()
        parser.print_help()
        print()
        print("─" * 55)
        print("  💡 Este script se está ejecutando sin argumentos.")
        print("     En la terminal usarías: python script.py <comando> [opciones]")
        print("─" * 55)

        # Demo automática para cuando lo ejecutas sin argumentos
        print()
        print("  DEMO AUTOMÁTICA:")
        print()

        class DemoArgs:
            pass

        demo_saludar = DemoArgs()
        demo_saludar.nombre = "Estudiante"
        demo_saludar.idioma = "es"
        demo_saludar.formal = False
        cmd_saludar(demo_saludar)

        demo_calc = DemoArgs()
        demo_calc.op = "suma"
        demo_calc.a = 42.5
        demo_calc.b = 17.3
        cmd_calcular(demo_calc)

        demo_conv = DemoArgs()
        demo_conv.tipo = "temp"
        demo_conv.cantidad = 100
        demo_conv.de = "C"
        demo_conv.a = "F"
        cmd_convertir(demo_conv)

        return

    # Despachar al subcomando correcto
    comandos = {
        "saludar":   cmd_saludar,
        "calcular":  cmd_calcular,
        "info":      cmd_info,
        "convertir": cmd_convertir,
    }

    fn = comandos.get(args.comando)
    if fn:
        fn(args)


if __name__ == "__main__":
    main()

# =============================================================================
# ¿Qué has aprendido?
# - sys.argv           → lista cruda de argumentos (básico)
# - argparse           → módulo estándar para CLIs profesionales
# - add_subparsers()   → subcomandos (como git commit, git push)
# - add_argument()     → define argumentos con tipo, default y help
# - choices=[]         → valida que el valor sea uno de los permitidos
# - action="store_true" → argumento booleano (flag, como --verbose)
# - parser.parse_args() → parsea sys.argv y devuelve un objeto con los valores
#
# Para usar en terminal:
#   python 04_argumentos_cli.py saludar --nombre Ana --idioma en
#   python 04_argumentos_cli.py calcular --op div --a 100 --b 7
#   python 04_argumentos_cli.py info --archivo estudiantes.csv
#   python 04_argumentos_cli.py convertir --tipo temp --cantidad 37 --de C --a F
# =============================================================================
