import cImage
from random import randint

def transforma_convol(imagem,mascara):
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura, altura)
    index = len(mascara)//2   
    for coluna in range(index,largura-index):
        for linha in range(index,altura-index):
            novo_pixel = convolucao(coluna,linha,imagem, mascara)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    return nova_imagem


def convolucao(x,y, imagem, filtro):
    index = len(filtro) // 2
    r,g,b = 0, 0, 0
    for i in range(-index, index+1):
        for j in range(-index,index+1):
            pixel = imagem.getPixel(x+j,y+i)
            r += pixel.getRed() * filtro[j+index][i+index]
            g += pixel.getGreen() * filtro[j+index][i+index]
            b += pixel.getBlue() * filtro[j+index][i+index]
    r = restringe(int(r),0,255)
    g = restringe(int(g),0,255)
    b = restringe(int(b),0,255)
    novo_pixel = cImage.Pixel(r, g,b) 
    return novo_pixel


def mostra_convol(imagem, mascara):
    """ Convolução de uma  imagem."""  
    # Cria imagens
    img = cImage.FileImage(imagem)
    img_ampliada = ampliar(img,3,3)
    nova_img = transforma_convol(img_ampliada,mascara)
    # Cria janela
    largura = img_ampliada.getWidth()
    altura = img_ampliada.getHeight()    
    janela = cImage.ImageWin('Convolução',2 * largura, altura )
    # Coloca imagens
    nova_img.setPosition(largura+1,0)
    img_ampliada.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 
    
def mostra_convol_2(imagem, mascara):
    """ Convolução de uma  imagem."""  
    # Cria imagens
    img = cImage.FileImage(imagem)
    nova_img = transforma_convol(img,mascara)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Convolução',2 * largura, altura )
    # Coloca imagens
    nova_img.setPosition(largura+1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 
 
 
def mostra_convol_cinza(imagem, mascara):
    """ Convolução de uma  imagem."""  
    # Cria imagens
    img_cor = cImage.FileImage(imagem)
    img = imagem_cinzentos(img_cor)
    nova_img = transforma_convol(img,mascara)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Convolução',2 * largura, altura )
    # Coloca imagens
    nova_img.setPosition(largura+1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 
 
 
def mostra_convol_pb(imagem, mascara, limiar):
    """ Convolução de uma  imagem."""  
    # Cria imagens
    img_cor = cImage.FileImage(imagem)
    img = imagem_cinzentos(img_cor)
    nova_img = transforma_pb(transforma_convol(img,mascara), limiar)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Convolução',2 * largura, altura )
    # Coloca imagens
    nova_img.setPosition(largura+1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 
    
def pixel_cinzento(pixel):
    """ Converte um pixel para escala de cinzentos tendo em atenção a diferença dos canais."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()    
    int_media = int(0.299*vermelho + 0.587*verde + 0.114*azul) // 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
    return novo_pixel

def preto_branco_pixel(pixel,limiar):
    #pixel_aux = pixel_cinzento(pixel)
    preto = cImage.Pixel(0,0,0)
    branco = cImage.Pixel(255,255,255)
    if pixel.getRed() < limiar :
        novo_pixel = branco
    else:
        novo_pixel = preto
    return novo_pixel

def imagem_cinzentos(imagem):
    """ Transforma para escala de cinzentos a imagem."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem=cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            novo_pixel = pixel_cinzento(pixel)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    return nova_imagem


def convolucao_mat(x,y, matriz, mascara):
    dim = len(mascara)
    index = dim // 2
    val = 0
    for i in range(-index, index+1):
        for j in range(-index,index+1):
            val += matriz[y+j][x+i] * mascara[j+index][i+index]
    return val


def gera_matriz(n,m, inf,sup):
    return [[randint(inf,sup) for col in range(m)] for lin in range(n)]

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

def transforma_pb(imagem, limiar):
    """ Transforma para preto e branco uma imagem em escala de cinzentos."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            novo_pixel = preto_branco_pixel(pixel,limiar)
            nova_imagem.setPixel(coluna,linha, novo_pixel)
    return nova_imagem


def restringe(canal, inf,sup):
    if canal > sup:
        canal = sup
    elif canal < inf:
        canal = inf
    return canal

if __name__ == '__main__':
    mascara = gera_matriz(3,3,-1,1)
    mat = gera_matriz(5,5,0,5)
    #imagem = cImage.FileImage('/images/duck_s.jpg')
    #nova_imagem = transforma_convol(imagem, mascara)
    masc_1 = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]
    sharpen = [[0,-1,0],[-1,5,-1],[0,1,0]]
    sharpen_2 = [[0,0,0,0,0],[0,0,-1,0,0],[0,-1,5,-1,0],[0,0,1,0,0], [0,0,0,0,0]]
    sharpen_3 = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    blur = [[1,1,1],[1,1,1],[1,1,1]]
    edge_enhance = [[0,0,0],[-1,1,0],[0,0,0]]
    edge_detect = [[0,1,0],[1,-4,1],[0,1,0]]
    emboss = [[-2,-1,0],[-1,1,1],[0,1,2]]
    sobel_v = [[-1,0,1],[-2,0,2],[-1,0,1]]
    sobel_h = [[1,2,1],[0,0,0],[-1,-2,-1]]
    gauss_1 = [[1/16,2/16,1/16],[2/16,4/16,2/16],[1/16,2/16,1/16]]
    #mostra_convol('/images/duck_s.jpg',mascara)
    #mostra_convol('/images/calvin_leia_s.jpg',masc_1)
    #mostra_convol('/images/calvin_leia_s.jpg',blur)
    #mostra_convol_2('/images/calvin_leia_s.jpg',sharpen)   
    #mostra_convol_2('/images/calvin_leia_s.jpg',sharpen_2)
    #mostra_convol_2('/images/calvin_leia_s.jpg',edge_enhance)
    #mostra_convol_2('/images/calvin_leia_s.jpg',edge_detect)
    #mostra_convol_2('/images/calvin_leia_s.jpg',emboss)
    #mostra_convol_2('/images/calvin_leia_s.jpg',sobel_v)
    #mostra_convol_2('/images/calvin_leia_s.jpg',sobel_h)
    #mostra_convol_2('/images/duck.jpg',sobel_v)
    #mostra_convol_2('/images/d_duck.jpeg',sharpen_3)
    #mostra_convol_cinza('/images/duck_s.jpg',sobel_v)
    #mostra_convol_cinza('/images/duck_s.jpg',sobel_h)
    #mostra_convol('/images/d_duck.jpeg',gauss_1)
    #mostra_convol('/images/calvin_leia_s.jpg',gauss_1)
    #mostra_convol_cinza('/images/calvin_leia_s.jpg',sobel_v)
    #mostra_convol_pb('/images/calvin_leia_s.jpg',sobel_v, 200)
    mostra_convol_pb('/images/d_duck.jpeg',sobel_v, 50)