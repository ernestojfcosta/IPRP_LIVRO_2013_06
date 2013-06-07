import turtle

def salta_tartaruga(tarta,distancia):
    tarta.pu()
    tarta.forward(distancia)
    tarta.pendown()
    
    
if __name__ == '__main__':
    toto = turtle.Turtle()
    toto.color('gray')
    toto.shape('turtle')
    titi = turtle.Turtle()
    titi.shape('triangle')
    salta_tartaruga(toto,100)
    titi.right(180)
    salta_tartaruga(titi,100)
    turtle.exitonclick()