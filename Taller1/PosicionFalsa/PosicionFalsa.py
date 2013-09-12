##################################################                                                
#                                                #
#       Metodo de la Posicion Falsa Mejorada     #                  
#       @AndresGutierrez                         #                 
#                                                #
#                                                #
##################################################
from math import *
ecuacion = input("Introdusca la funcion: ")
xl = float(input("Intoduszca el limite inferior: "))
xu = float(input("Introduzca el limite superior: "))
ea = float(input("Introduzca el valor del error deseado: "))
contadorSuperior,contadorInferior,xmed= 0,0,0
def funcion(x):
    return eval(ecuacion)
temp = funcion(xl)
temp1 = funcion(xu)
while(True):
    xold = xmed
    xmed = xu -(temp1*(xl-xu))/(temp-temp1)
    temp2 = funcion(xmed) 
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
    if error < ea:
        break
    
print ("La raiz es:",xmed)
    