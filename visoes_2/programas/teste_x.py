import cImage
import math

def mostra_reduz_cores(imagem, palete):
    """ Substitui na imagem as cores pelas mais próximas na palete."""  
    # Cria imagens
    img = cImage.FileImage(imagem)
    nova_img = reduz_cores(img, palete)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Reduz Cores', 2 * largura, altura )
    # Coloca imagens
    nova_img.setPosition(largura+1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 

def reduz_cores(imagem, palete):
    largura = imagem.getWidth()
    altura = imagem.gethjeight()
    nova_imagem = cImage.EmptyImage(largura, altura)
    for coluna in range(largura):
	for linha in range(altura):
	    pixel = image.getPixel(coluna, linha)
	    novo_pixel = distancia_palete(pixel, palete)
	    nova_imagem.setPixel(coluna, linha, novo_pixel)
    return nova_imagem

