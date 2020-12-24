import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from principalManager import BPlusMode as bp
def cargardatos():
    bp.createDatabase("josue")
    bp.createDatabase("josue2")
    bp.createDatabase("josue3")
    bp.createTable('josue', 'tabla1',1)
    bp.createTable('josue', 'tabla2',2)
    bp.createTable('josue', 'tabla3',3)

    bp.createTable('josue2', 'tab1',1)
    bp.createTable('josue2', 'tab2',2)
    bp.createTable('josue2', 'tab3',3)

    bp.createTable('josue3', 't1',1)
    bp.createTable('josue3', 't2',2)
    bp.createTable('josue3', 't3',3)

    bp.insert('josue', 'tabla1', ['item1'])
    bp.insert('josue', 'tabla1', ['item2'])
    bp.insert('josue', 'tabla1', ['item3'])
    bp.insert('josue', 'tabla1', ['item4'])
    bp.insert('josue', 'tabla1', ['item5'])

    bp.insert('josue2', 'tab1', ['casa1'])
    bp.insert('josue2', 'tab1', ['casa2'])
    bp.insert('josue2', 'tab1', ['casa3'])
    bp.insert('josue2', 'tab1', ['casa4'])
    bp.insert('josue2', 'tab1', ['casa5'])

    bp.insert('josue3', 't1', ['comida1'])
    bp.insert('josue3', 't1', ['comida2'])
    bp.insert('josue3', 't1', ['comida3'])
    bp.insert('josue3', 't1', ['comida4'])
    bp.insert('josue3', 't1', ['comida5'])

    bp.insert('josue', 'tabla2', ['item1','item1,2'])
    bp.insert('josue', 'tabla2', ['item2','item2,2'])
    bp.insert('josue', 'tabla2', ['item3','item3,2'])
    bp.insert('josue', 'tabla2', ['item4','item4,2'])
    bp.insert('josue', 'tabla2', ['item5','item5,2'])


    bp.insert('josue2', 'tab2', ['misa1','misa1,2'])
    bp.insert('josue2', 'tab2', ['misa2','misa2,2'])
    bp.insert('josue2', 'tab2', ['misa3','misa3,2'])
    bp.insert('josue2', 'tab2', ['misa4','misa4,2'])
    bp.insert('josue2', 'tab2', ['misa5','misa5,2'])

    bp.insert('josue3', 't2', ['carrito1','carrito1,2'])
    bp.insert('josue3', 't2', ['carrito2','carrito2,2'])
    bp.insert('josue3', 't2', ['carrito3','carrito3,2'])
    bp.insert('josue3', 't2', ['carrito4','carrito4,2'])
    bp.insert('josue3', 't2', ['carrito5','carrito5,2'])

    bp.insert('josue', 'tabla3', ['anillo1','item1,2', 'item1,3'])
    bp.insert('josue', 'tabla3', ['anillo2','item2,2', 'item2,3'])
    bp.insert('josue', 'tabla3', ['anillo3','item3,2', 'item3,3'])
    bp.insert('josue', 'tabla3', ['anillo4','item4,2', 'item4,3'])
    bp.insert('josue', 'tabla3', ['anillo5','item5,2', 'item5,3'])


    bp.insert('josue2', 'tab3', ['misa1','misa1,2', 'misa1,3'])
    bp.insert('josue2', 'tab3', ['misa2','misa2,2', 'misa2,3'])
    bp.insert('josue2', 'tab3', ['misa3','misa3,2', 'misa3,3'])
    bp.insert('josue2', 'tab3', ['misa4','misa4,2', 'misa4,3'])
    bp.insert('josue2', 'tab3', ['misa5','misa5,2', 'misa5,3'])

    bp.insert('josue3', 't3', ['carrito1','carrito1,2', 'carrito1,3'])
    bp.insert('josue3', 't3', ['carrito2','carrito2,2', 'carrito2,3'])
    bp.insert('josue3', 't3', ['carrito3','carrito3,2', 'carrito3,3'])
    bp.insert('josue3', 't3', ['carrito4','carrito4,2', 'carrito4,3'])
    bp.insert('josue3', 't3', ['carrito5','carrito5,2', 'carrito5,3'])

cargardatos()


#bp.server unicamente se usa para estos(generarReporteDB, generarReporteTabla)
#bp.alter, bp.createtable (menos show.tabla y show.database)


def informacion():
    messagebox.showinfo("INFORMACION", "GRUPO NO. 3 \n Josue Gonzalez") 


