# Optimizacion de espacio (3D-Realidad aumentada)

## CODIGO:
SO3D-AR

## INTEGRANTES:
Silva,Daniel Alexander
Fuchilieri, Sebastian

## Descripcion
El proyecto se basa en un algoritmo cuya entrada es un espacio 3D con posibilidad de tener objetos dentro que dificulten la colocacion de otros objetos. El objetivo del algoritmo seria encontrar la mejor forma (relativa a la posicion del usuario) de colocar uno o varios objetos en el espacio antes mencionado. Esto se haria en funcion de varios parametros:

- Alto (proporcional al ancho)
- Ancho (proporcional al alto)
- Proximidad al observador
- Estar en una superficie (suelo)
- Otras variables a conciderar a futuro


La salida del algoritmo sera el espacio con los objetos colocados, se podrá evaluar su rendimiento y aplicación en base a los valores de la función objetivo y la realidad de como quedo el resultado final. El alcance previsto del proyecto se limita al funcionamiento interno del algoritmo sin tener en cuenta el acople de la herramienta de realidad aumentada o los procesadores de imagen.
### Metricas a evaluar

Se va a evaluar:
La cantidad de veces reales que llega a un estado objetivo
Cuanto tarda en colocar dichos objetos
Realmente si la colocacion es eficiente para un humano aunque llegue al estado objetivo

## Justificacion
Creemos que la problemática es soluble a través de IA ya que la aplicación de heurísticas adecuadas en problemas de optimización forman parte de este campo y además dan muy buenos resultados como vimos en el laboratorio de la materia.
La solucion se va a hacer a traves de un algoritmo Genetico, se va a evaluar e investigar que tecnicas se pueden aplicar para hacer el cruzamiento en un espacio 3d que es la parte mas complicada.

## Cronograma de Actividades


Actividad 1. Investigacion de formas de aplicar el algoritmo genetico y tecnicas de cruzamiento 3D. [7 días]
Actividad 2. Pruebas de cruzamiento [6  días]
Actividad 3. Implementacion de mutacion. [2 días]
Actividad 4. Implementación de algoritmo genetico. [3 días]
Actividad 5. Ajuste de la parametrizacion del algoritmo genetico. [7 días]
Actividad 6. Pruebas y ajuste para llegar a las metricas requeridas. [4 día]
Actividad 7. Análisis de los resultados. [2 días]
Actividad 8. Escritura de informe final. [3 días]

## Estimacion de actividades

La idea es terminar de presentar el proyecto en la ultima mesa de marzo antes de que termine el a;o academico
Por eso se planea trabajar en el proyecto a partir finales de enero, llevando todo el desarrollo durante febrero y marzo
para aprovechar las mesas de consulta y revisar el avance.

Estimacion de tiempo: 1-2 meses de desarrollo.