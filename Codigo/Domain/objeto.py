
class Objeto:
    # x,y,z son el centro del objeto
    x = None
    y = None
    z = None
    alto = 0
    ancho = 0
    largo = 0
    fitness = 0
    puntoDado = (0,0,0)

    def __init__(self, x, y, z,largo, ancho, alto, puntoDado):
        self.x = x
        self.y = y
        self.z = z
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
        self.vecStartX = []
        self.vecEndX = []
        
        self.vecStartY = []
        self.vecEndY = []
        
        self.vecStartZ = []
        self.vecEndZ = []
        self.punto1 = ()
        self.punto7 = ()
        self.puntoDado = puntoDado
        
        self.obtenerCoordenadasCompletas()
    
    def obtenerCoordenadasCompletas(self):
        self.vecStartX = []
        self.vecEndX = []
        
        self.vecStartY = []
        self.vecEndY = []
        
        self.vecStartZ = []
        self.vecEndZ = []
        self.punto1 = ()
        self.punto7 = ()

        #Primer punto ()
        punto1X = self.x - self.largo/2
        punto1Y = self.y - self.ancho/2
        punto1Z = self.z - self.alto/2

        #Segundo punto
        punto2X = self.x - self.largo/2
        punto2Y = self.y + self.ancho/2
        punto2Z = self.z - self.alto/2

        #Tercer punto
        punto3X = self.x + self.largo/2
        punto3Y = self.y + self.ancho/2
        punto3Z = self.z - self.alto/2

        #Cuarto punto
        punto4X = self.x + self.largo/2
        punto4Y = self.y - self.ancho/2
        punto4Z = self.z - self.alto/2
        
        #Quinto punto
        punto5X = self.x - self.largo/2
        punto5Y = self.y - self.ancho/2
        punto5Z = self.z + self.alto/2
        
        
        #Sexto punto
        punto6X = self.x - self.largo/2
        punto6Y = self.y + self.ancho/2
        punto6Z = self.z + self.alto/2

        #Septimo punto
        punto7X = self.x + self.largo/2
        punto7Y = self.y + self.ancho/2
        punto7Z = self.z + self.alto/2


        #Octavo punto
        punto8X = self.x + self.largo/2
        punto8Y = self.y - self.ancho/2
        punto8Z = self.z + self.alto/2

        self.punto1 = (punto1X, punto1Y, punto1Z)
        self.punto7 = (punto7X, punto7Y, punto7Z)
        #Vectores
        #Base izquierda
        self.vecStartX.append(punto1X)
        self.vecStartY.append(punto1Y)
        self.vecStartZ.append(punto1Z)
        
        self.vecEndX.append(punto2X)
        self.vecEndY.append(punto2Y)
        self.vecEndZ.append(punto2Z)
        
        
        #Base trasera
        self.vecStartX.append(punto2X)
        self.vecStartY.append(punto2Y)
        self.vecStartZ.append(punto2Z)
        
        self.vecEndX.append(punto3X)
        self.vecEndY.append(punto3Y)
        self.vecEndZ.append(punto3Z)
        
        #Base Derecha
        self.vecStartX.append(punto3X)
        self.vecStartY.append(punto3Y)
        self.vecStartZ.append(punto3Z)
        
        self.vecEndX.append(punto4X)
        self.vecEndY.append(punto4Y)
        self.vecEndZ.append(punto4Z)
        
        #Base Frontal
        self.vecStartX.append(punto4X)
        self.vecStartY.append(punto4Y)
        self.vecStartZ.append(punto4Z)
        
        self.vecEndX.append(punto1X)
        self.vecEndY.append(punto1Y)
        self.vecEndZ.append(punto1Z)
        
        #Columna Frontal Izquierda
        self.vecStartX.append(punto1X)
        self.vecStartY.append(punto1Y)
        self.vecStartZ.append(punto1Z)
        
        self.vecEndX.append(punto5X)
        self.vecEndY.append(punto5Y)
        self.vecEndZ.append(punto5Z)
        
        
        #Columna Frontal Derecha
        self.vecStartX.append(punto4X)
        self.vecStartY.append(punto4Y)
        self.vecStartZ.append(punto4Z)
        
        self.vecEndX.append(punto8X)
        self.vecEndY.append(punto8Y)
        self.vecEndZ.append(punto8Z)
        
        #Columna Trasera Izquierda
        self.vecStartX.append(punto2X)
        self.vecStartY.append(punto2Y)
        self.vecStartZ.append(punto2Z)
        
        self.vecEndX.append(punto6X)
        self.vecEndY.append(punto6Y)
        self.vecEndZ.append(punto6Z)
        
        #Columna Trasera Derecha
        self.vecStartX.append(punto3X)
        self.vecStartY.append(punto3Y)
        self.vecStartZ.append(punto3Z)
        
        self.vecEndX.append(punto7X)
        self.vecEndY.append(punto7Y)
        self.vecEndZ.append(punto7Z)
        
        #Superior Izquierda
        self.vecStartX.append(punto6X)
        self.vecStartY.append(punto6Y)
        self.vecStartZ.append(punto6Z)
        
        self.vecEndX.append(punto5X)
        self.vecEndY.append(punto5Y)
        self.vecEndZ.append(punto5Z)
        
        #Superior Derecha
        self.vecStartX.append(punto7X)
        self.vecStartY.append(punto7Y)
        self.vecStartZ.append(punto7Z)
        
        self.vecEndX.append(punto8X)
        self.vecEndY.append(punto8Y)
        self.vecEndZ.append(punto8Z)
        
        #Superior Trasera
        self.vecStartX.append(punto7X)
        self.vecStartY.append(punto7Y)
        self.vecStartZ.append(punto7Z)
        
        self.vecEndX.append(punto6X)
        self.vecEndY.append(punto6Y)
        self.vecEndZ.append(punto6Z)
        
        #Superior Frontal
        self.vecStartX.append(punto5X)
        self.vecStartY.append(punto5Y)
        self.vecStartZ.append(punto5Z)
        
        self.vecEndX.append(punto8X)
        self.vecEndY.append(punto8Y)
        self.vecEndZ.append(punto8Z)    