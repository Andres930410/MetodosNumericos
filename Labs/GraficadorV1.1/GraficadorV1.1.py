from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import sys
from sympy import diff,Symbol



class Mover:
    def __init__(self, rect):
        self.rect = rect
        self.press = None
        

    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes: return

        contains, attrd = self.rect.contains(event)
        if not contains: return
        print ('event contains', self.rect.get_xdata())
        
        
        x0 = self.rect.get_xdata()
        self.press = x0, event.xdata

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None: return
        if event.inaxes != self.rect.axes: return
        x0, xpress  = self.press
        dx = event.xdata - xpress
        #dy = event.ydata - ypress
        #print 'x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f'%(x0, xpress, event.xdata, dx, x0+dx)
        self.rect.set_xdata(x0+dx)
        
        
        #self.rect.set_y(y0+dy)
        
        self.rect.figure.canvas.draw()


    def on_release(self, event):
        'on release we reset the press data'
        self.press = None
        self.rect.figure.canvas.draw()
        
        
        
    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)
        



class Graficador():
    look = None
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Graficador")
        self.frame = ttk.Frame(self.root)
        self.frame.pack()
        
        #self.frame = Frame(self.root)
        self.root.maxsize(450, 250)
        
        
        self.b2=ttk.Button( self.frame, text='Salir',command=self.Salir).grid(row=4,column=0,columnspan=2)
        self.b1=ttk.Button( self.frame, text="Graficar",command=self.Graficar).grid(row=4,column=3,columnspan=2)
        self.textoentry=StringVar()
        self.textoentry1=StringVar()
        self.textoentry2=StringVar()
        self.entry1=ttk.Entry(self.frame,textvariable=self.textoentry,width=20).grid(row=1,column=2,columnspan=2)
        self.label1=ttk.Label(self.frame,text="Funcion").grid(row=1,column=1)
        self.entry2=ttk.Entry(self.frame,textvariable=self.textoentry1,width=9).grid(row=2,column=3)
        self.entry3=ttk.Entry(self.frame,textvariable=self.textoentry2,width=9).grid(row=2,column=2)
        self.label2=ttk.Label(self.frame,text="Rango  ").grid(row=2,column=1)
        self.valor = StringVar()
        self.metodos  = ('Biseccion', 'Falsa Posicion', 'Newton-Rapson',"Secante")
        self.metodos1 = ttk.Combobox(self.frame, textvariable = self.valor, values = self.metodos, state = 'readonly',width=15)
        self.metodos1.grid(row=3,column=2,columnspan=2)
        self.metodos1.current(0)
        self.label3=ttk.Label(self.frame,text="Metodo  ").grid(row=3,column=1)
        
        
        self.root.resizable(0,0)
        #self.root.pack()
        self.frame.mainloop(0)
        
                
        
 
        
