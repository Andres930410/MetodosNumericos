from numpy import * 
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
import sympy as ans



class LineBuilder:
    def __init__(self, line):
        self.press = None
        self.line = line
        self.cidpress = line.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = line.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = line.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.line.axes: return

        contains, attrd = self.line.contains(event)
        if not contains: return
        print ('event contains', self.line.get_xdata(),self.line.get_ydata())
        x0, y0 = self.line.get_xdata(),self.line.get_ydata()
        self.press = x0, y0, event.xdata, event.ydata

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None: return
        if event.inaxes != self.line.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print 'x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f'%(x0, xpress, event.xdata, dx, x0+dx)
        self.line.set_xdata(x0+dx)
        self.line.set_ydata(y0+dy)

        self.line.figure.canvas.draw()


    def on_release(self, event):
        'on release we reset the press data'
        self.press = None
        self.line.figure.canvas.draw()

class Interpolar:
    def __init__(self, line):
        self.lines=line
    def interpolar(self,event):
        plt.figure("Interpolacion")
        x=[]
        y=[]
        for i in self.lines:
            x.append(float(i.get_xdata()))
            y.append(float(i.get_ydata()))
        print(x)
        print(y)
        x1 = float(input("Introdusca el valor a interpolar: "))
        self.Lagrange(x,y,len(x),x1)
        self.Newton(x,y,len(x),x1)
        
    def Lagrange(self,x,y,n,x1):
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
        pol=str(ans.factor(pol))
   
        x = sorted(x)
        x=arange(x[0],x[len(x)-1]+0.1,0.1)

        plt.subplot(2,1,1)
        plt.title("p(x)="+pol)
        plt.plot(x,eval(pol))
        plt.grid()
        
    def Newton(self,x,y,n,x1):
        
        a = zeros(n**2).reshape(n,n)#La tabla de valores de la intepolacion
        a[:,0]=y
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
        x2=[]
        for z in range(len(x)):
            x2.append((x[z]*-1))
        
        for j in range(1,n):
            signo=""
            if(a[0,j])>=0:
                signo="+"
            xt=""
            for i in range(0,j):
                signo2=""
                if x2[i]>=0:
                    signo2="+"
                xt=xt+"*(x"+signo2+str(x2[i])+")"
            p=p+signo+str(a[0,j])+xt
        p=str(ans.factor(p))
        x = sorted(x)
        x=arange(x[0],x[len(x)-1]+0.1,0.1)

        plt.subplot(2,1,2)
        plt.title("p(x)="+p)
        plt.plot(x,eval(p))
        plt.grid()
        plt.show()
    

fig = plt.figure("Puntos")
ax = fig.add_subplot(111)
l=(loadtxt("matriz.dat"))
x = l[0,:]#asignamos toda la primera fila
y = l[1,:]#asignamos toda la segunda fila
plt.grid()
dr=[]
lines=[]
for m in range(len(x)):
    line, = ax.plot(x[m],y[m],"bo")  # empty line
    print(x[m],y[m])
    lines.append(line)
    dr.append(LineBuilder(line))
interpolar1=Interpolar(lines)
plt.subplots_adjust(bottom=0.2)
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Interpolar')
bnext.on_clicked(interpolar1.interpolar)

plt.show()

#interpolar1.interpolar()