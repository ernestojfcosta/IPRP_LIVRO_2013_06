def distorcer(imagem, factor_x, factor_y):
    """
    Distorce uma imagem de acordo com os factores indicados.
    Cada pixel vai darorigem a um rectângulo de dimensões
    factor_x X factor_y.
    """  
    # Cria imagens
    img = cImage.FileImage(imagem)
    nova_img = altera(img, factor_x,factor_y)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Distorce', factor_x * (largura+1) , factor_y * (altura+1))
    # Coloca imagens
    img.setPosition(0,0)
    nova_img.setPosition(largura + 1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick()    
    

def altera(imagem,factor_x, factor_y):
    """
    Altera a imagem de acordo com os factores.
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