#---------------VENTANAS-------------------
def ventanaBD():

    def ventanaMostrarTabla():
        if my_listbox.get(ANCHOR)!= "":
            ventana5=Toplevel()
            ventana5.geometry("800x500")
            ventana5.title="GRAFICA DE BASES DE DATOS"


            cTableContainer = tk.Canvas(ventana5)
            fTable = tk.Frame(cTableContainer)
            sbHorizontalScrollBar = tk.Scrollbar(ventana5)
            sbVerticalScrollBar = tk.Scrollbar(ventana5)

            # Updates the scrollable region of the Canvas to encompass all the widgets in the Frame
            def updateScrollRegion():
                cTableContainer.update_idletasks()
                cTableContainer.config(scrollregion=fTable.bbox())

            # Sets up the Canvas, Frame, and scrollbars for scrolling
            def createScrollableContainer():
                cTableContainer.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
                sbHorizontalScrollBar.config(orient=tk.HORIZONTAL, command=cTableContainer.xview)
                sbVerticalScrollBar.config(orient=tk.VERTICAL, command=cTableContainer.yview)

                sbHorizontalScrollBar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
                sbVerticalScrollBar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
                cTableContainer.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
                cTableContainer.create_window(0, 0, window=fTable, anchor=tk.NW)

            # Adds labels diagonally across the screen to demonstrate the scrollbar adapting to the increasing size

            createScrollableContainer()
            bp.server.showT(my_listbox.get(ANCHOR))
            if os.path.isfile('Tablas.png')==True:
                imagen =PhotoImage(file="Tablas.png")
                fondo=Label(fTable, image=imagen, ).grid(column=0, row=1)
                updateScrollRegion()
            else:
                messagebox.showerror("Error", "No se encontro la imagen")
            my_listbox2.delete(0,tk.END)
            lista2=[]
            lista2=bp.showTables(my_listbox.get(ANCHOR))

 
            for item in lista2:
                my_listbox2.insert(END, item)
            ventana5.mainloop()
        else:
            messagebox.showerror("Error", "Seleccione primero una Base de Datos")
        

    def abrirImagenDB():
            #exist path ..
        if os.path.isfile('DB.png')==True:
            #open File
            os.system('DB.png')
        else:
            messagebox.showerror("Error", "No se encontro la imagen")
    
    def graficaBD():
        ventana4=Toplevel()
        ventana4.geometry("800x500")
        ventana4.title="GRAFICA DE BASES DE DATOS"


        cTableContainer = tk.Canvas(ventana4)
        fTable = tk.Frame(cTableContainer)
        sbHorizontalScrollBar = tk.Scrollbar(ventana4)
        sbVerticalScrollBar = tk.Scrollbar(ventana4)

        # Updates the scrollable region of the Canvas to encompass all the widgets in the Frame
        def updateScrollRegion():
            cTableContainer.update_idletasks()
            cTableContainer.config(scrollregion=fTable.bbox())

        # Sets up the Canvas, Frame, and scrollbars for scrolling
        def createScrollableContainer():
            cTableContainer.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
            sbHorizontalScrollBar.config(orient=tk.HORIZONTAL, command=cTableContainer.xview)
            sbVerticalScrollBar.config(orient=tk.VERTICAL, command=cTableContainer.yview)

            sbHorizontalScrollBar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
            sbVerticalScrollBar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
            cTableContainer.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
            cTableContainer.create_window(0, 0, window=fTable, anchor=tk.NW)

        # Adds labels diagonally across the screen to demonstrate the scrollbar adapting to the increasing size

        createScrollableContainer()


        imagen =PhotoImage(file="DB.png")
        fondo=Label(fTable, image=imagen, ).grid(column=0, row=1)
        updateScrollRegion()

        ventana4.mainloop()

    def ventanaGraficaTuplas():
        if my_listbox2.get(ANCHOR)!= "":
            ventanaGraficaTupla=Toplevel()
            ventanaGraficaTupla.geometry("800x500")
            ventanaGraficaTupla.title="GRAFICA DE BASES DE DATOS"

            bp.showRegister(my_listbox.get(ANCHOR), my_listbox2.get(ANCHOR))




            cTableContainer = tk.Canvas(ventanaGraficaTupla)
            fTable = tk.Frame(cTableContainer)
            sbHorizontalScrollBar = tk.Scrollbar(ventanaGraficaTupla)
            sbVerticalScrollBar = tk.Scrollbar(ventanaGraficaTupla)

            # Updates the scrollable region of the Canvas to encompass all the widgets in the Frame
            def updateScrollRegion():
                cTableContainer.update_idletasks()
                cTableContainer.config(scrollregion=fTable.bbox())

            # Sets up the Canvas, Frame, and scrollbars for scrolling
            def createScrollableContainer():
                cTableContainer.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
                sbHorizontalScrollBar.config(orient=tk.HORIZONTAL, command=cTableContainer.xview)
                sbVerticalScrollBar.config(orient=tk.VERTICAL, command=cTableContainer.yview)

                sbHorizontalScrollBar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
                sbVerticalScrollBar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
                cTableContainer.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
                cTableContainer.create_window(0, 0, window=fTable, anchor=tk.NW)

            # Adds labels diagonally across the screen to demonstrate the scrollbar adapting to the increasing size

            createScrollableContainer()


            imagen =PhotoImage(file="salida.png")
            fondo=Label(fTable, image=imagen, ).grid(column=0, row=1)
            updateScrollRegion()



            ventanaGraficaTupla.mainloop()
        else:
            messagebox.showerror("Error", "Seleccione primero una Tabla")
  


    ventana2=Toplevel()
    ventana2.geometry("1000x225")
    ventana2.title="Gestor de Bases de Datos"


    boton2=Button(ventana2, text="GRAFICA BD, HERRAMIENTA EXTERNA", command=abrirImagenDB,bg="yellow", width = 62).place(x=50, y=70)
    boton4=Button(ventana2, text="GRAFICA BD TYTUS", command=graficaBD,bg="yellow", width = 62).place(x=50, y=100)
    
    # separador
    separador = ttk.Separator(ventana2, orient='vertical').place(x=550, relwidth=0.2, relheight=1)
    #Listbox para Bases de Datos
    my_listbox=Listbox(ventana2 )
    my_listbox.place(x=625, y =5)
    lista=[]
    lista=bp.server.generarReporteDB()

 
    for item in lista:
        my_listbox.insert(END, item)

    botonTablas=Button(ventana2, text="Mostrar grafica de tablas", command=ventanaMostrarTabla,bg="green", fg="white").place(x=625-10,  y=175)      

    #ListBox para mostrar Tablas
    my_listbox2=Listbox(ventana2 )
    my_listbox2.place(x=800, y =5)

        
    botonTablas=Button(ventana2, text="Mostrar grafica de Tuplas", command=ventanaGraficaTuplas,bg="green", fg="white").place(x=800-10,  y=175)      
    
