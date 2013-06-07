import cImage

def quadrilatero(lado_1,lado_2,cor):
    """
    Cria uma figura rectangular, colorida.
    """
    imagem = cImage.EmptyImage(lado_1,lado_2)
    pixel = cImage.Pixel(cor[0],cor[1],cor[2])
    for coluna in range(lado_1):  
        for linha in range(lado_2):
            imagem.setPixel(coluna,linha,pixel)       
    return imagem

def cria_e_mostra(lado_1,lado_2, cor, pos,janela):
    imagem = quadrilatero(lado_1,lado_2,cor)
    imagem.setPosition(pos[0],pos[1])
    imagem.draw(janela)

def main73():
    janela = cImage.ImageWin('Mondrian',600,600)
    # cria imagem, posiciona e mostra
    cria_e_mostra(400,400,(255,0,0),(200,0),janela)
    cria_e_mostra(200,200,(0,0,255),(0,400),janela)
    cria_e_mostra(50,100,(255,255,0),(550,500),janela)
    cria_e_mostra(10,600,(0,0,0),(190,0),janela)
    cria_e_mostra(190,20,(0,0,0),(0,150),janela)
    cria_e_mostra(600,10,(0,0,0),(0,390),janela)
    cria_e_mostra(5,200,(0,0,0),(545,400),janela)
    cria_e_mostra(50,10,(0,0,0),(550,500),janela)
    # finito!
    janela.exitOnClick()
    
    
if __name__ =='__main__':
    main()
    