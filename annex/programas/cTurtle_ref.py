# Módulo cTurtle
import cTurtle

def quadrado(tartaruga,lado,pos,angulo):
    """ Usa a tartaruga para desenhar um quadrado de lado
    lado e orientação inicial ângulo.
    """
    # Preparação 
    tartaruga.up() 
    tartaruga.goto(pos) 
    tartaruga.setheading(angulo) 
    tartaruga.down() 
 
    # desenha quadrado 
    for conta in range(4): 
        tartaruga.forward(lado) 
        tartaruga.right(90) 
    tartaruga.hideturtle() 

    
def circunferencia(tartaruga,raio, posicao):
    # Preparação
    tartaruga.up() 
    tartaruga.goto(posicao) 
    tartaruga.down() 
    
    # desenha
    tartaruga.circle(raio)
    
    tartaruga.hideturtle()
        
def main2():
    tarta1 = cTurtle.Turtle()
    tarta1.begin_fill()
    tarta1.pen(shown=True,pendown=False,pencolor='blue',fillcolor='blue', speed=5)
    circunferencia(tarta1,30,(50,50))
    tarta1.end_fill()
    
    tarta2 = cTurtle.Turtle()
    tarta2.begin_fill()
    tarta2.pen(shown=False,pendown=False,pencolor='red',fillcolor='red', speed=2)
    circunferencia(tarta2, 100, (-100,-100))
    tarta2.end_fill()
    tarta1.exitOnClick()
    
def main0():
    tarta = cTurtle.Turtle()
    quadrado(tarta,100,(50,50),45)
    tarta.exitOnClick()
    
    
def main1():
    tarta1 = cTurtle.Turtle()
    tarta1.fill(True)
    tarta1.color('red')
    quadrado(tarta1,100,(50,50),45)
    tarta1.fill(False)

    tarta2 = cTurtle.Turtle()
    tarta2.begin_fill()
    tarta2.color('blue')
    quadrado(tarta2,100,(-50,.50),45)
    tarta2.end_fill()
    
    tarta1.exitOnClick()
    
if __name__ == '__main__':
    main2()
