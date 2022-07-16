from graficador import Graficador
import numpy as np

class Entorno:

    def __init__(self):
        i = 20
        j = 20
        k = 20
        self.espacio = np.zeros((i,j,k))

    def iniciar(self):
        graficador = Graficador()
        for i in range(len(self.objetos)):
            color = 'b' if i % 2 == 0 else 'r'
            graficador.graficar(self.objetos[i], color)
        graficador.show()
        
    def objetosAlEspacio(self, objetos):
        for objeto in objetos:
            self.colocarObjeto(objeto)
           
    def validarPosicionVacia(self, objeto):
        #indice es x(0), y(1) y z(2)
        for i in range(objeto.punto1[0]*2, objeto.punto2[0]*2):
            for j in range(objeto.punto1[1]*2, objeto.punto2[1]*2):
                for k in range(objeto.punto1[2]*2, objeto.punto2[2]*2):
                    if self.espacio[i,j,k] == "1":
                        return False
        return True
                        
    def colocarObjeto(self, objeto):
        #indice es x(0), y(1) y z(2)
         for i in range(objeto.punto1[0]*2, objeto.punto2[0]*2):
                for j in range(objeto.punto1[1]*2, objeto.punto2[1]*2):
                    for k in range(objeto.punto1[2]*2, objeto.punto2[2]*2):
                        self.espacio[i,j,k] = "1"

    def validarBase(self, coordX, coordY, coordZ):
        if coordX < 0 or coordX >= self.i or coordY < 0 or coordY >= self.j or coordZ < 0 or coordZ >= self.k:
            return False
        
        if self.espacio[coordX-1, coordY-1, coordZ-1] == "0":
            return False