import turtle
import math


def marca(x,y):
    """ Marca um ponto na posição (x,y)."""
    turtle.penup()
    turtle.goto(x,y)
    turtle.dot(6)

    

def linha(x1,y1,x2,y2):
    """ Traça uma linha entre dois pontos."""
    turtle.up()
    turtle.goto(x1,y1)
    turtle.pd()
    turtle.goto(x2,y2)
    turtle.up()
    turtle.hideturtle()

def grafico_0(tartaruga,funcao, inicio,fim, n):
    """ Desenha o gráfico da função f entre inf e sup usando n segmentos."""
    # Tamanho dos segmentos
    tam_seg = (fim - inicio)/n
    x = inicio
    # Posiciona-se
    tartaruga.up()
    tartaruga.goto(x, funcao(x))
    tartaruga.down()
    for conta in range(n):
        x = x + tam_seg
        tartaruga.goto(x, funcao(x))
  
    
def grafico_1(tartaruga,funcao, inicio,fim, n):
    """ Desenha o gráfico da função f entre inf e sup usando n segmentos."""
    # Tamanho dos segmentos
    tam_seg = (fim - inicio)/n
    x = inicio
    # Posiciona-se
    tartaruga.up()
    tartaruga.goto(x, funcao(x))
    tartaruga.dot(6)
    tartaruga.down()
    # Desenha
    for conta in range(n):
        x = x + tam_seg
        tartaruga.goto(x, funcao(x))
        tartaruga.dot(6)



def grafico_2(tartaruga,funcao, inicio,fim):
    """ Desenha o gráfico da função f entre inf e sup."""
    # Tamanho dos segmentos
    delta = 0.1
    x = inicio
    # Posiciona-se
    tartaruga.up()
    tartaruga.goto(x, funcao(x))
    tartaruga.dot(6)
    tartaruga.down()
    for conta in range(1000):
        x = x + delta
        if x > fim:
            break
        tartaruga.goto(x, funcao(x))
        tartaruga.dot(6)

       
if __name__ == '__main__': 
    # Inicializa
    turtle.setworldcoordinates(-math.pi, -2, math.pi,2)
    linha(-math.pi,0,math.pi,0)
    linha(0,-2,0,2)
    # Seno
    toto = turtle.Turtle() 
    toto.pen(pensize=3, pencolor='gray')
    grafico_1(toto,math.sin, -math.pi,math.pi,50)
    toto.up()
    toto.goto(0.5,1)
    toto.write('SENO(X)', font=('ARIAL', 14,'bold'))
    toto.hideturtle()
    # Coseno
    titi = turtle.Turtle() 
    titi.pen(pensize=3)
    grafico_1(titi,math.cos, -math.pi,math.pi,50)
    titi.up()
    titi.goto(-0.7,1)
    titi.write('COSENO(X)', font=('ARIAL', 14,'bold'))
    titi.hideturtle()
    # Termina
    turtle.exitonclick()    


    
    
    
