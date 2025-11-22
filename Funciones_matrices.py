import matplotlib.pyplot as plt
import numpy as np

# --- SIMULADOR DE VIRALIDAD INSTAGRAM ---
print("--- SIMULADOR DE VIRALIDAD INSTAGRAM ---")
print("Responde a las preguntas para calcular la tasa de crecimiento (k)")

# 1. Entrada de Datos (Variables de la Pregunta 5)

# --- CORRECCIÓN APLICADA AQUÍ: Validación de entrada para evitar errores ---
entrada = input("1. ¿Cuántas interacciones tuvo en la primera hora? (ej. 50, 500): ")
if not entrada.isdigit():
    print("Error de tipeo detectado. Usaremos 100 interacciones por defecto para la prueba.")
    v0 = 100
else:
    v0 = int(entrada)

# Factores de Contenido (Propuesta 2)
print("\n--- Factores de Contenido ---")
usa_audio_tendencia = input("2. ¿Usa audio en tendencia? (si/no): ").lower()
# Validación simple para hashtags
try:
    calidad_hashtags = int(input("3. Calidad de hashtags (1 a 10): "))
except ValueError:
    calidad_hashtags = 5 # Valor promedio si fallan al escribir
    print("   (Usando calidad 5 por defecto)")

duracion_optima = input("4. ¿Duración entre 7-15 seg? (si/no): ").lower()

# --- MODELO MATEMÁTICO (Nociones Matemáticas) ---

# Base de crecimiento (crecimiento orgánico lento)
k = 0.1

# Sumamos valor a 'k' según las respuestas (Respuesta a Pregunta 5)
if "si" in usa_audio_tendencia:
    k += 0.25  # El audio impulsa mucho la viralidad
if "si" in duracion_optima:
    k += 0.15  # Duración correcta retiene audiencia

# Aporte gradual de hashtags (máximo 0.1 extra)
k += (calidad_hashtags / 10) * 0.1 
