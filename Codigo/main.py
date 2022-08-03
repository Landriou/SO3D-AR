from Entorno import Entorno
from Domain.objeto import Objeto
from graficador import Graficador
from AgenteGenetico import AgenteGenetico
from time import time


#A
obje1= Objeto(1,1,1,2,2,2,(0,0,0))
#B
obje2= Objeto(5,1,2,2,2,4,(0,0,0))
#C
obje3= Objeto(2,6,1.5,2,5,3,(0,0,0))
#D
obje4= Objeto(7,6,2.5,4,6,5,(0,0,0))
#E
obje5= Objeto(7,4,5.5,1,1,1,(0,0,0))
#F
obje6= Objeto(7,8,6.5,1,1,3,(0,0,0))
#G
obje7= Objeto(2,4,3.5,1,1,1,(0,0,0))
#H
obje8= Objeto(2,7,3.5,1,1,1,(0,0,0))
#I
obje9= Objeto(2,6,5.5,2,5,3,(0,0,0))
#J
obje10= Objeto(2,4,7.5,1,1,1,(0,0,0))

objetos = [obje1, obje2, obje3, obje4, obje5, obje6, obje7, obje8, obje9, obje10]
ent = Entorno()
ent.objetos = objetos
ent.objetosAlEspacio(objetos)


objeto_test = Objeto(2,4,9,1,1,1,(5,5,5))

agente = AgenteGenetico(256,ent,objeto_test)
start_time = time()
agente.startGenetico()
elapsed_time = time() - start_time
print ("Tiempo de ejecucion: %.10f segundos." % elapsed_time)

# print("HIJOS 1")
# for i in range(len(agente.evolucion_generacional_hijo1)):
#     print()
#     for j in range(len(agente.evolucion_generacional_hijo1[i])):
#         print(round(agente.evolucion_generacional_hijo1[i][j].fitness, 2))

# print()
# print("HIJOS 2")
# for i in range(len(agente.evolucion_generacional_hijo2)):
#     print()
#     for j in range(len(agente.evolucion_generacional_hijo2[i])):
#         print(round(agente.evolucion_generacional_hijo2[i][j].fitness, 2))


# for i in range(len(agente.valores_poblacion_inicial)):
#     print(str(round(agente.valores_poblacion_inicial[i].fitness, 4)).replace(".", ","))

# for i in range(100):
#     agente = AgenteGenetico(8, ent, objeto_test)
#     bestObjeto = agente.startGenetico(objetos)
#     print(str(round(bestObjeto.fitness, 4)).replace(".", ","))