def ventanaFuncionesBD():
    ventanaFun=Toplevel()
    ventanaFun.geometry("550x300")
    ventanaFun.title="Funciones de Base de datos"

            
    def createDatabase():

        if texto.get()=="":
            informacion.set("Debe colocarle un nombre a  la base de datos...")
            
        else:
            x=bp.createDatabase(str(texto.get()))
            if x==0:
                informacion.set("Base de datos creada correctamente")
            elif x==1:
                informacion.set("Ocurrio un error al crear la Base de datos")
            elif x==2:
                informacion.set("Base de Datos existente")
            bp.server.generarReporteDB()
            


            texto.set("")
    def showDatabase():
        ventanashowDatabase=Toplevel()
        ventanashowDatabase.geometry("400x600")
        ventanashowDatabase.title="BASES DE DATOS EXISTENTES"
        Label(ventanashowDatabase, text="LISTA DE BASES DE DATOS:", fg="blue").place(x=50,y=20)
        my_listbox=Listbox(ventanashowDatabase , width="50", height="30")
        my_listbox.place(x=50, y =50)
        lista=[]
        x=lista=bp.server.generarReporteDB()
        informacion.set("Lista de BD cargada exitosamente")
        for item in lista:
            my_listbox.insert(END, item) 

    def alterDatabase():
        x=bp.alterDatabase(textoOld.get(), textoNew.get())
        if x==0:
            informacion.set("Alter Database ejecutado correctamente")
        elif x==1:
            informacion.set("Error en la Operacion")
        elif x==2:
            informacion.set("DataBase Old no existe")
        elif x==3:
            informacion.set("DataBase new existente")

        textoOld.set("")
        textoNew.set("")
    
    def dropDatabase():
        x=bp.dropDatabase(textoEliminarBD.get())
        if x==0:
            informacion.set("Base de Datos eliminada correctamente...")
        elif x==1:
            informacion.set("Error al eliminar Base de Datos..")
        elif x==2:
            informacion.set("Base de datos no Existente")

        
        textoEliminarBD.set("")


        #label informacion
    informacion=StringVar()
    Label(ventanaFun, text="...", fg="red", textvariable=informacion).pack()

    
    #CREAR BASE DE DATOS-------------------------------------
    boton1=Button(ventanaFun, text="CREAR BD", command=createDatabase, width="20").place(x=50, y=100)
    texto = StringVar()
    Label(ventanaFun, text="Nombre de BD").place(x=250, y=80)
    textoBD= Entry(ventanaFun, textvariable=texto, width="40" ).place(x=250, y=100 + 5)
    # separador
    separador1 = ttk.Separator(ventanaFun, orient='horizontal').place(y=135, relwidth=1.2, relheight=1)
    #MOSTRAR BASE DE DATOS-------------------------------------
    botonMostrarBD=Button(ventanaFun, text="MOSTRAR BD's", command=showDatabase, width="62", bg="yellow").place(x=50, y=150)
        # separador
    separador2 = ttk.Separator(ventanaFun, orient='horizontal').place(y=185, relwidth=1.2, relheight=1)
    #ALTER BASE DE DATOS-------------------------------------
    botonModificar=Button(ventanaFun, text="ALTER BD", command=alterDatabase, width="20").place(x=50, y=200)
    
    textoOld = StringVar()
    Label(ventanaFun, text="Old:").place(x=250, y=200 -10)
    cajaOld= Entry(ventanaFun, textvariable=textoOld, width="20" ).place(x=220, y=200+10)

    textoNew = StringVar()
    Label(ventanaFun, text="New:").place(x=250 + 150, y=200 -10)
    cajaNew= Entry(ventanaFun, textvariable=textoNew, width="20" ).place(x=220+ 150, y=200+10)

            # separador
    separador2 = ttk.Separator(ventanaFun, orient='horizontal').place(y=240, relwidth=1.2, relheight=1)

        #ELIMINAR BASE DE DATOS-------------------------------------
    botonEliminarBD=Button(ventanaFun, text="ELIMINAR BD", command=dropDatabase, width="20").place(x=50, y=260)
    textoEliminarBD = StringVar()
    Label(ventanaFun, text="Nombre de BD").place(x=250, y=245)
    textoBD= Entry(ventanaFun, textvariable=textoEliminarBD, width="40" ).place(x=250, y=260+5)

