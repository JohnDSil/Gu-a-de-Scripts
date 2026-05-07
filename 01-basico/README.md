# 📘 Nivel 1 — Lo Básico: Tu primer contacto con Python

> **Objetivo:** Entender qué es un script, cómo funciona Python, y escribir tus primeros programas reales.

---

## 🧠 ¿Qué aprenderás en este nivel?

Al terminar este nivel serás capaz de:

- Ejecutar un script de Python desde la terminal
- Usar variables para guardar información
- Entender los tipos de datos básicos (texto, números, booleanos)
- Pedirle información al usuario
- Hacer operaciones matemáticas simples
- Mostrar resultados en pantalla

---

## 📖 Conceptos explicados

### 1. ¿Qué es un script?

Un **script** es simplemente un archivo de texto con instrucciones que el ordenador sigue en orden, de arriba a abajo, una por una.

Imagina que le dejas una nota a alguien con pasos a seguir:

```
1. Encender el ordenador
2. Abrir el navegador
3. Buscar el correo
```

Un script es exactamente eso, pero escrito en un lenguaje que el ordenador entiende: **Python**.

---

### 2. Variables

Una **variable** es como una caja con una etiqueta. Dentro guardas información, y puedes acceder a ella usando la etiqueta.

```python
nombre = "Ana"       # La caja se llama 'nombre' y contiene "Ana"
edad = 25            # La caja 'edad' contiene el número 25
```

**Reglas para nombrar variables:**
- Sin espacios: usa `_` en su lugar → `mi_nombre` ✅
- Empieza por letra, no por número → `1nombre` ❌
- Usa nombres descriptivos → `x` es malo, `temperatura` es bueno

---

### 3. Tipos de datos

Python distingue qué tipo de información guardas:

| Tipo | Nombre en Python | Ejemplo |
|------|-----------------|---------|
| Texto | `str` (string) | `"Hola mundo"` |
| Número entero | `int` | `42` |
| Número decimal | `float` | `3.14` |
| Verdadero/Falso | `bool` | `True` o `False` |

Puedes comprobar el tipo con `type()`:

```python
print(type("Hola"))   # <class 'str'>
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type(True))     # <class 'bool'>
```

---

### 4. Entrada y salida

**Salida** (mostrar algo en pantalla):
```python
print("Esto aparece en pantalla")
```

**Entrada** (pedirle algo al usuario):
```python
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)
```

⚠️ **Importante:** `input()` siempre devuelve texto (`str`). Si necesitas un número, debes convertirlo:

```python
edad = int(input("¿Cuántos años tienes? "))   # Convierte a entero
precio = float(input("¿Cuánto cuesta? "))      # Convierte a decimal
```

---

### 5. Operaciones matemáticas

| Operación | Símbolo | Ejemplo | Resultado |
|-----------|---------|---------|-----------|
| Suma | `+` | `5 + 3` | `8` |
| Resta | `-` | `10 - 4` | `6` |
| Multiplicación | `*` | `3 * 4` | `12` |
| División | `/` | `10 / 4` | `2.5` |
| División entera | `//` | `10 // 4` | `2` |
| Resto (módulo) | `%` | `10 % 3` | `1` |
| Potencia | `**` | `2 ** 8` | `256` |

---

### 6. F-strings: la forma moderna de formatear texto

Las **f-strings** son la forma más cómoda de mezclar texto con variables:

```python
nombre = "Carlos"
edad = 30
print(f"Hola, {nombre}. Tienes {edad} años.")
# Resultado: Hola, Carlos. Tienes 30 años.
```

Solo añade una `f` antes de las comillas y escribe las variables entre `{}`.

---

## 📂 Scripts de este nivel

| Archivo | Qué hace |
|---------|---------|
| [`01_hola_mundo.py`](./scripts/01_hola_mundo.py) | El clásico primer programa |
| [`02_variables.py`](./scripts/02_variables.py) | Cómo declarar y usar variables |
| [`03_tipos_datos.py`](./scripts/03_tipos_datos.py) | Explorar los tipos de datos |
| [`04_entrada_usuario.py`](./scripts/04_entrada_usuario.py) | Interactuar con el usuario |
| [`05_calculadora_simple.py`](./scripts/05_calculadora_simple.py) | Script útil: calculadora básica |

---

## ▶️ Cómo ejecutar los scripts

Abre una terminal en esta carpeta y escribe:

```bash
python scripts/01_hola_mundo.py
```

O si usas Python 3 explícitamente:

```bash
python3 scripts/01_hola_mundo.py
```

---

## 🏆 Retos del nivel 1

Cuando termines de leer los scripts, ve a la carpeta [`retos/`](./retos/retos.md) y completa los ejercicios.

No mires las soluciones antes de intentarlo. ¡El esfuerzo es parte del aprendizaje!

---

## ✅ Checklist antes de pasar al nivel 2

Antes de continuar, asegúrate de que puedes responder estas preguntas:

- [ ] ¿Qué diferencia hay entre `int` y `float`?
- [ ] ¿Por qué `input()` devuelve siempre un `str`?
- [ ] ¿Cómo se llama la función para mostrar algo en pantalla?
- [ ] ¿Qué hace el operador `%`?
- [ ] ¿Cómo funciona una f-string?

Si puedes responderlas todas, ¡estás listo para el Nivel 2! 🚀

---

*← [Volver al índice principal](../README.md)*
