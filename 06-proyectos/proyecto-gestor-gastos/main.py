# main.py — Punto de entrada del Gestor de Gastos
import datos
import logica
import interfaz
from datetime import datetime


def accion_anadir(gastos):
    campos = interfaz.pedir_gasto()
    if not campos:
        interfaz.error("Gasto cancelado.")
        return gastos
    nuevo = logica.crear_gasto(gastos, **campos)
    datos.guardar_gastos(gastos)
    interfaz.ok(f"Gasto de {nuevo['cantidad']:.2f}€ añadido: {nuevo['descripcion']}")
    return gastos


def accion_ver_todos(gastos):
    interfaz.mostrar_lista(gastos, "TODOS LOS GASTOS")


def accion_ver_mes(gastos):
    hoy = datetime.now()
    mes = logica.filtrar_por_mes(gastos, hoy.year, hoy.month)
    meses_str = ["","Enero","Febrero","Marzo","Abril","Mayo","Junio",
                 "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    titulo = f"GASTOS DE {meses_str[hoy.month].upper()} {hoy.year}"
    interfaz.mostrar_lista(mes, titulo)


def accion_estadisticas(gastos):
    stats = logica.estadisticas_generales(gastos)
    interfaz.pantalla_estadisticas(stats)


def accion_presupuesto(gastos):
    while True:
        try:
            presupuesto = float(input("\n  Presupuesto mensual (€): ").replace(",", "."))
            if presupuesto > 0:
                break
            print("  ⚠️  Debe ser positivo.")
        except ValueError:
            print("  ⚠️  Número inválido.")
    restante, gastado = logica.presupuesto_restante(gastos, presupuesto)
    interfaz.pantalla_presupuesto(presupuesto, restante, gastado)


def accion_eliminar(gastos):
    interfaz.mostrar_lista(gastos)
    try:
        id_eliminar = int(input("  ID del gasto a eliminar: "))
    except ValueError:
        interfaz.error("ID inválido.")
        return gastos

    gasto = next((g for g in gastos if g["id"] == id_eliminar), None)
    if not gasto:
        interfaz.error(f"No existe el gasto #{id_eliminar}.")
        return gastos

    print(f"\n  Gasto seleccionado: {gasto['descripcion']} — {gasto['cantidad']:.2f}€")
    if interfaz.confirmar("¿Eliminar este gasto?"):
        logica.eliminar_gasto(gastos, id_eliminar)
        datos.guardar_gastos(gastos)
        interfaz.ok("Gasto eliminado.")
    return gastos


def main():
    interfaz.pantalla_bienvenida()
    gastos = datos.cargar_gastos()

    # Datos de demo si está vacío
    if not gastos:
        print("  💡 Primera vez: cargando datos de ejemplo para que puedas explorar...\n")
        demos = [
            ("Supermercado Mercadona", 87.50, "🍔 Alimentación", "2025-01-05"),
            ("Alquiler enero",        650.00, "🏠 Vivienda",      "2025-01-01"),
            ("Gasolina",               48.30, "🚗 Transporte",    "2025-01-08"),
            ("Netflix",                18.99, "🎮 Ocio",          "2025-01-10"),
            ("Farmacia",               12.40, "💊 Salud",         "2025-01-11"),
            ("Restaurante cumpleaños", 35.00, "🍔 Alimentación",  "2025-01-14"),
            ("Alquiler febrero",      650.00, "🏠 Vivienda",      "2025-02-01"),
            ("Ropa invierno",          95.00, "👕 Ropa",          "2025-02-03"),
            ("Supermercado",           72.10, "🍔 Alimentación",  "2025-02-09"),
            ("Spotify",                 9.99, "🎮 Ocio",          "2025-02-10"),
        ]
        for desc, cant, cat, fecha in demos:
            logica.crear_gasto(gastos, desc, cant, cat, fecha)
        datos.guardar_gastos(gastos)
        print(f"  ✅ {len(demos)} gastos de ejemplo cargados.\n")

    acciones = {
        "1": accion_anadir,
        "2": accion_ver_todos,
        "3": accion_ver_mes,
        "4": accion_estadisticas,
        "5": accion_presupuesto,
        "6": accion_eliminar,
    }

    while True:
        interfaz.pantalla_menu()
        opcion = input("  Opción: ").strip()

        if opcion == "0":
            print("\n  👋 ¡Hasta pronto! Tus gastos están guardados.\n")
            break

        accion = acciones.get(opcion)
        if accion:
            resultado = accion(gastos)
            if resultado is not None:
                gastos = resultado
        else:
            interfaz.error("Opción no válida.")

        interfaz.pausa()


if __name__ == "__main__":
    main()
