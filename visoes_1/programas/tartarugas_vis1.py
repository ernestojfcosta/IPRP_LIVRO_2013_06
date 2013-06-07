# Tartarugas
import turtle

def quadrado_1(lado,pos, angulo):
    """
    Desenha um quadrado com o comprimento de lado, o vértice inferior
    esquerdo em pos e  direcção inicial angulo.
    """
    # Preparação
    turtle.goto(pos)
    turtle.setheading(angulo)
    # Desenha
    for conta in range(4):
        turtle.forward(lado)
        turtle.right(90)

    
def quadrado_2(lado,pos, angulo):
    """
    Desenha um quadrado com o comprimento de lado, o vértice inferior
    esquerdo em pos e  direcção inicial angulo.
    """
    # Preparação
    turtle.up()
    turtle.goto(pos)
    turtle.setheading(angulo)
    turtle.down()
    
    # desenha quadrado
    for conta in range(4):
        turtle.forward(lado)
        turtle.right(90)
    turtle.hideturtle()


def tri_equi(lado):
    """
    Desenha um triângulo equilátero e lado lado.   
    """
    for i in range(3):
        turtle.forward(lado)
        turtle.right(120)
    turtle.hideturtle()


def pentagono(lado):
    """
    Desenha um pentágono.
    """
    for i in range(5):
        turtle.forward(lado)
        turtle.right(72)
    turtle.hideturtle() 
    
def poligono_regular(comp_lado,num_lados):
    """
    Desenha um polígono regular.
    """
    angulo_viragem = 360 /num_lados
    # Desenha
    for i in range(num_lados):
        turtle.forward(comp_lado)
        turtle.right(angulo_viragem)
    turtle.hideturtle()  

# Exercicio

def forma(comp_lado,num_lados, angulo_viragem):
    """
    Desenha uma forma repetindo num_lados a operação avança comp_lados, roda angulo_viragem.
    """
    # Desenha
    for i in range(num_lados):
        turtle.forward(comp_lado)
        turtle.right(angulo_viragem)
    turtle.hideturtle() 
    tuertle.exitonclick()
    
# Do manual de Python
def demo():
    turtle.color('blue', 'green')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()

if __name__ == '__main__':
    #poligono_regular(1,360)
    forma(100,5,144)
    