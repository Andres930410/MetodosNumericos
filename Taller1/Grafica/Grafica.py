##################################################                                                
#                                                #
#         Graficas                               #                  
#         @AndresGutierrez                       #                 
#                                                #
#                                                #
##################################################

import numpy as np 
import matplotlib.pyplot as plt
import math
plt.figure('Graficas') 
x=np.arange(0,2.1,0.1)
#y=2*np.sin(4*x)-x**2+10*x  #f(x)=2sin(4x)-x^2+10x
y=3/(x+1) -1.8
plt.subplot(2,2,1) #Dividimos la ventana 2filas y 2columnas y se pinta en la 1fila,1col
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.title('f(x) = 3/(x+1) -1.8')
plt.annotate('Raiz', xy=(0.66664,0), xytext=(1, 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05),)
plt.plot(x,y)
plt.grid()
plt.subplot(2,2,2) #Dividimos la ventana 2filas y 2columnas y se pinta en la 1fila,2col
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.title('f(x) = sin(x) + cos (x) -1.1')
x1=np.arange(0,0.61,0.01)
y1 = np.sin(x1) + np.cos (x1) -1.1
plt.annotate('Raiz', xy=(0.10542,0), xytext=(0.2, -0.1),
            arrowprops=dict(facecolor='black', shrink=0.05),)
plt.plot(x1,y1)
plt.grid()
plt.subplot(2,1,2)#Dividimos la ventana 2filas y 1columnas y se pinta en la 2fila,1col
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.title('f(x) = 1/6[(6^(1/7))/(x^(6/7))]-0.1')
x2=np.arange(2,3.1,0.1)
y2=(0.215284723)/(x2**0.857142857)-0.1
plt.annotate('Raiz', xy=(2.44153,0), xytext=(2.5, -0.015),
            arrowprops=dict(facecolor='black', shrink=0.05),)
plt.plot(x2,y2)
plt.grid()

plt.show()
