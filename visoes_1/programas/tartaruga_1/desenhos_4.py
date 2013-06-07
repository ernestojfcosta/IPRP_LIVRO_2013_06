#-*- coding: utf-8 -*-


import matplotlib
from pylab import *


    
def grafico(etiqueta,func, inf, sup, delta=0.001):
    """Faz o gráfico da função entre os dois valores."""
    t = arange(inf,sup,delta)

    plot(t,func(t), label=etiqueta)
    
        

def derivada(func,x):
    delta_x = 0.1
    return (func(x + delta_x) - func(x))/delta_x



    
if __name__ =='__main__':
    xlabel('x')
    ylabel('f(x)')
    axhline(color='gray')
    axvline(color='gray')
    grafico('Seno de x',sin,-pi,pi)
    grafico('Coseno de x', cos,-pi,pi)
    grid()
    legend(loc='upper left')
    show()
             
        