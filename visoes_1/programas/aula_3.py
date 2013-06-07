from turtle import *

def quadrado(lado):
    """Desenha um quadrado de lado  lado.
    
    """
    forward(lado)
    right(90)
    forward(lado)
    right(90)
    forward(lado)
    right(90)
    forward(lado)
    right(90)
    
def quadrado_2(lado):
    """Desenha um quadrado de lado  lado.
    
    """
    conta = 0
    while conta < 4:
        forward(lado)
        right(90)
        conta = conta + 1
        
def quadrado_3(lado):
    """Desenha um quadrado de lado lado.
    
    """
    for i in range(4):
        forward(lado)
        right(90)
    
 
def tri_equi(lado):
    """Desenha um triângulo equilátero e lado lado.
    
    """
    for i in range(3):
        forward(lado)
        right(120)
    hideturtle()

def desenha_quad_tri(lado):
    """Desenho de um quadrado e um triângulo.
    
    """
    quadrado_3(lado)
    penup()
    sety(ycor() + 1.5 * lado)
    pendown()
    tri_equi(lado)
    hideturtle()
    exitonclick()

from turtle import *

def salta_tartaruga(tarta,distancia):
    tarta.pu()
    tarta.forward(distancia)
    tarta.pendown()
    
    
# Problema 3.1

def quad(lado,xcor,ycor,orient):
    """Desenha um quadrado em que o lado, a posição inicial e a orientação inicial podem variar.
    
    """
    penup()
    goto(xcor,ycor)
    setheading(orient)
    pendown()
    for i in range(4):
	forward(lado)
	right(90)
    hideturtle()
    
# Problema 3.2


# Problema 3.3


# Problema 3.4

def poligono(num_lados,tam_lado):
    """Desenha um polígono regular.
    
    """
    angulo = 360.0 / num_lados
    for i in range(num_lados):
	forward(tam_lado)
	right(angulo)
    hideturtle()
    
	

# Problema 3.5

import math

def circunf_a():
    """Desenha circunferência sem querer saber do raio.
    
    """
    poligono(100,5)
    

def circunf(raio):
    """Desenha uma circunferência conhecido o raio.
    
    """
    perimetro = 2 * math.pi * raio
    tam_lado = int(perimetro / 360.0)
    poligono(360,tam_lado)
    hideturtle()
 
    
def circunf_centro(raio, xcor_centro,ycor_centro):
    """Desenha uma circunferência conhecido o raio.
    
    """
    perimetro = 2 * math.pi * raio
    tam_lado = int(perimetro / 360.0)
    penup()
    goto(xcor_centro, ycor_centro)
    pendown()
    poligono(360,tam_lado)
    hideturtle()    
    

# Problema 3.6

# Problema 3.7

# Problema 3.8

# Problema 3.9

def quad_concent(n,lado,d):
    """Desenha n quadrados concêntricos.
    
    """
    x0 = xcor()
    y0 = ycor()
    for i in range(n):
	quad(lado+i*2*d, x0-i*d, y0+i*d, 0)


def nautilus(n, lado, xcor,ycor, angulo):
    """Desenha n quadrados com lados e orientações variáveis.
    Desenha uma forma semelhante a um Nautilus.
    
    """
    reset()
    for conta in range(n):
	quad(lado,xcor,ycor,lado)
	lado = lado + 10
	angulo = angulo + 15
    hideturtle()

# Problema ?
from random import randint

def alea(num_lados):
    """Desenha num_lados aleatoriamente.
    
    """
    for conta in range(num_lados):
	novo_x = randint(-100,100)
	novo_y = randint(-100,100)
	goto(novo_x,novo_y)
    hideturtle()

def alea_cor(num_lados):
    """Desenha num_lados aleatoriamente.
    
    """
    colormode(255)
    for conta in range(num_lados):
	novo_x = randint(-200,200)
	novo_y = randint(-200,200)
	r = randint(0,255)
	g = randint(0,255)
	b = randint(0,255)
	color((r,g,b))
	goto(novo_x,novo_y)
    hideturtle()
    
    
if __name__ == '__main__':
    #meu_lado = 50
    #desenha_quad_tri(meu_lado)
    #quad(meu_lado, 50,75,45)
    #poligono(100,5)
    #circunf(100)
    #quad_concent(5,20,5)
    """
    toto = Turtle()
    toto.color('red')
    toto.shape('turtle')
    titi = Turtle()
    titi.color('green')
    titi.shape('triangle')
    salta_tartaruga(toto,100)
    titi.right(180)
    
    salta_tartaruga(titi,100)

    speed(0)
    nautilus(20,20,0,0,-30)
    """
    alea_cor(30)
    exitonclick()
    
    