def ventanaTabla1():
    def createTable():

        if (textoNombreBD.get()=="") or (textoNombreTabla.get()=="") or (textoColumnas.get()==""):
            informacion.set("Completar todos los campos...")
            
        else:
            try:
                x=bp.createTable(textoNombreBD.get(),textoNombreTabla.get(), int(textoColumnas.get()))
                if x==0:
                    informacion.set("Tabla creada correctamente...")
                elif x==1:
                    informacion.set("Error en la Operacion...")
                elif x==2:
                    informacion.set("La base de datos no existe...")
                elif x==2:
                    informacion.set("La tabla existe...")
            except:
                informacion.set("Debe colocar un numero en las Columnas... ")
            
            

          
            textoNombreBD.set("")
            textoNombreTabla.set("")
            textoColumnas.set("")
    
    def showTables():

        if (    textoShowTables.get()==""):
            informacion.set( "Colocar el nombre de la base de datos..")
            
        else:
            try:
                x=bp.showTables(textoShowTables.get())
               
                if x==[]:
                    informacion.set("Base de datos sin tablas...")
                elif x==None:
                    informacion.set("No existe la base de datos...")
                else:
                    informacion.set("Lista de tablas cargada exitosamente")
                    def ventanaMostrarTablas():
                        ventanashowTable=Toplevel()
                        ventanashowTable.geometry("400x600")
                        ventanashowTable.title="LISTA DE TABLAS"
                        Label(ventanashowTable, text="LISTA DE TABLAS DE: " + textoShowTables.get(), fg="blue").place(x=50,y=20)
                        my_listbox2=Listbox(ventanashowTable , width="50", height="30")
                        my_listbox2.place(x=50, y =50)
                        lista=[]
                        x=lista=bp.showTables(textoShowTables.get())

                        for item in lista:
                            my_listbox2.insert(END, item) 
                    ventanaMostrarTablas()
                    textoShowTables.set("")
            except:
                informacion.set("Error desconocido ")
            
            

          
            textoNombreBD.set("")
            textoNombreTabla.set("")
            textoColumnas.set("")

    def extractTable():
        if textoNombreExtract.get()!="" and textoNombreTablaExtract.get()!="":
            x=bp.extractTable(textoNombreExtract.get(), textoNombreTablaExtract.get())
        
            print(x)
            if x==[]:
                informacion.set("Tabla Vacia...")
            elif x==None:
                informacion.set("Ha ocurrido un error, verificar BD y tabla")
            else:
                informacion.set("")
                ventanaExtract=Toplevel()
                ventanaExtract.geometry("800x300")
                ventanaExtract.title="EXTRACT TABLE"

                #Frame para acoplarlo con el dataGrid
                miFrame3=Frame(ventanaExtract)
                miFrame3.pack()
                miFrame3.config(width="300", height="200")

                Label(miFrame3, text="BD: " + textoNombreExtract.get() + " TABLA: " + textoNombreTablaExtract.get(), fg="blue").pack()
                #Lista de Listas
                arreglo=x
                #Averiguando cuantas columnas tiene la primera Lista(el resto tiene las mismas)
                listaCol=[]
                for x in range(0, len(arreglo[0]), 1):
                    listaCol += [x+1]

                #creando el DataGrid y agregandolo al Frame
                datagrid=ttk.Treeview(miFrame3, columns=(listaCol), show="headings")
                datagrid.pack()

                #Scrollbar horizontal y agregandolo a la ventana
                scrollbar_horizontal = ttk.Scrollbar(ventanaExtract, orient='horizontal', command = datagrid.xview)
                scrollbar_horizontal.pack(side='bottom', fill=X)
                datagrid.configure(xscrollcommand=scrollbar_horizontal.set)
                
                #Agregando las cabeceras
                for i in listaCol:
                    datagrid.heading(i, text="Columna"+ str(i))

                #insertando todos los registros de la lista de listas
                for x in arreglo:
                    datagrid.insert('', 'end', values=x)
        else:
            informacion.set("Debe llenar los datos de BD y Tabla")
                            

    def extractRangeTable():
        if (textoNombreExtractRange.get()!="" and textoNombreTablaExtractRange.get()!="" and textoNoColumna.get()!=""
        and textoRangeLower.get()!="" and textoRangeUpper.get()!=""):
            try:
                int(textoNoColumna.get())
                int(textoRangeLower.get())
                int(textoRangeUpper.get())
                informacion.set("")
                salida=bp.extractRangeTable(textoNombreExtractRange.get(), textoNombreTablaExtractRange.get(), int(textoNoColumna.get()), int(textoRangeLower.get()), int(textoRangeUpper.get()))
                if salida==[]:
                    informacion.set("BD y Tabla existe pero sin registros...")
                elif salida==None:
                    informacion.set("Ha ocurrido un error. Sino la BD o Tabla no existen")
                else:
                    ventanaExtractRange=Toplevel()
                    ventanaExtractRange.geometry("400x300")
                    ventanaExtractRange.title="EXTRACT RANGE TABLE"

                    #Frame para acoplarlo con el dataGrid
                    miFrame3=Frame(ventanaExtractRange)
                    miFrame3.pack()
                    miFrame3.config(width="300", height="200")

                    Label(miFrame3, text="BD:" + textoNombreExtractRange.get() +" TABLA: " + textoNombreTablaExtractRange.get(), fg="blue").pack()
                    #Lista de Listas
                    arreglo=salida
                    #Averiguando cuantas columnas tiene la primera Lista(el resto tiene las mismas)
            

                    #creando el DataGrid y agregandolo al Frame
                    datagrid=ttk.Treeview(miFrame3, columns=(1), show="headings")
                    datagrid.pack()

                    #Agregando las cabeceras
                    datagrid.heading(1, text="Extract Range Table")

                    #insertando todos los registros de la lista de listas
                    for x in arreglo:
                        datagrid.insert('', 'end', values=x)

            except:
                informacion.set("Debe ingresar numeros en Columna, Lower y Upper")
        else:
            informacion.set("Debe llenar BD, Tabla, Columna, Lower y Upper")
                            
    def alterTable():
        if textoAlterTable.get()!="" and textoOldTable.get()!="" and textoNewTable.get()!="":
            salida=bp.alterTable(textoAlterTable.get(),textoOldTable.get(), textoNewTable.get())
            if salida==0:
                informacion.set("Cambio de nombre a la Tabla exitoso...")
                textoAlterTable.set("")
                textoOldTable.set("")
                textoNewTable.set("")
            elif salida==1:
                informacion.set("Error al intentar cambiar de nombre a la Tabla")
            elif salida==2:
                informacion.set("La Base de Datos no Existe")
            elif salida==3:
                informacion.set("La Tabla no existe")
            elif salida==4:
                informacion.set("La Tabla nueva ya existe, cambiar de nombre")
        else:
            informacion.set("No deje campos vacios, BD, tabla vieja, tabla nueva...")

    def alterAddColumn():
        if (textoNombreBDAlterAddColumn.get()!="" and textoTablaAlterAddColumn.get()!="" and textoDefectoAlterAddColumn.get()!=""):
            None 
            informacion.set("")
            salidaAlter=bp.alterAddColumn(textoNombreBDAlterAddColumn.get(), textoTablaAlterAddColumn.get(), textoDefectoAlterAddColumn.get())
            if salidaAlter==0:
                informacion.set("Columna agregada correctamente")
                textoNombreBDAlterAddColumn.set("")
                textoTablaAlterAddColumn.set("")
                textoDefectoAlterAddColumn.set("")
            elif salidaAlter==1:
                informacion.set("Error al agregar la columna")
            elif salidaAlter==2:
                informacion.set("La base de datos No existe")
            elif salidaAlter==3:
                informacion.set("La Tabla no existe")
        else:
            informacion.set("No deje campos vacios. BD, Tabla o Valor por Defecto")


    ventanaTab=Toplevel()
    ventanaTab.geometry("1100x500")
    ventanaTab.title="Funciones de Tablas"

    #label informacion
    informacion=StringVar()
    Label(ventanaTab, text="...", fg="red", textvariable=informacion).pack()

    #CREAR TABLA-------------------------------------
    boton1=Button(ventanaTab, text="CREATE TABLE", command=createTable, width="20").place(x=10, y=100)
        
        #textbox nombre BD existente
    textoNombreBD = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=85)
    cajaNombreBD= Entry(ventanaTab, textvariable=textoNombreBD, width="35" ).place(x=250, y=5 + 100)

            #textbox nombre nueva Tabla
    textoNombreTabla = StringVar()
    Label(ventanaTab, text="Nombre NUEVA tabla: ").place(x=500, y=85)
    cajaNombreTabla= Entry(ventanaTab, textvariable=textoNombreTabla, width="35" ).place(x=500, y=5 + 100)

                #textbox numeroColumnas
    textoColumnas = StringVar()
    Label(ventanaTab, text="Numero de Columnas: ").place(x=750, y=85)
    cajaNombreColumnas= Entry(ventanaTab, textvariable=textoColumnas, width="35" ).place(x=750, y=5 + 100)

        # _________________________________________separador ________________________________________________________
    separador1 = ttk.Separator(ventanaTab, orient='horizontal').place(y=140, relwidth=1.2, relheight=1)

    #SHOW TABLES-------------------------------------
    botonShowTables=Button(ventanaTab, text="SHOW TABLES", command=showTables, width="20").place(x=10, y=160)
        
        #textbox NOMBRE BASES
    textoShowTables = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=160-15)
    cajaShowTables= Entry(ventanaTab, textvariable=textoShowTables, width="35" ).place(x=250, y=5 + 160)

            # _________________________________________separador ________________________________________________________
    separador2 = ttk.Separator(ventanaTab, orient='horizontal').place(y=200, relwidth=1.2, relheight=1)
    botonExtractTable=Button(ventanaTab, text="EXTRACT TABLE", command=extractTable, width="20").place(x=10, y=220)
    

    textoNombreExtract = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=210)
    cajaNombreExtract= Entry(ventanaTab, textvariable=textoNombreExtract, width="35" ).place(x=250, y= 230)

            #textbox nombre nueva Tabla
    textoNombreTablaExtract = StringVar()
    Label(ventanaTab, text="Nombre de Tabla: ").place(x=500, y=210)
    cajaNombreTablaExtract= Entry(ventanaTab, textvariable=textoNombreTablaExtract, width="35" ).place(x=500, y=230)

        # _________________________________________separador ________________________________________________________
    separador7 = ttk.Separator(ventanaTab, orient='horizontal').place(y=260, relwidth=1.2, relheight=1)
            #EXTRACT RANGE TABLE
    botonExtracRangetTable=Button(ventanaTab, text="EXTRACT RANGE TABLE", command=extractRangeTable, width="20").place(x=10, y=280)
    
    textoNombreExtractRange = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=270)
    cajaNombreExtractRange= Entry(ventanaTab, textvariable=textoNombreExtractRange, width="35" ).place(x=250, y= 290)


    textoNombreTablaExtractRange = StringVar()
    Label(ventanaTab, text="Nombre de Tabla: ").place(x=500, y=270)
    cajaNombreTablaExtractRange= Entry(ventanaTab, textvariable=textoNombreTablaExtractRange, width="35" ).place(x=500, y=290)

    textoNoColumna = StringVar()
    Label(ventanaTab, text="# Columna: ").place(x=750, y=270)
    cajaNoColumna= Entry(ventanaTab, textvariable=textoNoColumna, width="15" ).place(x=750, y=290)

    textoRangeLower = StringVar()
    Label(ventanaTab, text="Lower: ").place(x=850, y=270)
    cajaRangeLower= Entry(ventanaTab, textvariable=textoRangeLower, width="15" ).place(x=850, y=290)

    textoRangeUpper = StringVar()
    Label(ventanaTab, text="Upper: ").place(x=950, y=270)
    cajaRangeUpper= Entry(ventanaTab, textvariable=textoRangeUpper, width="15" ).place(x=950, y=290)

        # _________________________________________separador ________________________________________________________
    separador8 = ttk.Separator(ventanaTab, orient='horizontal').place(y=330, relwidth=1.2, relheight=1)


    botonAlterTable=Button(ventanaTab, text="ALTER TABLE", command=alterTable, width="20").place(x=10, y=360)
    
    textoAlterTable = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=360-20)
    cajaNombreBDAlterTable= Entry(ventanaTab, textvariable=textoAlterTable, width="35" ).place(x=250, y= 360)

    
    textoOldTable = StringVar()
    Label(ventanaTab, text="Tabla Vieja: ").place(x=500, y=360-20)
    cajaOldTable= Entry(ventanaTab, textvariable=textoOldTable, width="35" ).place(x=500, y=360)

    textoNewTable = StringVar()
    Label(ventanaTab, text="Tabla Nueva: ").place(x=750, y=360-20)
    cajaNewTable= Entry(ventanaTab, textvariable=textoNewTable, width="35" ).place(x=750, y=360)

            # _________________________________________separador ________________________________________________________
    separador9 = ttk.Separator(ventanaTab, orient='horizontal').place(y=410, relwidth=1.2, relheight=1)

    botonalterAddColumn=Button(ventanaTab, text="ALTER ADD COLUMN", command=alterAddColumn, width="20").place(x=10, y=440)
    
    textoNombreBDAlterAddColumn = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=440-20)
    cajaNombreBDAlterAddColumn= Entry(ventanaTab, textvariable=textoNombreBDAlterAddColumn, width="35" ).place(x=250, y= 440)

    
    textoTablaAlterAddColumn = StringVar()
    Label(ventanaTab, text="Tabla: ").place(x=500, y=440-20)
    cajaTablaAlterAddColumn= Entry(ventanaTab, textvariable=textoTablaAlterAddColumn, width="35" ).place(x=500, y=440)

    textoDefectoAlterAddColumn = StringVar()
    Label(ventanaTab, text="Valor por Defecto: ").place(x=750, y=440-20)
    cajaDefectoAlterAddColumn= Entry(ventanaTab, textvariable=textoDefectoAlterAddColumn, width="35" ).place(x=750, y=440)



