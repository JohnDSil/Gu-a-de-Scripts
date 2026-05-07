# 📘 Nivel 3 — Funciones: Código reutilizable y organizado

> **Objetivo:** Dejar de repetir código. Aprender a empaquetar lógica en bloques reutilizables que puedes llamar cuando quieras.

---

## 🧠 ¿Qué aprenderás en este nivel?

Al terminar este nivel serás capaz de:

- Definir y llamar tus propias funciones
- Usar parámetros y valores por defecto
- Entender qué es `return` y cuándo usarlo
- Distinguir variables locales de globales
- Organizar un programa grande en funciones pequeñas
- Documentar funciones con docstrings

---

## 📖 Conceptos explicados

### 1. ¿Por qué funciones?

Sin funciones, si necesitas hacer lo mismo en 5 sitios distintos, copias el código 5 veces. Si hay un error, lo tienes que corregir en 5 sitios. Mal plan.

Con funciones, lo escribes una vez y lo llamas desde donde quieras:

```python
# Sin funciones (código repetido)
print("=" * 30)
print("  Bienvenido")
print("=" * 30)
# ... más tarde ...
print("=" * 30)
print("  Resultados")
print("=" * 30)

# Con funciones (código limpio)
def cabecera(titulo):
    print("=" * 30)
    print(f"  {titulo}")
    print("=" * 30)

cabecera("Bienvenido")
# ... más tarde ...
cabecera("Resultados")
```

---

### 2. Definir una función

```python
def nombre_funcion(parametro1, parametro2):
    """Docstring: explica qué hace esta función."""
    # código de la función
    return resultado
```

- `def` → palabra clave para definir una función
- `nombre_funcion` → nombre descriptivo (usa snake_case)
- `parametros` → información que recibe la función (opcional)
- `return` → valor que devuelve la función (opcional)

---

### 3. Parámetros y argumentos

```python
def saludar(nombre, saludo="Hola"):   # saludo tiene valor por defecto
    print(f"{saludo}, {nombre}!")

saludar("Ana")              # Hola, Ana!        (usa el valor por defecto)
saludar("Luis", "Buenos días")  # Buenos días, Luis! (sobreescribe el defecto)
saludar(nombre="Marta", saludo="Ey")  # También funciona con nombre=valor
```

---

### 4. Return: devolver un valor

Una función puede devolver un resultado para usarlo después:

```python
def sumar(a, b):
    return a + b           # Devuelve el resultado

resultado = sumar(3, 7)    # resultado = 10
print(resultado * 2)       # 20 — usamos el resultado en otra operación
```

Sin `return`, la función devuelve `None` (nada).

---

### 5. Variables locales vs globales

```python
mensaje = "Soy global"     # Variable global: accesible en todo el programa

def mi_funcion():
    mensaje = "Soy local"  # Variable local: solo existe dentro de la función
    print(mensaje)         # "Soy local"

mi_funcion()
print(mensaje)             # "Soy global" — la global no fue modificada
```

**Regla de oro:** Las funciones no deben modificar variables globales. Es mejor pasarles los datos como parámetros y recibir el resultado con `return`.

---

### 6. Funciones que devuelven múltiples valores

```python
def estadisticas(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    media  = sum(numeros) / len(numeros)
    return minimo, maximo, media   # Devuelve una tupla

mn, mx, med = estadisticas([4, 7, 2, 9, 1])
print(f"Mín: {mn}, Máx: {mx}, Media: {med}")
```

---

### 7. Docstrings: documenta tu código

```python
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal.

    Args:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.

    Returns:
        float: El valor del IMC redondeado a 2 decimales.
    """
    return round(peso / altura ** 2, 2)
```

---

## 📂 Scripts de este nivel

| Archivo | Qué hace |
|---------|---------|
| [`01_primera_funcion.py`](./scripts/01_primera_funcion.py) | Definir, llamar y entender las funciones básicas |
| [`02_parametros_return.py`](./scripts/02_parametros_return.py) | Parámetros, valores por defecto y return |
| [`03_funciones_utiles.py`](./scripts/multiple/03_funciones_utiles.py) | Librería de funciones útiles del día a día |
| [`04_scope_y_buenas_practicas.py`](./scripts/validacion/04_scope_y_buenas_practicas.py) | Scope, docstrings y cómo organizar un programa |
| [`05_juego_refactorizado.py`](./scripts/05_juego_refactorizado.py) | El juego del Nivel 2 reescrito con funciones |

---

## ✅ Checklist antes de pasar al nivel 4

- [ ] ¿Puedes escribir una función con parámetros y `return` de memoria?
- [ ] ¿Entiendes la diferencia entre variable local y global?
- [ ] ¿Sabes cuándo usar `return` y cuándo no?
- [ ] ¿Tus funciones tienen docstring?
- [ ] ¿Has completado al menos 3 retos?

---

*← [Volver al índice principal](../README.md)*
