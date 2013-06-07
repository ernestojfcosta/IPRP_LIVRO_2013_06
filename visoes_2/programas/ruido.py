import cImage

def elimina_ruido(imagem):
    """ Elimina o ruido de uma imagem  calculando a mediana."""
    # Inicializa
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura,altura) 
    # Percorre a imagem e calcula
    for coluna in range(1,largura-1):
        for linha in range(1,altura-1):
            novo_pixel = mediana(coluna,linha,imagem)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    return nova_imagem


def mediana(coluna, linha, imagem):
    """Calcula a mediana dos pixeis na vizinhança do pixel (coluna,linha)."""
    r,g,b = [], [], []
    for c in [-1,0,1]:
        for l in [-1,0,1]:
            nova_coluna = coluna+c
            nova_linha = linha+l
            pixel = imagem.getPixel(nova_coluna, nova_linha)     
            # Actualiza pixel por canal
            r.append(pixel.getRed())
            g.append(pixel.getGreen())
            b.append(pixel.getBlue())
    r.sort()
    med_r = r[len(r)//2]
    med_g = g[len(g)//2]
    med_b = b[len(b)//2]
    novo_pixel = cImage.Pixel(med_r,med_g,med_b)
    return novo_pixel 
    
def mostra(imagem):
    """ Procede à diminiuição do ruído da imagem."""  
    # Cria imagens
    img = cImage.FileImage(imagem)
    nova_img = elimina_ruido(img)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Elimina ruído', 2 * largura, altura )
    # Coloca imagens
    nova_img.setPosition(largura+1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 

    
if __name__ == '__main__':
    mostra('/images/engine.png')