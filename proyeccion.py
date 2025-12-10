def proyectar(a, b, horas):
    proyeccion = []

    for h in range(1, horas + 1):
        valor = a * (b ** h)
        proyeccion.append((h, int(valor)))

    return proyeccion
