def ritmo_interaccion_elevado(interacciones, umbral=1.30):
    if len(interacciones) < 2:
        return False

    anterior = interacciones[-2]
    actual = interacciones[-1]

    if anterior <= 0:
        return False

    ritmo = actual / anterior
    return ritmo >= umbral
