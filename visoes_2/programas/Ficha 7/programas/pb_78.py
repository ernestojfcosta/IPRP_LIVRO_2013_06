import cImage

# 7.8 
def preto_branco(imagem_fich, limiar):
    """ Transforma para imagem a preto e branco."""

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
   
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

    return nova_imagem
    
def pixel_cinzento(pixel):
    """ Converte um pixel para escala de cinzentos."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()
    
    int_media = (vermelho + verde + azul) / 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
    return novo_pixel

def main78(nome_fich,limiar):
    # Prepara
    imagem = cImage.FileImage(nome_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    # Converte
    nova_imagem = preto_branco(nome_fich,limiar)
    # Cria janela
    janela = cImage.ImageWin('Preto e Branco',2*largura ,altura )
    # Mostra
    imagem.draw(janela)
    nova_imagem.setPosition(largura,0)
    nova_imagem.draw(janela)
    # Termina
    janela.exitOnClick() 

if __name__ == '__main__':
    main78('/tempo/imagens/duck3.jpg', 128)
    