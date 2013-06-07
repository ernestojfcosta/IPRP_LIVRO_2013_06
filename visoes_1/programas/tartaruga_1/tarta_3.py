from cTurtle import *

def segmento(tartaruga,pos1,pos2):
    """ traça um segmento  entre pos 1 e pos2."""
    tartaruga.pu()
    tartaruga.goto(pos1)
    tartaruga.pd()
    tartaruga.goto(pos2)

    
def tri(tartaruga,p1,p2,p3):
    segmento(tartaruga,p1,p2)
    segmento(tartaruga,p2,p3)
    segmento(tartaruga,p3,p1)
    
def formas(tartaruga, *pontos):
    for i in range(len(pontos)-1):
        segmento(tartaruga, pontos[i], pontos[i+1])
    segmento(tartaruga,pontos[-1], pontos[0])

def formas_b(tartaruga, cor,*pontos):
    tarta.begin_fill()
    tarta.fillcolor(cor)
    for i in range(len(pontos)-1):
        segmento(tartaruga, pontos[i], pontos[i+1])
    segmento(tartaruga,pontos[-1], pontos[0])
    tarta.end_fill()
    
def figuras(tarta,n):
    f = 0.83282
    phi = 6.89637
    s= 100
    c=1.0
    for i in range(n):
        tarta.fillcolor(c,0.5,1-c)
        tarta.pen(pensize=s)
        dummy = tarta.clone()
        s = s * f
        c = c * f
        tarta.rt(phi)
        
        
    
if __name__ == '__main__':
    tarta = Turtle()
    tarta.addshape('triangle', ((5,-3),(0,5),(-5,-3)))
    tarta.shape('triangle')
    #tarta.colormode(1.0)
    """
    tarta.setheading(90)
    tarta.pen(pencolor='red',pensize = 10, outline =1)
    inicio = (0,0)
    fim = (100,100)
    segmento(tarta, inicio,fim)
    """
    p1 =(100,100)
    p2 = (-100,100)
    p3 = (-100, -100)
    #tri(tarta,p1,p2,p3)
    p4 = (100,-100)
    tarta.begin_fill()
    tarta.fillcolor((1,0,1))
    formas(tarta,p1,p2,p3,p4)
    print tarta.pen()
    tarta.end_fill()
    """
    #formas_b(tarta,'blue',p1,p2,p3,p4)
    #figuras(tarta,20)
    tarta.exitOnClick()
    """