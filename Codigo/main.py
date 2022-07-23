from Entorno import Entorno
from Domain.objeto import Objeto
from graficador import Graficador
from AgenteGenetico import AgenteGenetico



#A
obje1= Objeto(1,1,1,2,2,2)
#B
obje2= Objeto(5,1,1,2,2,5)
#C
obje3= Objeto(2,6,1.5,2,5,3)
#D
obje4= Objeto(7,6,2.5,4,6,5)
#E
obje5= Objeto(7,4,5.5,1,1,1)
#F
obje6= Objeto(7,8,6.5,1,1,3)
#G
obje7= Objeto(2,4,3.5,1,1,1)
#H
obje8= Objeto(2,7,3.5,1,1,1)
#I
obje9= Objeto(2,6,5.5,2,5,3)
#J
obje10= Objeto(2,4,7.5,1,1,1)


objetos = [obje1, obje2, obje3, obje4, obje5, obje6, obje7, obje8, obje9, obje10]
ent = Entorno()
ent.objetos = objetos
# ent.iniciar()

objeto_test = Objeto(1,1,1,2,2,2)
objeto_test1 = Objeto(5,10,15,2,2,2)
objeto_test2 = Objeto(2,4,6,2,2,2)
agente = AgenteGenetico(10, ent, objeto_test)
ind1, ind2 = agente.cruzamiento(objeto_test1, objeto_test2)
print()
print(ind1.x)
print(ind1.y)
print(ind1.z)
print()
print(ind2.x)
print(ind2.y)
print(ind2.z)
