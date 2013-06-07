import random
import math
import turtle


def monte_carlo_animado(num_dardos):
    """
    Valor de pi pelo método de monte Carlo.
    Versão gráfica.
    """
    # prepara a visualização
    turtle.setworldcoordinates(-2,-2,2,2)
    
    janela = turtle.Turtle()
    janela.hideturtle()
    
    janela.up()
    janela.goto(-1,0)
    janela.down()
    janela.goto(1,0)
    
    janela.up()
    janela.goto(0,1)
    janela.down()
    janela.goto(0,-1)   
    
    # vamos aos cálculos
    conta_dardos_in = 0
    janela.up()
    
    for i in range(num_dardos):
        x = random.random()
        y = random.random()
        
        d = math.sqrt(x**2 + y**2)
        janela.goto(x,y)
        
        if d <= 1:
            conta_dardos_in = conta_dardos_in + 1
            janela.color("blue")
        else:
            janela.color("red")
        
        janela.dot()
    
    janela.exitonclick() 
    
    res = 4 * (conta_dardos_in / float(num_dardos))
    
    return res
    
    
if __name__ == '__main__':
    print monte_carlo_animado(1500)
