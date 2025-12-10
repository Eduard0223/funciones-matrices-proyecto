def ingresar_datos():
    t = []
    i = []
    hora = 0

    print("*** INGRESO DE DATOS ***")

    while True:
        x = int(input(f"Interacciones en la hora {hora}: "))
        t.append(hora)
        i.append(x)

        seguir = input("¿Agregar otra hora? (s/n): ").lower()
        if seguir != "s":
            break

        hora += 1

    return t, i
