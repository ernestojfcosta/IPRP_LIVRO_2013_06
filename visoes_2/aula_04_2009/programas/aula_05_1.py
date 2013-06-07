import cImage

def cria_imagem_preto():
    janela = cImage.ImageWin('teste',600,400)
    imagem = cImage.EmptyImage(600,400)
    imagem.draw(janela)
    janela.exitOnClick()

    
def cria_imagem_branco():
    janela = cImage.ImageWin('teste',600,400)
    imagem = cImage.EmptyImage(600,400)
    pixel_branco = cImage.Pixel(255,255,255)
    for coluna in range(600):
        for linha in range(400):
            imagem.setPixel(coluna,linha,pixel_branco)
    imagem.draw(janela)
    janela.exitOnClick()
    
    
if __name__ == '__main__':
    cria_imagem_branco()
    