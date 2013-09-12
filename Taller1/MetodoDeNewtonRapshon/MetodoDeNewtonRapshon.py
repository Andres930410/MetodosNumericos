##################################################                                                
#                                                #
#         Metodo de Newthon-Rapshon              #                  
#         @AndresGutierrez                       #                 
#                                                #
#                                                #
##################################################

from sympy import *
from math import *

ecuacion = input("Introdusca la funcion: ")
x0 = float(input('Introdusca el valor incial: '))
errordeseado = float(input('Introdusca el valor del  error deseado: '))
errorAbsoluto = 100
x = Symbol('x') #defino la variablr con respecto a la cual se deriva
def funcion(ecuacion ,x):
    return eval(ecuacion)
derivative = str(diff(ecuacion,x))#derivada de la ecuacion
while(True):
    temp = funcion(ecuacion , x0)#funcion calculada en el punto
    temp1 = funcion(derivative ,x0)#deriva calculada en el punto
    
    if(temp1!=0):
        x_i= x0 -(temp/temp1)#verificamos que la derivada no de cero o si no da una divicion por cero
    else:   
        #elejimos un nuevo punto
        x_i = input("Introdusca un nuevo valor inicial")
    if funcion(ecuacion ,x_i)==0:
        break
    if x_i!=0:#se calcula el error  
        errorAbsoluto = ((x_i-x0)/x_i)*100
    
    x0=x_i#volvemos el el x nuevo como el nuevo x viejo para proceder a calcular el otro
    if errorAbsoluto < errordeseado:
        break
    
print("La solucion es :",x0)