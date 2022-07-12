from Domain.objeto import Objeto
from graficador import Graficador


graf = Graficador()

#obje = Objeto(3,3,3,2,2,2)
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

graf.graficar(obje1, 'b')
graf.graficar(obje2, 'r')
graf.graficar(obje3, 'g')
graf.graficar(obje4, 'b')
graf.graficar(obje5, 'b')
graf.graficar(obje6, 'b')
graf.graficar(obje7, 'r')
graf.graficar(obje8, 'g')
graf.graficar(obje9, 'b')
graf.graficar(obje10, 'b')
graf.show()