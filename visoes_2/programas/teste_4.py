import cImage

if __name__ == '__main__':
    imagem = cImage.EmptyImage(320,240,(255,255,0))
    for row in range(240//2):
        for col in range(320//2):
            imagem.setPixel(col,row,cImage.Pixel(255,0,0))
            
    janela = cImage.ImageWin('cria',320,240)
    imagem.draw(janela)
    janela.exitOnClick()