import cImage
import random

def espelho_h_e(imagem_fich):
    """Faz o espelho orizontal de uma imagem.
    Usa a parte esquerda."""
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Espelho Horizontal Esquerda', 2*largura,altura)
    imagem.draw(janela)

    nova_imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura/2):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna, linha)
            nova_imagem.setPixel(coluna,linha,pixel)
            nova_imagem.setPixel(largura - coluna - 1,linha,pixel)
    nova_imagem.setPosition(largura + 1, 0)
    nova_imagem.draw(janela)
    janela.exitOnClick()
    
def espelho_h_d(imagem_fich):
    """Faz o espelho orizontal de uma imagem.
    Usa a parte direita."""
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Espelho Horizontal Direita', 2*largura,altura)
    imagem.draw(janela)

    nova_imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura/2, largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna, linha)
            nova_imagem.setPixel(coluna,linha,pixel)
            nova_imagem.setPixel(largura - coluna - 1,linha,pixel)
    nova_imagem.setPosition(largura + 1, 0)
    nova_imagem.draw(janela)
    janela.exitOnClick()
    
def espelho_v_s(imagem_fich):
    """Faz o espelho vertical de uma imagem.
    Usa a parte superior."""
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Espelho Vertical Superior', 2*largura,altura)
    imagem.draw(janela)

    nova_imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura/2):
            pixel = imagem.getPixel(coluna, linha)
            nova_imagem.setPixel(coluna,linha,pixel)
            nova_imagem.setPixel(coluna,altura - linha - 1,pixel)
    nova_imagem.setPosition(largura + 1, 0)
    nova_imagem.draw(janela)
    janela.exitOnClick()
    

def espelho_v_i(imagem_fich):
    """Faz o espelho vertical de uma imagem.
    Usa a parte inferior."""
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Espelho Vertical Inferior', 2*largura,altura)
    imagem.draw(janela)

    nova_imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura/2):
            pixel = imagem.getPixel(coluna, altura - linha - 1)
            nova_imagem.setPixel(coluna,linha,pixel)
            nova_imagem.setPixel(coluna,altura - linha - 1,pixel)
    nova_imagem.setPosition(largura + 1, 0)
    nova_imagem.draw(janela)
    janela.exitOnClick()
  
def espelho_4_e_s(imagem_fich):
    """Faz o espelho em quatro direcções.
    Usa a parte inferior esquerda."""
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Espelho 4', 2*largura,altura)
    imagem.draw(janela)

    nova_imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura/2):
        for linha in range(altura/2):
            pixel = imagem.getPixel(coluna, linha)
            nova_imagem.setPixel(coluna,linha,pixel)
            # inferior esquerda
            nova_imagem.setPixel(coluna,altura - linha - 1,pixel)
            # superior direita
            nova_imagem.setPixel(largura - coluna -1,linha,pixel)
            # inferior direita
            nova_imagem.setPixel(largura - coluna -1,altura - linha - 1,pixel)            
    nova_imagem.setPosition(largura + 1, 0)
    nova_imagem.draw(janela)
    janela.exitOnClick()    
    
if __name__ =='__main__':
    #espelho_h_e('/tempo/imagens/duck.jpg')
    #espelho_h_d('/tempo/imagens/duck.jpg')
    #espelho_v_s('/tempo/imagens/duck.jpg')
    #espelho_v_i('/tempo/imagens/duck.jpg')
    espelho_4_e_s('/tempo/imagens/duck.jpg')