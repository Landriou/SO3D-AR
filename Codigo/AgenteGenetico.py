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
    def generarPoblacion(self):
        population = []

        while len(population) < 20:

            rand_i = random.randint(0, (self.env.i / 2) - 1)
            rand_j = random.randint(0, (self.env.j / 2) - 1)
            rand_k = random.randint(0, (self.env.k / 2) - 1)
            new_obj = Objeto(rand_i, rand_j, rand_k, self.obj.largo, self.obj.ancho, self.obj.alto)

            if self.env.validarPosicionVacia(new_obj):
                if self.validarPosiciones(new_obj):
                    # CALCULAR EL FITNESS DEL OBJETO
                    population.append(new_obj)
        
        self.population = population
        


        
    # Valida que una posicion de un objeto no interfiere con los demas objetos
    # - El objeto debe estar sobre una superficie
    # - La superficie debe ser mayor o igual a las dimensiones de la base del objeto
    def validarPosiciones(self, obj):
        puntoX = []
        puntoY = []
        puntoZ = []

        #Primer punto ()
        puntoX.append(obj.x - self.obj.largo/2)
        puntoY.append(obj.y - self.obj.ancho/2)
        puntoZ.append(obj.z - self.obj.alto/2)

        #Segundo punto
        puntoX.append(obj.x - self.obj.largo/2)
        puntoY.append(obj.y + self.obj.ancho/2)
        puntoZ.append(obj.z - self.obj.alto/2)

        #Tercer punto
        puntoX.append(obj.x + self.obj.largo/2)
        puntoY.append(obj.y + self.obj.ancho/2)
        puntoZ.append(obj.z - self.obj.alto/2)

        #Cuarto punto
        puntoX.append(obj.x + self.obj.largo/2)
        puntoY.append(obj.y - self.obj.ancho/2)
        puntoZ.append(obj.z - self.obj.alto/2)

        # Valido base de apoyo para el objeto en el punto 1
        for i in range(4):
            if self.env.validarBase(int(puntoX[i]), int(puntoY[i]), int(puntoZ[i])) == False:
                return False
        
        return True

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
        #Nueva poblacion
        self.generarPoblacion()

        # Iteramos hasta que se cumpla el numero de intentos
        for i in range(self.maxTryStates):
            new_population = []
            while len(self.population) > 1:
                # Seleccionamos 2 individuos
                ind_1 = random.choice(self.population)
                self.population.remove(ind_1)
                ind_2 = random.choice(self.population)
                self.population.remove(ind_2)

                hijo_1, hijo_2 = self.cruzamiento(ind_1, ind_2)

                # Mutamos el hijo 1
                hijo_1 = self.mutacion(hijo_1)

                # Validamos y guardamos hijo1
                if self.env.validarPosicionVacia(hijo_1):
                    if self.validarPosiciones(hijo_1):
                        # CALCULAR EL FITNESS DEL OBJETO
                        new_population.append(new_obj)

                # Mutamos el hijo 2
                hijo_2 = self.mutacion(hijo_2)

                # Validamos y guardamos hijo2
                if self.env.validarPosicionVacia(hijo_2):
                    if self.validarPosiciones(hijo_2):
                        # CALCULAR EL FITNESS DEL OBJETO
                        new_population.append(new_obj)


                # Guardamos a los padres
                self.population.append(ind_1)
                self.population.append(ind_2)

            # Guardamos si sobro un objeto
            if len(self.population) > 0:
                new_population.append(self.population[0])
                self.population.remove(self.population[0])


                
            # Eliminamos X cantidad de los peores individuos de la nueva poblacion



            # Guardamos al mejor individuo de la nueva poblacion

            self.population = new_population


            