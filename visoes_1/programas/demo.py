# Tartarugas
import turtle

def quadrado_1(lado,pos, angulo):
    """
    Desenha um quadrado com o comprimento de lado, o vértice inferior
    esquerdo em pos e  direcção inicial angulo.
    """
    for conta in range(4):
        turtle.forward(lado)
        turtle.right(90)
    turtle.hideturtle()
    
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

color('blue', 'green')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
hideturtle()
done()

if __name__ == '__main__':
    