# MEDIDOR DE VIRALIDAD

-Descripción-

Proyecto en Python que analiza el crecimiento de un reel utilizando datos reales de interacciones por hora.
El sistema evalúa el ritmo de interacción, ajusta un modelo exponencial a los datos y proyecta el comportamiento futuro.
Incluye factores del contenido que pueden influir en la tasa de crecimiento.

-Modelo Matemático-

El comportamiento se modela mediante la función:

I(t) = a * (b ** t)

donde:
a = punto inicial
b = tasa de crecimiento
t = horas

La función se define y ajusta en regresion.py, y se utiliza para proyectar valores en proyeccion.py.

Estructura del Proyecto
funciones-matrices-proeycto/
│
├── main.py
├── ingreso_datos.py
├── deteccion.py
├── regresion.py
├── proyeccion.py
└── factores.py

Funcionamiento

El usuario ingresa las interacciones acumuladas por hora.
El sistema analiza el ritmo de interacción entre las últimas horas.
Si el ritmo es suficientemente alto, se ajusta un modelo exponencial utilizando SciPy.
Se aplican factores del contenido que pueden modificar la tasa de crecimiento.
Se proyectan las interacciones futuras según el modelo ajustado.
Se muestran los resultados de forma clara y directa.

-Uso-

Ejecutar:

python main.py


El programa solicitará los datos y mostrará la proyección correspondiente.

Ejemplo de salida
Interacciones en la hora 0: 200
Interacciones en la hora 1: 560

Ritmo de interacción elevado. Ajustando modelo.

Punto inicial (a): 200
Tasa de crecimiento (b): 2.8049

En 1 hora(s) más: 560 interacciones estimadas
En 2 hora(s) más: 1567 interacciones estimadas

-Resumen-
El programa permite analizar el crecimiento temprano de un reel mediante un modelo matemático simple, considerando tanto los datos reales como factores del contenido.
Proporciona una proyección clara sobre su posible evolución en las horas siguientes.