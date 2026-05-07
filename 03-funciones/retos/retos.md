# 🏆 Retos — Nivel 3: Funciones

> Regla de oro de este nivel: **cada función debe hacer una sola cosa**. Si te cuesta ponerle nombre, probablemente hace demasiado.

---

## 🥉 Reto 1 — Mini calculadora con funciones

**Dificultad:** ⭐ Fácil

Vuelve a la calculadora del Nivel 1 y reescríbela usando funciones. Crea una función para cada operación y una función `mostrar_menu()` que muestre las opciones.

**Estructura esperada:**
```python
def sumar(a, b): ...
def restar(a, b): ...
def multiplicar(a, b): ...
def dividir(a, b): ...        # maneja división por cero
def mostrar_menu(): ...
def pedir_numero(mensaje): ...  # con validación
def main(): ...               # orquesta todo

if __name__ == "__main__":
    main()
```

**Requisito:** La función `dividir()` debe devolver `None` si el divisor es 0, y el código que la llama debe gestionar ese caso.

---

## 🥉 Reto 2 — Conversor de unidades

**Dificultad:** ⭐ Fácil

Crea una librería de funciones para convertir entre unidades:

```
Temperatura:  celsius_a_fahrenheit(c), fahrenheit_a_celsius(f), celsius_a_kelvin(c)
Longitud:     metros_a_km(m), km_a_metros(km), metros_a_millas(m)
Peso:         kg_a_libras(kg), libras_a_kg(lb)
```

Luego crea un menú interactivo que permita elegir la conversión y el valor.

<details>
<summary>💡 Pista</summary>

Todas las funciones siguen el mismo patrón: reciben un número, hacen la conversión y devuelven el resultado. Son funciones puras y simples, perfectas para practicar.

</details>

---

## 🥈 Reto 3 — Gestor de lista de tareas

**Dificultad:** ⭐⭐ Medio

Crea un gestor de tareas en memoria usando funciones. La lista de tareas es una lista de diccionarios:

```python
tareas = [
    {"id": 1, "titulo": "Estudiar Python", "completada": False},
    {"id": 2, "titulo": "Hacer ejercicio", "completada": True},
]
```

Implementa estas funciones:
- `agregar_tarea(tareas, titulo)` → añade una tarea nueva
- `completar_tarea(tareas, id_tarea)` → marca una tarea como completada
- `eliminar_tarea(tareas, id_tarea)` → elimina una tarea
- `listar_tareas(tareas)` → muestra todas las tareas
- `contar_pendientes(tareas)` → devuelve cuántas hay sin completar

Y un `main()` con un menú interactivo para usar todas las funciones.

<details>
<summary>💡 Pista</summary>

Para buscar una tarea por ID:
```python
def buscar_tarea(tareas, id_tarea):
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            return tarea
    return None   # Si no la encuentra
```

</details>

---

## 🥈 Reto 4 — Analizador de texto avanzado

**Dificultad:** ⭐⭐ Medio

El usuario introduce un párrafo de texto y el programa lo analiza con varias funciones:

| Función | Qué devuelve |
|---------|-------------|
| `contar_palabras(texto)` | número de palabras |
| `contar_oraciones(texto)` | número de oraciones (terminan en `.`, `!` o `?`) |
| `palabra_mas_larga(texto)` | la palabra más larga |
| `palabras_frecuentes(texto, n)` | las `n` palabras más repetidas |
| `es_texto_largo(texto)` | True si tiene más de 100 palabras |
| `leer_nivel(texto)` | "Básico" / "Medio" / "Avanzado" según longitud media de palabras |

Muestra un informe completo con todas las estadísticas.

<details>
<summary>💡 Pista para palabras frecuentes</summary>

```python
def palabras_frecuentes(texto, n=5):
    palabras = texto.lower().split()
    conteo = {}
    for p in palabras:
        p_limpia = p.strip(".,!?;:")   # quita puntuación pegada
        conteo[p_limpia] = conteo.get(p_limpia, 0) + 1
    # Ordenar por frecuencia (de mayor a menor)
    ordenado = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
    return ordenado[:n]
```

</details>

---

## 🥇 Reto 5 — Juego del ahorcado

**Dificultad:** ⭐⭐⭐ Difícil

Implementa el clásico juego del ahorcado **con funciones bien separadas**. Este reto es especialmente para practicar la organización del código.

**Funciones sugeridas:**
```python
def elegir_palabra(lista_palabras): ...     # elige aleatoriamente
def inicializar_tablero(palabra): ...       # crea lista de '_' del tamaño de la palabra
def mostrar_tablero(tablero, intentos_malos, letras_usadas): ...
def letra_valida(letra, letras_usadas): ... # comprueba que no se haya usado ya
def actualizar_tablero(tablero, palabra, letra): ... # revela las letras acertadas
def ha_ganado(tablero): ...                 # True si no quedan '_'
def dibujar_ahorcado(intentos_malos): ...   # dibuja el muñeco en ASCII
def main(): ...
```

**Lista de palabras de ejemplo:**
```python
PALABRAS = ["python", "programacion", "funcion", "variable",
            "bucle", "condicional", "parametro", "argumento"]
```

---

## 🌟 Reto Bonus — Generador de contraseñas seguras

**Dificultad:** ⭐⭐ Medio | Sin pistas 😈

Crea un generador de contraseñas con estas funciones:

- `generar_contrasena(longitud, mayusculas, numeros, simbolos)` → genera una contraseña aleatoria
- `evaluar_seguridad(contrasena)` → devuelve "Débil" / "Media" / "Fuerte" / "Muy fuerte"
- `main()` → pide las opciones al usuario y muestra varias contraseñas generadas

Usa el módulo `random` y `string` (consulta `string.ascii_letters`, `string.digits`, `string.punctuation`).

---

*← [Volver al Nivel 3](../README.md) | [Ir al Nivel 4 →](../../04-archivos/)*
