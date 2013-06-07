import cImage


def mostra_imagem(imagem,pos,janela):
    """ 
    Mostra imagem numa dada posição da janela.
    """
    imagem.setPosition(pos[0],pos[1])
    imagem.draw(janela)

def cria_forma(largura,altura, r,g,b):
    imagem = cImage.EmptyImage(largura,altura)
    pixel = cImage.Pixel(r,g,b)
    for coluna in range(largura):
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel)
    return imagem

def main(largura,altura):
    janela = cImage.ImageWin('Toto',largura,altura)
    imagem = cria_forma(largura/3,altura/2,255,0,0)
    mostra_imagem(imagem,(50,100),janela)
    janela.exitOnClick()

if __name__=='__main__':
    main(600,400)