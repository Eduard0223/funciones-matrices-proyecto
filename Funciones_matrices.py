import matplotlib.pyplot as plt
import numpy as np
import math

# --- CONFIGURACIÓN DE LA SIMULACIÓN (Propuesta 2: Factores) ---
print("--- SIMULADOR DE VIRALIDAD INSTAGRAM ---")
print("Responde a las preguntas para calcular la tasa de crecimiento (k)")

# 1. Entrada de Datos (Variables de la Pregunta 5)
# Interacciones en la primera hora (V0)
entrada = input("1. ¿Cuántas interacciones tuvo en la primera hora? (ej. 50, 500): ")
if not entrada.isdigit():
    print("¡Error de tipeo! Usaremos 100 por defecto para probar.")
    v0 = 100
else:
    v0 = int(entrada)

