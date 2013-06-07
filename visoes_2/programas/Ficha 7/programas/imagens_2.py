import cImage


def mostra_imagem(imagem,pos,janela):
    """ 
    Mostra imagem numa dada posição da janela.
    """
    imagem.setPosition(pos[0],pos[1])
    imagem.draw(janela)

def cria_forma_1(largura,altura, r,g,b):
    imagem = cImage.EmptyImage(largura,altura)
    pixel = cImage.Pixel(r,g,b)
    for linha in range(altura):
        pixel_preto=cImage.Pixel(0,0,0)
        imagem.setPixel(0,linha,pixel_preto)
    for coluna in range(1,largura):
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel)
    return imagem

def main(largura,altura):
    janela = cImage.ImageWin('Imagens',2*largura,altura)
    imagem1 = cria_forma_1(largura,altura,255,0,0)
    imagem2 = cria_forma_1(largura,altura,0,0,255)
    #mostra_imagem(imagem1,(0,0),janela)
    mostra_imagem(imagem2,(largura,0), janela)
    janela.exitOnClick()

if __name__=='__main__':
    main(200,100)