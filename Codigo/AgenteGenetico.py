from random import randint, triangular, uniform


class AgenteGenetico:
     
    def __init__(self, maxTryStates, env):
        self.maxTryStates = maxTryStates
        self.env = env
        self.envMaximoLocal = None
        
    #En base a un objeto, genera muchos entornos con el objeto en posiciones aleatorias
    def obtenerPoblaciones(self):
        print("hola")
        
    # Valida que una posicion de un objeto no interfiere con los demas objetos
    # - El objeto debe estar sobre una superficie
    # - La superficie debe ser mayor o igual a las dimensiones de la base del objeto
    # - Que el alto quepa en el area
    # - Que el ancho quepa en el area
    # - El objeto no se debe superponer(traspasar) con otro objeto
    def validarPosiciones(self):
        print("hola")
        
    # Genera nuevos entornos? despues de validar las pociciones nuevas, deberia copiar los entornos
    # o resolverlo de otra forma
    def nuevoEntornos(self):
        print("hola")
        
    # Calcula el fitness de un entorno en particular
    def calcularFitness(self):
        print("hola")
       
    # Cruza 2 entornos y devuelve un entorno con "mejores resultados"
    def cruzamiento(self):
        print("hola")
        
    # Modifica algun parametro del entorno aleatoriamente
    def mutacion(self):
        print("hola")
        
        
    # Resuelve toda la logica del algoritmo genetico, aca deberia ir todo el codigo llamadp
    def startGenetico(self):
        
       for i in range(self.maxTryStates):
           
           #Nueva poblacion
           
           #Matar a los debiles
           
           #While
           #seleccionar a los mejores
           #cruzarlos
           #mutarlos
           #calcular el fitness
           #guardar el mejor caso
           
           # dar otra iteracion con la nueva poblacion
           print("hola")