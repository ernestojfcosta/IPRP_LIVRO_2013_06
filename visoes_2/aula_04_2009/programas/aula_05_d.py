#! -*- encoding: utf-8 -*-

# e ainda mais gráficos...

import cImage
import random

#from aula_05_c import *


def pixel_cinzento(pixel):
    """ Converte um pixel para escala de cinzentos."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()
    
    int_media = (vermelho + verde + azul) / 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
    return novo_pixel



# Miller 6.13

def pixel_negativo(pixel):
    """Passa ao negativo."""
    r = 255 - pixel.getRed()
    g = 255 - pixel.getGreen()
    b = 255 - pixel.getBlue()
    pixel = cImage.Pixel(r,g,b)
    return pixel
    
# Miller 6.14   
def pixel_sem_vermelho(pixel):
    """Retira vermelho"""
    g = pixel.getGreen()
    b = pixel.getBlue()
    pixel = cImage.Pixel(0,g,b)
    return pixel  

# Miller 6.15

def preto_branco(pixel):
    """Converte para preto e branco. Limiar fixo."""
    r = pixel.getRed()
    g = pixel.getGreen()
    b = pixel.getBlue()
    
    cor_media = ( r + g + b) / 3
    
    if cor_media < 128:
        novo_pixel = cImage.Pixel(0,0,0)
    else:
        novo_pixel = cImage.Pixel(255,255,255)
    return novo_pixel

# Miller 6.16

def muda_pixel(pixel):
    """ Muda pixel de modo aleatório."""
    r = (pixel.getRed() + random.randint(0,25)) % 255
    g = (pixel.getGreen() + random.randint(0,25)) % 255
    b = (pixel.getBlue() + random.randint(0,25)) % 255
    novo_pixel = cImage.Pixel(r,g,b)
    return novo_pixel


# 6.17 
def pixel_sepia(pixel):
    """ Tempo do passado."""
    r = pixel.getRed()
    g = pixel.getGreen()
    b = pixel.getBlue()
    novo_r = (r * 0.393 + g * 0.769 + b * 0.189) % 255
    novo_g = (r * 0.349 + g * 0.686 + b * 0.168) % 255
    novo_b = (r * 0.272 + g * 0.534 + b * 0.131) % 255
    novo_pixel = cImage.Pixel(novo_r,novo_g,novo_b)
    return novo_pixel
    
def pixel_sepia_b(pixel):
    """ Tempo do passado."""
    r = pixel.getRed()
    g = pixel.getGreen()
    b = pixel.getBlue()
    
    novo_r = (r * 0.393 + g * 0.769 + b * 0.189)
    novo_g = (r * 0.349 + g * 0.686 + b * 0.168)
    novo_b = (r * 0.272 + g * 0.534 + b * 0.131)
    if novo_r > 255: novo_r = r 
    if novo_g > 255: novo_g = g 
    if novo_b > 255: novo_b = b

    novo_pixel = cImage.Pixel(novo_r,novo_g,novo_b)
    return novo_pixel   
    
# ----------------------------
# ABSTRACÇÃO
# ----------------------------
def manipula_imagem(imagem, funcao_cor):
    """ Manipula uma imagem de acordo com uma função."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            novo_pixel = funcao_cor(pixel)
            nova_imagem.setPixel(coluna,linha, novo_pixel)
    return nova_imagem

def transforma(imagem_fich, funcao_cor):
    """ Transforma uma imagem de acordo com a função de cor."""
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Transformação de Imagem', 2*largura,altura)
    imagem.draw(janela)
    
    nova_imagem = manipula_imagem(imagem,funcao_cor)
    nova_imagem.setPosition(largura + 1, 0)
    nova_imagem.draw(janela)
    janela.exitOnClick()
    
if __name__ == '__main__':
    #transforma('/tempo/imagens/duck.jpg',pixel_cinzento)
    #transforma('/tempo/imagens/duck.jpg',preto_branco)
    #transforma('/tempo/imagens/duck.jpg',pixel_negativo)
    #transforma('/tempo/imagens/duck.jpg',pixel_sem_vermelho)
    #transforma('/tempo/imagens/duck.jpg',muda_pixel)
    transforma('/tempo/imagens/duck.jpg',pixel_sepia_b)