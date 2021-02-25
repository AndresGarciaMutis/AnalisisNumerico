# FUNCION A RESOLVER

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 2, 0.1)
tolerancia = [10**-8, 10**-16, 10**-32, 10**-56]


def f(x):
    return x*np.sin(x) - 1


def secant(x0,x1,e,N):
    step = 1
    con = True
    funcion = []
    res = []
    valores = np.arange(-1, 2, 0.1)
    
    for k in valores:
        funcion.append(f(k))

    while con:
        if f(x0) == f(x1):
            print('Error, No se pude dividir en cero')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('Iteracion-%d, x2 = %0.6f Y f(x2) = %0.6f ' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
        res.append(x2)
     
        tol = str(e)
        x =[x0, x1, x2]
        y =[f(x0), f(x1), f(x2)]
        plt.plot(valores,funcion)
        plt.plot(x, y)
        plt.title("Metodo de la secante en xsin(x)-1 con tol: " + tol)
        plt.ylabel("F(x)")
        plt.xlabel("x")
        plt.show()
        
        if step > N:
            print('No Convergente')
            break
        
        con = abs(f(x2)) > e
    print('\n Resultado de la raiz: %0.24f' % x2)
    return res



    
        
def SecanteAitken(p0,tolerance): 
                
    while True:                 
        p1 = 1+f(p0)
        p2 = 1+f(p1)
        
        if abs(p1-p0) < tolerance: break
        p0 = p0 - (p1-p0)**2/(p0+p2-2*p1)
            
   
    return p0
        


##Gráfica de la funcion
funcion = []
for k in x:
    funcion.append(f(k))
    
plt.plot(x,funcion)
plt.show()



x0 = -1
x1 = 2
N = 25
#secant(x0,x1,10**-8,N)
y  =[]
xx= []
for i in tolerancia:
    tol = str(i)
    print("Tolerancia: ", i)
    y = secant(x0,x1,i,N)
    y = sorted(y)
    for k in y:
        xa = SecanteAitken(k,i)
        xx.append(xa)

    plt.plot(xx,y)
    plt.title("Secante-Aitken de xsin(x)-1 con tol: " + tol)
    plt.show()

#x = np.arange(0,10,0.1)



