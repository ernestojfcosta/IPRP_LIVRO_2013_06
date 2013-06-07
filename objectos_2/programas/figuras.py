import cTurtle
import random

def figura(lista_coordenadas):
    """
    Desenha uma figura unindo as coordenadas da lista.
    """
    tartaruga = cTurtle.Turtle()
    tartaruga.up()
    ponto_inicial = lista_coordenadas[0]
    tartaruga.goto(ponto_inicial)
    tartaruga.down()
    
    for i in range(1,len(lista_coordenadas)):
        tartaruga.goto(lista_coordenadas[i])
    tartaruga.goto(ponto_inicial) # -- fecha desenho
    
    tartaruga.ht()
    return 'fim'

def gera_pontos(quantidade, valor):
    """
    Gera pares de nœmeros inteiros (aleat—rios) entre (-valor, valor)
    """
    coordenadas = list()
    for i in range(quantidade):
        x= random.randint(-valor,valor)
        y = random.randint(-valor,valor)
        coordenadas.append((x,y))
    return coordenadas


if __name__ == '__main__':
    
    coordenadas = gera_pontos(10, 200)
    # --- desenha
    figura(coordenadas)
        
        
    