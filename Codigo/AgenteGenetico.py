from random import randint, triangular, uniform
from Domain.objeto import Objeto
import copy


class AgenteGenetico:
     
    def __init__(self, maxTryStates, env, obj):
        self.maxTryStates = maxTryStates
        self.env = env
        self.envMaximoLocal = None
        self.obj = obj
        
    #En base a un objeto, genera muchos posibles entornos
    def generarPoblacions(self):
        population = []

        while len(population) < 20:

            rand_i = randint(0, (self.env.i / 2) - 1)
            rand_j = randint(0, (self.env.j / 2) - 1)
            rand_k = randint(0, (self.env.k / 2) - 1)
            new_obj = Objeto(rand_i, rand_j, rand_k, self.obj.largo, self.obj.ancho, self.obj.alto)

            if self.env.validarPosicionVacia(new_obj):
                if self.validarPosiciones():
                    population.append(new_obj)
        
        return population
        


        
    # Valida que una posicion de un objeto no interfiere con los demas objetos
    # - El objeto debe estar sobre una superficie
    # - La superficie debe ser mayor o igual a las dimensiones de la base del objeto
    def validarPosiciones(self):
        puntoX = []
        puntoY = []
        puntoZ = []

        #Primer punto ()
        puntoX.append(self.obj.x - self.obj.largo/2)
        puntoY.append(self.obj.y - self.obj.ancho/2)
        puntoZ.append(self.obj.z - self.obj.alto/2)

        #Segundo punto
        puntoX.append(self.obj.x - self.obj.largo/2)
        puntoY.append(self.obj.y + self.obj.ancho/2)
        puntoZ.append(self.obj.z - self.obj.alto/2)

        #Tercer punto
        puntoX.append(self.obj.x + self.obj.largo/2)
        puntoY.append(self.obj.y + self.obj.ancho/2)
        puntoZ.append(self.obj.z - self.obj.alto/2)

        #Cuarto punto
        puntoX.append(self.obj.x + self.obj.largo/2)
        puntoY.append(self.obj.y - self.obj.ancho/2)
        puntoZ.append(self.obj.z - self.obj.alto/2)

        # Valido base de apoyo para el objeto en el punto 1
        for i in range(4):
            if self.env.validarBase(int(puntoX[i]), int(puntoY[i]), int(puntoZ[i])) == False:
                return False
        
        return True

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