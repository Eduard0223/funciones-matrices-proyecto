import numpy as np
from scipy.optimize import curve_fit

def modelo(t, a, b):
    return a * (b ** t)

def ajustar(tiempos, interacciones):
    # Convertimos a arreglos para scipy
    t = np.array(tiempos)
    i = np.array(interacciones)

    # valores iniciales simples 
    a0 = max(i[0], 1)
    b0 = 1.05

    # Ajuste de curva exponencial
    (a, b), _ = curve_fit(modelo, t, i, p0=(a0, b0))

    return a, b
