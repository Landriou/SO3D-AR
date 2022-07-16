Para poder hacer un algoritmo que termine posicionando un objeto en el mejor lugar posible dentro de un area con objetos debemos preguntarnos primero
que es un mejor lugar, o tambien que es un lugar, para lo cual definimos las siguientes reglas de posicionamiento
Estas reglas son las mas basicas que se preveen, sin embargo el sistema seria escalable para agregar mas en un futuro.

# Reglas de posicionamiento
- El objeto debe estar sobre una superficie
- La superficie debe ser mayor o igual a las dimensiones de la base del objeto
- Que el alto quepa en el area
- Que el ancho quepa en el area
- El objeto no se debe superponer(traspasar) con otro objeto


# Parametros de como queremos que quede
- Mientras mas grande la superficie donde este apoyado mejor
- Mientras mas distancia tenga de otros objetos mejor
- Mientras mas distancia haya frente a otro objeto desde arriba mejor
- Mientras mas cercano este al punto dado mejor

# Parametros del objeto
- Posicion: las coordenadas x,y,z del objeto en el espacio
- Alto
- Ancho
- Largo
- Punto cercano de referencia
- Posicion relativa del objeto, como queremos que quede, de costado, vertical, horizontal, sobre que base se deberia apoyar