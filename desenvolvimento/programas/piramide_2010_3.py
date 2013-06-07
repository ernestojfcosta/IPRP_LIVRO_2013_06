from turtle import *

lado= 30 # lado do quadrado

def piramide(niveis):
    for i in range(1,niveis+1):
        # desenha um linha de quadrados
        linha(i)
        # nova posição
        pu()
        sety(ycor() - lado)
        setx(xcor() - i * lado - float(lado)/2)
        pd()
    return 'Fim'
	
def linha(n):
    for k in range(n):
        # desenha quadrado
        quadrado()
        # nova posição
        setx(xcor() + lado)
    return 'Fim'	
	
def quadrado():
    # desenha
    for i in range(4):
        fd(lado)
        rt(90)
    return 'Fim'


if __name__ == '__main__':
    piramide(3)
    turtle.exitonclick()
    