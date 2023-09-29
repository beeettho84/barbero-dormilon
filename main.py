import time #libreria para uso de tiempo
from tkinter import *  # libreria para generacion de interfaces graficas
from PIL import ImageTk, Image #libreria para uso de labels con imagenes
import threading #libreria para uso de hilos
import random  # libreria para generacion de numeros aleatorios
import sys #libreria para el uso de cierre de procesos, ventanas e hilos

tenedores = [True, True, True, True, True]
root = Tk()
root.title("Comensales")#titulamos la ventana
root.geometry("850x450") #ingresamos las dimensiones que tendra la ventana

class filosofo:
    semaforo = 0
    te = 0
    n = 0
    img = ''
    corx = 0
    cory = 0
    hilo = threading.Thread()

    def __init__(self, num, imagen, px, py):
        self.n = num
        self.img = imagen
        self.corx = px
        self.cory = py
        self.actualizar()

    def iniciar(self):
        self.hilo = threading.Thread(target=self.esperar)
        self.hilo.start()

    def esperar(self):
        global tenedores
        self.semaforo = 0
        #print("Filosofo ", self.n, " espera")
        self.actualizar()
        if tenedores[self.n] and tenedores[self.n - 1]:
            tenedores[self.n] = False
            tenedores[self.n-1] = False
            #print("El filosofo",self.n,"Va a comer")
            self.comer()
        else:
            time.sleep(3)
            self.esperar()

    def comer(self):
        self.semaforo = 1
        print("Filosofo ", self.n, " come ")
        Frame(root, width=9, height=55, bg='#AA0000').place(anchor=N, x=cordXt[self.n], y=cordYt[self.n])
        Frame(root, width=9, height=55, bg='#AA0000').place(anchor=N, x=cordXt[self.n-1], y=cordYt[self.n-1])
        self.actualizar()
        self.te = (random.randint(1, 10))*3
        time.sleep(self.te)
        self.pensar()

    def pensar(self):
        global tenedores
        tenedores[self.n] = True
        tenedores[self.n - 1] = True
        self.semaforo = 2
        #print("Filosofo ", self.n, " Piensa")
        Label(root, image=imgTenedor, bg='#AA0000').place(anchor=N, x=cordXt[self.n], y=cordYt[self.n])
        Label(root, image=imgTenedor, bg='#AA0000').place(anchor=N, x=cordXt[self.n-1], y=cordYt[self.n-1])
        self.actualizar()
        self.te = (random.randint(1, 10)*3)
        time.sleep(self.te)
        self.esperar()

    def actualizar(self):
        if self.semaforo == 0:
            Label(root, image=self.img, bg='blue').place(anchor=N, x=self.corx, y=self.cory)
        elif self.semaforo == 1:
            Label(root, image=self.img, bg='green').place(anchor=N, x=self.corx, y=self.cory)
        elif self.semaforo == 2:
            Label(root, image=self.img, bg='yellow').place(anchor=N, x=self.corx, y=self.cory)

def correr():
    f0.iniciar()
    f1.iniciar()
    f2.iniciar()
    f3.iniciar()
    f4.iniciar()

def cerrar():
    sys.exit()
    root.destroy()

#declaracion de componentes
imgFil1 = Image.open("socrates.png") #indicamos que imagen usaremos
imgFil2 = Image.open("aristoteles2.jpg")
imgFil3 = Image.open("platon2.png")
imgFil4 = Image.open("diogenes.png")
imgFil5 = Image.open("hipocrates.png")
ac = Image.open("circulo rojo.png")
imgFil1 = imgFil1.resize((72,78),Image.LANCZOS) #redimensionamos la imagen y usamos LANCZOS para que no se pixelee
imgFil2 = imgFil2.resize((60,80),Image.LANCZOS)
imgFil3 = imgFil3.resize((90,80),Image.LANCZOS)
imgFil4 = imgFil4.resize((90,80),Image.LANCZOS)
imgFil5 = imgFil5.resize((90,80),Image.LANCZOS)
ac = ac.resize((300,300), Image.LANCZOS)
imgF1 = ImageTk.PhotoImage(imgFil1) #hacemos que sea intepretable para TKinter
imgF2 = ImageTk.PhotoImage(imgFil2)
imgF3 = ImageTk.PhotoImage(imgFil3)
imgF4 = ImageTk.PhotoImage(imgFil4)
imgF5 = ImageTk.PhotoImage(imgFil5)
aco = ImageTk.PhotoImage(ac)
#sibologia
Frame(root, bg='blue', width=30, height=30).place(anchor=N, x=30, y=15)
Label(root, text='Esperando').place(anchor=N, x=90, y=20)
Frame(root, bg='green', width=30, height=30).place(anchor=N, x=30, y=55)
Label(root, text='Comiendo').place(anchor=N, x=90, y=60)
Frame(root, bg='yellow', width=30, height=30).place(anchor=N, x=30, y=95)
Label(root, text='Pensando').place(anchor=N, x=90, y=100)

#orden elegido por el acomodo de interfaz grafica
f0 = filosofo(0, imgF1, 270, 120)
f4 = filosofo(4, imgF4, 450, 10)
acom = Label(root, image=aco, ).place(x=300, y=80)
f1 = filosofo(1, imgF2, 280, 300)
f2 = filosofo(2, imgF3, 635, 300)
f3 = filosofo(3, imgF5, 650, 120)
btnInicio = Button(root, text="Iniciar", font="Arial 14 bold", command= lambda: correr()).place(anchor=N, x=400, y=400)
btnCerrar = Button(root, text="Cerrar", font="Arial 14 bold", command= lambda: cerrar()).place(anchor=N, x=500, y=400)
#colocar platos
cordX = [360, 450, 380, 520, 550]
cordY = [150, 90, 290, 290, 150]
#colocar tenedores
cordXt = [330, 450, 580, 520, 380]
cordYt = [210, 310, 220, 110, 110]
imgpl = Image.open("spagheti.png")
imgpl = imgpl.resize((50,50), Image.LANCZOS)
imgPlato = ImageTk.PhotoImage(imgpl)
imgt = Image.open("tenedor.png")
imgt = imgt.resize((9,50), Image.LANCZOS)
imgTenedor = ImageTk.PhotoImage(imgt)
for i in range(5):
    Label(root, image=imgPlato, bg='#AA0000').place(anchor=N, x=cordX[i], y=cordY[i])
    Label(root, image=imgTenedor, bg='#AA0000').place(anchor=N, x=cordXt[i], y=cordYt[i])

root.mainloop()
