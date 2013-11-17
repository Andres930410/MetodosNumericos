from numpy import *
import matplotlib.pyplot as plt
import sympy as ans


plt.figure('Interpolacion') 

l=(loadtxt("matriz.dat"))
x = l[0,:]#asignamos toda la primera fila
y = l[1,:]#asignamos toda la segunda fila

x1 = int(input("Introdusca el valor a interpolar: "))
n=len(x)
yi=0
pol=""


for i in range(0,n):
    producto=y[i]
    termino=str(y[i])
    for j in range(0,n):
        if(i!=j):
            producto = producto*(x1-x[j])/(x[i]-x[j]) #factores de langrage
            termino=termino+"*(x-"+str(x[j])+")/("+str(x[i])+"-"+str(x[j])+")"
    yi=yi+producto#resultado de la interpolacion
    pol = pol+"+"+termino
print(yi)
plt.subplot(2,1,1)
plt.ylabel('Eje y')
plt.xlabel('Eje x')
x1 = x
plt.scatter(x1,y)
plt.grid()
plt.subplot(2,1,2)
plt.ylabel('Eje y')
plt.xlabel('Eje x')


x=arange(x[0],x[len(x)-1]+0.1,0.1)

pol = str(ans.factor(pol))
plt.title("p(x)="+pol)
plt.plot(x,eval(pol))
plt.grid()

plt.show()
