# logica.py — Cálculos, filtros y estadísticas de gastos
from datetime import datetime, timedelta


def siguiente_id(gastos):
    return max((g["id"] for g in gastos), default=0) + 1


def crear_gasto(gastos, descripcion, cantidad, categoria, fecha=None):
    """Crea un nuevo gasto y lo añade a la lista."""
    gasto = {
        "id":          siguiente_id(gastos),
        "descripcion": descripcion.strip(),
        "cantidad":    round(float(cantidad), 2),
        "categoria":   categoria,
        "fecha":       fecha or datetime.now().strftime("%Y-%m-%d"),
    }
    gastos.append(gasto)
    return gasto


def eliminar_gasto(gastos, id_gasto):
    original = len(gastos)
    gastos[:] = [g for g in gastos if g["id"] != id_gasto]
    return len(gastos) < original


def filtrar_por_mes(gastos, año, mes):
    prefijo = f"{año}-{mes:02d}"
    return [g for g in gastos if g["fecha"].startswith(prefijo)]


def filtrar_por_categoria(gastos, categoria):
    return [g for g in gastos if g["categoria"] == categoria]


def filtrar_por_rango(gastos, fecha_inicio, fecha_fin):
    return [g for g in gastos if fecha_inicio <= g["fecha"] <= fecha_fin]


def estadisticas_generales(gastos):
    if not gastos:
        return {}

    total     = sum(g["cantidad"] for g in gastos)
    por_cat   = {}
    por_mes   = {}

    for g in gastos:
        cat = g["categoria"]
        por_cat[cat] = por_cat.get(cat, 0) + g["cantidad"]

        mes = g["fecha"][:7]   # "YYYY-MM"
        por_mes[mes] = por_mes.get(mes, 0) + g["cantidad"]

    cat_max  = max(por_cat, key=por_cat.get)
    mes_max  = max(por_mes, key=por_mes.get)
    media    = total / len(por_mes) if por_mes else 0

    return {
        "total":        round(total, 2),
        "num_gastos":   len(gastos),
        "media_mensual": round(media, 2),
        "por_categoria": {k: round(v, 2) for k, v in sorted(por_cat.items(), key=lambda x: -x[1])},
        "por_mes":       {k: round(v, 2) for k, v in sorted(por_mes.items())},
        "categoria_top": cat_max,
        "mes_top":       mes_max,
        "gasto_mayor":   max(gastos, key=lambda g: g["cantidad"]),
        "gasto_menor":   min(gastos, key=lambda g: g["cantidad"]),
    }


def presupuesto_restante(gastos, presupuesto_mensual):
    """Calcula cuánto queda del presupuesto en el mes actual."""
    hoy     = datetime.now()
    mes_actual = filtrar_por_mes(gastos, hoy.year, hoy.month)
    gastado    = sum(g["cantidad"] for g in mes_actual)
    return round(presupuesto_mensual - gastado, 2), round(gastado, 2)
