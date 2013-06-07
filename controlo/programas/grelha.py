import turtle
import random

def grelha(dim,lado):
    """Desenha uma grelha dim x dim em que cada célula tem de lado."""
    turtle.color("gray")
    tam = (dim*lado)
    x = -tam//2
    y = tam//2
    turtle.penup()
    turtle.goto(x,y)

    # Desenha linha
    for lin in range(dim+1):
        turtle.pendown()
        turtle.forward(tam)
        turtle.penup()
        turtle.setposition(x,turtle.ycor() - lado)
    # Desenha colunas
    turtle.setposition(x,y)
    turtle.rt(90)
    for col in range(dim+1):
        turtle.pendown()
        turtle.forward(tam)
        turtle.penup()
        turtle.setposition(turtle.xcor() + lado,y)        
    turtle.hideturtle()
   
    
    
    
def grelha_2(dim,lado):
    """Desenha uma grelha dim x dim em que cada célula tem de lado lado."""
    turtle.color("gray")
    tam = (dim*lado)
    x = -tam//2
    y = tam//2
    turtle.penup()
    turtle.goto(x,y)
    for lin in range(dim):  
        # Desenha linha de quadrados
        for col in range(dim):
            turtle.pendown()
            quadrado(lado)            
            turtle.penup()
            turtle.setx(turtle.xcor() + lado)
        # reposiciona
        turtle.penup()
        turtle.setposition(x, turtle.ycor()-lado)        
    turtle.hideturtle()

def passeio(dim, lado, passos):    
    # Prepara grelha
    turtle.speed(0)
    grelha_2(dim,lado)
    turtle.color('red')
    turtle.home()
    turtle.pendown()
    # Passeio
    turtle.speed(6)
    turtle.dot()
    turtle.showturtle()
    lim_x = lim_y = (dim*lado)//2
    cor_x = 0
    cor_y = 0
    for i in range(passos):
        vai_para = random.choice(['N','E','S','W'])
        if (vai_para == 'N') and (cor_y < lim_y):
            cor_y += lado
            turtle.setheading(90)
            turtle.fd(lado)
        elif (vai_para == 'E') and (cor_x < lim_x):
            cor_x += lado
            turtle.setheading(0)
            turtle.fd(lado)
        elif (vai_para == 'S') and (cor_y > -lim_y):
            cor_y -= lado
            turtle.setheading(270)
            turtle.fd(lado)
        elif (vai_para == 'W') and (cor_x > -lim_x):
            cor_x -= lado
            turtle.setheading(180)
            turtle.fd(lado) 
        else:
            print((vai_para,turtle.xcor(),turtle.ycor()))
            continue
                
    
def quadrado(lado):
    for i in range(4):
        turtle.fd(lado)
        turtle.rt(90)
        
if __name__ == '__main__':
    #grelha_2(4,20)
    passeio(8,20,50)
    turtle.exitonclick()