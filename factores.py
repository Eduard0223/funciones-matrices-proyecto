#factores de ocntenido
def factores_contenido():
    musica = input("¿Usa música en tendencia? (s/n): ").lower() == "s"
    hashtags = input("¿Tiene buenos hashtags? (s/n): ").lower() == "s"
    duracion = input("¿La duración es ideal (8-12s)? (s/n): ").lower() == "s"

    bonus = 0

    if musica:
        bonus += 0.25
    if hashtags:
        bonus += 0.15
    if duracion:
        bonus += 0.15

    return bonus
