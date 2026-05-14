# 📘 Nivel 6 — Proyectos: Todo converge aquí

> **Objetivo:** Construir aplicaciones completas, con estructura profesional, que resuelven problemas reales de principio a fin.

---

## 🧠 ¿Qué aprenderás en este nivel?

Al terminar este nivel habrás construido tres aplicaciones reales y aprenderás a:

- Estructurar un proyecto en varios módulos (archivos `.py` con responsabilidades claras)
- Separar datos, lógica y presentación
- Escribir código que un compañero pueda entender y mantener
- Gestionar dependencias con `requirements.txt`

---

## 📐 Estructura profesional de un proyecto

```
mi_proyecto/
│
├── main.py          ← Punto de entrada. Solo orquesta, no hace lógica.
├── datos.py         ← Leer y escribir archivos (JSON, CSV...)
├── logica.py        ← Las reglas: cálculos, validaciones, búsquedas
├── interfaz.py      ← Todo lo que ve el usuario (print/input)
├── config.py        ← Constantes y rutas
│
├── datos/           ← Archivos de datos generados en ejecución
├── requirements.txt ← pip install -r requirements.txt
└── README.md        ← Cómo usar el proyecto
```

**¿Por qué dividir?**  
Si algo falla, sabes exactamente en qué archivo buscar. Si quieres cambiar cómo se guardan los datos, solo tocas `datos.py`. Si quieres cambiar la pantalla, solo tocas `interfaz.py`.

---

## 📂 Proyectos de este nivel

| Carpeta | Proyecto | Lo que practica |
|---------|---------|----------------|
| [`proyecto-agenda/`](./proyecto-agenda/) | 📒 Agenda de Contactos | Módulos, CRUD completo, búsqueda, exportación CSV |
| [`proyecto-gestor-gastos/`](./proyecto-gestor-gastos/) | 💰 Gestor de Gastos | Estadísticas, gráficos ASCII, filtros por fecha |
| [`proyecto-quiz/`](./proyecto-quiz/) | 🎮 Quiz con Ranking | API externa, ranking persistente, temporizador |

---

## 🏁 ¿Y después del Nivel 6?

Este repositorio te llevó de zero a aplicaciones reales. Los siguientes pasos:

- **Interfaces gráficas** → `tkinter` (incluido en Python)
- **Bases de datos** → `sqlite3` (incluido en Python)
- **Web backend** → `Flask` o `FastAPI`
- **Análisis de datos** → `pandas` + `matplotlib`
- **Tests** → `pytest`

---

*← [Volver al índice principal](../README.md)*