def ventanaTabla2():
    def AlterDropColumn():
        if (textoNombreBDAlterDropColumn.get()!="" and textoNombreTablaAlterDropColumn.get()!="" and textoColumnaAlterDropColumn.get()!=""):
            try:
                int(textoColumnaAlterDropColumn.get())
                salida=bp.alterDropColumn(textoNombreBDAlterDropColumn.get(), textoNombreTablaAlterDropColumn.get(), int(textoColumnaAlterDropColumn.get()))

                if salida==0:
                    informacion.set("Columna Eliminada correctamente")
                elif salida==1:
                    informacion.set("Error al Eliminar columna")
                elif salida==2:
                    informacion.set("La base de datos no existe")
                elif salida==3:
                    informacion.set("La tabla no existe")
                elif salida==4:
                    informacion.set("Columna fuera de los limites")
                
            except:
                informacion.set("Debe ingresar un numero en Columna")
        else:
            informacion.set("No dejar campos vacios. Nombre Bd, Tabla, columna a eliminar")
    def dropTable():
        if textoNombreBDDropTable.get()!="" and textoNombreTablaDropTable.get()!="":
            salida=bp.dropTable(textoNombreBDDropTable.get(), textoNombreTablaDropTable.get())
            
            if salida==0:
                informacion.set("Tabla eliminada correctamente...")
                textoNombreBDDropTable.set("")
                textoNombreTablaDropTable.set("")
            elif salida==1:
                informacion.set("Error en la eliminacion de la tabla...")
            elif salida==2:
                informacion.set("La base de datos no existe...")
            elif salida==3:
                informacion.set("La tabla no existe...")
        else:
            informacion.set("No deje campos vacios en BD y Tabla")
    
    ventanaTab2=Toplevel()
    ventanaTab2.geometry("1100x500")
    ventanaTab2.title="Funciones de Tablas"

    #label informacion
    informacion=StringVar()
    Label(ventanaTab2, text="...", fg="red", textvariable=informacion).pack()

    #Boton -------------------------------------
    botonAlterDropColumn=Button(ventanaTab2, text="ALTER DROP COLUMN", command=AlterDropColumn, width="20").place(x=10, y=100)
        
        #textbox nombre BD existente
    textoNombreBDAlterDropColumn = StringVar()
    Label(ventanaTab2, text="Nombre BD: ").place(x=250, y=85)
    cajaNombreBDAlterDropColumn= Entry(ventanaTab2, textvariable=textoNombreBDAlterDropColumn, width="35" ).place(x=250, y=5 + 100)

            #textbox nombre Tabla
    textoNombreTablaAlterDropColumn = StringVar()
    Label(ventanaTab2, text="Nombre Tabla: ").place(x=500, y=85)
    cajaNombreTablaAlterDropColumn= Entry(ventanaTab2, textvariable=textoNombreTablaAlterDropColumn, width="35" ).place(x=500, y=5 + 100)

                #textbox Columna para eliminar
    textoColumnaAlterDropColumn = StringVar()
    Label(ventanaTab2, text="Columna a Eliminar: ").place(x=750, y=85)
    cajaNombreColumnaAlterDropColumns= Entry(ventanaTab2, textvariable=textoColumnaAlterDropColumn, width="35" ).place(x=750, y=5 + 100)
    
        # _________________________________________separador ________________________________________________________
    separador1 = ttk.Separator(ventanaTab2, orient='horizontal').place(y=140, relwidth=1.2, relheight=1)

    #SHOW TABLES-------------------------------------
    botonDropTable=Button(ventanaTab2, text="DROP TABLE", command=dropTable, width="20").place(x=10, y=160)
        
        #textbox NOMBRE BASE DATOS
    textoNombreBDDropTable = StringVar()
    Label(ventanaTab2, text="Nombre BD: ").place(x=250, y=160-15)
    cajaBDDropTable= Entry(ventanaTab2, textvariable=textoNombreBDDropTable, width="35" ).place(x=250, y=5 + 160)

            #textbox NOMBRE TABLA A ELIMINAR
    textoNombreTablaDropTable = StringVar()
    Label(ventanaTab2, text="Tabla a Eliminar: ").place(x=500, y=160-15)
    cajaTablaDropTable= Entry(ventanaTab2, textvariable=textoNombreTablaDropTable, width="35" ).place(x=500, y=5 + 160)

            # _________________________________________separador ________________________________________________________
    separador2 = ttk.Separator(ventanaTab2, orient='horizontal').place(y=200, relwidth=1.2, relheight=1)
    botonExtractTable=Button(ventanaTab2, text="ALTER ADD PK",bg="red", command=None, width="20").place(x=10, y=220)
    

    

        # _________________________________________separador ________________________________________________________
    

    separador7 = ttk.Separator(ventanaTab2, orient='horizontal').place(y=260, relwidth=1.2, relheight=1)
    '''
            #EXTRACT RANGE TABLE
    botonExtracRangetTable=Button(ventanaTab, text="EXTRACT RANGE TABLE", command=extractRangeTable, width="20").place(x=10, y=280)
    
    textoNombreExtractRange = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=270)
    cajaNombreExtractRange= Entry(ventanaTab, textvariable=textoNombreExtractRange, width="35" ).place(x=250, y= 290)


    textoNombreTablaExtractRange = StringVar()
    Label(ventanaTab, text="Nombre de Tabla: ").place(x=500, y=270)
    cajaNombreTablaExtractRange= Entry(ventanaTab, textvariable=textoNombreTablaExtractRange, width="35" ).place(x=500, y=290)

    textoNoColumna = StringVar()
    Label(ventanaTab, text="# Columna: ").place(x=750, y=270)
    cajaNoColumna= Entry(ventanaTab, textvariable=textoNoColumna, width="15" ).place(x=750, y=290)

    textoRangeLower = StringVar()
    Label(ventanaTab, text="Lower: ").place(x=850, y=270)
    cajaRangeLower= Entry(ventanaTab, textvariable=textoRangeLower, width="15" ).place(x=850, y=290)

    textoRangeUpper = StringVar()
    Label(ventanaTab, text="Upper: ").place(x=950, y=270)
    cajaRangeUpper= Entry(ventanaTab, textvariable=textoRangeUpper, width="15" ).place(x=950, y=290)

        # _________________________________________separador ________________________________________________________
    separador8 = ttk.Separator(ventanaTab, orient='horizontal').place(y=330, relwidth=1.2, relheight=1)


    botonAlterTable=Button(ventanaTab, text="ALTER TABLE", command=alterTable, width="20").place(x=10, y=360)
    
    textoAlterTable = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=360-20)
    cajaNombreBDAlterTable= Entry(ventanaTab, textvariable=textoAlterTable, width="35" ).place(x=250, y= 360)

    
    textoOldTable = StringVar()
    Label(ventanaTab, text="Tabla Vieja: ").place(x=500, y=360-20)
    cajaOldTable= Entry(ventanaTab, textvariable=textoOldTable, width="35" ).place(x=500, y=360)

    textoNewTable = StringVar()
    Label(ventanaTab, text="Tabla Nueva: ").place(x=750, y=360-20)
    cajaNewTable= Entry(ventanaTab, textvariable=textoNewTable, width="35" ).place(x=750, y=360)

            # _________________________________________separador ________________________________________________________
    separador9 = ttk.Separator(ventanaTab, orient='horizontal').place(y=410, relwidth=1.2, relheight=1)

    botonalterAddColumn=Button(ventanaTab, text="ALTER ADD COLUMN", command=alterAddColumn, width="20").place(x=10, y=440)
    
    textoNombreBDAlterAddColumn = StringVar()
    Label(ventanaTab, text="Nombre BD: ").place(x=250, y=440-20)
    cajaNombreBDAlterAddColumn= Entry(ventanaTab, textvariable=textoNombreBDAlterAddColumn, width="35" ).place(x=250, y= 440)

    
    textoTablaAlterAddColumn = StringVar()
    Label(ventanaTab, text="Tabla: ").place(x=500, y=440-20)
    cajaTablaAlterAddColumn= Entry(ventanaTab, textvariable=textoTablaAlterAddColumn, width="35" ).place(x=500, y=440)

    textoDefectoAlterAddColumn = StringVar()
    Label(ventanaTab, text="Valor por Defecto: ").place(x=750, y=440-20)
    cajaDefectoAlterAddColumn= Entry(ventanaTab, textvariable=textoDefectoAlterAddColumn, width="35" ).place(x=750, y=440)
    '''

