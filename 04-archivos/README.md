# 📘 Nivel 4 — Archivos: Leer, escribir y persistir datos

> **Objetivo:** Hacer que tus scripts recuerden información entre ejecuciones. Un programa que no guarda datos olvida todo al cerrarse.

---

## 🧠 ¿Qué aprenderás en este nivel?

Al terminar este nivel serás capaz de:

- Leer y escribir archivos de texto `.txt`
- Manejar errores de archivo con `try/except`
- Leer y escribir archivos CSV (datos tabulares)
- Leer y escribir archivos JSON (datos estructurados)
- Guardar y recuperar el estado de un programa entre ejecuciones

---

## 📖 Conceptos explicados

### 1. Abrir un archivo: open()

```python
# Modos de apertura:
# 'r'  → leer (read)        — el archivo debe existir
# 'w'  → escribir (write)   — crea el archivo o lo sobreescribe
# 'a'  → añadir (append)    — añade al final sin borrar lo anterior
# 'r+' → leer y escribir

archivo = open("datos.txt", "r", encoding="utf-8")
contenido = archivo.read()
archivo.close()              # ¡Siempre cierra el archivo!
```

---

### 2. La forma correcta: with open()

`with` cierra el archivo automáticamente, aunque haya errores:

```python
# ✅ Forma recomendada — siempre usa with
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
# El archivo se cierra solo al salir del bloque with
```

---

### 3. Leer un archivo

```python
with open("notas.txt", "r", encoding="utf-8") as f:
    todo = f.read()              # Lee TODO el archivo como un string
    
with open("notas.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()       # Lee como lista de líneas (con '\n' al final)

with open("notas.txt", "r", encoding="utf-8") as f:
    for linea in f:              # Línea por línea (eficiente en archivos grandes)
        print(linea.strip())     # .strip() quita el '\n' del final
```

---

### 4. Escribir en un archivo

```python
# 'w' crea el archivo si no existe, o lo sobreescribe si ya existe
with open("resultado.txt", "w", encoding="utf-8") as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")

# 'a' añade al final sin borrar lo que había
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Nueva entrada de log\n")
```

---

### 5. Manejo de errores con try/except

```python
try:
    with open("archivo_que_no_existe.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("Sin permisos para leer el archivo")
except Exception as e:
    print(f"Error inesperado: {e}")
```

---

### 6. CSV: datos en tabla

```python
import csv

# Leer CSV
with open("datos.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)        # Lee cada fila como diccionario
    for fila in lector:
        print(fila["nombre"], fila["edad"])

# Escribir CSV
datos = [{"nombre": "Ana", "edad": 21}, {"nombre": "Luis", "edad": 23}]
with open("salida.csv", "w", newline="", encoding="utf-8") as f:
    campos = ["nombre", "edad"]
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()            # Escribe la cabecera
    escritor.writerows(datos)         # Escribe todas las filas
```

---

### 7. JSON: datos estructurados

```python
import json

# Leer JSON
with open("config.json", "r", encoding="utf-8") as f:
    datos = json.load(f)              # Convierte JSON → diccionario Python

# Escribir JSON
config = {"version": "1.0", "max_intentos": 7}
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)
    # indent=4 → formateado con sangría legible
    # ensure_ascii=False → permite caracteres españoles
```

---

## 📂 Scripts de este nivel

| Archivo | Qué hace |
|---------|---------|
| [`01_leer_escribir_txt.py`](./scripts/01_leer_escribir_txt.py) | Operaciones básicas con archivos de texto |
| [`02_manejo_errores.py`](./scripts/02_manejo_errores.py) | try/except y errores comunes de archivos |
| [`03_csv_datos.py`](./scripts/03_csv_datos.py) | Leer y escribir archivos CSV |
| [`04_json_datos.py`](./scripts/04_json_datos.py) | Leer y escribir archivos JSON |
| [`05_diario_personal.py`](./scripts/05_diario_personal.py) | Proyecto: diario que persiste entre sesiones |

---

## 📁 Archivos de datos incluidos

En la carpeta `datos/` encontrarás archivos de ejemplo para practicar:
- `info_python.txt` → texto para practicar lectura
- `estudiantes.csv` → tabla de datos de ejemplo
- `puntuaciones.json` → JSON de ejemplo del juego

---

## ✅ Checklist antes de pasar al nivel 5

- [ ] ¿Sabes la diferencia entre `'r'`, `'w'` y `'a'`?
- [ ] ¿Usas siempre `with open()` en lugar de `open()` y `close()`?
- [ ] ¿Especificas siempre `encoding="utf-8"`?
- [ ] ¿Manejas los errores con `try/except`?
- [ ] ¿Has completado al menos 3 retos?

---

*← [Volver al índice principal](../README.md)*
