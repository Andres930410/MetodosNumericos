##################################################                                                
#                                                #
#         Metodo de la Biseccion                 #                  
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
temp = f(x1) #guarda el valor de la funcion en el limite inferior
while True:
    xmed=(x1+x2)/2
    temp1= f(xmed) #guarda el valor de la funcion en el valor de la mitad del intervalo
    if temp1==0.0:
        break
    if (temp*temp1)<0:
        x2=xmed
    else:
        temp = temp1
        x1=xmed
    error=abs((x2-x1)/(x2+x1))
    if error<errordeseado:
        break
print("la raiz es:",xmed)

