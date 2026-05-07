# 📘 Nivel 2 — Control de Flujo: if, elif, else y bucles

> **Objetivo:** Hacer que tus scripts tomen decisiones y repitan acciones automáticamente.

---

## 🧠 ¿Qué aprenderás en este nivel?

Al terminar este nivel serás capaz de:

- Hacer que tu programa elija entre opciones según una condición
- Usar `if`, `elif` y `else` correctamente
- Repetir acciones con bucles `for` y `while`
- Combinar condiciones con `and`, `or`, `not`
- Controlar los bucles con `break` y `continue`
- Evitar el error más común: el bucle infinito

---

## 📖 Conceptos explicados

### 1. Condicionales: if / elif / else

El bloque `if` ejecuta código **solo si** una condición es verdadera.

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")   # Solo se ejecuta si la condición es True
```

`elif` (else if) añade más condiciones alternativas. `else` es el "en cualquier otro caso":

```python
nota = 65

if nota >= 90:
    print("Sobresaliente")
elif nota >= 70:
    print("Notable")
elif nota >= 50:
    print("Aprobado")
else:
    print("Suspenso")
```

⚠️ **La indentación es OBLIGATORIA en Python.** El código dentro de un `if` debe tener 4 espacios (o 1 tabulación) de margen. Sin indentación, Python da error.

---

### 2. Operadores de comparación

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Distinto de | `5 != 3` | `True` |
| `>` | Mayor que | `7 > 3` | `True` |
| `<` | Menor que | `2 < 1` | `False` |
| `>=` | Mayor o igual | `5 >= 5` | `True` |
| `<=` | Menor o igual | `4 <= 3` | `False` |

⚠️ `=` **asigna** un valor. `==` **compara**. ¡No los confundas!

---

### 3. Operadores lógicos: and, or, not

Permiten combinar varias condiciones:

```python
edad = 20
tiene_carnet = True

# and: las DOS deben ser True
if edad >= 18 and tiene_carnet:
    print("Puede conducir")

# or: basta con que UNA sea True
dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("Es fin de semana")

# not: invierte el resultado
conectado = False
if not conectado:
    print("El usuario no está conectado")
```

---

### 4. Bucle for

Repite un bloque de código **para cada elemento** de una secuencia:

```python
# Iterar sobre un rango de números
for i in range(5):       # i toma los valores 0, 1, 2, 3, 4
    print(i)

# range(inicio, fin, paso)
for i in range(1, 10, 2):   # 1, 3, 5, 7, 9
    print(i)

# Iterar sobre texto
for letra in "Python":
    print(letra)

# Iterar sobre una lista
frutas = ["manzana", "pera", "naranja"]
for fruta in frutas:
    print(fruta)
```

---

### 5. Bucle while

Repite mientras una condición sea verdadera. Se usa cuando **no sabes de antemano cuántas veces** hay que repetir:

```python
intentos = 0

while intentos < 3:
    print(f"Intento {intentos + 1}")
    intentos += 1

print("Fin del bucle")
```

⚠️ **Peligro: bucle infinito.** Si la condición nunca se hace `False`, el programa nunca para. Asegúrate siempre de que la condición cambia en cada iteración.

---

### 6. break y continue

```python
# break: sale del bucle inmediatamente
for i in range(10):
    if i == 5:
        break        # Para el bucle cuando i llega a 5
    print(i)         # Imprime 0, 1, 2, 3, 4

# continue: salta al siguiente ciclo sin ejecutar el resto
for i in range(10):
    if i % 2 == 0:
        continue     # Salta los números pares
    print(i)         # Solo imprime impares: 1, 3, 5, 7, 9
```

---

## 📂 Scripts de este nivel

| Archivo | Qué hace |
|---------|---------|
| [`01_if_elif_else.py`](./scripts/01_if_elif_else.py) | Condicionales completas con ejemplos reales |
| [`02_operadores_logicos.py`](./scripts/02_operadores_logicos.py) | and, or, not en situaciones prácticas |
| [`03_bucle_for.py`](./scripts/03_bucle_for.py) | El bucle for con range, listas y strings |
| [`04_bucle_while.py`](./scripts/04_bucle_while.py) | El bucle while, break y continue |
| [`05_adivina_el_numero.py`](./scripts/05_adivina_el_numero.py) | Proyecto: juego completo de adivinanza |

---

## ✅ Checklist antes de pasar al nivel 3

- [ ] ¿Entiendes la diferencia entre `=` y `==`?
- [ ] ¿Sabes cuándo usar `for` y cuándo usar `while`?
- [ ] ¿Puedes explicar qué hace `break` y `continue`?
- [ ] ¿Has completado al menos 3 de los retos?
- [ ] ¿Tu código tiene la indentación correcta?

---

*← [Volver al índice principal](../README.md)*
