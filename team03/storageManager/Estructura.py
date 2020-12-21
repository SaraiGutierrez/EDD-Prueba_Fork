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
        if paginaPadre == None:
            self.seElimino = False
        
        # [apuntador, 5, apuntador, 10, apuntador, 20, apuntador]
        if clave > pagina.contenido[-2].clave:  # apuntador derecha
            if not pagina.esHoja():
                # Pagina intermedia
                self.seElimino, esHoja = self.eliminar(clave, pagina, pagina.contenido[-1])  # R
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
                return self.seElimino, False
            else:
                # Hoja
                # No Existe el valor
                return self.seElimino, False
        elif pagina.contenido[-2].clave == clave:
            self.seElimino = True
            if not pagina.esHoja():
                # Pagina intermedia
                self.seElimino, esHoja = self.eliminar(clave, pagina, pagina.contenido[-1])  # R
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
                        print('falta el codigo en esta parte')
                        tmp = pagina.contenido[-1]
                        ant = tmp
                        while tmp != None:
                            ant = tmp
                            tmp = tmp.contenido[0]
                        pagina.contenido = pagina.contenido[:-2] + [ant.contenido[1]] + pagina.contenido[-1:]
                return self.seElimino, False
            else:
                # Hoja
                pagina.contenido = pagina.contenido[:-2]  # Eliminó
                return self.seElimino, True
