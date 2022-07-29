from Entorno import Entorno
from Domain.objeto import Objeto
from graficador import Graficador
from AgenteGenetico import AgenteGenetico



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


obje11= Objeto(9,1,0.5,1,1,1,(0,0,0))

obje12= Objeto(0.5,9.5,0.5,1,1,1,(0,0,0))

obje13= Objeto(4,9.5,0.5,1,1,1,(0,0,0))

obje14= Objeto(1,1,2.5,1,1,1,(0,0,0))

obje15= Objeto(5,1,4.5,1,1,1,(0,0,0))

obje16= Objeto(2.5,8,7.5,1,1,1,(0,0,0))

obje17= Objeto(2.5,6.5,7.5,1,1,1,(0,0,0))

obje18= Objeto(1.5,6.5,7.5,1,1,1,(0,0,0))
# #E
# obje5= Objeto(7,4,5.5,1,1,1,(0,0,0))
# #F
# obje6= Objeto(7,8,6.5,1,1,3,(0,0,0))
# #G
# obje7= Objeto(2,4,3.5,1,1,1,(0,0,0))
# #H
# obje8= Objeto(2,7,3.5,1,1,1,(0,0,0))
# #I
# obje9= Objeto(2,6,5.5,2,5,3,(0,0,0))
# #J
# obje10= Objeto(2,4,7.5,1,1,1,(0,0,0))

# #A
# obje1= Objeto(1,1,1,2,2,2,(0,0,0))
# #B
# obje2= Objeto(5,1,2,2,2,4,(0,0,0))
# #C
# obje3= Objeto(2,6,1.5,2,5,3,(0,0,0))
# #D
# obje4= Objeto(7,6,2.5,4,6,5,(0,0,0))
# #E
# obje5= Objeto(7,4,5.5,1,1,1,(0,0,0))
# #F
# obje6= Objeto(7,8,6.5,1,1,3,(0,0,0))
# #G
# obje7= Objeto(2,4,3.5,1,1,1,(0,0,0))
# #H
# obje8= Objeto(2,7,3.5,1,1,1,(0,0,0))
# #I
# obje9= Objeto(2,6,5.5,2,5,3,(0,0,0))
# #J
# obje10= Objeto(2,4,7.5,1,1,1,(0,0,0))


objetos = [obje1, obje2, obje3, obje4, obje5, obje6, obje7, obje8, obje9, obje10]
ent = Entorno()
ent.objetos = objetos
ent.objetosAlEspacio(objetos)

objeto_test = Objeto(6,4,6,1,1,1,(0,0,0))
agente = AgenteGenetico(10, ent, objeto_test)

bestObjeto = agente.startGenetico(objetos)
#print(bestObjeto.x)
#print(bestObjeto.y)
#print(bestObjeto.z)
ent.objetos.append(bestObjeto)
ent.iniciar()
