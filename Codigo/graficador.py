from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

class Graficador:
    fig = None
    ax = None
    def __init__(self):
        fig = plt.figure()
        self.ax = fig.add_subplot(111, projection='3d')
        self.ax.set_xlim([0,10])
        self.ax.set_ylim([0,10])
        self.ax.set_zlim([0,10])

    def graficar(self, objeto, color):
       
        for i in range(len(objeto.vecStartX)):
            self.ax.plot([objeto.vecStartX[i], objeto.vecEndX[i]], [objeto.vecStartY[i], objeto.vecEndY[i]],zs = [objeto.vecStartZ[i], objeto.vecEndZ[i]], color = color)

    def show(self):
        plt.show()
   
