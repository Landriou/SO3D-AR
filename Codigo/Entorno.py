from graficador import Graficador
import numpy as np

class Entorno:
    espacio = None
    objetos = None
    i = 0
    j = 0
    k = 0

    def __init__(self):
        self.i = 20
        self.j = 20
        self.k = 20
        self.espacio = np.zeros((self.i,self.j,self.k))


    def iniciar(self):
        graficador = Graficador()
        for i in range(len(self.objetos)):
            color = 'b' if i % 2 == 0 else 'r'
            if i == len(self.objetos) - 1:
                color = 'g'
            graficador.graficar(self.objetos[i], color)
        graficador.show()
        
    def objetosAlEspacio(self, objetos):
        for objeto in objetos:
            self.colocarObjeto(objeto)
           
    def validarPosicionVacia(self, objeto):
        #indice es x(0), y(1) y z(2)
        for i in range(int(objeto.punto1[0]*2), int(objeto.punto7[0]*2) ):
            for j in range(int(objeto.punto1[1]*2), int(objeto.punto7[1]*2)):
                for k in range(int(objeto.punto1[2]*2), int(objeto.punto7[2]*2)):
                    if self.espacio[i,j,k] == 1:
                        return False
        return True
                        
    def colocarObjeto(self, objeto):
        #indice es x(0), y(1) y z(2)
         for i in range(int(objeto.punto1[0]*2), int(objeto.punto7[0]*2)):
                for j in range(int(objeto.punto1[1]*2), int(objeto.punto7[1]*2)):
                    for k in range(int(objeto.punto1[2]*2), int(objeto.punto7[2]*2)):
                        self.espacio[i,j,k] = 1

    def validarBase(self, coordX, coordY, coordZ):
        if ((coordX * 2) >= 0) and ((coordX * 2) < self.i):
            if ((coordY * 2) >= 0) and ((coordY * 2) < self.j):
                if ((coordZ * 2) >= 0) and ((coordZ * 2) < self.k):
                    
                    if self.espacio[int((coordX*2)), int((coordY*2)), int((coordZ*2))-1] == 1:
                        if self.espacio[int((coordX*2)), int((coordY*2)), int((coordZ*2))] != 1:
                            return True
        
        return False