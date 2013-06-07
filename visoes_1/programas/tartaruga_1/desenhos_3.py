#-*- coding: utf-8 -*-


from turtle import *
from math import *

def linha(x1,y1,x2,y2):
    """ Traça uma linha entre dois pontos."""
    up()
    goto(x1,y1)
    pd()
    goto(x2,y2)
    up()
    
def grafico(func, inf, sup):
    """Faz o gráfico da função entre os dois valores."""
    delta = 0.1
    x = inf
    pu()
    goto(inf,func(x))
    pd()
    while x < sup:
        x = x + delta
        goto(x,func(x))
        
def grafico_2(func,inf, sup, n):
	"""Faz o gráfico da função entre inf e sup usando n segmentos."""
	pass
	
def derivada(func,x):
    delta_x = 0.1
    return (func(x + delta_x) - func(x))/delta_x

def main():
    # eixos
    setworldcoordinates(-pi,-2,pi,2)
    linha(-pi,0,pi,0)
    linha(0,-2,0,2)
    # inicializa
    pen(pensize=3, pencolor='red')
    grafico(sin, -pi,pi)
    pen(pencolor='blue')
    grafico(cos,-pi,pi)
    hideturtle()
    exitonclick()
    
if __name__ =='__main__':
    main()
    
             
        