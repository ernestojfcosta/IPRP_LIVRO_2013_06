from cTurtle import *


if __name__ == '__main__':
    tarta = Turtle()
    tarta.tracer(20,50)
    comp = 2
    for i in range(200):
        tarta.fd(comp)
        tarta.rt(90)
        comp = comp + 2
    tarta.exitOnClick()