# interfaz.py — Pantallas, gráficos ASCII y formularios del gestor de gastos
from datetime import datetime
from config import CATEGORIAS, MONEDA, VERSION


SEP = "─" * 54


def pantalla_bienvenida():
    print()
    print("╔════════════════════════════════════════════════════╗")
    print("║           💰  GESTOR DE GASTOS PERSONALES         ║")
    print(f"║                        v{VERSION:<26}║")
    print("╚════════════════════════════════════════════════════╝")
    print()


def pantalla_menu():
    print("═" * 54)
    opciones = [
        ("1", "➕  Añadir gasto"),
        ("2", "📋  Ver todos los gastos"),
        ("3", "📅  Ver gastos del mes actual"),
        ("4", "📊  Estadísticas y gráficos"),
        ("5", "🎯  Comprobar presupuesto mensual"),
        ("6", "🗑️   Eliminar gasto"),
        ("0", "🚪  Salir"),
    ]
    for k, v in opciones:
        print(f"    {k}.  {v}")
    print(SEP)


def mostrar_gasto_linea(g):
    fecha = g["fecha"]
    cat   = g["categoria"].split(" ", 1)[-1]   # Sin emoji
    desc  = g["descripcion"][:28]
    print(f"  #{g['id']:<4} {fecha}  {cat:<14} {desc:<28} {g['cantidad']:>8.2f}{MONEDA}")


def mostrar_lista(gastos, titulo="GASTOS"):
    if not gastos:
        print(f"\n  📭 No hay gastos registrados.\n")
        return
    total = sum(g["cantidad"] for g in gastos)
    print(f"\n  {titulo} ({len(gastos)} registros)")
    print(f"  {SEP}")
    print(f"  {'ID':<6} {'FECHA':<12} {'CATEGORÍA':<14} {'DESCRIPCIÓN':<28} {'IMPORTE':>9}")
    print(f"  {SEP}")
    for g in sorted(gastos, key=lambda x: x["fecha"], reverse=True):
        mostrar_gasto_linea(g)
    print(f"  {SEP}")
    print(f"  {'TOTAL':>62} {total:>8.2f}{MONEDA}")
    print()


def grafico_barras(datos_dict, titulo, max_ancho=30):
    """
    Dibuja un gráfico de barras horizontal en ASCII.

    Args:
        datos_dict: {etiqueta: valor_numerico}
        max_ancho: ancho máximo de la barra más larga
    """
    print(f"\n  {titulo}")
    print(f"  {SEP}")

    if not datos_dict:
        print("  (Sin datos)")
        return

    maximo = max(datos_dict.values()) if datos_dict else 1

    for etiqueta, valor in datos_dict.items():
        longitud_barra = int((valor / maximo) * max_ancho)
        barra = "█" * longitud_barra + "░" * (max_ancho - longitud_barra)
        # Etiqueta corta para que quepa
        etiq_corta = etiqueta.split(" ", 1)[-1][:15] if " " in etiqueta else etiqueta[:15]
        print(f"  {etiq_corta:<16} {barra}  {valor:>8.2f}{MONEDA}")
    print()


def grafico_evolucion_mensual(por_mes):
    """Gráfico de evolución del gasto mes a mes."""
    if not por_mes:
        return
    print(f"\n  EVOLUCIÓN MENSUAL")
    print(f"  {SEP}")
    maximo = max(por_mes.values())
    for mes, total in por_mes.items():
        año, m = mes.split("-")
        meses_str = ["","Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
        etiq = f"{meses_str[int(m)]} {año}"
        barras = int((total / maximo) * 25)
        barra  = "▓" * barras
        print(f"  {etiq:<10} {barra:<25}  {total:.2f}{MONEDA}")
    print()


def pantalla_estadisticas(stats):
    if not stats:
        print("\n  📭 Sin datos para mostrar.\n")
        return

    print(f"\n  📊 ESTADÍSTICAS GENERALES")
    print(f"  {SEP}")
    print(f"  Total gastado:       {stats['total']:>10.2f}{MONEDA}")
    print(f"  Número de gastos:    {stats['num_gastos']:>10}")
    print(f"  Media mensual:       {stats['media_mensual']:>10.2f}{MONEDA}")
    print(f"  Categoría top:       {stats['categoria_top']}")
    print(f"  Mes con más gasto:   {stats['mes_top']}")
    mayor = stats["gasto_mayor"]
    print(f"  Gasto más alto:      {mayor['cantidad']:.2f}{MONEDA} — {mayor['descripcion']}")

    grafico_barras(stats["por_categoria"], "GASTO POR CATEGORÍA")
    grafico_evolucion_mensual(stats["por_mes"])


def pantalla_presupuesto(presupuesto, restante, gastado):
    pct_usado  = min(int((gastado / presupuesto) * 100), 100) if presupuesto else 0
    barras_ok  = int(pct_usado / 5)
    barra      = "█" * barras_ok + "░" * (20 - barras_ok)
    estado     = "🟢 Bien" if pct_usado < 70 else ("🟡 Cuidado" if pct_usado < 90 else "🔴 Excedido")

    print(f"\n  🎯 PRESUPUESTO MES ACTUAL")
    print(f"  {SEP}")
    print(f"  Presupuesto:  {presupuesto:.2f}{MONEDA}")
    print(f"  Gastado:      {gastado:.2f}{MONEDA}  ({pct_usado}%)")
    print(f"  Restante:     {restante:.2f}{MONEDA}")
    print(f"\n  [{barra}] {pct_usado}%  {estado}")
    print()


def seleccionar_categoria():
    """Muestra las categorías y devuelve la elegida."""
    print("\n  Categorías:")
    for i, cat in enumerate(CATEGORIAS, 1):
        print(f"    {i:>2}. {cat}")
    while True:
        try:
            opcion = int(input("  Elige categoría (número): "))
            if 1 <= opcion <= len(CATEGORIAS):
                return CATEGORIAS[opcion - 1]
            print("  ⚠️  Número fuera de rango.")
        except ValueError:
            print("  ⚠️  Introduce un número.")


def pedir_gasto():
    """Formulario para añadir un gasto. Devuelve dict o None si cancela."""
    print()
    desc = input("  Descripción: ").strip()
    if not desc:
        return None

    while True:
        try:
            cantidad = float(input("  Cantidad (€): ").replace(",", "."))
            if cantidad <= 0:
                print("  ⚠️  La cantidad debe ser positiva.")
                continue
            break
        except ValueError:
            print("  ⚠️  Introduce un número válido.")

    categoria = seleccionar_categoria()

    fecha_str = input(f"  Fecha (YYYY-MM-DD) [hoy]: ").strip()
    if not fecha_str:
        fecha_str = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            print("  ⚠️  Fecha inválida, se usará la fecha de hoy.")
            fecha_str = datetime.now().strftime("%Y-%m-%d")

    return {"descripcion": desc, "cantidad": cantidad,
            "categoria": categoria, "fecha": fecha_str}


def ok(msg):    print(f"\n  ✅ {msg}\n")
def error(msg): print(f"\n  ❌ {msg}\n")
def pausa():    input("  [Pulsa Enter para continuar]")
def confirmar(msg): return input(f"  {msg} (si/no): ").strip().lower() in ["si","sí","s"]
