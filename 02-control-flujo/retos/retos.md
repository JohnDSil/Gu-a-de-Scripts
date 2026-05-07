# 🏆 Retos — Nivel 2: Control de Flujo

> Como siempre: intenta cada reto antes de mirar las pistas. El tiempo que pasas atascado es el tiempo que más aprendes.

---

## 🥉 Reto 1 — Clasificador de triángulos

**Dificultad:** ⭐ Fácil

Pide al usuario los tres lados de un triángulo y determina:
1. Si es un triángulo válido (la suma de dos lados siempre debe ser mayor que el tercero)
2. Si es válido, clasifícalo:
   - **Equilátero**: los tres lados iguales
   - **Isósceles**: dos lados iguales
   - **Escaleno**: todos los lados distintos

**Ejemplo de salida:**
```
Lado 1: 5
Lado 2: 5
Lado 3: 7

✅ Triángulo válido.
Tipo: Isósceles (dos lados iguales)
```

<details>
<summary>💡 Pista</summary>

Para validar el triángulo, comprueba que:
- `a + b > c`
- `a + c > b`
- `b + c > a`

Las tres condiciones deben cumplirse con `and`.

Para clasificar, usa `if a == b == c` para equilátero, y `a == b or b == c or a == c` para isósceles.

</details>

---

## 🥉 Reto 2 — Tabla de multiplicar

**Dificultad:** ⭐ Fácil

Pide un número al usuario y muestra su tabla de multiplicar completa (del 1 al 10), bien formateada.

**Ejemplo de salida:**
```
¿De qué número quieres la tabla? 7

📊 Tabla del 7:
  7 × 1  =  7
  7 × 2  = 14
  7 × 3  = 21
  ...
  7 × 10 = 70
```

**Extra:** Después de mostrar la tabla, pregunta al usuario si quiere ver otra. Si dice que sí, repite con el nuevo número (usa un `while`).

<details>
<summary>💡 Pista</summary>

Usa `for i in range(1, 11)` para los multiplicadores del 1 al 10.
Para alinear los números, usa `{resultado:3}` en la f-string (reserva 3 espacios).

</details>

---

## 🥈 Reto 3 — FizzBuzz

**Dificultad:** ⭐⭐ Medio

El clásico ejercicio de programación. Imprime los números del 1 al 100, pero:

- Si el número es múltiplo de 3, imprime **"Fizz"**
- Si es múltiplo de 5, imprime **"Buzz"**
- Si es múltiplo de 3 **y** de 5, imprime **"FizzBuzz"**
- Si no es múltiplo de ninguno, imprime el número

**Ejemplo de salida (primeros 20):**
```
1  2  Fizz  4  Buzz  Fizz  7  8  Fizz  Buzz  11  Fizz  13  14  FizzBuzz  16  17  Fizz  19  Buzz
```

> 💡 Pista conceptual: el operador `%` (módulo) te da el resto de una división. Si `n % 3 == 0`, el número es múltiplo de 3.

---

## 🥈 Reto 4 — Validador de contraseña segura

**Dificultad:** ⭐⭐ Medio

Crea un script que pida una contraseña al usuario y compruebe si cumple los siguientes criterios de seguridad:

| Criterio | Requisito |
|----------|-----------|
| Longitud | Al menos 8 caracteres |
| Mayúsculas | Al menos una letra mayúscula |
| Minúsculas | Al menos una letra minúscula |
| Números | Al menos un dígito |
| Carácter especial | Al menos uno de: `! @ # $ % & * _` |

Muestra qué criterios cumple y cuáles no, y di si la contraseña es segura o no.

**Ejemplo de salida:**
```
Contraseña: MiPass1!

✅ Longitud suficiente (8+ caracteres)
✅ Tiene mayúsculas
✅ Tiene minúsculas
✅ Tiene números
✅ Tiene carácter especial

🔐 Contraseña SEGURA.
```

<details>
<summary>💡 Pista</summary>

Para comprobar si algún carácter de un string cumple una condición, usa un bucle `for` con `break`, o la función `any()`:

```python
tiene_mayuscula = any(c.isupper() for c in contrasena)
tiene_numero    = any(c.isdigit() for c in contrasena)
especiales      = "!@#$%&*_"
tiene_especial  = any(c in especiales for c in contrasena)
```

</details>

---

## 🥇 Reto 5 — Mini cajero automático

**Dificultad:** ⭐⭐⭐ Difícil

Simula un cajero automático con las siguientes funcionalidades:

1. El cajero tiene un saldo inicial (tú decides cuánto)
2. Muestra un menú con opciones:
   - `1` — Consultar saldo
   - `2` — Ingresar dinero
   - `3` — Retirar dinero
   - `4` — Salir
3. Valida que el usuario no retire más de lo que tiene
4. Muestra el historial de operaciones al salir

**Ejemplo de interacción:**
```
╔═══════════════════╗
║ CAJERO AUTOMÁTICO ║
╚═══════════════════╝

1. Consultar saldo
2. Ingresar dinero
3. Retirar dinero
4. Salir

Opción: 2
¿Cuánto quieres ingresar? 500
✅ Ingreso de 500.00€ realizado. Saldo actual: 1500.00€

Opción: 3
¿Cuánto quieres retirar? 2000
❌ Saldo insuficiente. Tienes 1500.00€.

Opción: 4
📋 Historial: 1 ingreso, 0 retiradas.
👋 ¡Hasta pronto!
```

<details>
<summary>💡 Pista</summary>

Usa `while True` con un menú y `if/elif/else` para cada opción.
Sal del bucle con `break` cuando el usuario elija la opción 4.
Usa dos contadores: `num_ingresos` y `num_retiradas`.

</details>

---

## 🌟 Reto Bonus — Piedra, papel o tijera

**Dificultad:** ⭐⭐⭐ Difícil | Sin pistas 😈

Crea el juego clásico de piedra, papel o tijera:

- El jugador elige entre piedra, papel o tijera
- El ordenador elige aleatoriamente (`random.choice(["piedra", "papel", "tijera"])`)
- Se muestran las dos elecciones y se determina el ganador
- Se juega al mejor de 3 rondas
- Al final se muestra el marcador total

---

*← [Volver al Nivel 2](../README.md) | [Ir al Nivel 3 →](../../03-funciones/)*
