from storageManager.Arbol_AVL import Arbol_AVL
from storageManager.Base_Datos import Base_Datos

class BPlusServer:
    def __init__(self):
        self.__db_Tree = Arbol_AVL()

    def createDB(self, nombre):
        nuevaDB = Base_Datos(nombre)
        self.__db_Tree.insertar(nuevaDB)

    def alterDB(self, old, new):
        #Buscar el nodo con el nombre viejo
        buscado = self.__db_Tree.buscarObjeto(old)
        #Crear una nueva DB con el nombre nuevo
        nuevaDB = Base_Datos(new)
        #Copiar los datos del nodo a cambiarle el nombre en nuevaDB
        nuevaDB.nombre = buscado.objeto.nombre
        nuevaDB.estructura = buscado.objeto.estructura
        #Eliminar la DB vieja
        self.__db_Tree.eliminar(old)
        #Insertar la DB nueva
        self.__db_Tree.insertar(nuevaDB)

    ''' METODO TEMPORAL PARA PROBAR MOSTRAR LA LISTA DE BASE DE DATOS EN PREORDEN'''
    def showDB(self):
        root = self.__db_Tree.getRoot()
        self.__db_Tree.imprimirPreOrden(root)
        ####PRUEBA PARA GENERAR EL GRAFO DE BASES DE DATOS####
        self.__db_Tree.reporteDB()

    ''' METODO TEMPORAL PARA PROBAR MOSTRAR LA LISTA DE BASE DE DATOS EN PREORDEN'''

    def dropDB(self, nombre):
        self.__db_Tree.eliminar(nombre)