#=================================================================================================================                
        else:
            indice = 1
            for x in pagina.contenido[1::2]:
                if clave < x.clave:  # apuntador izq
                    if not self.esHoja():
                        # Pagina intemedia
                        
                        self.seElimino, esHoja = self.eliminar(clave, pagina, pagina.contenido[indice - 1])  # R
                        
                        # |izq | 10 | der | 12 | |
                        izq = pagina.contenido[indice - 1]
                        der = pagina.contenido[indice + 1]
                        if len(izq.contenido[1::2]) < 2:
                            # || 8 || 10 || 11 ||
                            if esHoja:
                                if indice == 1:
                                    if len(der.contenido[1::2]) >= 3: # no hay espacio en la derecha (hoja)
                                        izq.contenido = izq.contenido + [der.contenido[1], None]
                                        der.contenido = der.contenido[2:]
                                        pagina.contenido = pagina.contenido[:1] + [der.contenido[1]] + pagina.contenido[2:]
                                    else:
                                        der.contenido = izq.contenido[:2] + der.contenido
                                        pagina.contenido = pagina.contenido[indice+1:]
                                else:
                                    izq2 = pagina.contenido[indice - 3]
                                    if len(der.contenido[1::2]) >= 3: # no hay espacio en la derecha (hoja)
                                        izq.contenido = izq.contenido + [der.contenido[1], None]
                                        der.contenido = [None] + der.contenido[3:]
                                        pagina.contenido = pagina.contenido[:indice-2] + [izq.contenido[1], pagina.contenido[indice - 1], der.contenido[1]] + pagina.contenido[indice+1:]
                                    elif len(izq.contenido[1::2]) >= 3: # no hay espacio en la izquierda (hoja) **
                                        izq.contenido = [None, izq2.contenido[-2]] + izq.contenido
                                        izq2.contenido = izq2.contenido[:-2]
                                        pagina.contenido = pagina.contenido[:indice-2] + [izq.contenido[1]] + pagina.contenido[indice-1:]
                                    else:
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
                                    izq2 = pagina.contenido[indice - 3]
                                    if len(der.contenido[1::2]) >= 3: # no hay espacio en la derecha
                                        izq.contenido = izq.contenido + [pagina.contenido[indice]] + [der.contenido[0]]
                                        pagina.contenido = pagina.contenido[:indice] + [der.contenido[1]] + pagina.contenido[indice+1:]
                                        der.contenido = der.contenido[2:]
                                    elif len(izq2.contenido[1::2]) >= 3: # no hay espacio en la izquierda
                                        izq.contenido = [izq2.contenido[-1]] + [pagina.contenido[indice-2]] +  izq.contenido
                                        pagina.contenido = pagina.contenido[:indice-2] + [izq2.contenido[-2]] + pagina.contenido[indice-1:]
                                        izq2.contenido = izq2.contenido[:-2]
                                    else: # si hay espacio en la izq
                                        izq2.contenido = izq2.contenido + [pagina.contenido[indice - 2]] + izq.contenido
                                        pagina.contenido = pagina.contenido[:indice - 2] + pagina.contenido[indice:]
                        return self.seElimino, False
                    else:
                        # Hoja
                        # No Existe el valor
                        return self.seElimino, False
                elif clave == x.clave:  # apuntador der
                    self.seElimino = True
                    if not pagina.esHoja():
                        # Pagina intemedia
                        self.seElimino, esHoja = self.eliminar(clave, pagina, pagina.contenido[indice + 1])  # R
                        der = pagina.contenido[indice + 1]
                        izq = pagina.contenido[indice - 1]
                        if len(der.contenido[1::2]) < 2:
                          if esHoja:
                            der2 = pagina.contenido[indice + 3] 
                            if len(der2.contenido[1::2]) >= 3: # no hay espacio en la derecha (hoja)
                                der.contenido = der.contenido + [der2.contenido[1], None]
                                der2.contenido = der2.contenido[2:]
                                pagina.contenido = pagina.contenido[:indice] + [der.contenido[1], pagina.contenido[indice+1], der2.contenido[1]] + pagina.contenido[indice+3:]
                            elif len(izq.contenido[1::2]) >= 3: # no hay espacio en la izquierda (hoja) **
                                der.contenido = [None, izq.contenido[-2]] + der.contenido
                                izq.contenido = izq.contenido[:-2]
                                pagina.contenido = pagina.contenido[:indice] + [der.contenido[1]] + pagina.contenido[indice+1:]
                            else:
                                izq.contenido = izq.contenido + [der.contenido[1], None] # Modificado
                                pagina.contenido = pagina.contenido[:indice] + pagina.contenido[indice+2:]
                          else:
                            der2 = pagina.contenido[indice + 3]
                            if len(der2.contenido[1::2]) >= 3:
                                #**********************************
                                tmp = pagina.contenido[indice + 1]
                                ant = tmp
                                while tmp != None:
                                    ant = tmp
                                    tmp = tmp.contenido[0]

                                tmp1 = pagina.contenido[indice + 3]
                                ant1 = tmp1
                                while tmp1 != None:
                                    ant1 = tmp1
                                    tmp1 = tmp1.contenido[0]
                                #**********************************
                                der.contenido = der.contenido + [ant1.contenido[1]] + [der2.contenido[0]]
                                pagina.contenido = pagina.contenido[:indice] + [ant.contenido[1], pagina.contenido[indice + 1], der2.contenido[1]] + pagina.contenido[indice+3:]
                                der2.contenido = der2.contenido[2:]
                            elif len(izq.contenido[1::2]) >= 3: # no hay espacio en la izquierda
                                #**********************************
                                tmp = pagina.contenido[indice + 1]
                                ant = tmp
                                while tmp != None:
                                    ant = tmp
                                    tmp = tmp.contenido[0]
                                #**********************************
                                der.contenido = [izq.contenido[-1]] + [ant.contenido[1]] + der.contenido 
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
                        return self.seElimino, False
                    else:
                        # Hoja
                        pagina.contenido = pagina.contenido[:indice] + pagina.contenido[indice+2:] # Eliminó
                        return self.seElimino, True
                indice += 2
        return self.seElimino, False

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
        self.hojas = []
        archivo = open('archivo.dot', 'w', encoding='utf-8')
        archivo.write('digraph structs {\n')
        archivo.write('node [shape=record];\n')
        self.contPag = 0
        self.graficarEncabezado(self.raiz, 0, archivo)
        self.contPag = 0
        self.graficarEnlace(self.raiz, 0, archivo, None)
        tmp = self.hojas[0]
        ant = tmp
        for x in self.hojas[1::1]:
            ant = tmp
            tmp = x
            archivo.write('{0} -> {1};\n'.format(ant, tmp))
        archivo.write('{rank=same; ')
        for x in self.hojas[::1]: archivo.write('{0}; '.format(x))
        archivo.write('}\n}\n')
        archivo.close()
        os.system('dot -Tpng archivo.dot -o salida.png')
        os.system('salida.png')

    def graficarEncabezado(self, pagina, level, archivo):
        f = ''
        for x in range(level + 1):
            f += 'f'

        nombre = 'pagina{0}'.format(self.contPag)
        archivo.write('{0} [label="'.format(nombre))
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
        else:
            self.hojas += [nombre]

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
        seElimino, esHoja = self.raiz.eliminar(clave, None, self.raiz)
        if seElimino == True:
            print(str(clave) + ' eliminado.')
        else:
            print('Error: La clave ' + str(clave) + ' no se eliminó.')
        return seElimino

    def truncateRoot(self):
        self.raiz = None




      
