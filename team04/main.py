import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from principalManager import BPlusMode as bp



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

  


    ventana2=Toplevel()
    ventana2.geometry("800x225")
    ventana2.title="Gestor de Bases de Datos"


    boton2=Button(ventana2, text="GRAFICA BD, HERRAMIENTA EXTERNA", command=abrirImagenDB,bg="yellow", width = 62).place(x=50, y=70)
    boton4=Button(ventana2, text="GRAFICA BD TYTUS", command=graficaBD,bg="yellow", width = 62).place(x=50, y=100)
    
    # separador
    separador = ttk.Separator(ventana2, orient='vertical').place(x=550, relwidth=0.2, relheight=1)
  
    my_listbox=Listbox(ventana2 )
    my_listbox.place(x=625, y =5)
    lista=[]
    lista=bp.server.generarReporteDB()

 
    for item in lista:
        my_listbox.insert(END, item)
        #MUESTRA EL ITEM SELECCIONADO
        #messagebox.showinfo("msj", my_listbox.get(ANCHOR))
    botonTablas=Button(ventana2, text="Mostrar tablas", command=ventanaMostrarTabla,bg="green", fg="white").place(x=625 +15,  y=175)      



  
    
def ventanaFuncionesBD():
    ventanaFun=Toplevel()
    ventanaFun.geometry("550x300")
    ventanaFun.title="Funciones de Base de datos"

            
    def createDatabase():

        if texto.get()=="":
            messagebox.showwarning("ADVERTENCIA", "Debe colocarle un nombre a  la base de datos...")
            
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
            messagebox.showwarning("ADVERTENCIA", "Completar todos los campos...")
            
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
                            






    ventanaTab=Toplevel()
    ventanaTab.geometry("1000x800")
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

    
    

def ventanaTabla2():
    None
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
                    textoBaseDatos.set("")
                    textoTabla.set("")
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