from numpy import *
import matplotlib.pyplot as plt
import sympy as ans

plt.figure('Interpolacion') 
l=(loadtxt("matriz.dat"))
x = l[0,:]#asignamos toda la primera fila
y = l[1,:]#asignamos toda la segunda fila

n=len(x)
#obtener tablas de diferencias
a = zeros(n**2).reshape(n,n)#La tabla de valores de la intepolacion
a[:,0]=y
x1 = int(input("Introdusca el valor a interpolar: "))
for j in range(1,n):
    for i in range(0,n-j):
        a[i,j]=(a[i+1,j-1]-a[i,j-1])/(x[i+j]-x[i])

#Encontrar el valor interpolado
xtemp=1
ytemp=a[0,0]
for j in range(0,n-1):
    xtemp=xtemp*(x1-x[j]) 
    ytemp=ytemp+a[0,j+1]*xtemp
    
print(ytemp)

#Construir la ecuacion
p=str(a[0,0])
xx=x*-1

for j in range(1,n):
    signo=""
    if(a[0,j])>=0:
        signo="+"
    xt=""
    for i in range(0,j):
        signo2=""
        if xx[i]>=0:
            signo2="+"
        xt=xt+"*(x"+signo2+str(xx[i])+")"
    p=p+signo+str(a[0,j])+xt
plt.subplot(2,1,1)
plt.ylabel('Eje y')
plt.xlabel('Eje x')
x1 = x
plt.scatter(x1,y)
plt.grid()
plt.subplot(2,1,2)
plt.ylabel('Eje y')
plt.xlabel('Eje x')
p=str(ans.factor(p))
plt.title("p(x)="+p)

x=arange(x[0],x[len(x)-1]+0.1,0.1)
plt.plot(x,eval(p))
plt.grid()

plt.show()