def ventanaTupla():
    ventanaTup=Toplevel()
    ventanaTup.geometry("800x500")
    ventanaTup.title="Funciones de Tuplas"

    def insertTupla():
        ventanaTup=Toplevel()
        ventanaTup.geometry("425x600")
        ventanaTup.title="INSERTAR TUPLA"
        def eliminarElemento():
            my_listbox.delete(ANCHOR)

        def agregarTupla():

            if textoBaseDatos.get()!="" and textoTabla.get()!="":
                listaTupla=[]
                for cont in range (0,my_listbox.size(),1):
                    listaTupla+=[my_listbox.get(cont)]
                x=bp.insert(textoBaseDatos.get(),textoTabla.get(), listaTupla)
                if x==0:
                    textoInfo.set("Tupla agregada correctamente")

                    my_listbox.delete(0,tk.END)
                elif x==1:
                    textoInfo.set("Error al agregar Tupla")
                elif x==2:
                    textoInfo.set("La Base de datos no Existe")
                elif x==3:
                    textoInfo.set("La Tabla no existe")
                elif x==4:
                    textoInfo.set("Llave primaria Duplicada")
                elif x==5:
                    textoInfo.set("Columnas fuera de los limites")
            else:
                textoInfo.set("Debe colocar una BD y una tabla")


        def agregarListBox():
            if textoItem.get()!="":
                my_listbox.insert(END, textoItem.get())
                textoItem.set("")
            else:
                None

        textoBaseDatos = StringVar()
        Label(ventanaTup, text="Nombre de BD").place(x=10, y=10)
        cajaBasedatos= Entry(ventanaTup, textvariable=textoBaseDatos, width="30" ).place(x=10, y=30)

        textoTabla = StringVar()
        Label(ventanaTup, text="Nombre de TABLA").place(x=215, y=10)
        cajaBasedatos= Entry(ventanaTup, textvariable=textoTabla, width="30" ).place(x=215, y=30)

        botonAgregarLista=Button(ventanaTup, text="AGREGAR A LA LISTA", command=agregarListBox, bg="green", fg="white", width="55").place(x=10,  y=50+40)
        botonEliminarElemento=Button(ventanaTup, text="ELIMINAR ELEMENTO", command=eliminarElemento, bg="red", fg="white", width="55").place(x=10, y=280+40)
        botonAgregarTupla=Button(ventanaTup, text="AGREGAR TUPLA", command=agregarTupla, bg="yellow", width="55").place(x=10, y=305+40) 

        textoItem = StringVar()
        Label(ventanaTup, text="ITEM: ").place(x=10,y=10+55)
        cajaItem= Entry(ventanaTup, textvariable=textoItem, width="58" ).place(x=50, y=10+55)


        my_listbox=Listbox(ventanaTup, width=64)
        my_listbox.place(x=15, y =100+40)

        textoInfo=StringVar()
        Label(ventanaTup, fg="blue", textvariable=textoInfo).place(x=10,y=400)
        textoInfo.set("hola")

