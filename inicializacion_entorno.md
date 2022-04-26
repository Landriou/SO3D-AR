# Instanciación del entorno 3D

El entorno en el cual nuestro algoritmo correrá, sera una matriz tridimensional.
En cada punto de esta matriz, se podrá encontrar vació o ocupado por un fragmento de un objeto.

En una primera instancia, el ambiente sera un espacio cuadrado vacío, en el cual colocaremos objetos fijos. Este entorno sera utilizado en todos los casos y ejecuciones del algoritmo, esto es para poder comparar los resultados e ir viendo mejoras o problemas en el desarrollo del algoritmo.

Se tomo esta decision para, posteriormente, poder vectorizar todo el espacio y luego mostrarlo gráficamente.

Con respecto a los objetos que se colocan en el espacio, no deben colisionar y deben tener ubicaciones físicamente validas, considerando algo valido como no superpuesto con otro objeto o con los propios limites del entorno.