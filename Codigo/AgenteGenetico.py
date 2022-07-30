import random
from Domain.objeto import Objeto
import copy


class AgenteGenetico:
     
    def __init__(self, maxTryStates, env, obj):
        self.maxTryStates = maxTryStates
        self.env = env
        self.envMaximoLocal = None
        self.obj = obj
        self.bestOption = None
        
    #En base a un objeto, genera muchos posibles entornos
    def generarPoblacion(self, objetos):
        self.poblacion_inicial = 50
        population = []

        lista = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9]
        # posibles_z = []
        # for i in range(len(objetos)):
        #     val = objetos[i].z + objetos[i].alto/2
        #     posibles_z.append(val)

        valores_validos = []
        while len(population) < self.poblacion_inicial:
            rand_i = random.choice(lista)
            rand_j = random.choice(lista)
            rand_k = random.choice(lista)
            new_obj = Objeto(rand_i, rand_j, rand_k, self.obj.largo, self.obj.ancho, self.obj.alto, self.obj.puntoDado)

            if ((rand_i - self.obj.largo/2) >= 0) and ((rand_i + self.obj.largo/2) < self.env.i):
                if ((rand_j - self.obj.ancho/2) >= 0) and ((rand_j + self.obj.ancho/2) < self.env.j):
                    if ((rand_k - self.obj.alto/2) >= 0) and ((rand_k + self.obj.alto/2) < self.env.k):
                        if self.validarPosiciones(new_obj):
                            if self.env.validarPosicionVacia(new_obj):
                                new_obj.fitness = self.calcularFitness(new_obj)
                                population.append(new_obj)
                                print()
                                print("----------------------------------------------------")
                                print(new_obj.fitnessDistancia)
                                print(new_obj.superficieFitness)
                                print(new_obj.fitnessDistanciaSuperior)
                                print(new_obj.fitnessdistanciaPuntoDado)
                                print(new_obj.fitness)
                                print()
        
        self.population = population


        


        
    # Valida que una posicion de un objeto no interfiere con los demas objetos
    # - El objeto debe estar sobre una superficie
    # - La superficie debe ser mayor o igual a las dimensiones de la base del objeto
    def validarPosiciones(self, obj):
        puntoX = []
        puntoY = []
        puntoZ = []

        if self.env.espacio[int(obj.x*2)][int(obj.y*2)][int(obj.z*2)] == 1:
            return False

        #Primer punto 
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
            if self.env.validarBase(puntoX[i], puntoY[i], puntoZ[i]) == False:
                return False
        
        return True

    # Calcula el fitness de un entorno en particular
    def calcularFitness(self, obj):

        # Calcular la fitness en base a la distancia horizontal de otros objetos
        # Mientras mas distancia tenga de otros objetos mejor 
        coordenadaZ = int(obj.z*2)
        menorDistancia = 1000000
        for i in range(len(self.env.espacio)):
            for j in range(len(self.env.espacio[i])):
                if self.env.espacio[i][j][coordenadaZ] == 1:
                    distancia = self.distancia(obj.x*2, obj.y*2, obj.z*2, i, j, coordenadaZ)
                    if distancia < menorDistancia:
                        menorDistancia = distancia
                        
        fitnessDistancia = menorDistancia*100/20
        obj.fitnessDistancia = fitnessDistancia
        # Calcular la fitness en base a la dimension de la superficie donde esta apoyado
        # Mientras mas grande la superficie donde este apoyado mejor
        superficieEncontrada = 0                
        for k in range(int(obj.z*2), -1, -1):
            if self.env.espacio[int(obj.x*2)][int(obj.y*2)][k] == 1:
                superficieEncontrada = k
                break
        
        contadorXSuperior = 0
        for u in range(int(obj.x*2),len(self.env.espacio)):
                contadorXSuperior = contadorXSuperior + 1
                if self.env.espacio[u][int(obj.y*2)][superficieEncontrada] != 1:
                    break
            
        contadorXInferior = 0
        for o in range(int(obj.x*2), -1, -1):
            contadorXInferior = contadorXInferior + 1
            if self.env.espacio[o][int(obj.y*2)][superficieEncontrada] != 1:
                break
                
        contadorYSuperior = 0
        for p in range(int(obj.y*2), len(self.env.espacio)):
            contadorYSuperior = contadorYSuperior + 1
            if self.env.espacio[int(obj.x*2)][p][superficieEncontrada] != 1:
                break

        contadorYInferior = 0
        for r in range(int(obj.y*2), -1, -1):
            contadorYInferior = contadorYInferior + 1
            if self.env.espacio[int(obj.x*2)][r][superficieEncontrada] != 1:
                break

        superficie = contadorXSuperior + contadorXInferior + contadorYSuperior + contadorYInferior
        
        superficieFitness = superficie*100/40
        obj.superficieFitness = superficieFitness
        # Calcular la fitness en base a la distancia vertical de otros objeto
        #  Mientras mas distancia haya frente a otro objeto desde arriba mejor
        
        coordenadaX = int(obj.x*2)
        menorDistanciaSuperior = 10000000000
        for q in range(len(self.env.espacio)):
            for w in range(len(self.env.espacio[i])):
                if self.env.espacio[coordenadaX][q][w] == 1:
                    distancia = self.distancia(obj.x*2, obj.y*2, obj.z*2, coordenadaX, q, w)
                    if distancia < menorDistanciaSuperior:
                        menorDistanciaSuperior = distancia
        
        fitnessDistanciaSuperior = menorDistanciaSuperior*100/20  
        obj.fitnessDistanciaSuperior = fitnessDistanciaSuperior          
             
        #Distancia hasta el techo

        # distanciaHastaElTecho = self.distancia(obj.x*2, obj.y*2, obj.z*2,obj.x*2, obj.y*2, 19)
        # distanciaHastaElTechoFitness = distanciaHastaElTecho*100/30
        # obj.distanciaHastaElTechoFitness = distanciaHastaElTechoFitness
      
        
        # Calcular la fitness en base a la distancia del punto dado.
        # Mientras mas cercano este al punto dado mejor
        distanciaPuntoDado = self.distancia(obj.x*2, obj.y*2, obj.z*2, obj.puntoDado[0],obj.puntoDado[1] ,obj.puntoDado[2] )
        fitnessdistanciaPuntoDado = distanciaPuntoDado*100/40
        obj.fitnessdistanciaPuntoDado = fitnessdistanciaPuntoDado
        
        return fitnessDistancia + superficieFitness + fitnessDistanciaSuperior - fitnessdistanciaPuntoDado 
        
        

        
    # una funcion que calcula la distancia entre 2 puntos
    def distancia(self, x1, y1, z1, x2, y2, z2):
        return ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**0.5
    
    
       
    # Cruza 2 objetos y devuelve ambos para despues quedarme con los mejores resultados
    def cruzamiento(self, ind_1, ind_2):
        posibilidades = ["x", "y", "z"]

        new_ind_1 = Objeto(ind_1.x, ind_1.y, ind_1.z, self.obj.largo, self.obj.ancho, self.obj.alto, self.obj.puntoDado)
        new_ind_2 = Objeto(ind_2.x, ind_2.y, ind_2.z, self.obj.largo, self.obj.ancho, self.obj.alto, self.obj.puntoDado)
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
            lista = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9]
            value = random.choice(posibilidades)
            if value == "x":
                obj.x = random.choice(lista)
            elif value == "y":
                obj.y = random.choice(lista)
            elif value == "z":
                obj.z = random.choice(lista)

        return obj
        
        
    # Resuelve toda la logica del algoritmo genetico, aca deberia ir todo el codigo llamadp
    def startGenetico(self, objetos):
        #Nueva poblacion
        self.generarPoblacion(objetos)
        
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
                        hijo_1.fitness = self.calcularFitness(hijo_1)
                        hijo_1.obtenerCoordenadasCompletas()
                        new_population.append(hijo_1)

                # Mutamos el hijo 2
                hijo_2 = self.mutacion(hijo_2)

                # Validamos y guardamos hijo2
                if self.env.validarPosicionVacia(hijo_2):
                    if self.validarPosiciones(hijo_2):
                        hijo_2.fitness = self.calcularFitness(hijo_2)
                        hijo_2.obtenerCoordenadasCompletas()
                        new_population.append(hijo_2)


                # Guardamos a los padres
                new_population.append(ind_1)
                new_population.append(ind_2)

            # Guardamos si sobro un objeto
            if len(self.population) > 0:
                new_population.append(self.population[0])
                self.population.remove(self.population[0])



            # Eliminamos X cantidad de los peores individuos de la nueva poblacion
            new_population = self.matarALosIncorrectos(new_population)
            new_population = self.matarALosPeores(new_population)


            # Guardamos al mejor individuo de la nueva poblacion
            if self.bestOption != None:
                if new_population[0].fitness > self.bestOption.fitness:
                    self.bestOption = new_population[0]
            else:
                self.bestOption = new_population[0]
            self.population = new_population
        return self.bestOption
            
    def matarALosPeores(self, population):
        population.sort(key=lambda x: x.fitness, reverse=True)
        return population[:self.poblacion_inicial]
        

    def matarALosIncorrectos(self, new_population):
        valid_population = []
        for i in range(len(new_population)):
            if self.validarPosiciones(new_population[i]) and self.env.validarPosicionVacia(new_population[i]):
                valid_population.append(new_population[i])
        return valid_population

                