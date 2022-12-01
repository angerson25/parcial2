# se importa la librería tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

# --------------------
# funciones de la app
# --------------------

def graficar_matriz():
    orden = int(x.get())
    for i in range (1, orden+1):
        coordenada1=0+(460-(460/i))
    
    
        rect1 = c.create_rectangle(coordenada1,coordenada1+(500/orden),coordenada1+(500/orden),coordenada1+(500/orden), fill="pink",outline="red")


def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará..")
    ventana_principal.destroy()

# ------------------
# ventana principal
# ------------------

# se crea una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas UIS")

# tamañan de la ventana
ventana_principal.geometry("500x660")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg= "black")

# ------------------
# variables globales
# ------------------

x = StringVar()
y = StringVar()

# ------------------------
# frame entrada datos
# ------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=90)
frame_entrada.place(x=10,y=10)



# etiqueta para x
lb_x = Label(frame_entrada, text = "Digite el orden de la matiz: ")
lb_x.config(bg="white", fg="blue", font=("Arial",14))
lb_x.place(x=10, y=10)

# entry para x
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Arial",14), justify=LEFT, fg="blue")
entry_x.focus_set()
entry_x.place(x=315,y=10,width=115, height=30)

# etiqueta para y
lb_y = Label(frame_entrada, text = "Numero a buscar: ")
lb_y.config(bg="white", fg="blue", font=("Arial",14))
lb_y.place(x=10, y=50)

# entry para y
entry_y = Entry(frame_entrada,textvariable=y)
entry_y.config(font=("Arial",14), justify=LEFT, fg="blue")
entry_y.place(x=315,y=50,width=115, height=30)

#variables
#orden = int(x.get())

# ------------------------
# frame operaciones
# ------------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=50)
frame_operaciones.place(x=10,y=110)

# boton para graficar
bt_calcular = Button(frame_operaciones, text="Graficar", command=graficar_matriz)
bt_calcular.place(x=45,y=10, width=100, height=30)

# boton para buscar
bt_borrar = Button(frame_operaciones, text="Buscar", command=salir)
bt_borrar.place(x=190,y=10, width=100, height=30)



# ------------------------
# frame resultados
# ------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=480)
frame_graficacion.place(x=10,y=170)

#creacion canvas
c = Canvas(frame_graficacion, width=460, height=460)
c.place(x=10, y=10)

# se ejecuta el metodo mainloop() de la clase Tk a través de la instancia ventana_principal.  Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc)  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()