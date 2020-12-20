from storageManager.arbolbplus import ArbolBmas

class Tabla:
    def __init__(self, nombre, columnas):
        self.nombre = nombre
        self.columnas = columnas
        self.estructura = ArbolBmas()

    def getNombreASCII(self):
        number = 0

        for c in self.nombre:
            number += ord(c)
        
        return number