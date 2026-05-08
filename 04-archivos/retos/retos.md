# 🏆 Retos — Nivel 4: Archivos

> En este nivel los retos son más "reales": los scripts crean archivos en disco que puedes abrir con tu editor o con Excel. ¡Comprueba que los datos se guardan correctamente!

---

## 🥉 Reto 1 — Contador de palabras de un archivo

**Dificultad:** ⭐ Fácil

Crea un script que lea el archivo `datos/info_python.txt` y muestre:
- Total de líneas
- Total de palabras
- Total de caracteres (con y sin espacios)
- La palabra más repetida
- Las 5 palabras más largas

**Bonus:** Que el usuario pueda elegir cualquier archivo `.txt` escribiendo su nombre.

<details>
<summary>💡 Pista</summary>

Para contar palabras únicas y su frecuencia, usa un diccionario:
```python
frecuencias = {}
for palabra in palabras:
    p = palabra.lower().strip(".,;:!?")
    frecuencias[p] = frecuencias.get(p, 0) + 1
mas_repetida = max(frecuencias, key=frecuencias.get)
```

</details>

---

## 🥉 Reto 2 — Generador de informe de notas

**Dificultad:** ⭐ Fácil

Lee el archivo `datos/estudiantes.csv` y genera **dos archivos de salida**:

1. `informe.txt` → un informe en texto plano bien formateado con todas las estadísticas
2. `aprobados.csv` → solo los estudiantes que aprobaron (nota >= 5)

**El informe.txt debe incluir:**
- Fecha de generación
- Total de estudiantes
- Media, nota máxima y mínima
- Listado completo con calificación en letra

<details>
<summary>💡 Pista</summary>

Para la fecha de generación:
```python
from datetime import datetime
fecha = datetime.now().strftime("%d/%m/%Y a las %H:%M")
```

</details>

---

## 🥈 Reto 3 — Gestor de tareas persistente

**Dificultad:** ⭐⭐ Medio

Toma el gestor de tareas del Nivel 3 (Reto 3) y añádele **persistencia**:
- Las tareas se guardan en un archivo `tareas.json`
- Al iniciar el programa, carga las tareas guardadas
- Al cerrar, guarda el estado actual
- Cada tarea tiene: `id`, `titulo`, `completada`, `fecha_creacion`, `prioridad` (alta/media/baja)

**Funcionalidades del menú:**
1. Ver tareas (filtrar por: todas / pendientes / completadas / alta prioridad)
2. Añadir tarea
3. Completar tarea
4. Eliminar tarea
5. Salir (guarda automáticamente)

<details>
<summary>💡 Pista</summary>

Estructura JSON sugerida:
```json
{
    "tareas": [
        {
            "id": 1,
            "titulo": "Estudiar Python",
            "completada": false,
            "prioridad": "alta",
            "fecha_creacion": "2025-01-15"
        }
    ],
    "ultimo_id": 1
}
```

Usa `"ultimo_id"` para no reutilizar IDs de tareas eliminadas.

</details>

---

## 🥈 Reto 4 — Procesador de log de errores

**Dificultad:** ⭐⭐ Medio

Crea un script que genere un archivo de log simulado y luego lo analice.

**Paso 1 — Generar el log:**
Crea `errores.log` con 50 líneas de eventos simulados con este formato:
```
[2025-01-15 14:32:01] INFO  Usuario 'Ana' ha iniciado sesión
[2025-01-15 14:32:15] ERROR Archivo 'config.json' no encontrado
[2025-01-15 14:33:02] WARN  Contraseña expirará en 3 días
[2025-01-15 14:33:45] INFO  Operación completada
```

Usa `random.choice()` para elegir entre INFO, WARN y ERROR, y genera mensajes variados.

**Paso 2 — Analizar el log:**
Lee el archivo y muestra:
- Total de líneas por nivel (INFO / WARN / ERROR)
- Lista de todos los mensajes de ERROR
- La hora con más actividad

---

## 🥇 Reto 5 — Organizador de archivos

**Dificultad:** ⭐⭐⭐ Difícil

Crea un script que analice una carpeta (la que el usuario indique) y genere un **informe JSON** con:

```json
{
    "carpeta": "/ruta/analizada",
    "fecha_analisis": "2025-01-15",
    "resumen": {
        "total_archivos": 23,
        "total_carpetas": 5,
        "tamanio_total_kb": 1248.5
    },
    "por_extension": {
        ".py":  {"cantidad": 8,  "tamanio_kb": 45.2},
        ".txt": {"cantidad": 3,  "tamanio_kb": 12.1},
        ".pdf": {"cantidad": 12, "tamanio_kb": 1191.2}
    },
    "archivos_grandes": [
        {"nombre": "documento.pdf", "tamanio_kb": 892.4}
    ]
}
```

**Bonus:** Que el script mueva todos los archivos a subcarpetas organizadas por extensión (`/documentos`, `/imagenes`, `/scripts`, etc.) pidiendo confirmación antes.

<details>
<summary>💡 Pista</summary>

Para recorrer todos los archivos de una carpeta:
```python
import os

for archivo in os.listdir(carpeta):
    ruta_completa = os.path.join(carpeta, archivo)
    if os.path.isfile(ruta_completa):
        extension = os.path.splitext(archivo)[1].lower()
        tamanio   = os.path.getsize(ruta_completa)
```

Para mover archivos: `import shutil` → `shutil.move(origen, destino)`

</details>

---

## 🌟 Reto Bonus — Exportador de contactos

**Dificultad:** ⭐⭐ Medio | Sin pistas 😈

Crea una agenda de contactos que:
- Guarda los datos en `contactos.json`
- Permite añadir, buscar, editar y eliminar contactos
- Puede **exportar** la agenda completa a `contactos.csv` (para importar en Excel o Gmail)
- Puede **importar** contactos desde un CSV externo, evitando duplicados por email

Cada contacto tiene: nombre, apellido, email, teléfono, grupo (amigos/trabajo/familia).

---

*← [Volver al Nivel 4](../README.md) | [Ir al Nivel 5 →](../../05-automatizacion/)*
