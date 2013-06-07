import turtle
import math

def linha(x1,y1,x2,y2):
    """ Traça uma linha entre dois pontos."""
    turtle.up()
    turtle.goto(x1,y1)
    turtle.pd()
    turtle.goto(x2,y2)
    turtle.up()
    
def grafico(func, inf, sup):
    """Faz o gráfico da função entre os dois valores."""
    delta = 0.1
    x = inf
    turtle.pu()
    turtle.goto(inf,func(x))
    turtle.pd()
    while x < sup:
        x = x + delta
        turtle.goto(x,func(x))
        
def grafico_2(func,inf, sup, n):
	"""Faz o gráfico da função entre inf e sup usando n segmentos."""
	pass
	
def derivada(func,x):
    delta_x = 0.1
    return (func(x + delta_x) - func(x))/delta_x

def main():
    # eixos
    turtle.setworldcoordinates(-pi,-2,pi,2)
    linha(-pi,0,pi,0)
    linha(0,-2,0,2)
    # inicializa
    turtle.pen(pensize=3, pencolor='red')
    grafico(sin, -pi,pi)
    turtle.pen(pencolor='blue')
    grafico(cos,-pi,pi)
    turtle.hideturtle()
    turtle.exitonclick()
    
if __name__ =='__main__':
    main()
    
             
        