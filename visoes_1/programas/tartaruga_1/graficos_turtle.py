import cTurtle
import math
import float_range

def linha(tartaruga,x1,y1,x2,y2):
    """ Desenha uma linha entre o ponto 1 e o ponto 2."""
    tartaruga.up()
    tartaruga.goto(x1,y1)
    tartaruga.down()
    tartaruga.goto(x2,y2)
    
def grafico(tartaruga,funcao, valores):
    """ Desenha o gráfico da função f."""
    tartaruga.up()
    tartaruga.goto(valores[0], funcao(valores[0]))
    tartaruga.down()
    
    for indice in range(1,len(valores)):
        tartaruga.goto(valores[indice], funcao(valores[indice]))
        
def derivada(f):
    """Derivada de uma função."""
    dx= 1.e-6
    def d(x):
        return (f(x + dx) - f(x))/dx
    return d


def integral(f):
    """ Integral definido."""
    dx = 1.e-6
    def int(x):
        return f(x) * dx
    return int

def main0():
    tartaruga = cTurtle.Turtle()
    linha(tartaruga,50,50,150,150)
    tartaruga.exitOnClick() 



def main2():

    xx = float_range.float_range_lista(-4,4,0.1)
    tartaruga = cTurtle.Turtle()
    tartaruga.pensize(3)   
    tartaruga.setWorldCoordinates(-4,-2,4,2)
    linha(tartaruga,-4,0,4,0)
    linha(tartaruga,0,-2,0,2)
    
    tartaruga.pencolor('red')
    grafico(tartaruga,math.sin,xx)
    tartaruga.up()
    tartaruga.goto(0.5,1)
    tartaruga.write('SIN', move=False, align='left', font=('Arial', 14, 'normal'))
    tartaruga.down()
    
    tartaruga.pencolor('blue')
    tartaruga.up()
    tartaruga.goto(-2,1.2)
    tartaruga.write('INTEGRAL SIN', move=False, align='left', font=('Arial', 14, 'normal'))
    tartaruga.down()
    grafico(tartaruga,integral(math.sin),xx)
    tartaruga.exitOnClick()  
    
def main1():

    xx = float_range.float_range_lista(-4,4,0.1)
    tartaruga = cTurtle.Turtle()
    tartaruga.pensize(3)   
    tartaruga.setWorldCoordinates(-4,-2,4,2)
    linha(tartaruga,-4,0,4,0)
    linha(tartaruga,0,-2,0,2)
    
    tartaruga.pencolor('red')
    grafico(tartaruga,math.cos,xx)
    tartaruga.up()
    tartaruga.goto(0.5,1)
    tartaruga.write('COS', move=False, align='left', font=('Arial', 14, 'normal'))
    tartaruga.down()
    
    tartaruga.pencolor('blue')
    tartaruga.up()
    tartaruga.goto(-2,1.2)
    tartaruga.write('DERIVADA COS', move=False, align='left', font=('Arial', 14, 'normal'))
    tartaruga.down()
    grafico(tartaruga,derivada(math.cos),xx)
    tartaruga.exitOnClick()  
    
    
def main3():

    xx = float_range.float_range_lista(-4,4,0.1)
    tartaruga = cTurtle.Turtle()
    tartaruga.pensize(3)   
    tartaruga.setWorldCoordinates(-4,-2,4,2)
    linha(tartaruga,-4,0,4,0)
    tartaruga.write('X', move=False, align='left', font=('Arial', 14, 'normal'))
    linha(tartaruga,0,-2,0,2)
    
    tartaruga.pencolor('red')
    tartaruga.up()
    tartaruga.goto(0.5,1)
    tartaruga.write('SIN(X)', move=False, align='left', font=('Arial', 14, 'normal'))
    grafico(tartaruga,math.sin,xx)

    tartaruga. exitOnClick()
 
    
def sector(raio,angulo):
    cTurtle.fd(raio)
    cTurtle.left(90)
    cTurtle.circle(raio, angulo)
    cTurtle.left(90)
    cTurtle.fd(raio)
    cTurtle.left(180-angulo)
    
    
if __name__ =='__main__':
    main1()