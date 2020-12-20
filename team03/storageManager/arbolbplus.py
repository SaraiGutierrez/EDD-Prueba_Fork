import math
import os


class Clave:
    def __init__(self, clave, data):
        self.clave = clave
        self.data = data


class Pagina:
    def __init__(self, contenido=[], paginaSiguiente=None, grado=5):
        self.grado = grado
        self.contenido = contenido
        # contenido -> [apuntador, clave1, apuntador, clave2, apuntador....]
        self.paginaSiguiente = paginaSiguiente

    def insertarEnPagina(self, clave, data, pagina=None):
        if self.paginaVacia():
            #posiciones   [0,    1,     2]
            # contenido -> [none, clave, none]
            self.contenido = [None, Clave(clave, data), None]
        elif clave > self.contenido[-2].clave:  # insertar de ultimo
            #posiciones [-3,   -2,    -1]
            #contenido  [none, clave, none]
            # despues
            ##contenido  [none, clave, none, clav2, none]
            self.contenido += [Clave(clave, data), pagina]
        elif clave < self.contenido[1].clave:  # insertar al principio
            #posiciones   [0,    1,     2,    3,      4,    5,      6]
            # contenido -> [none, clave, none, Clave2, none, clave3, none]
            #              [:1]  + ClaveNueva, none + clave, none, Clave2, none, clave3, none
           # contenido -> [none,                      clave, none, Clave2, none, clave3, none]
            self.contenido = self.contenido[:1] + \
                [Clave(clave, data), pagina] + self.contenido[1:]
        else:  # Insertar en medio
            i = 1
            while i < len(self.contenido) and clave > self.contenido[i].clave:
                i += 2
            self.contenido = self.contenido[:i] + \
                [Clave(clave, data), pagina] + self.contenido[i:]
        if len(self.contenido[1::2]) >= self.grado:
            return self.dividir()
        return None, None, False

    def dividir(self):

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



    # paginaPadre => pagina anterior
    # pagina => pagina actual
    def eliminar(self, clave, paginaPadre=None, pagina=None):
        # [apuntador, 5, apuntador, 10, apuntador, 20, apuntador]
        print('clave: '+str(clave) + ' pag.clave: '+str(pagina.contenido[-2].clave))
        if clave > pagina.contenido[-2].clave:  # apuntador derecha
            if not pagina.esHoja():
                # Pagina intermedia
                esHoja = self.eliminar(clave, pagina, pagina.contenido[-1])  # R
                der = pagina.contenido[-1]
                izq = pagina.contenido[-3]
                if len(der.contenido[1::2]) < 2:
                  if esHoja:
                      if len(izq.contenido[1::2]) >= 3: #********************* Probando...
                          der.contenido = [None, izq.contenido[-2]] + der.contenido
                          izq.contenido = izq.contenido[:-2]
                          pagina.contenido = pagina.contenido[:-2] + [der.contenido[1]] + pagina.contenido[-1:]
                      else:
                        izq.contenido = izq.contenido + [der.contenido[1], None] # Modificado
                        pagina.contenido = pagina.contenido[:-2]
                  else:
                    if len(izq.contenido[1::2]) >= 3: # no hay espacio en la izquierda
                        der.contenido =  [izq.contenido[-1]] + [pagina.contenido[-2]] + der.contenido
                        pagina.contenido = pagina.contenido[:-2] + [izq.contenido[-2]] + pagina.contenido[-1:]
                        izq.contenido = izq.contenido[:-2]
                    else:
                      izq.contenido = izq.contenido + [pagina.contenido[- 2]] + der.contenido
                      pagina.contenido = pagina.contenido[:-2]
                return False
            else:
                # Hoja
                # No Existe el valor
                return False
        elif pagina.contenido[-2].clave == clave:
            if not pagina.esHoja():
                # Pagina intermedia
                esHoja = self.eliminar(clave, pagina, pagina.contenido[-1])  # R
                der = pagina.contenido[-1]
                izq = pagina.contenido[-3]
                if len(der.contenido[1::2]) < 2:
                  if esHoja:
                      if len(izq.contenido[1::2]) >= 3: #********************* Probando...
                          der.contenido = [None, izq.contenido[-2]] + der.contenido
                          izq.contenido = izq.contenido[:-2]
                          pagina.contenido = pagina.contenido[:-2] + [der.contenido[1]] + pagina.contenido[-1:]
                      else:
                        izq.contenido = izq.contenido + [der.contenido[1], None] # Modificado
                        pagina.contenido = pagina.contenido[:-2]
                  else:
                    if len(izq.contenido[1::2]) >= 3: # no hay espacio en la izquierda
                        der.contenido = [izq.contenido[-1]] + [der.contenido[0].contenido[1]] + der.contenido 
                        pagina.contenido = pagina.contenido[:-2] + [izq.contenido[-2]] + pagina.contenido[-1:]
                        izq.contenido = izq.contenido[:-2]
                    else:
                        izq.contenido = izq.contenido + [der.contenido[0].contenido[1]] + der.contenido
                        pagina.contenido = pagina.contenido[:-2]
                else:
                    if esHoja:
                        pagina.contenido = pagina.contenido[:-2] + [der.contenido[1]] + pagina.contenido[-1:]
                    else:
                        tmp = pagina.contenido[-1]
                        ant = tmp
                        while tmp != None:
                            ant = tmp
                            tmp = tmp.contenido[0]
                        pagina.contenido = pagina.contenido[:-2] + [ant.contenido[1]] + pagina.contenido[-1:]
                return False
            else:
                # Hoja
                pagina.contenido = pagina.contenido[:-2]  # Eliminó
                return True
