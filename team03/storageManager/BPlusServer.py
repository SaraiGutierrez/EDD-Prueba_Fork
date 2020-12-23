from storageManager.Arbol_AVL import Arbol_AVL
from storageManager.Base_Datos import Base_Datos
from storageManager.Tabla import Tabla

class BPlusServer:
    def __init__(self):
        self.__db_Tree = Arbol_AVL()

    ##################
    # Databases CRUD #
    ##################

    def createDB(self, nombre):
        nuevaDB = Base_Datos(nombre)
        self.__db_Tree.insertar(nuevaDB)

    def alterDB(self, old, new):
        #Buscar el nodo con el nombre viejo
        idBuscado = self.__getNombreASCII(old)
        buscado = self.__db_Tree.buscarObjeto(idBuscado, old)
        #Crear una nueva DB con el nombre nuevo
        nuevaDB = Base_Datos(new)
        #Copiar los datos del nodo a cambiarle el nombre en nuevaDB
        nuevaDB.estructura = buscado.objeto.estructura
        #Eliminar la DB vieja
        self.__db_Tree.eliminar(buscado.objeto)
        #Insertar la DB nueva
        self.__db_Tree.insertar(nuevaDB)

    def showDB(self):
        ############BORRAR#######SOLO PRUEBA###################
        #root = self.__db_Tree.getRoot()
        #self.__db_Tree.imprimirPreOrden(root)
        ####PRUEBA PARA GENERAR EL GRAFO DE BASES DE DATOS####
        self.__db_Tree.reporteDB()
        ############BORRAR#######SOLO PRUEBA###################
        return self.__db_Tree.getListaNombres()

    def dropDB(self, nombre):
        #Buscar el nodo a eliminar y traerlo
        idBuscado = self.__getNombreASCII(nombre)
        buscado = self.__db_Tree.buscarObjeto(idBuscado, nombre)

        self.__db_Tree.eliminar(buscado.objeto)

    ###############
    # Tables CRUD #
    ###############

    def createT(self, database, nombre, columnas):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Crear un nuevo objeto de Tabla
        nuevaT = Tabla(nombre, columnas)

        #Se inserta la nueva tabla en el arbol
        dbBuscada.objeto.estructura.insertar(nuevaT)

    def showT(self, database):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        ############BORRAR#######SOLO PRUEBA###################
        ####PRUEBA PARA GENERAR EL GRAFO DE TABLAS####
        dbBuscada.objeto.estructura.reporteTablas()
        ############BORRAR#######SOLO PRUEBA###################
        return dbBuscada.objeto.estructura.getListaNombres()

    def extractT(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        
        return tableBuscada.objeto.estructura.extractTable()
        

    def extractRangeT(self, database, table, columnNumber, lower, upper):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        
        return tableBuscada.objeto.estructura.extractRangeTable(columnNumber, lower, upper)
        

    def alterT(self, database, tableOld, tableNew):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Traer el arbol de tablas de la base de datos requerida
        table_tree = dbBuscada.objeto.estructura

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(tableOld)
        tableBuscada = table_tree.buscarObjeto(idTable, tableOld)

        #Crear una nueva Tabla con el nombre nuevo y por default columnas:0
        nuevaT = Tabla(tableNew, 0)

        #Copiar los datos del nodo a cambiarle el nombre en nuevaT
        nuevaT.estructura = tableBuscada.objeto.estructura
        nuevaT.columnas = tableBuscada.objeto.columnas

        #Eliminar la Tabla vieja
        dbBuscada.objeto.estructura.eliminar(tableBuscada.objeto)
        #Insertar la Tabla nueva
        dbBuscada.objeto.estructura.insertar(nuevaT)

    def alterAddC(self, database, table, default):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        
        tableBuscada.objeto.estructura.alterAddColumn(default)

    def alterDropC(self, database, table, columnNumber):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        
        return tableBuscada.objeto.estructura.alterDropColumn(columnNumber)

    def dropT(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        dbBuscada.objeto.estructura.eliminar(tableBuscada.objeto)

    ##################
    # Registers CRUD #
    ##################

    def insert(self, database, table, register):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        
        return tableBuscada.objeto.estructura.insert(register)
    
    def cargarCSV(self, filepath, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        return tableBuscada.objeto.estructura.loadCSV(filepath)

    def extractR(self, database, table, columns):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        return tableBuscada.objeto.estructura.extractRow(columns)

    def actualizarDatos(self, database, table, register, columns):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        return tableBuscada.objeto.estructura.update(register, columns)
        

    def eliminarRegistro(self, database, table, columns):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        return tableBuscada.objeto.estructura.delete(columns)

    def truncateT(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        tableBuscada.objeto.estructura.truncateRaiz()

    #############
    # Utilities #
    #############

    def __getNombreASCII(self, cadena):
        number = 0

        for c in cadena:
            number += ord(c)
        
        return number

    def generarReporteDB(self):
        ####PRUEBA PARA GENERAR EL GRAFO DE BASES DE DATOS####
        self.__db_Tree.reporteDB()
        return self.__db_Tree.getListaNombres()

    def generarReporteTabla(self, database):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        ####PRUEBA PARA GENERAR EL GRAFO DE TABLAS####
        dbBuscada.objeto.estructura.reporteTablas()
        return dbBuscada.objeto.estructura.getListaNombres()

    def generarReporteBMasPlus(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        tableBuscada.objeto.estructura.graficar()

    def existeDB(self, database):
        existe = True
        #Buscar el nodo con de la DB y retornarlo
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        if dbBuscada is None:
            existe = False

        return existe

    def existeTabla(self, database, table):
        existe = True
        #Buscar el nodo con de la DB y retornarlo
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        if tableBuscada is None:
            existe = False

        return existe