import coImage
import math
import random

def cria_arco(raio, amplitude):
    """ 
    Desenha (um arco de circunferência) com amplitude e raio.
    """
    largura = 4*raio
    altura = 4*raio
    imagem = coImage.EmptyImage(largura, altura)
    # define a cor foregroung como branco
    pixel_branco = coImage.Pixel(255,255,255)
    for coluna in range(-raio//2,raio//2):
        for linha in range(-raio//2,raio//2):
            imagem.setPixel(coluna,linha,pixel_branco)
       
    # Cor preta para o desenho
    pixel = cria_random_pixel()

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
    janela = coImage.ImageWin('Janela', 4*raio, 4*raio)
    largura = janela.getWidth()
    altura = janela.getHeight()
    janela.setCoords(-raio//2,-raio//2,raio//2,raio//2)
    
    # cria imagem
    imagem = cria_arco(raio,amplitude)

    # mostra
    imagem.draw(janela)
    
    # termina
    janela.exitOnClick()
    
if __name__=='__main__':
    main77(100,90,(0,0))
    #print cria_arco(30,90)
    