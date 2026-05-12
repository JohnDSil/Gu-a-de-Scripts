# 🏆 Retos — Nivel 5: Automatización
 
> En este nivel los retos producen resultados tangibles: archivos organizados, informes generados, datos reales de internet. ¡Comprueba que funcionan de verdad!
 
---
 
## 🥉 Reto 1 — Renombrador masivo de archivos
 
**Dificultad:** ⭐ Fácil
 
Crea un script que renombre todos los archivos de una carpeta siguiendo un patrón. El usuario elige:
 
- **Modo fecha:** añade la fecha de hoy al inicio → `20250115_foto.jpg`
- **Modo numerado:** numera todos los archivos → `001_foto.jpg`, `002_video.mp4`
- **Modo minúsculas:** convierte todos los nombres a minúsculas
El script debe mostrar una previsualización antes de renombrar y pedir confirmación.
 
<details>
<summary>💡 Pista</summary>
Para renombrar un archivo:
```python
import os
os.rename(nombre_actual, nombre_nuevo)
```
 
Para previsualizar sin hacer nada, guarda los pares `(origen, destino)` en una lista y muéstralos antes de preguntar.
 
</details>
---
 
## 🥉 Reto 2 — Monitor de carpeta
 
**Dificultad:** ⭐ Fácil
 
Crea un script que "fotografíe" el estado de una carpeta en dos momentos y muestre las diferencias:
 
```
📁 Analizando cambios en: /mi/carpeta
   Entre: 14:30:00 y 14:35:00
 
   ➕ Añadidos:   nuevo_archivo.txt
   ✏️  Modificados: documento.pdf  (antes 45 KB, ahora 67 KB)
   ❌ Eliminados:  borrador.docx
   ─────────────────────────────
   Sin cambios: 12 archivos
```
 
<details>
<summary>💡 Pista</summary>
Haz dos "instantáneas" del estado: un diccionario `{nombre: tamanio}`.
Compara los dos diccionarios para encontrar añadidos, eliminados y modificados.
 
```python
def instantanea(carpeta):
    return {
        archivo: os.path.getsize(os.path.join(carpeta, archivo))
        for archivo in os.listdir(carpeta)
        if os.path.isfile(os.path.join(carpeta, archivo))
    }
```
 
</details>
---
 
## 🥈 Reto 3 — Descargador de datos de API
 
**Dificultad:** ⭐⭐ Medio
 
Usa la API pública de [JSONPlaceholder](https://jsonplaceholder.typicode.com) (no necesita registro) para:
 
1. Descargar los 100 posts de `https://jsonplaceholder.typicode.com/posts`
2. Descargar los 10 usuarios de `https://jsonplaceholder.typicode.com/users`
3. Guardarlos en archivos JSON locales con timestamp en el nombre
4. Generar un informe TXT que muestre:
   - Cuántos posts tiene cada usuario
   - El usuario más activo
   - La longitud media de los títulos
**Bonus:** Que el script detecte si ya tiene datos descargados de hoy y los reutilice en lugar de volver a descargar.
 
<details>
<summary>💡 Pista</summary>
```python
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
# posts es una lista de dicts con: id, userId, title, body
 
# Para contar posts por usuario:
posts_por_usuario = {}
for post in posts:
    uid = post["userId"]
    posts_por_usuario[uid] = posts_por_usuario.get(uid, 0) + 1
```
 
</details>
---
 
## 🥈 Reto 4 — Limpiador de archivos duplicados
 
**Dificultad:** ⭐⭐ Medio
 
Crea un script que detecte archivos duplicados en una carpeta comparando su contenido (no solo el nombre).
 
El script debe:
1. Calcular el hash MD5 de cada archivo
2. Agrupar los archivos con el mismo hash (= contenido idéntico)
3. Mostrar los grupos de duplicados con sus rutas y tamaños
4. Preguntar cuáles eliminar (guardando siempre el original)
```
🔍 Encontrados 3 grupos de duplicados:
 
  Grupo 1 (23.4 KB):
    📄 foto_vacaciones.jpg         ← ORIGINAL (más antiguo)
    📄 foto_vacaciones_copia.jpg   ← DUPLICADO
    📄 foto_vacaciones (2).jpg     ← DUPLICADO
 
  ¿Eliminar duplicados del Grupo 1? (si/no):
```
 
<details>
<summary>💡 Pista</summary>
```python
import hashlib
 
def calcular_md5(ruta_archivo):
    """Calcula el hash MD5 de un archivo."""
    hash_md5 = hashlib.md5()
    with open(ruta_archivo, "rb") as f:   # "rb" = read binary
        for bloque in iter(lambda: f.read(4096), b""):
            hash_md5.update(bloque)
    return hash_md5.hexdigest()
```
 
</details>
---
 
## 🥇 Reto 5 — Pipeline de procesamiento de datos
 
**Dificultad:** ⭐⭐⭐ Difícil
 
Construye un pipeline automático que:
 
1. **Descarga** datos de una API (por ejemplo temperatura de 7 días de Open-Meteo)
2. **Transforma** los datos: calcula media, máximo, mínimo por día
3. **Guarda** un CSV con los datos procesados con timestamp
4. **Genera** un informe TXT con análisis y tendencias
5. **Hace backup** del informe anterior antes de sobreescribir
6. **Registra** en un log cada ejecución con hora y resultado
El script debe funcionar completamente desatendido (sin input del usuario) para poder automatizarse con cron o Task Scheduler.
 
**API sugerida:** `https://api.open-meteo.com/v1/forecast?latitude=37.39&longitude=-5.99&daily=temperature_2m_max,temperature_2m_min&timezone=Europe/Madrid&forecast_days=7`
 
<details>
<summary>💡 Pista de estructura</summary>
```python
def main():
    log = Logger("pipeline.log")
    log.info("Inicio del pipeline")
 
    try:
        datos_raw  = descargar_datos()
        datos_proc = transformar(datos_raw)
        ruta_csv   = guardar_csv(datos_proc)
        ruta_inf   = generar_informe(datos_proc)
        hacer_backup(ruta_inf)
        log.info(f"Pipeline completado. Informe: {ruta_inf}")
    except Exception as e:
        log.error(f"Pipeline fallido: {e}")
```
 
</details>
---
 
## 🌟 Reto Bonus — Automatizador de tareas con argumentos
 
**Dificultad:** ⭐⭐⭐ Difícil | Sin pistas 😈
 
Crea una herramienta de línea de comandos completa que combine:
- **Organizar** archivos de una carpeta: `python tool.py organizar --carpeta ~/Descargas`
- **Backup** de un archivo: `python tool.py backup --archivo datos.csv --destino ~/backups`
- **Informe** de una carpeta: `python tool.py informe --carpeta ~/Documentos --salida informe.txt`
- **Limpiar** backups antiguos: `python tool.py limpiar --carpeta ~/backups --dias 30`
Usa `argparse` con subcomandos. La herramienta debe tener `--verbose` global para mostrar más detalles.
 
---
 
*← [Volver al Nivel 5](../README.md) | [Ir al Nivel 6 →](../../06-proyectos/)*
