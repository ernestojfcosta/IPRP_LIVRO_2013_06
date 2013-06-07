import cImage

def blur(imagem):
    """Suaviza uma imagem."""
    # Inicializa
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura,altura) 
    # Percorre a imagem e calcula
    for coluna in range(1,largura-1):
        for linha in range(1,altura-1):
            novo_pixel = media_2(coluna,linha,imagem)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    return nova_imagem

def media(coluna, linha, imagem):
    """Calcula o valor médio dos pixeis na vizinhança do pixel (coluna,linha)."""
    # Extrai pixeis
    vizinhos = []
    for c in [-1,0,1]:
        for l in [-1,0,1]:
            vizinhos.append(imagem.getPixel(coluna+c,linha+l))                    
    # Calcula pixel "médio" por canal
    r = sum([vizinhos[i].getRed() for i in range(9)])//9
    g = sum([vizinhos[i].getGreen() for i in range(9)])//9
    b = sum([vizinhos[i].getBlue() for i in range(9)])//9
    # Constrói Pixel
    novo_pixel = cImage.Pixel(r,g,b)
    return novo_pixel


def media_2(coluna, linha, imagem):
    """Calcula o valor médio dos pixeis na vizinhança do pixel (coluna,linha)."""
    r,g,b = 0, 0, 0
    for c in [-1,0,1]:
        for l in [-1,0,1]:
            nova_coluna = coluna+c
            nova_linha = linha+l
            pixel = imagem.getPixel(nova_coluna, nova_linha)     
            # Actualiza pixel por canal
            r += pixel.getRed()
            g += pixel.getGreen()
            b += pixel.getBlue()
    
    novo_pixel = cImage.Pixel(r//9,g//9,b//9)
    return novo_pixel 
    
def mostra_blur(imagem):
    """ Procede à diminiuição da pixelização da imagem."""  
    # Cria imagens
    img = cImage.FileImage(imagem)
    img_ampliada = ampliar(img,3,2)
    nova_img = blur(img_ampliada)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Blur', 6 * largura, 2*altura )
    # Coloca imagens
    nova_img.setPosition(3*largura+1,0)
    img_ampliada.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 
    
def ampliar(imagem,factor_x, factor_y):
    """
    Altera a imagem de acordo com os factores.
    Estes devem ser números inteiros positivos.
    """
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(factor_x * largura, factor_y * altura)
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna, linha)
            # repete o pixel numa área definida pelos factores
            for i_x in range(factor_x):
                for i_y in range(factor_y):
                    nova_imagem.setPixel(factor_x * coluna + i_x, factor_y * linha + i_y, pixel)
    return nova_imagem  
    
if __name__ == '__main__':
    mostra_blur('/images/calvin_leia_s.jpg')

