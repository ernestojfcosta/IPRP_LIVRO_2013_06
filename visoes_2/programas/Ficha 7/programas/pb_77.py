import cImage
import math
import random

def cria_arco(raio, amplitude,pos):
    """ 
    Desenha (um arco de circunferência) com amplitude e raio.
    """
    largura = raio + 1
    altura = raio + 1
    imagem = cImage.EmptyImage(largura,altura)
    # define a cor foregroung como branco
    pixel_branco = cImage.Pixel(255,255,255)
    for coluna in range(largura):
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel_branco)
       
    # define a cor do pixel
    pixel = cria_random_pixel()
    
    # posiciona
    imagem.setPosition(pos[0],pos[1])
    
    # cria
    for angulo in range(amplitude):
        cordx = int(raio * math.cos(math.radians(angulo)))
        cordy = int(raio * math.sin(math.radians(angulo)))
        imagem.setPixel(cordx,cordy,pixel)
    return imagem
    
# auxiliar
def cria_random_pixel():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    p = cImage.Pixel(r,g,b)
    return p
    
def main77(raio,amplitude,pos):
    # cria janela
    janela = cImage.ImageWin('Janela', 4*raio, 4*raio)
    # posiciona e cria imagem
    imagem = cria_arco(raio,amplitude,pos)
    # mostra
    imagem.draw(janela)
    # termina
    janela.exitOnClick()
    
if __name__=='__main__':
    main77(100,180,(200,200))
    #print cria_arco(30,90)
    