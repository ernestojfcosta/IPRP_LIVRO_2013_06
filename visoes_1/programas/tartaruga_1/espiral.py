import cTurtle

def espiral(comp_min, comp_max, passo, angulo):
    """
    Desenho de espirais por justaposi��o de segmentos de recta que 
    v�o rodando de um certo �ngulo. Assumo sentido crescente e rota��o
    id�ntica � dos ponteiros do rrel�gio.
    """
    cTurtle.down()
    for segmento in range(comp_min, comp_max, passo):
        cTurtle.forward(segmento)
        cTurtle.right(angulo)
    cTurtle.up()
    cTurtle.hideturtle()
    
espiral(5,50,2,33)
