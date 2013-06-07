# _*_ coding: utf-8 _*_

from turtle import *
from frange import float_range 
from math import cos

def linha(x1,y1,x2,y2):
    """ Desenha uma linha entre os pontos referidos."""
    pu()
    goto(x1,y1)
    pd()
    goto(x2,y2)
    
def grafico(funcao,inf, sup, incremento):
    """ Calcula os pontos da função entre inf e sup, com 
    incrementos de incremento."""
    pu()
    goto(inf, funcao(inf))
    pd()
    for x in float_range(inf+incremento,sup + incremento, incremento):
        goto(x,funcao(x))
       

def derivada(funcao, delta_x):
    """ Calcula a derivada de uma função."""
    def d(x):
        return (funcao(x + delta_x) - funcao(x)) / float(delta_x)
    return d
    
def main():
    setworldcoordinates(-4,-2,4,2)
    linha(-4,0,4,0)
    linha(0,-2,0,2)
    pensize(3)
    pencolor('green')
    dx = 0.1
    grafico(cos, -4,4,dx)
    pencolor('red')
    grafico(derivada(cos,dx),-4,4,dx)
    hideturtle()
    exitonclick()
    
    
if __name__ == '__main__':
    main()