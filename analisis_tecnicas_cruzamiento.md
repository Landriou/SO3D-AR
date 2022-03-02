# Investigación de técnicas de cruzamiento genético

Después de una comparativa entre los 4 principales algoritmos de cruzamiento encontrados: 

- Single-Point Crossover, Multi-Point Crossover, Linear Crossover, Blend crossover, Simulated binary crossover

Y un apoyo sobre el paper mencionado en el documento anterior, se decidió elegir Multi-Point Crossover con mutación aleatoria.
En este cruzamiento, se determinan de forma aleatoria o especificada, los puntos de corte en el cromosoma, obteniendo porciones de genes, los cuales serian intercambiados entre los padres para así poder generar a los respectivos hijos del cruzamiento. Sumado a esto, con una probabilidad aleatoria, se determina una posible mutación, en la cual se aplica una variación sobre un gen aleatorio. De esta forma, se obtiene una población que va tendiendo al resultado optimo, pero se evita quedar atrapado en un optimo local.

El uso de esta técnica de cruzamiento se debe a la estructura de cromosomas y genes que se aplicara para resolver el problema, siendo esta la forma más practica que se encontró para llevar a cabo el proceso genético. 

Dicha estructura de genes y cromosomas sera explicada en otro documento llamado estructura_genoma.md

Las demás técnicas de cruzamiento fueron descartadas ya que no resultaban tan interesantes o no se les vio una buena aplicación para nuestro problema.

A la hora de tomar la decisión, los dos candidatos finales fueron Blend Crossover y Multi-Point Crossover.
Blend Crossover, mediante una fórmula matemática, determina un rango entre los padres, de los cuales de forma aleatoria, se obtienen a los hijos. Este método nos resulto bastante interesante y con una característica particular, de a poco va a tendiendo a los casos con mejor fitnes. Pero termino siendo descartado, ya que con una investigación posterior, se encontró que puede ser más fácil que dicha tendencia termine cayendo en un optimo local.

Por otro lado, Multi-Point Crossover cumple con todas las necesidades que nos planteamos a la hora de cruzar padres y generar los hijos, ya que al realizar múltiples cortes y hacer los cruzamientos, esto se puede interpretar como un objeto que cambia su posición en un espacio 3d, variando su posición relativa en el espacio y sus dimensiones, todo esto considerando que los genes representan diferentes características del objeto a colocar en el espacio.