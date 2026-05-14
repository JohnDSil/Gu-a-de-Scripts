# config.py
import os

BASE_DIR   = os.path.dirname(__file__)
DATOS_DIR  = os.path.join(BASE_DIR, "datos")
RUTA_RANKING = os.path.join(DATOS_DIR, "ranking.json")

SEGUNDOS_POR_PREGUNTA = 15
PREGUNTAS_POR_PARTIDA = 10
PUNTOS_POR_CORRECTA   = 10
BONUS_RAPIDO          = 5    # Bonus si responde en menos de 5 segundos

# Preguntas de respaldo (si no hay internet)
PREGUNTAS_OFFLINE = [
    {"pregunta": "¿Cuántos bits tiene un byte?",
     "opciones": ["4", "8", "16", "32"], "correcta": 1},
    {"pregunta": "¿Qué significa CPU?",
     "opciones": ["Central Processing Unit", "Computer Power Unit",
                  "Core Program Utility", "Central Program Upload"], "correcta": 0},
    {"pregunta": "¿Cuál es el lenguaje de marcado de las páginas web?",
     "opciones": ["CSS", "Python", "HTML", "SQL"], "correcta": 2},
    {"pregunta": "¿Qué tipo de dato es True en Python?",
     "opciones": ["int", "str", "bool", "float"], "correcta": 2},
    {"pregunta": "¿Qué símbolo se usa para comentarios en Python?",
     "opciones": ["//", "/*", "#", "--"], "correcta": 2},
    {"pregunta": "¿Qué función imprime en pantalla en Python?",
     "opciones": ["echo()", "print()", "write()", "show()"], "correcta": 1},
    {"pregunta": "¿Cuántos colores tiene el arco iris?",
     "opciones": ["5", "6", "7", "8"], "correcta": 2},
    {"pregunta": "¿Qué planeta es el más grande del sistema solar?",
     "opciones": ["Saturno", "Neptuno", "Jupiter", "Urano"], "correcta": 2},
    {"pregunta": "¿En qué año se fundó Google?",
     "opciones": ["1994", "1996", "1998", "2000"], "correcta": 2},
    {"pregunta": "¿Qué es un algoritmo?",
     "opciones": ["Un tipo de ordenador", "Una secuencia de pasos para resolver un problema",
                  "Un lenguaje de programación", "Un sistema operativo"], "correcta": 1},
]