#=================================================================================================================                
        else:
            indice = 1
            for x in pagina.contenido[1::2]:
                if clave < x.clave:  # apuntador izq
                    if not self.esHoja():
                        # Pagina intemedia
                        esHoja = self.eliminar(clave, pagina, pagina.contenido[indice - 1])  # R
                        
                        # |izq | 10 | der | 12 | |
                        izq = pagina.contenido[indice - 1]
                        der = pagina.contenido[indice + 1]
                        if len(izq.contenido[1::2]) < 2:
                            # || 8 || 10 || 11 ||
                            if esHoja:
                                if indice == 1:
                                    if len(der.contenido[1::2]) >= 3: #******************** Probando
                                        izq.contenido = izq.contenido + [der.contenido[1], None]
                                        der.contenido = der.contenido[2:]
                                        pagina.contenido = pagina.contenido[:1] + [der.contenido[1]] + pagina.contenido[2:]
                                    else:
                                        der.contenido = izq.contenido[:2] + der.contenido
                                        pagina.contenido = pagina.contenido[indice+1:]
                                else:
                                    if len(der.contenido[1::2]) >= 3: #******************** Probando
                                        izq.contenido = izq.contenido + [der.contenido[1], None]
                                        der.contenido = [None] + der.contenido[3:]
                                        pagina.contenido = pagina.contenido[:indice-2] + [izq.contenido[1], pagina.contenido[indice - 1], der.contenido[1]] + pagina.contenido[indice+1:]
                                    else:
                                        izq2 = pagina.contenido[indice - 3]
                                        izq2.contenido = izq2.contenido +  [izq.contenido[1], None] # Modificado
                                        pagina.contenido = [izq2] + pagina.contenido[indice:]
                            else:
                                if indice == 1:
                                    if len(der.contenido[1::2]) >= 3: # no hay espacio en la derecha
                                        izq.contenido = izq.contenido + [pagina.contenido[indice]] + [der.contenido[0]]
                                        pagina.contenido = pagina.contenido[:indice] + [der.contenido[1]] + pagina.contenido[indice+1:]
                                        der.contenido = der.contenido[2:]
                                    else:
                                        der.contenido = izq.contenido + [pagina.contenido[1]] + der.contenido
                                        pagina.contenido = pagina.contenido[indice+1:]
                                else:
                                    if len(der.contenido[1::2]) >= 3: # no hay espacio en la derecha
                                        izq.contenido = izq.contenido + [pagina.contenido[indice]] + [der.contenido[0]]
                                        pagina.contenido = pagina.contenido[:indice] + [der.contenido[1]] + pagina.contenido[indice+1:]
                                        der.contenido = der.contenido[2:]
                                    else:
                                        izq2 = pagina.contenido[indice - 3]
                                        izq2.contenido = izq2.contenido + [pagina.contenido[indice - 2]] + izq.contenido
                                        pagina.contenido = pagina.contenido[:indice - 2] + pagina.contenido[indice:]
                        return False
                    else:
                        # Hoja
                        # No Existe el valor
                        return False
                elif clave == x.clave:  # apuntador der
                    if not pagina.esHoja():
                        # Pagina intemedia
                        print('Pagina intermedia')
                        esHoja = self.eliminar(clave, pagina, pagina.contenido[indice + 1])  # R
                        der = pagina.contenido[indice + 1]
                        izq = pagina.contenido[indice - 1]
                        if len(der.contenido[1::2]) < 2:
                          if esHoja:
                            der2 = pagina.contenido[indice + 3]
                            if len(der2.contenido[1::2]) >= 3:
                                der.contenido = der.contenido + [der2.contenido[1], None]
                                der2.contenido = der2.contenido[2:]
                                pagina.contenido = pagina.contenido[:indice] + [der.contenido[1], pagina.contenido[indice+1], der2.contenido[1]] + pagina.contenido[indice+3:]
                            else:
                                izq.contenido = izq.contenido + [der.contenido[1], None] # Modificado
                                pagina.contenido = pagina.contenido[:indice] + pagina.contenido[indice+2:]
                          else:
                            if len(izq.contenido[1::2]) >= 3: # no hay espacio en la izquierda
                                der.contenido = [izq.contenido[-1]] + [der.contenido[0].contenido[1]] + der.contenido 
                                pagina.contenido = pagina.contenido[:indice] + [izq.contenido[-2]] + pagina.contenido[indice+1:]
                                izq.contenido = izq.contenido[:-2]
                            else:
                                izq.contenido = izq.contenido + [der.contenido[0].contenido[1]] + der.contenido
                                pagina.contenido = pagina.contenido[:indice] + pagina.contenido[indice+2:]
                        else:
                            if esHoja:
                                pagina.contenido = pagina.contenido[:indice] + [der.contenido[1]] + pagina.contenido[indice + 1:]
                            else:
                                tmp = pagina.contenido[indice + 1]
                                ant = tmp
                                while tmp != None:
                                    ant = tmp
                                    tmp = tmp.contenido[0]
                                pagina.contenido = pagina.contenido[:indice] + [ant.contenido[1]] + pagina.contenido[indice + 1:]
                        return False
                    else:
                        # Hoja
                        pagina.contenido = pagina.contenido[:indice] + pagina.contenido[indice+2:] # Eliminó
                        return True
                indice += 2
        return False






