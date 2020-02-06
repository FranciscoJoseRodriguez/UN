#Hecho por Francisco Jose Rodriguez
#Math Tool Box es un proyecto creado con GNU/Linux 

from tkinter import *
from tkinter import messagebox
import tkinter as tk
import math

#Funciones

#En la epoca Griega Antigua, los matematicos se enfrentaron a un problema que no podian solucionar.
#El problema de Basilea era un jaleo para los matematicos, calcular la suma de los inversos cuadrados.
#Leonhard Euler luego de mucho tiempo resolvio este problema, su resultado fue pi elevado al cuadrado sobre seis.
#Luego tenemos que Pi sera igual a la raiz del factor entre la sucesion y la seis.
 
def Basilea():
    a = 0
    b = 0
    for i in range(1, Basilea_limit.get() + 1):
        a = (1 / i ** 2)
        b = a + b
    c = math.sqrt(6*b)
    messagebox.showinfo("Resultado", "El resultado es: " + str(c))

#EL numero e en honor a Lonhard Euler es una constante que aparece de manera natural en muchos lugares.
#Su utilidad en los logaritmos naturales es indispensable, ademas es un numero muy recurrente en la economía o la forensía.
#Calcular su recurrencia es facil ya que se hace mediantes la suma (1 + 1/n)**n


def Euler():
    a = 0
    for i in range(1, E_limit.get() + 1):
        a = (1 + 1/i)**i
    messagebox.showinfo("Resultado", "El resultado es: " + str(a))

#El numero mas bello del mundo, el numero aureo, de proporciones perfectas, aparece de manera natural en los cuerpos.
#Debemos su descubrimiento a Pizzano Leonardo, (Fibonacci), pues fue el quien se dio cuenta de su recurrencia en el arte de aquella epoca.
#No es facil calcular este numero por su caprichoso comportamiento, pero sabemos que es (1+ raíz de 5)/2
#Aprovechando esta particularidad solo debemos hallar la razí de cinco.
#[Para mas información ver la funcion Root] 
def Phi():
    a = 0
    for i in range(1, Phi_limit.get() + 1):
        a = (1 + 1/i)**i
    b=(1/2) * math.log(5,a)
    r = a ** b
    c = (1+r)/2
    messagebox.showinfo("Resultado", "El resultado es: " + str(c))

#El numero e tiene muchas propiedades, una de ellas es su equivalencia en las raices.
#La raiz de un x es igual a e elevado a un medio del logaritmo natural de x
#Luego entre mayor precision en e tengamos, mayor precision tendra nuestra raíz.

def Root():
    c = Root_n.get()
    for i in range(1, Root_limit.get() + 1):
        a = (1 + 1/i)**i
    b=(1/2) * math.log(c,a)
    r = a ** b
    messagebox.showinfo("Resultado", "El resultado es: " + str(r))

ventana = Tk()
Basilea_limit = IntVar()
E_limit = IntVar()
Phi_limit = IntVar()
Root_n = IntVar()
Root_limit = IntVar()
ventana.geometry("630x430")
ventana.title("Math Tool Box (Beta 0.1)")

#Numeros irracionales
Message_1 = Label(ventana, text="Ingresa el limite de Basilea").place(x=160, y=10)
Entrance_1 = Entry(ventana, textvariable=Basilea_limit).place(x=380, y=10)
Button_1 = Button(ventana, text="Aceptar", command=Basilea).place(x=310, y=50)
Message_2 = Label(ventana, text="Ingresa el limite de e").place(x=160, y=110)
Entrance_2 = Entry(ventana, textvariable=E_limit).place(x=380, y=110)
Button_2 = Button(ventana, text="Aceptar", command=Euler).place(x=310, y=150)
Message_3 = Label(ventana, text="Ingresa el limite de phi").place(x=160, y=210)
Entrance_3 = Entry(ventana, textvariable=Phi_limit).place(x=380, y=210)
Button_3 = Button(ventana, text="Aceptar", command=Phi).place(x=310, y=250)
Message_4 = Label(ventana, text="Ingresa la raíz a calcular").place(x=160, y=310)
Entrance_4 = Entry(ventana, textvariable=Root_n).place(x=380, y=310)
Message_4_1 = Label(ventana, text="Ingresa el limite de la raíz").place(x=160, y=340)
Entrance_4_1 = Entry(ventana, textvariable=Root_limit).place(x=380, y=340)
Button_4 = Button(ventana, text="Aceptar", command=Root).place(x=310, y=390)

ventana.mainloop()

