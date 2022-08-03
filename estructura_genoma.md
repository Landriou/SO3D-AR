# Descripción de la estructura del genoma

El genoma que construimos esta conformado por las siguientes características:

Posición con respecto al eje X
Posición con respecto al eje Y
Posición con respecto al eje Z
Alto
Ancho
Profundidad

En esta primera instancia, para no complejizar ni el desarrollo ni el modelo, las únicas variables que se verán afectadas por el Multi-Point Crossover seran las primeras 6 variables, las relacionadas con los ejes coordenados, respecto a la posición y a la rotación.

Con estos cruzamientos, vamos a lograr el reposición del objeto en el espacio, cambiando su ubicación pero no sus características, es decir, en cada mutación, lo único que se cambiaría seria la orientación el objeto, no sus características.