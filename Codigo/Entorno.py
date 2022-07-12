from graficador import Graficador


class Entorno:
    def __init__(self, objetos):
        self.objetos = objetos
        

    def iniciar(self):
        graficador = Graficador()
        for i in range(len(self.objetos)):
            color = 'b' if i % 2 == 0 else 'r'
            graficador.graficar(self.objetos[i], color)
        graficador.show()