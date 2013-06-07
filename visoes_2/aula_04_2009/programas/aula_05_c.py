#! -*- encoding: utf-8 -*-

# Mais coisas para imagens
# Miller 6.7 a 6.11


import cImage


# Escala de cinzentos

def pixel_cinzento(pixel):
    """ Converte um pixel para escala de cinzentos."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()
    
    int_media = (vermelho + verde + azul) / 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
    return novo_pixel

def escala_cinzentos(imagem_fich):
    """ Transforma para escala de cinzentos a imagem."""

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Escala de cinzentos', 2* largura, altura)
    imagem.draw(janela)
    nova_imagem=cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            novo_pixel = pixel_cinzento(pixel)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    nova_imagem.setPosition(largura+1,0)
    nova_imagem.draw(janela)
    janela.exitOnClick()
    
def retira_vermelho(imagem_fich):
    """ Retira vermelho."""

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Sem Vermelho', 2* largura, altura)
    imagem.draw(janela)
    nova_imagem=cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel= imagem.getPixel(coluna,linha)
            novo_pixel = cImage.Pixel(0,pixel.getGreen(),pixel.getBlue())
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    nova_imagem.setPosition(largura+1,0)
    nova_imagem.draw(janela)
    janela.exitOnClick()

def reforca_vermelho(imagem_fich):
    """ Intensifica vermelho."""

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Sem Vermelho', 2* largura, altura)
    imagem.draw(janela)
    nova_imagem=cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel= imagem.getPixel(coluna,linha)
            novo_pixel = cImage.Pixel(255,pixel.getGreen(),pixel.getBlue())
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    nova_imagem.setPosition(largura+1,0)
    nova_imagem.draw(janela)
    janela.exitOnClick()

    
def intensifica_vermelho(imagem_fich, valor):
    """ Intensifica vermelho. Valor = número entre 0 e 100."""

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Sem Vermelho', 2* largura, altura)
    imagem.draw(janela)
    nova_imagem=cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel= imagem.getPixel(coluna,linha)
            r = pixel.getRed()
            novo_r = max(r, r + ((valor * r) % 255)) 
            novo_pixel = cImage.Pixel(novo_r,pixel.getGreen(),pixel.getBlue())
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    nova_imagem.setPosition(largura+1,0)
    nova_imagem.draw(janela)
    janela.exitOnClick()    
 
    
def manipula_cor(imagem_fich, val_r,val_g,val_b):
    """ Manipula cores. Altera de modo independente os
    três canais de cor."""

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Manipula cores', 2* largura, altura)
    imagem.draw(janela)
    nova_imagem=cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel= imagem.getPixel(coluna,linha)
            r = pixel.getRed()
            g = pixel.getGreen()
            b = pixel.getBlue()
            novo_r = max(r, r + ((val_r * r) % 255))
            novo_g = max(g, g + ((val_g * g) % 255)) 
            novo_b = max(r, r + ((val_b * b) % 255)) 
            novo_pixel = cImage.Pixel(novo_r,novo_g, novo_b)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    nova_imagem.setPosition(largura+1,0)
    nova_imagem.draw(janela)
    janela.exitOnClick()      
    
def preto_branco(imagem_fich, limiar):
    """ Transforma para imagem a preto e branco."""

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Preto e Branco', 2* largura, altura)
    imagem.draw(janela)
    nova_imagem=cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            pixel_aux = pixel_cinzento(pixel)
            if pixel_aux.getRed() < limiar :
                novo_pixel = cImage.Pixel(0,0,0)
            else:
                novo_pixel = cImage.Pixel(255,255,255)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    nova_imagem.setPosition(largura+1,0)
    nova_imagem.draw(janela)
    janela.exitOnClick()    
    
if __name__ =='__main__':
    #escala_cinzentos('/tempo/imagens/duck.jpg')
    #retira_vermelho('/tempo/imagens/duck.jpg')
    #reforca_vermelho('/tempo/imagens/duck.jpg')
    #intensifica_vermelho('/tempo/imagens/duck.jpg',0.25)
    #manipula_cor('/tempo/imagens/duck.jpg',1,1,1)
    preto_branco('/tempo/imagens/duck.jpg',64)