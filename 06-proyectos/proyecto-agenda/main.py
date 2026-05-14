# main.py — Punto de entrada de la Agenda de Contactos
# Solo orquesta: llama a funciones de otros módulos. No hace lógica aquí.
#
# Estructura del proyecto:
#   config.py   → constantes y rutas
#   datos.py    → leer/escribir JSON y CSV
#   logica.py   → CRUD, búsqueda, validación
#   interfaz.py → todo lo visual (print/input)
#   main.py     → orquestación (este archivo)

import datos
import logica
import interfaz
from config import RUTA_CSV


def accion_nuevo(contactos):
    interfaz.info("Escribe 'cancelar' en el nombre para volver.")
    campos = interfaz.pedir_contacto()
    if not campos:
        interfaz.error("Contacto no creado.")
        return contactos

    nuevo = logica.crear_contacto(contactos, **campos)
    datos.guardar_contactos(contactos)
    interfaz.ok(f"Contacto #{nuevo['id']} '{nuevo['nombre']} {nuevo['apellido']}' añadido.")
    return contactos


def accion_ver_todos(contactos):
    interfaz.mostrar_lista(contactos, "TODOS LOS CONTACTOS")

    if contactos:
        id_ver = interfaz.pedir_id("  Ver detalle (ID) o Enter para volver: ")
        if id_ver:
            c = logica.obtener_por_id(contactos, id_ver)
            if c:
                interfaz.mostrar_contacto_detalle(c)
            else:
                interfaz.error(f"No existe el contacto #{id_ver}.")


def accion_buscar(contactos):
    termino = input("\n  🔍 Buscar: ").strip()
    if not termino:
        return

    resultados = logica.buscar_contactos(contactos, termino)
    if resultados:
        interfaz.mostrar_lista(resultados, f"RESULTADOS PARA '{termino}'")
    else:
        interfaz.error(f"No se encontraron contactos con '{termino}'.")


def accion_editar(contactos):
    interfaz.mostrar_lista(contactos)
    id_editar = interfaz.pedir_id("  ID del contacto a editar: ")
    if not id_editar:
        interfaz.error("ID no válido.")
        return contactos

    contacto = logica.obtener_por_id(contactos, id_editar)
    if not contacto:
        interfaz.error(f"No existe el contacto #{id_editar}.")
        return contactos

    interfaz.mostrar_contacto_detalle(contacto)
    print("\n  Edita los campos (Enter para mantener el valor actual):")
    cambios = interfaz.pedir_contacto(contacto_existente=contacto)

    if cambios and interfaz.confirmar("¿Guardar cambios?"):
        logica.actualizar_contacto(contactos, id_editar, cambios)
        datos.guardar_contactos(contactos)
        interfaz.ok("Contacto actualizado correctamente.")
    else:
        interfaz.info("Edición cancelada.")

    return contactos


def accion_eliminar(contactos):
    interfaz.mostrar_lista(contactos)
    id_eliminar = interfaz.pedir_id("  ID del contacto a eliminar: ")
    if not id_eliminar:
        interfaz.error("ID no válido.")
        return contactos

    contacto = logica.obtener_por_id(contactos, id_eliminar)
    if not contacto:
        interfaz.error(f"No existe el contacto #{id_eliminar}.")
        return contactos

    interfaz.mostrar_contacto_detalle(contacto)
    if interfaz.confirmar(f"¿Eliminar a '{contacto['nombre']} {contacto['apellido']}'?"):
        logica.eliminar_contacto(contactos, id_eliminar)
        datos.guardar_contactos(contactos)
        interfaz.ok("Contacto eliminado.")
    else:
        interfaz.info("Eliminación cancelada.")

    return contactos


def accion_exportar(contactos):
    if datos.exportar_csv(contactos):
        interfaz.ok(f"Exportado a: {RUTA_CSV}")
        interfaz.info(f"{len(contactos)} contactos exportados. Puedes abrirlo con Excel.")
    else:
        interfaz.error("No hay contactos para exportar.")


def main():
    interfaz.pantalla_bienvenida()
    contactos = datos.cargar_contactos()

    acciones = {
        "1": accion_nuevo,
        "2": accion_ver_todos,
        "3": accion_buscar,
        "4": accion_editar,
        "5": accion_eliminar,
        "6": lambda c: interfaz.pantalla_estadisticas(c) or c,
        "7": accion_exportar,
    }

    while True:
        interfaz.pantalla_menu(len(contactos))
        opcion = input("  Opción: ").strip()

        if opcion == "0":
            print("\n  👋 ¡Hasta pronto! Tus contactos están guardados.\n")
            break

        accion = acciones.get(opcion)
        if accion:
            resultado = accion(contactos)
            if resultado is not None:
                contactos = resultado
        else:
            interfaz.error("Opción no válida.")

        interfaz.pausa()


if __name__ == "__main__":
    main()
