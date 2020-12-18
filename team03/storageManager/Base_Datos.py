class Base_Datos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estructura = None

    def getNombreASCII(self):
        number = 0

        for c in self.nombre:
            number += ord(c)
        
        return number