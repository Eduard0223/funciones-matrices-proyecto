from ingreso_datos import ingresar_datos
from deteccion import ritmo_interaccion_elevado
from regresion import ajustar
from proyeccion import proyectar
from factores import factores_contenido
print("\n*** MEDIDOR DE VIRALIDAD ***\n")

t, i = ingresar_datos()

if ritmo_interaccion_elevado(i):
    print("\nRitmo de interaccion elevado. Ajustando modelo.\n")
    a, b = ajustar(t, i)
    bonus = factores_contenido()
    b = b * (1 + bonus)
    print(f"Punto inicial (a): {a:.0f}")
    print(f"Tasa de crecimiento (b): {b:.1f}")

    h = int(input("\nHoras a proyectar: "))
    p = proyectar(a, b, h)

    print("\n*** Proyeccion ***")
    for hora, valor in p:
        print(f"En {hora} hora(s) más: {valor} interacciones estimadas")
else:
    print("\nNo hay aceleracion, no parece viral.")