#    def mostrar(self): self.root.deiconify() # Muestra una ventana
#    def ocultar(self):self.root.iconify() # Oculta una ventana
    def Graficar(self):  
        self.temp = self.textoentry.get()
        self.temp4 = self.valor.get()
        temp1 = self.textoentry1.get()
        temp2 = self.textoentry2.get()
        try:
            self.m=float(temp1)
            self.n=float(temp2)
            limit=0
        except ValueError:
            limit=1
        if(self.temp!=""):
            try:
                x = arange(self.n,self.m,0.1)
                eval(self.temp)
                funcion=0
            except :
                funcion=1
        else:
            funcion=1
        if(limit==0 and funcion==0):#Hay una funcion
    
            self.textoentry.set("")
            self.textoentry1.set("")
            self.textoentry2.set("")
            
            x = arange(self.n,self.m,0.1)
           
            temp5=self.valor.get()
            
            fig = plt.figure("Graficador")
            self.ax = fig.add_subplot(111)
            if(temp5!="Newton-Rapson"):
                self.rects = self.ax.axvline(self.n+0.1, linewidth=4,color = 'g') 
                self.rects1 = self.ax.axvline(self.m-0.1, linewidth=4,color = 'g')
           
                drs = []
                self.dr = Mover(self.rects)
                self.dr1 = Mover(self.rects1)
                self.dr.connect()
                self.dr1.connect()
                drs.append(self.dr)
                drs.append(self.dr1)
                
            else:
                self.rects = self.ax.axvline(self.n+0.1, linewidth=4,color = 'g') 
                self.rects1 = self.ax.axvline(self.m, linewidth=0.01,color = 'g')
                drs = []
                self.dr = Mover(self.rects)
                self.dr.connect()
                drs.append(self.dr)
            
            plt.ylabel('Eje y')
            plt.xlabel('Eje x')
            plt.title(self.temp)
            self.ax.plot(x,eval(self.temp))
            #self.ax.axvspan(self.n+0.1,self.m-0.1, alpha = 0.25)
            plt.grid()
            
            plt.show()
            
            self.a1=self.rects.get_xdata()
            self.a2=self.rects1.get_xdata()
            self.elegirMetodo(self.a1,self.a2)
           
        limit=0 
        funcion=0
    def f(self,x):
        return eval(self.temp)    
    def funcion(self,ecuacion ,x):
        return eval(ecuacion) 
    def elegirMetodo(self,a1,b1):
        if self.temp4=="Biseccion":
            self.Biseccion(float(a1[0]), float(b1[0]))
        elif self.temp4=="Falsa Posicion" :
            self.PosicionFalsa(float(a1[0]), float(b1[0]))
        elif self.temp4=='Newton-Rapson':
             self.NewtonRapson(float(a1[0]))
        elif self.temp4=="Secante":
             self.Secante(float(a1[0]), float(b1[0]))
        
    def Biseccion(self,a,b):
        print("Biseccion")
        print("Comenzando en el intervalo(",a,b,")")
        temp = self.f(a)
        while True:
            xmed=(a+b)/2
                
            temp1= self.f(xmed) #guarda el valor de la funcion en el valor de la mitad del intervalo
            if temp1==0.0:
                break
            if (temp*temp1)<0:
                b=xmed
            else:
                temp = temp1
                a=xmed
            error=abs((b-a)/(b+a))
            if error<0.00000001:
                break
        print("la raiz es:",xmed)
    def PosicionFalsa(self,xl,xu):
        print("Posicion Falsa")
        print("Comenzando en el intervalo(",xl,xu,")")
        temp = self.f(xl)
        temp1 = self.f(xu)
        while(True):
            xold = xmed
            xmed = xu -(temp1*(xl-xu))/(temp-temp1)
            temp2 = self.f(xmed) 
            if temp2==0.0:
                break
            if temp*temp2 < 0:
                xu = xmed
                temp1 = temp2
                contadorInferior+=1 #solo se esta acercando por el lado del limite superior
                contadorSuperior=0
                if contadorInferior == 3:
                    contadorInferior = 0 #Se reinicia el contador de acercamiento
                    temp = temp/2 #Acercamos la funcion por el limite inferior
            else:
                xl = xmed
                temp = temp2
                contadorSuperior+=1 #solo se esta acercando por el lado del limite inferior
                contadorInferior=0
            if contadorSuperior == 3:
                contadorSuperior = 0 #Se reinicia el contador de acercamiento
                temp1 = temp1/2 #Acercamos la funcion por el limite superior
                error = abs((xmed-xold)/xmed)*100    
            if error < 0.00000001:
                break
    
        print ("La raiz es:",xmed)
    def NewtonRapson(self,x0):
        print("Newton Rapson")
        print("Comenzando en el intervalo(",x0,")")
        x = Symbol('x')
        derivative = str(diff(self.temp,x))#derivada de la ecuacion
                         
        while(True):
            temp = self.f(x0)#funcion calculada en el punto
            temp1 = self.funcion(derivative ,x0)#deriva calculada en el punto
    
            if(temp1!=0):
                x_i= x0 -(temp/temp1)#verificamos que la derivada no de cero o si no da una divicion por cero
            else:   
                #elejimos un nuevo punto
                x_i = input("Introdusca un nuevo valor inicial")
            if self.f(x_i)==0:
                break
            if x_i!=0:#se calcula el error  
                errorAbsoluto = abs(((x_i-x0)/x_i))*100
    
                x0=x_i#volvemos el el x nuevo como el nuevo x viejo para proceder a calcular el otro
            if errorAbsoluto < 0.00000001:
                break
    
        print("La solucion es :",x0)
    def Secante(self,x1,x2):
        print("Secante")
        print("Comenzando en el intervalo(",x1,x2,")")
        while(True):
            temp = self.f(x1)
            temp1 = self.f(x2)
            xtemp = x2-(temp1*(x1-x2))/(temp-temp1)
            x1=x2
            x2=xtemp
    
            if(self.f(xtemp)==0.0):
                break
            error = abs((x2-x1)/x2)*100
            if(error < 0.00000001):
                break;
        print("La raiz es:",x2)
        
    def Salir(self):
        self.frame.quit()
    


  
if __name__ == '__main__':
    
    Graficador()
    

    