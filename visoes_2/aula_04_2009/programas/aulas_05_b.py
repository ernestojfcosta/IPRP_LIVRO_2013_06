#! -*- encoding: utf-8 -*-
# Coisas com imagens

import cImage
import random
import math


def negativo_pixel(pixel):
    red = 255 - pixel.getRed()
    green = 255 - pixel.getGreen()
    blue = 255 - pixel.getBlue()
    novo_pixel = cImage.Pixel(red,green,blue)
    return novo_pixel

def negativo_imagem(imagem_ficheiro):

    imagem_velha = cImage.FileImage(imagem_ficheiro)
    largura = imagem_velha.getWidth()
    altura = imagem_velha.getHeight()
    janela = cImage.ImageWin('Negativos',2*largura,altura)
    imagem_velha.draw(janela)
    

    imagem_nova = cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for  linha in range(altura):
            pixel_original = imagem_velha.getPixel(coluna,linha)
            novo_pixel = negativo_pixel(pixel_original)
            imagem_nova.setPixel(coluna,linha,novo_pixel)
    imagem_nova.setPosition(largura+1,0)
    imagem_nova.draw(janela)
    janela.exitOnClick()
    

if __name__ == '__main__':
    negativo_imagem('/tempo/imagens/duck.jpg')
    
    
            
            