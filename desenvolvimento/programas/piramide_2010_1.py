from turtle import *

lado= 30 # lado do quadrado

def piramide(niveis):
    for i in range(1,niveis+1):
        # desenha um linha de quadrados
        linha(i)
    return 'Fim'
	
def linha(n):
    for k in range(n):
        # desenha quadrado
        quadrado()
    return 'Fim'	
	
def quadrado():
    # desenha
    for i in range(4):
        fd(lado)
        rt(90)
    return 'Fim'


if __name__ == '__main__':
    piramide(3)
    