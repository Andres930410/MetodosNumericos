##################################################                                                
#                                                #
#         Metodo de la Secante                   #                  
#         @AndresGutierrez                       #                 
#                                                #
#                                                #
##################################################
from math import *

ecuacion= input("Introdusca la funcion: ")
x1=float(input('Introdusca el extremo inferior del intervalo aproximado: '))
x2=float(input('Introdusca el extremo superior del intervalo aproximado: '))
errordeseado=float(input('Introdusca el valor del  error deseado: '))

def f(x):
    return eval(ecuacion)

while(True):
    temp = f(x1)
    temp1 = f(x2)
    xtemp = x2-(temp1*(x1-x2))/(temp-temp1)
    x1=x2
    x2=xtemp
    print(x1,x2)
    if(f(xtemp)==0.0):
        break
    error = abs((x2-x1)/x2)*100
    if(error < errordeseado):
        break;
print("La raiz es:",x2)