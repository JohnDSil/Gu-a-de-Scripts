# 🏆 Retos — Nivel 1: Lo Básico

> Completa estos retos **antes** de mirar cualquier solución. El error es parte del proceso.
> Si tu script funciona aunque sea de forma diferente a lo esperado, ¡también cuenta!

---

## 📋 Normas de los retos

1. Crea un archivo `.py` nuevo para cada reto (ej: `reto_01.py`)
2. Añade comentarios explicando qué hace cada parte
3. Prueba tu script antes de darlo por terminado
4. Si te atascas más de 20 minutos, mira una pista. Si sigues atascado, busca la solución.

---

## 🥉 Reto 1 — Tarjeta de presentación

**Dificultad:** ⭐ Fácil

Crea un script que le pregunte al usuario:
- Su nombre
- Su edad
- Su ciudad
- Su hobby favorito

Y luego muestre una "tarjeta de presentación" bien formateada con esa información.

**Ejemplo de salida esperada:**
```
╔══════════════════════════════════╗
║       TARJETA DE PRESENTACIÓN    ║
╠══════════════════════════════════╣
║  Nombre:  Ana García             ║
║  Edad:    21 años                ║
║  Ciudad:  Barcelona              ║
║  Hobby:   Fotografía             ║
╚══════════════════════════════════╝
```

<details>
<summary>💡 Pista (solo si llevas más de 20 min)</summary>

Usa `input()` cuatro veces para recoger los datos.
Luego construye la salida con `print()` y f-strings.
Para las líneas decorativas, puedes usar caracteres como `=`, `-`, `*` o los bordes de caja `╔ ║ ╚`.

</details>

---

## 🥈 Reto 2 — Conversor de temperatura

**Dificultad:** ⭐⭐ Medio

Crea un script que pida una temperatura en **grados Celsius** y la convierta a:
- Fahrenheit: `F = (C × 9/5) + 32`
- Kelvin: `K = C + 273.15`

Muestra los tres valores con exactamente 2 decimales.

**Ejemplo de salida esperada:**
```
Temperatura en Celsius: 100

Conversiones:
  100.00 °C  →  212.00 °F
  100.00 °C  →  373.15 K
```

<details>
<summary>💡 Pista</summary>

Usa `float(input(...))` para admitir decimales.
Aplica las fórmulas guardando los resultados en variables.
Para mostrar exactamente 2 decimales en una f-string: `{variable:.2f}`

</details>

---

## 🥈 Reto 3 — Contador de palabras

**Dificultad:** ⭐⭐ Medio

Crea un script que pida al usuario que escriba una frase cualquiera y luego muestre:
- El número de caracteres (sin contar espacios)
- El número de caracteres (contando espacios)
- El número de palabras

**Pista para contar palabras:** `frase.split()` divide el texto en palabras y devuelve una lista. Puedes usar `len()` sobre esa lista.

**Ejemplo de salida:**
```
Escribe una frase: El cielo es azul hoy

📊 Análisis de tu frase:
   Caracteres (sin espacios): 17
   Caracteres (con espacios): 21
   Número de palabras:        5
```

<details>
<summary>💡 Pista</summary>

- `len(frase)` cuenta todos los caracteres incluyendo espacios
- `frase.replace(" ", "")` elimina los espacios del texto
- `frase.split()` devuelve una lista de palabras
- `len(frase.split())` cuenta las palabras

</details>

---

## 🥇 Reto 4 — Calculadora de IMC

**Dificultad:** ⭐⭐⭐ Difícil

Crea un script que calcule el **Índice de Masa Corporal (IMC)** de una persona.

**Fórmula:** `IMC = peso (kg) / altura² (m)`

El script debe:
1. Pedir el nombre, peso (en kg) y altura (en metros) del usuario
2. Calcular el IMC
3. Mostrar el resultado con 2 decimales
4. Indicar en qué categoría está según la OMS:

| IMC | Categoría |
|-----|-----------|
| Menos de 18.5 | Bajo peso |
| Entre 18.5 y 24.9 | Peso normal |
| Entre 25 y 29.9 | Sobrepeso |
| 30 o más | Obesidad |

**Ejemplo de salida:**
```
Nombre: Carlos
Peso (kg): 75
Altura (m): 1.78

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Resultado para Carlos:
  IMC: 23.67
  Categoría: Peso normal ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

<details>
<summary>💡 Pista</summary>

Para calcular altura al cuadrado: `altura ** 2`
Para la categoría, necesitas condiciones `if / elif / else` (las verás en detalle en el Nivel 2, pero puedes intentarlo ya).

Formato básico:
```python
if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"
```

</details>

---

## 🌟 Reto Bonus — Generador de nombre de usuario

**Dificultad:** ⭐⭐ Medio | Sin pistas esta vez 😈

Crea un script que genere automáticamente un nombre de usuario a partir de los datos del usuario.

**Reglas para generar el username:**
- Toma las **3 primeras letras del nombre** (en minúsculas)
- Añade las **2 primeras letras del apellido** (en minúsculas)
- Añade el **año de nacimiento** al final

**Ejemplo:**
- Nombre: `María`, Apellido: `González`, Año: `2001`
- Username generado: `mariag2001`

**Extra:** Si el nombre tiene menos de 3 letras o el apellido menos de 2, usa todas las letras disponibles.

---

## ✅ Cuando termines los retos...

Revisa tu código y pregúntate:
- ¿Tiene comentarios que expliquen qué hace cada parte?
- ¿Los nombres de las variables son descriptivos?
- ¿Funciona correctamente con valores extremos? (números negativos, texto vacío, etc.)

Cuando estés satisfecho, ¡pasa al [Nivel 2: Control de Flujo](../../02-control-flujo/)!

---

*← [Volver al Nivel 1](../README.md)*
