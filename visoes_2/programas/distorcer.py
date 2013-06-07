import cImage

def altera(imagem,factor_x, factor_y):
    """Altera a imagem de acordo com os factores.
    Estes devem ser inteiros.
    """
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    nova_imagem = cImage.EmptyImage(factor_x * largura, factor_y * altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna, linha)

            for i_x in range(factor_x):
                for i_y in range(factor_y):
                    nova_imagem.setPixel(factor_x * coluna + i_x, factor_y * linha + i_y, pixel)
    return nova_imagem

def main():
    """ Para testar..."""
    janela = cImage.ImageWin('Estica e Encolhe', 2 *375,480)
    imagem = cImage.FileImage('/tempo/imagens/duck3.jpg')
    #imagem.draw(janela)
    
    nova_img = altera(imagem, 2,1)
    #nova_img.setPosition(0,360 + 1)
    nova_img.draw(janela)
    janela.exitOnClick()
    
if __name__ =='__main__':
    main()
    