# 📘 Nivel 5 — Automatización: Python trabaja por ti
 
> **Objetivo:** Hacer que Python haga tareas repetitivas en tu lugar. Si lo haces más de dos veces a mano, escribe un script.
 
---
 
## 🧠 ¿Qué aprenderás en este nivel?
 
Al terminar este nivel serás capaz de:
 
- Organizar y mover archivos automáticamente con `os` y `shutil`
- Trabajar con fechas y horas con `datetime`
- Ejecutar comandos del sistema con `subprocess`
- Hacer peticiones a APIs reales con `requests`
- Construir scripts que se usan desde la terminal con argumentos
- Generar informes automáticos combinando todo lo anterior
---
 
## 📖 Conceptos explicados
 
### 1. shutil: mover, copiar y eliminar archivos
 
```python
import shutil, os
 
shutil.move("origen.txt", "destino/origen.txt")   # Mover
shutil.copy("archivo.txt", "copia.txt")            # Copiar
shutil.rmtree("carpeta_entera/")                   # Eliminar carpeta
 
# Recorrer carpetas recursivamente
for raiz, carpetas, archivos in os.walk("/mi/carpeta"):
    for archivo in archivos:
        ruta_completa = os.path.join(raiz, archivo)
```
 
---
 
### 2. datetime: fechas y horas
 
```python
from datetime import datetime, timedelta
 
ahora     = datetime.now()
hoy       = ahora.strftime("%d/%m/%Y")       # "15/01/2025"
manana    = ahora + timedelta(days=1)
hace_7d   = ahora - timedelta(days=7)
 
# Comparar y calcular diferencias
diferencia = ahora - hace_7d   # timedelta
print(diferencia.days)          # 7
```
 
---
 
### 3. requests: peticiones a internet
 
```python
import requests
 
respuesta = requests.get("https://api.ejemplo.com/datos")
 
if respuesta.status_code == 200:       # 200 = OK
    datos = respuesta.json()           # Si la API devuelve JSON
else:
    print(f"Error: {respuesta.status_code}")
```
 
---
 
### 4. sys.argv: argumentos de línea de comandos
 
```python
import sys
 
# Ejecutando: python script.py Ana 25
# sys.argv = ['script.py', 'Ana', '25']
 
nombre = sys.argv[1]    # 'Ana'
edad   = int(sys.argv[2])  # 25
```
 
---
 
### 5. subprocess: ejecutar comandos del sistema
 
```python
import subprocess
 
resultado = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)
print(resultado.stdout)   # 'Python 3.11.0'
```
 
---
 
## 📂 Scripts de este nivel
 
| Archivo | Qué hace |
|---------|---------|
| [`01_organizar_archivos.py`](./scripts/01_organizar_archivos.py) | Ordena una carpeta por tipo de archivo automáticamente |
| [`02_fechas_y_backups.py`](./scripts/02_fechas_y_backups.py) | Backups con fecha, limpieza automática de antiguos |
| [`03_peticiones_web.py`](./scripts/03_peticiones_web.py) | Consulta APIs públicas reales: clima, divisas, chistes |
| [`04_argumentos_cli.py`](./scripts/04_argumentos_cli.py) | Scripts que se usan como comandos de terminal |
| [`05_informe_automatico.py`](./scripts/05_informe_automatico.py) | Proyecto: genera informes completos desde CSV + JSON |
 
---
 
## ⚠️ Dependencia externa
 
```bash
pip install requests
```
 
---
 
## ✅ Checklist antes de pasar al nivel 6
 
- [ ] ¿Puedes mover archivos y recorrer carpetas con `os.walk()`?
- [ ] ¿Sabes calcular fechas con `timedelta`?
- [ ] ¿Has consultado una API real con `requests`?
- [ ] ¿Entiendes `sys.argv` para recibir argumentos desde la terminal?
- [ ] ¿Has completado al menos 3 retos?
---
 
*← [Volver al índice principal](../README.md)*