class ArbolBmas:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, data):
        if self.estaVacio():
            self.raiz = Pagina([None, Clave(clave, data), None])
        else:
            valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(
                clave, data, self.raiz)
            if seDividio:
                self.raiz = Pagina([self.raiz, valorMediana, nuevaPagina])

    def insertarRecursivo(self, clave, data, paginaTemporal):
        if paginaTemporal.esHoja():
            return paginaTemporal.insertarEnPagina(clave, data)
        else:
            if clave > paginaTemporal.contenido[-2].clave:
                valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(
                    clave, data, paginaTemporal.contenido[-1])
            else:
                i = 1
                while i < len(paginaTemporal.contenido) and clave > paginaTemporal.contenido[i].clave:
                    i += 2
                valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(
                    clave, data, paginaTemporal.contenido[i-1])
            if seDividio:
                return paginaTemporal.insertarEnPagina(valorMediana.clave, valorMediana.data, nuevaPagina)
            else:
                return None, None, False

                #[apuntador, Clave, Apuntador]

    def estaVacio(self):
        return self.raiz == None

    def recorrer(self):
        self.recorrerRecursivo(self.raiz, 0)

    def recorrerRecursivo(self, pagina, level):
        if not pagina.esHoja():
            # [puntero, clave, puntero, clave2, puntero, clave3]
            for x in pagina.contenido[::2]:
                self.recorrerRecursivo(x, level+1)
        print("Level: "+str(level))
        for x in pagina.contenido[1::2]:
            print(x.data)

    def imprimirLista(self, pagina):
        if pagina.esHoja():
            aux = pagina
            i = 0
            while aux:
                print("Pagina: " + str(i))
                for x in aux.contenido[1::2]:
                    print(x.data)
                aux = aux.paginaSiguiente
                i += 1
        else:
            self.imprimirLista(pagina.contenido[0])

    # contador de F = level + 1
    def graphviz(self):
        archivo = open('archivo.dot', 'w', encoding='utf-8')
        archivo.write('digraph structs {\n')
        archivo.write('node [shape=record];\n')
        self.contPag = 0
        self.graficarEncabezado(self.raiz, 0, archivo)
        self.contPag = 0
        self.graficarEnlace(self.raiz, 0, archivo, None)
        archivo.write('}\n')
        archivo.close()
        os.system('dot -Tpng archivo.dot -o salida.png')
        os.system('salida.png')

    def graficarEncabezado(self, pagina, level, archivo):
        f = ''
        for x in range(level + 1):
            f += 'f'

        archivo.write('pagina{0} [label="'.format(self.contPag))
        self.contPag += 1

        pos = 0  # posicion actual del arreglo
        bandera = True
        for x in pagina.contenido[::1]:
            if bandera:
                # puntero
                archivo.write('<{0}{1}> '.format(f, pos))
            else:
                # clave
                archivo.write('|<{0}{1}> {2} |'.format(f, pos, x.data))
            bandera = not bandera
            pos += 1
        archivo.write('"];\n')

        if not pagina.esHoja():
            for x in pagina.contenido[::2]:
                self.graficarEncabezado(x, level+1, archivo)

    def graficarEnlace(self, pagina, level, archivo, padre):
        f = ''
        for x in range(level + 1):
            f += 'f'

        if not (padre is None):
            self.contPag += 1
            archivo.write('{0} -> pagina{1};\n'.format(padre, self.contPag))

        pos = 0  # posicion actual del arreglo
        bandera = True
        nombre = 'pagina' + str(self.contPag)
        for x in pagina.contenido[::1]:  # pagina0
            if bandera:
                # puntero
                if not pagina.esHoja():
                    # no es Hoja
                    self.graficarEnlace(x, level+1, archivo,
                                        '{0}:{1}{2}'.format(nombre, f, pos))
            bandera = not bandera
            pos += 1

    def eliminar(self, clave):
        esHoja = self.raiz.eliminar(clave, None, self.raiz)
        print('fin eliminacion')


def main():
    arbol = ArbolBmas()

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]:
        arbol.insertar(i, str(i))
        
    arbol.eliminar(13)
    arbol.eliminar(19)
    arbol.recorrer()
    arbol.imprimirLista(arbol.raiz)
    arbol.graphviz()


if __name__ == "__main__":
    main()
