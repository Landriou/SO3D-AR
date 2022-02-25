# Investigación de técnicas de cruzamiento genético

Después de una comparativa entre los 4 principales algoritmos de cruzamiento encontrados: 

- Single-Point Crossover,Multi-Point Crossover, Linear Crossover, Blend crossover, Simulated binary crossover

Y un apoyo sobre el paper mencionado en el documento anterior, se decidió elegir Multi-Point Crossover con mutación aleatoria.
En este cruzamiento, se determinan de forma aleatoria o especificada, los puntos de corte en el cromosoma, obteniendo porciones de genes, los cuales serian intercambiados entre los padres para así poder generar a los respectivos hijos del cruzamiento. Sumado a esto, con una probabilidad aleatoria, se determina una posible mutación, en la cual se aplica una variación sobre un gen aleatorio. De esta forma, se obtiene una población que va tendiendo al resultado optimo, pero se evita quedar atrapado en un optimo local.

EL uso de esta técnica de cruzamiento se debe a la estructura de cromosomas y genes que se aplicara para resolver el problema, siendo esta la forma más practica que se encontró para llevar a cabo el proceso genético. 

Dicha estructura de genes y cromosomas sera explicada en otro documento llamado estructura_genoma.md