import cImage
from operator import itemgetter

def mostra_ampliar(imagem, factor_x, factor_y):
    """
    Distorce uma imagem de acordo com os factores indicados.
    Cada pixel vai darorigem a um rectângulo de dimensões
    factor_x X factor_y.
    """  
    # Cria imagens
    img = cImage.FileImage(imagem)
    nova_img = distorcer(img, factor_x,factor_y)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Distorce', (factor_x + 1)  * largura  , factor_y  * altura )
    # Coloca imagens
    img.draw(janela)
    nova_img.setPosition(largura + 1,0)
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



def blur(img):
    """ Diminuição da pixelização"""
    largura = img.getWidth()
    altura = img.getHeight()
    imagem = img.toList()
    nova_imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(1,largura-1):
        for linha in range(1,altura-1):
            pixel = img.getPixel(coluna, linha)
            # Calcula valores da vizinhança
            lista_pix = [imagem[linha + i_y][coluna + i_x] for i_y in [-1,0,1] for i_x in [-1,0,1]]
            # Suaviza
            r = sum(get_red(lista_pix))//9
            g = sum(get_green(lista_pix))//9
            b = sum(get_blue(lista_pix))//9
            novo_pixel = cImage.Pixel(r,g,b)
            nova_imagem.setPixel(coluna, linha, novo_pixel)
    return nova_imagem



def get_canal(lista_pix, canal):
    """Vai buscar todas as componentes do canal. canal pode ser 0 (red), 1 (green) e 2 (blue."""
    return list(map(itemgetter(canal),lista_pix))


def get_red(lista_rgb):
    return list(map(itemgetter(0),lista_rgb))

def get_green(lista_rgb):
    return list(map(itemgetter(1),lista_rgb))

def get_blue(lista_rgb):
    return list(map(itemgetter(2),lista_rgb))

def pixel_to_tuple(pix):
    return (pix.getRed(),pix.getGreen(), pix.getBlue())


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


def mostra_encolher(imagem, factor_x, factor_y):
    """
    Encolhe uma imagem de acordo com os factores indicados.
    """  
    # Cria imagens
    img = cImage.FileImage(imagem)
    nova_img = encolher(img, factor_x,factor_y)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()  
    nova_largura = largura//factor_x
    nova_altura = largura//factor_y
    janela = cImage.ImageWin('Distorce',  largura + nova_largura,  altura)
    # Coloca imagens
    img.draw(janela)
    nova_img.setPosition(largura + 1,0)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick()    
    
    
def encolher(imagem,factor_x, factor_y):
    """
    Encolhe a imagem de acordo com os factores.
    Estes devem ser inteiros.
    """
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    nova_largura = int(largura / factor_x)
    nova_altura =  int(altura / factor_y)
    
    nova_imagem = cImage.EmptyImage(nova_largura,nova_altura)
    
    for coluna in range(nova_largura):
        for linha in range(nova_altura):
            pixel = imagem.getPixel(coluna * factor_x, linha * factor_y)
            nova_imagem.setPixel(coluna,linha, pixel)
    return nova_imagem

if __name__ == '__main__':
    #distorcer('/images/calvin_leia_s.jpg',2,3)
    #distorcer_b('/images/calvin_leia.jpg',3,2)
    mostra_blur('/images/calvin_leia_s.jpg')