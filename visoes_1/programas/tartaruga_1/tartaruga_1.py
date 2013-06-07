import cTurtle

def quadrado_a(lado):
    """
    Desenha um quadrado.
    """
    cTurtle.showturtle()
    #-----------
    cTurtle.fd(lado)
    cTurtle.rt(90)
    cTurtle.fd(lado)
    cTurtle.rt(90)    
    cTurtle.fd(lado)
    cTurtle.rt(90)
    cTurtle.fd(lado)
    cTurtle.rt(90)
    #----------
    cTurtle.hideturtle()

def quadrado_b(lado):
    """
    Desenha um quadrado.
    """
    cTurtle.showturtle()
    #-----------
    for i in range(4):
        cTurtle.forward(lado)
        cTurtle.right(90)

    #----------
    cTurtle.hideturtle()
    
    
def pentagono(lado):
    """
    Desenha um pentagono.
    """
    cTurtle.showturtle()
    #-----------
    for i in range(5):
        cTurtle.forward(lado)
        cTurtle.right(72)

    #----------
    cTurtle.hideturtle()  
    
def poligono_regular(comp_lado,num_lados):
    """
    Desenha um pol’gono.
    """
    cTurtle.showturtle()
    angulo_viragem = 360 /num_lados
    #-----------
    for i in range(num_lados):
        cTurtle.forward(comp_lado)
        cTurtle.right(angulo_viragem)

    #----------
    cTurtle.hideturtle()     

    
def poligono_regular_b(comp_lado,num_lados):
   """
   Desenha um pol’gono.
   """
   cTurtle.bgcolor("red")
   cTurtle.begin.fill()
   cTurtle.showturtle()
   CTurtle.pencolor("red")
   angulo_viragem = 360 /num_lados
   #-----------
   for i in range(num_lados):
       cTurtle.forward(comp_lado)
       cTurtle.right(angulo_viragem)

   #----------
   cTurtle.hideturtle()  
   cTurtle.end_fill()
    
    
    
    
poligono_regular(50,8)