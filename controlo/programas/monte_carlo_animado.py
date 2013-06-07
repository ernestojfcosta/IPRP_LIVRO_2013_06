import random
import turtle

def quadrado(tartaruga, lado, origem):
    tartaruga.up()
    tartaruga.goto(origem)
    tartaruga.down()
    for i in range(4):
        tartaruga.fd(lado)
        tartaruga.left(90)
    tartaruga.hideturtle()
    

def monte_carlo_animado(num_dardos):
    """
    Valor de pi pelo método de Monte Carlo.
    Versão gráfica.
    """
    # prepara a visualização
    turtle.setworldcoordinates(-2,-2,2,2)
    
    janela = turtle.Turtle()
    janela.hideturtle()
    # Desenha os eixos
    janela.up()
    janela.goto(-1,0)
    janela.down()
    janela.goto(1,0)
    
    janela.up()
    janela.goto(0,1)
    janela.down()
    janela.goto(0,-1)
    
    # Desenha circunferência
    janela.up()
    janela.goto(0,-1)
    janela.down()
    janela.circle(1, steps=360)
    
    # Desenha quadrado
    
    quadrado(janela,2,(-1,-1))
  
    
    # vamos aos cálculos
    conta_dardos_in = 0
    janela.up()
    
    for i in range(num_dardos):
        x = random.random()
        y = random.random()
        
        d = (x**2 + y**2)** 0.5
        janela.goto(x,y)
        
        if d <= 1:
            conta_dardos_in = conta_dardos_in + 1
            janela.color("blue")
        else:
            janela.color("red")
        
        janela.dot()   
    res = 4 * (conta_dardos_in / num_dardos)
    return res
    
    
if __name__ == '__main__':
    print((monte_carlo_animado(1500)))
    turtle.exitonclick() 