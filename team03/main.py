import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from principalManager import BPlusMode as bp

def informacion():
    messagebox.showinfo("INFORMACION", "GRUPO NO. 3 \n Josue Gonzalez") 


#---------------VENTANAS-------------------
def ventanaBD():

    def ventanaMostrarTabla():
        ventana3=Toplevel()
        ventana3.geometry("800x500")
        ventana3.title="TABLAS"
        messagebox.showinfo("info", "elemento seleccionado: " + my_listbox.get(ANCHOR))

    def abrirImagenDB():
            #exist path ..
        if os.path.isfile('complete.png')==True:
            #open File
            os.system('complete.png')
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
    #lista=[]
    lista= bp.server.generarReporteDB()
    print(bp.server.generarReporteDB())
 
    for item in lista:
        my_listbox.insert(END, item)
        #MUESTRA EL ITEM SELECCIONADO
        #messagebox.showinfo("msj", my_listbox.get(ANCHOR))
    botonTablas=Button(ventana2, text="Mostrar tablas", command=ventanaMostrarTabla,bg="green", fg="white").place(x=625 +15,  y=175)      



  
    
def ventanaFunciones():
    ventanaFun=Toplevel()
    ventanaFun.geometry("800x500")
    ventanaFun.title="Funciones de Base de datos"

            
    def createDatabase():

        if texto.get()=="":
            messagebox.showwarning("ADVERTENCIA", "Debe colocarle un nombre a  la base de datos...")
            
        else:
            bp.createDatabase(texto.get())



            texto.set("")
    def showDatabase():
        messagebox.showinfo("info", "metodo showDatabase")
    
    

    def alterDatabase():
        messagebox.showinfo("info", "contiene old: "+ textoOld.get())
        messagebox.showinfo("info", "contiene new: "+ textoNew.get())
        textoOld.set("")
        textoNew.set("")


    

    
    #CREAR BASE DE DATOS-------------------------------------
    boton1=Button(ventanaFun, text="CREAR BD", command=createDatabase, width="20").place(x=50, y=100)
    texto = StringVar()
    Label(ventanaFun, text="Nombre de BD").place(x=250, y=80)
    textoBD= Entry(ventanaFun, textvariable=texto, width="40" ).place(x=250, y=100 + 5)
    
    #MOSTRAR BASE DE DATOS-------------------------------------
    botonMostrarBD=Button(ventanaFun, text="MOSTRAR BD's", command=showDatabase, width="62", bg="yellow").place(x=50, y=150)
    
    #ALTER BASE DE DATOS-------------------------------------
    botonModificar=Button(ventanaFun, text="ALTER BD", command=alterDatabase, width="20").place(x=50, y=200)
    
    textoOld = StringVar()
    Label(ventanaFun, text="Old:").place(x=250, y=200 -10)
    cajaOld= Entry(ventanaFun, textvariable=textoOld, width="20" ).place(x=250, y=200+10)

    textoNew = StringVar()
    Label(ventanaFun, text="New:").place(x=250 + 150, y=200 -10)
    cajaNew= Entry(ventanaFun, textvariable=textoNew, width="20" ).place(x=250+ 150, y=200+10)

    

#-------------FIN VENTANAS-----------------    

#---------------VENTANA PRINCIPAL-------------------
ventana=tk.Tk()
ventana.title("STORAGE MANAGER - GROUP3")
ventana.resizable(0,0) 

#ventana.geometry('1400x780')

#creando el frame para poder colocar cosas dentro
miFrame=Frame()
miFrame.pack()

miFrame.config(width="600", height="200")
miFrame.config(bd=12)


miFrame.config(cursor="plus")

imagen =PhotoImage(file="logoTytus.png")
fondo=Label(miFrame, image=imagen).place(x=100,y=-20)


boton1=Button(miFrame, text="BASES DE DATOS", command=ventanaBD).place(x=150, y=100)
boton1=Button(miFrame, text="FUNCIONES", command=ventanaFunciones).place(x=300, y=100)
ventana.mainloop()
#--------------- FIN VENTANA PRINCIPAL-------------------