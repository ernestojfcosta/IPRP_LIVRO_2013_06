import cImage

def roda_90(imagem):
    """ Roda uma imagem 90 graus para a direita."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    nova_imagem = cImage.EmptyImage(altura,largura) # troca por causa da rotação
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            nova_imagem.setPixel(linha,coluna,pixel)
    return nova_imagem

def main(imagem_fich):
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    nova_imagem = roda_90(imagem)
    janela = cImage.ImageWin('Roda 90', altura,largura) #por causa da rotação
    
    nova_imagem.draw(janela)
    
    janela.exitOnClick()
    

if __name__ =='__main__':
    main('/tempo/imagens/duck3.jpg')
    
    