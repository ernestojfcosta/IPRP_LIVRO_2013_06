

from turtle import *

def quadrado(lado):
    for i in range(4):
        forward(lado)
        lt(90)
        
def sector(raio,angulo):
    forward(raio)
    left(90)
    circle(raio, angulo)
    left(90)
    forward(raio)
    lt(180 - angulo)

def vai_para(x,y):
    penup()
    goto(x,y)
    pd()
    
def main(lado,raio,angulo):
    # posisiona-se
    vai_para(-125,-125)
    # quadrado
    fillcolor("yellow")
    pensize(3)
    begin_fill()
    quadrado(lado)
    end_fill()
    # posiciona-se
    vai_para(0,0)
    # 3 sectores
    fillcolor('black')
    begin_fill()
    for i in range(3):
        sector(raio,angulo)
        lt(120)
    end_fill()
    # circulo no meio
    pencolor('yellow')
    vai_para(25,0)
    lt(90)
    fillcolor('black')
    begin_fill()
    circle(25)
    end_fill()
    hideturtle()
    exitonclick()
    
main(250,100,60)