################################################################################################################
################################################################################################################

    #METODO DE BUSQUEDA DENTRO DEL ARBOL  ---------------------------------------------------------
    def Busqueda(self,valor) ->list:
        val = []
        self._Busqueda(self.raiz,valor, val)
        return val
    
    def _Busqueda(self, pagina,valor,val) -> list:
        #ES LA ULTIMA PAGINA 
       
        if self.VerHoja(pagina):
            for val in pagina.contenido[1::2]:
                if val.clave ==valor:
                    print("valor encontrado :", val.data)
                    val = val.data
                    break
            return val
        # CORROBORAR  SI ES POR LA IZQUIERDA
        else:
            cont=1
            #i= len(pagina.contenido)      
            for x in pagina.contenido[1::2]:
                print("el valor es: ", x.data)
                if cont==1:
                    if len(pagina.contenido)==3:
                        if valor < x.clave: 
                            self._Busqueda(pagina.contenido[0], valor,val)
                            break
                        else:
                            self._Busqueda(pagina.contenido[2], valor,val)
                            break
                        
                    else:
                        if valor >= x.clave and valor < pagina.contenido[cont+2].clave: 
                            self._Busqueda(pagina.contenido[cont+1], valor,val)
                            break
                        elif valor < x.clave: 
                            self._Busqueda(pagina.contenido[0], valor,val)
                            break
                 
                elif cont == len(pagina.contenido)-2:
                    if valor >= x.clave: 
                        self._Busqueda(pagina.contenido[cont+1], valor,val)
                        break
                   
                elif valor >= x.clave and valor < pagina.contenido[cont+2].clave:
                    self._Busqueda(pagina.contenido[cont+1], valor,val)
                    break
                cont+=2

    def VerHoja(self, pag):
        esHoja = True
        i = 0      
        while i < len(pag.contenido):
            esHoja &= pag.contenido[i] == None 
            i += 2 
        return esHoja       

    def Update(self,diccionario, val ):
        return self._Upadate(diccionario,self.raiz,val )


    def _Upadate(self,diccionario,pagina,valor):
         #ES LA ULTIMA PAGINA 
        if self.VerHoja(pagina):
            for val in pagina.contenido[1::2]:
                if val.clave ==valor:
                    try:
                        # CAMBIO DE DATOS DENTRO DEL REGISTRO
                        print("Datos anteriores: " , val.data)
                        for x in diccionario:
                            val.data[x]=diccionario[x]
                        
                        print ("Nuevos datos: " ,val.data)
                        return 0
                    except ( IndexError):
                        print("Error 1")
                        return 1
            return 4
           
        # CORROBORAR  SI ES POR LA IZQUIERDA
        else:
            cont=1
            #i= len(pagina.contenido)      
            for x in pagina.contenido[1::2]:
                print("el valor es: ", x.data)
                if cont==1:
                    if len(pagina.contenido)==3:
                        if valor < x.clave: 
                            self._Upadate(diccionario,pagina.contenido[0], valor)
                            break
                        else:
                            self._Upadate(diccionario,pagina.contenido[2], valor)
                            break
                        
                    else:
                        if valor >= x.clave and valor < pagina.contenido[cont+2].clave: 
                            self._Upadate(diccionario,pagina.contenido[cont+1], valor)
                            break
                        elif valor < x.clave: 
                            self._Upadate(diccionario,pagina.contenido[0], valor)
                            break
                 
                elif cont == len(pagina.contenido)-2:
                    if valor >= x.clave: 
                        self._Upadate(diccionario,pagina.contenido[cont+1], valor)
                        break
                   
                elif valor >= x.clave and valor < pagina.contenido[cont+2].clave:
                    self._Upadate(diccionario,pagina.contenido[cont+1], valor)
                    break
                cont+=2


    # ACCEDER A LA LISTA ENLAZADA DE LAS HOJAS AL FINAL DEL ARBOL 
    def ListaEnlazada(self,columns,lower,upper):
        registro=[]
        self._ListaEnlazada(self.raiz,registro,columns,lower,upper)
        return registro  
    
    def _ListaEnlazada(self,pagina,lista,column,lower,upper):
        try: 
            if self.VerHoja(pagina):
                #  PARA LA FUNCION DE EXTRAER TODOS LOS VALORES DE LA TABLA EXTRACT TABLE
                if column ==None and lower == None and upper == None:
                    lista.clear()
                    while pagina !=None:
                        for val in pagina.contenido[1::2]:
                            lista.append(val.data)
                        
                        pagina = pagina.paginaSiguiente
                    print(" FUNCION EXTRACT TABLE")
                    for r in lista:

                        print("los valores son:" ,r)
                    
                    return lista
                #  PARA LA FUNCION DE EXTRAER TODOS LOS VALORES DE LA TABLA EXTRACT CON RANGO EXTRAC RANGE
                else: 
                    lista.clear()
                    try:
                        contador = 0 
                        while pagina !=None:

                            for val in pagina.contenido[1::2]:
                                if contador >= lower :
                                    lista.append(val.data[column])
                                if contador == upper:
                                    break
                                else: 
                                    contador += 1
                                        
                            pagina = pagina.paginaSiguiente
                            if contador == upper:
                                break

                        print(" FUNCION EXTRACT  RANGE TABLE")
                        for r in lista:
                            print("los valores son:" ,r)
                        return lista
                    except(IndexError):
                        return None

            else: 
                self._ListaEnlazada(pagina.contenido[0],lista,column,lower,upper)
        except( IOError):
            return []

    def AlterCol(self,function, column): # function: recibe la funcion Add o Drop column: valor de columna
        val= self._AlterCol(self.raiz,  function, column)
        return val 
    
    def _AlterCol(self, pagina,  function , column) -> int:
        retorno = 0
        try:
            if self.VerHoja(pagina):      # se comprueba que es el ultimo nivel del arbol 
                
                # FUNCION PARA AGREGAR 
                if function == "Add":
                    while pagina != None:
                        for val in pagina.contenido[1::2]:
                            val.data.append(column)
                        pagina = pagina.paginaSiguiente
                   
                
                # FUNCION PARA ELIMINAR COLUMNA
                elif function == "Drop":
                    while pagina != None:
                        for val in pagina.contenido[1::2]:
                            val.data.pop(column)
                        pagina = pagina.paginaSiguiente
                    
            #    CUANDO NO ES HOJA Y ES UNA PAGINA CON HIJOS 
            else: 
                self._AlterCol(pagina.contenido[0],function,column)
            return retorno
        except(IndexError, TypeError):
            return 1

    # RETORNA TODAS LAS LLAVES PRIMARIAS DE LOS REGISTROS 
    # ACCEDER A LA LISTA ENLAZADA DE LAS HOJAS AL FINAL DEL ARBOL 
    def Claves_Hojas(self,):
        registro=[]
        self._Claves_Hojas(self.raiz,registro)
        return registro  
    
    def _Claves_Hojas(self,pagina,lista):
        try: 
            if self.VerHoja(pagina):
                #  PARA LA FUNCION DE EXTRAER TODOS LOS VALORES DE LA TABLA EXTRACT TABLE
                lista.clear()
                while pagina !=None:
                    for val in pagina.contenido[1::2]:
                        lista.append(val.clave)
                        
                    pagina = pagina.paginaSiguiente
                print(" FUNCION EXTRACT TABLE")
                for r in lista:
                    print("los valores son:" ,r)
                    
                return lista
                #  PARA LA FUNCION DE EXTRAER TODOS LOS VALORES DE LA TABLA EXTRACT CON RANGO EXTRAC RANGE
            else: 
                self._Claves_Hojas(pagina.contenido[0],lista)
        except( IOError):
            return []










"""
#**********************

def main():
    arbol = ArbolBmas()

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]:
        arbol.insertar(i, str(i))
    
    arbol.eliminar(31)
    arbol.eliminar(46)
    arbol.eliminar(35)
    #arbol.eliminar(41)
    #arbol.eliminar(15)
    #arbol.recorrer()
    #arbol.imprimirLista(arbol.raiz)
    arbol.graphviz()


if __name__ == "__main__":
    main()
"""