# -*- coding: utf-8 -*-

import turtle

def grafico(funcao,inicio,num,cor):
    """
    Faz o gráfico da função a partir do ponto inic.
    """
    x = inicio
    turtle.pencolor(cor)
    turtle.up()
    turtle.goto(x,0)
    turtle.down()
    turtle.dot(6)
    
    for i in range(1,num):
        x = funcao(x)
        turtle.goto(i,x)
        turtle.dot(6)

# Funções de teste        
def f(x):
    return 3.9*x*(1 - x)

def g(x):
    return 3.9 * (x - x**2)

def h(x):
    return 3.9*x - 3.9*x*x

def main(n):
    turtle.setworldcoordinates(-1.0,-0.1,n+1,1.1)
    grafico(f,0.35,n,'red')
    grafico(g,0.35,n,'green')
    grafico(h,0.35,n,'blue')
    turtle.exitonclick()
    
if __name__ == '__main__':
    main(80)

        