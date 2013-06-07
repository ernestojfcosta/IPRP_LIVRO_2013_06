from cTurtle import *

def add_ponteiro(tarta):
    tarta.setheading(90)
    tarta.polystart()
    tarta.fd(100)
    tarta.lt(90)
    tarta.fd(20)
    tarta.rt(120)
    tarta.fd(40)
    tarta.rt(120)
    tarta.fd(40)
    tarta.rt(120)
    tarta.fd(20)
    tarta.polyend()
    ponteiro = tarta.getpoly()
    tarta.addshape('ponteiro',ponteiro)
    
def segundos():
    tarta.setheading((tarta.heading() - 6) % 360)
    tarta.onTimer(segundos,500)

if __name__ == '__main__':
    tarta = Turtle()
    add_ponteiro(tarta)
    tarta.clear()
    tarta.setheading(90)
    """
    tarta.shape('ponteiro')
    tarta.fillcolor('blue')
    segundos()
    """
    for i in range(61):
        tarta.setheading(-i*6 + 90)
        tarta.shape('ponteiro')
        tarta.fillcolor('blue')
        tarta.delay(100)
    tarta.exitOnClick()