#BOTONES PARA LA VENTANA DE TUPLAS---------------------------------------------------------------------------
    botonInsertTupla=Button(ventanaTup, text="INSERTAR TUPLA", command=insertTupla, width="20").place(x=10, y=40)

    separador6 = ttk.Separator(ventanaTup, orient='horizontal').place(y=80, relwidth=1.2, relheight=1)


    

#-------------FIN VENTANAS-----------------    

#---------------VENTANA PRINCIPAL-------------------
ventana=tk.Tk()
ventana.title("STORAGE MANAGER - GROUP3")
ventana.resizable(0,0) 

#ventana.geometry('1400x780')

#creando el frame para poder colocar cosas dentro
miFrame=Frame()
miFrame.pack()

miFrame.config(width="575", height="300")
miFrame.config(bd=12)



miFrame.config(cursor="plus")

imagen =PhotoImage(file="logoTytus.png")
fondo=Label(miFrame, image=imagen).place(x=100,y=0)


boton1=Button(miFrame, text="BASES DE DATOS", command=ventanaBD,width = 30, bg="#01C3FF", fg="#FFFFFF").place(x=170, y=100+20)
botonFunBD=Button(miFrame, text="FUNCIONES DE BD", command=ventanaFuncionesBD, width = 30, bg="#03A6D7", fg="#FFFFFF").place(x=170, y=125+20)
botonFunTable1=Button(miFrame, text="FUNCIONES DE TABLAS 1", command=ventanaTabla1, width = 30, bg="#0380A6", fg="#FFFFFF").place(x=170, y=150+20)
botonFunTable2=Button(miFrame, text="FUNCIONES DE TABLAS 2", command=ventanaTabla2, width = 30, bg="#005A75", fg="#FFFFFF").place(x=170, y=175+20)
botonFunTuplas=Button(miFrame, text="FUNCIONES DE TUPLAS", command=ventanaTupla, width = 30, bg="#004D64", fg="#FFFFFF").place(x=170, y=200+20)
ventana.mainloop()
#--------------- FIN VENTANA PRINCIPAL-------------------