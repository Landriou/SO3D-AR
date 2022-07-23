import random
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

            rand_i = random.randint(0, (self.env.i / 2) - 1)
            rand_j = random.randint(0, (self.env.j / 2) - 1)
            rand_k = random.randint(0, (self.env.k / 2) - 1)
            new_obj = Objeto(rand_i, rand_j, rand_k, self.obj.largo, self.obj.ancho, self.obj.alto)

            if self.env.validarPosicionVacia(new_obj):
                if self.validarPosiciones():
                    population.append(new_obj)
        
        self.population = population
        


        
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
       
    # Cruza 2 objetos y devuelve ambos para despues quedarme con los mejores resultados
    def cruzamiento(self, ind_1, ind_2):
        posibilidades = ["x", "y", "z"]

        new_ind_1 = Objeto(ind_1.x, ind_1.y, ind_1.z, self.obj.largo, self.obj.ancho, self.obj.alto)
        new_ind_2 = Objeto(ind_2.x, ind_2.y, ind_2.z, self.obj.largo, self.obj.ancho, self.obj.alto)
        for i in range(2):
            value = random.choice(posibilidades)
            posibilidades.remove(value)
            print("vuelta: ", i )
            print(value)
            if value == "x":
                holder = new_ind_1.x
                new_ind_1.x = new_ind_2.x
                new_ind_2.x = holder
            elif value == "y":
                holder = new_ind_1.y
                new_ind_1.y = new_ind_2.y
                new_ind_2.y = holder
            elif value == "z":
                holder = new_ind_1.z
                new_ind_1.z = new_ind_2.z
                new_ind_2.z = holder

        return new_ind_1,new_ind_2

        
        
    # Modifica algun parametro del objeto aleatoriamente
    def mutacion(self, obj):
        rnd = random.uniform(0, 1)
        if rnd < 0.2:
            posibilidades = ["x", "y", "z"]
            value = random.choice(posibilidades)
            if value == "x":
                obj.x = random.randint(0, (self.env.i / 2) - 1)
            elif value == "y":
                obj.y = random.randint(0, (self.env.j / 2) - 1)
            elif value == "z":
                obj.z = random.randint(0, (self.env.k / 2) - 1)

        return obj
        
        
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