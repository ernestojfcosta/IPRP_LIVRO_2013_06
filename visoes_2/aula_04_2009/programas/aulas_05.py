#! -*- encoding: utf-8 -*-
# Coisas com imagens

import cImage
import random
import math

# criar uma imagem só com um fundo colorido

def cria_imagem(largura,altura,pixel):
    """
    Cria uma imagem com as dimensões largura x altura com a cor do pixel.
    """
    janela = cImage.ImageWin("Janela", largura, altura)
    imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel)
    imagem.draw(janela)
    imagem.save("/tempo/imagens/uniforme.jpg")
    janela.exitOnClick()

def desenha_linha(largura,altura,pixel):
    """
    Cria uma imagem com as dimensões largura x altura
    e desenha um diagonal com a cor do pixel.
    """
    janela = cImage.ImageWin("Janela", largura, altura)
    imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura):
            if coluna == linha:
                imagem.setPixel(coluna,linha,pixel)
    imagem.draw(janela)
    imagem.save("/tempo/imagens/linha.jpg")
    janela.exitOnClick()    
# mostrar uma imagem

def mostra_imagem(caminho_imagem):
    """
    Mostra uma imagem guardada num ficheiro.
    """
    minha_janela = cImage.ImageWin("A minha imagem",530,380)
    imagem = cImage.FileImage(caminho_imagem)
    imagem.draw(minha_janela)
    minha_janela.exitOnClick()

# book miller 6.1

def cria_random_pixel():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    p = cImage.Pixel(r,g,b)
    return p

def linha_random_cor(largura,altura):
    janela = cImage.ImageWin('A minha Janela',largura,altura)
    imagem = cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            if coluna == linha:
                pixel = cria_random_pixel()
                imagem.setPixel(coluna,linha,pixel)
    imagem.draw(janela)
    janela.exitOnClick()
    
def random_cor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

# 6.2 Miller
def desenha_quadrado_cheio(janela,posx,posy, lado):
    """
    Desenha um quadrado cheio na janela de lado com o canto superior
    esquerdo em (posx,posy).
    """
    imagem = cImage.EmptyImage(lado,lado)
    imagem.setPosition(posx,posy)
    p = cria_random_pixel()
    for linha in range(lado):  
        for coluna in range(lado):
            imagem.setPixel(coluna,linha,p)
    imagem.draw(janela)
    janela.exitOnClick()
    
    
def desenha_quadrado(janela, posx,posy,lado):
    """
    Desenha um quadrado na janela de lado com o canto superior
    esquerdo em (posx,posy).
    """
    imagem = cImage.EmptyImage(lado,lado)
    imagem.setPosition(posx,posy)
    p = cria_random_pixel()
    pixel_branco = cImage.Pixel(255,255,255)
    for coluna in range(lado):
        for linha in range(lado):
            lado1 = coluna == 0
            lado2 = coluna == (lado - 1)
            lado3 = linha == 0
            lado4 = linha == (lado - 1)

            if  lado1 or lado2 or lado3 or lado4:
                imagem.setPixel(coluna,linha,p)
            else:
                imagem.setPixel(coluna,linha, pixel_branco)
    imagem.draw(janela)
    janela.exitOnClick()
                
            

def desenha_recta(janela, x1,y1,x2,y2):
    largura = janela.getWidth()
    altura = janela.getHeight()
    # imagem com fundo branco
    imagem = cImage.EmptyImage(largura,altura)
    pixel_branco = cImage.Pixel(255,255,255)
    for coluna in range(largura):
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel_branco)
            
    pixel = cria_random_pixel()
    # desenha recta
    for x in range(x1,x2):
        y = ((y2 - y1) / (x2 -x1)) * ( x - x1) + y1
        imagem.setPixel(x,y,pixel)
    imagem.draw(janela)
    
def desenha_quadrado_b(janela, posx, posy, lado):
    largura = janela.getWidth()
    altura = janela.getHeight()
    # imagem com fundo branco
    imagem = cImage.EmptyImage(largura,altura)
    pixel_branco = cImage.Pixel(255,255,255)
    for coluna in range(largura):
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel_branco)
            
    pixel = cria_random_pixel()
    desenha_recta(janela, posx,posy, posx + lado, posy)
    desenha_recta(janela, posx,posy + lado, posx + lado, posy + lado)
    desenha_recta(janela, posx,posy, posx, posy + lado)
    desenha_recta(janela, posx + lado,posy, posx + lado, posy + lado)
    
# 6.3 Miller

def arco(x,y, raio, amplitude):
    """ 
    Desenha (um arco de circunferência) com centro em (x,y) e raio.
    """
    janela = cImage.ImageWin('Janela', 600, 400)
    imagem = cImage.EmptyImage(600,400)
    pixel_branco = cImage.Pixel(255,255,255)
    for coluna in range(600):
        for linha in range(400):
            imagem.setPixel(coluna,linha,pixel_branco)
            
    #imagem.setPosition(x,y)
    pixel = cria_random_pixel()
    
    for angulo in range(amplitude):
        cordx = (raio * math.cos((math.pi /float(180)) * angulo)) + x
        cordy = (raio * math.sin((math.pi /float(180)) * angulo))  + y
        imagem.setPixel(cordx,cordy,pixel)
    imagem.draw(janela)
    janela.exitOnClick()
    
def main2():
    janela = cImage.ImageWin('Janela', 600, 400)
    desenha_recta(janela,100,100,200,200)
    janela.exitOnClick()
    
def main3():
    janela = cImage.ImageWin('Janela', 600, 400)
    desenha_quadrado_b(janela,100,100,100)
    janela.exitOnClick()
    
if __name__ == '__main__':
    #mostra_imagem("/tempo/imagens/duck.jpg")

    #p = cImage.Pixel(0,0,255)
    #cria_imagem(300,200,p)
    #desenha_linha(300,200,p)
    #linha_random_cor(300,300)
    #main3()
    arco(300,200, 100,90)

    