class Clave:
    def __init__(self, clave, data):
        self.clave = clave
        self.data = data

class Pagina:
    def __init__(self, contenido = [], paginaSiguiente = None , grado=5):
        self.grado = grado
        self.contenido = contenido
        self.paginaSiguiente = paginaSiguiente
    
    def insertarEnPagina(self,clave, data, pagina = None):
      if self.paginaVacia():
        self.contenido = [None, Clave(clave, data), None]
      elif clave > self.contenido[-2].clave:
        self.contenido += [Clave(clave, data), pagina]
      elif clave < self.contenido[1].clave:
        self.contenido = self.contenido[:1] + [Clave(clave, data), pagina] + self.contenido[1:]
      else:
        i = 1
        while i<len(self.contenido) and clave > self.contenido[i].clave: i += 2
        self.contenido = self.contenido[:i] + [Clave(clave, data), pagina] + self.contenido[:i]
      if len(self.contenido[1::2]) >= self.grado:
        return self.dividir()
      return None, None, False    
          
    def dividir(self):
      #punteros y datas en un mismo arreglo, la mediana es igual al grado para numeros impares
      valorMediana = self.contenido[self.grado]
      nuevaPagina = Pagina(self.contenido[self.grado+1:])
      if self.esHoja():
        nuevaPagina = Pagina([None]+self.contenido[self.grado:])
        nuevaPagina.paginaSiguiente = self.paginaSiguiente
        self.paginaSiguiente = nuevaPagina
      self.contenido = self.contenido[:self.grado]
      return valorMediana, nuevaPagina, True

    def paginaVacia(self):
        return len(self.contenido) == 0

    def esHoja(self):
      esHoja = True
      i = 0      
      while i < len(self.contenido):
        esHoja &= self.contenido[i] == None 
        i += 2 
      return esHoja       

class ArbolBmas:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, data):
        if self.estaVacio():
          self.raiz = Pagina([None, Clave(clave, data), None])
        else:
          valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(clave, data, self.raiz)
          if seDividio:
            self.raiz = Pagina([self.raiz, valorMediana, nuevaPagina])           
    
    def insertarRecursivo(self, clave, data, paginaTemporal):
      if paginaTemporal.esHoja():
        return paginaTemporal.insertarEnPagina(clave, data)
      else:
        if clave > paginaTemporal.contenido[-2].clave:
          valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(clave, data, paginaTemporal.contenido[-1])            
        else:
          i = 1
          while i<len(paginaTemporal.contenido) and clave > paginaTemporal.contenido[i].clave: i += 2
          valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(clave, data, paginaTemporal.contenido[i-1])
        if seDividio:
            return paginaTemporal.insertarEnPagina(valorMediana.clave,valorMediana.data, nuevaPagina)
        else:
            return None, None, False          

    def estaVacio(self):
        return self.raiz == None
    
    def recorrer(self):
      self.recorrerRecursivo(self.raiz, 0)
    
    def recorrerRecursivo(self, pagina, level):
      if not pagina.esHoja():
        for x in pagina.contenido[::2]:
          self.recorrerRecursivo(x, level+1)
      print("Level: "+str(level))
      for x in pagina.contenido[1::2]:
          print(x.data)

def main():
  arbol = ArbolBmas()
  arbol.insertar(13,"13")
  arbol.insertar(12, "12")
  arbol.insertar(11, "11")
  arbol.insertar(10,"10")
  arbol.insertar(9, "9")
  arbol.insertar(8, "8")
  arbol.insertar(7, "7")
  arbol.insertar(6, "6")
  arbol.insertar(5, "5")
  arbol.insertar(4, "4")
  arbol.insertar(3, "3")
  arbol.insertar(2, "2")
  arbol.insertar(1, "1")  
  arbol.recorrer()

if __name__ == "__main__":
    main()