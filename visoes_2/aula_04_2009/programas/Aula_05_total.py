import cImage
import random
import math

def mostra_imagem(img_fich):
    imagem = cImage.FileImage(img_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Imagem', largura,altura)
    imagem.draw(janela)
    janela.exitOnClick()
    
def cria_imagem_cor_1(largura,altura):
    janela = cImage.ImageWin('Teste 1',largura,altura)
    imagem = cImage.EmptyImage(largura,altura)
    pixel_branco = cImage.Pixel(255,204,102)
    for coluna in range(largura):
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel_branco)
    imagem.draw(janela)
    janela.exitOnClick()

def cria_imagem_cor_2(largura,altura):
    janela = cImage.ImageWin('Teste 2',largura,altura)
    imagem = cImage.EmptyImage(largura,altura)

    for coluna in range(largura):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        pixel = cImage.Pixel(r,g,b)
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel)
    imagem.draw(janela)
    janela.exitOnClick()    
    
def cria_imagem_cor_3(largura,altura):
    janela = cImage.ImageWin('Teste 2',largura,altura)
    imagem = cImage.EmptyImage(largura,altura)

    for coluna in range(largura):
        for linha in range(altura):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            pixel = cImage.Pixel(r,g,b)
            imagem.setPixel(coluna,linha,pixel)
    imagem.draw(janela)
    janela.exitOnClick()
    
    
def cria_imagem_cor_4(largura,altura):
    janela = cImage.ImageWin('Teste 2',largura,altura)
    imagem = cImage.EmptyImage(largura,altura)
    
    for linha in range(altura):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        pixel = cImage.Pixel(r,g,b)
        for coluna in range(largura):
            imagem.setPixel(coluna,linha,pixel)
    imagem.draw(janela)
    janela.exitOnClick()   
    
def desenha_linha(largura,altura,pixel):
    """
    Cria uma imagem com as dimens›es largura x altura
    e desenha um diagonal com a cor do pixel.
    """
    janela = cImage.ImageWin('Linha', largura, altura)
    imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura):
            if coluna == linha:
                imagem.setPixel(coluna,linha,pixel)
    imagem.draw(janela)
    imagem.save("/tempo/imagens/linha.jpg")
    janela.exitOnClick() 

    
def cria_random_pixel():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    p = cImage.Pixel(r,g,b)
    return p

def desenha_quadrado_cheio(posx,posy, lado):
    """
    Desenha um quadrado cheio na janela de lado com o canto superior
    esquerdo em (posx,posy).
    """
    janela=cImage.ImageWin('Quadrado',2*lado,2*lado)
    imagem = cImage.EmptyImage(lado,lado)
    imagem.setPosition(posx,posy)
    p = cria_random_pixel()
    for linha in range(lado):  
        for coluna in range(lado):
            imagem.setPixel(coluna,linha,p)
    imagem.draw(janela)
    janela.exitOnClick()

def arco(x,y, raio, amplitude):
    """ 
    Desenha (um arco de circunferncia) com centro em (x,y) e raio.
    """
    largura = 4 * raio
    altura = 4 * raio
    janela = cImage.ImageWin('Janela', largura, altura)
    imagem = cImage.EmptyImage(largura,largura)
    pixel_branco = cImage.Pixel(255,255,255)
    for coluna in range(largura):
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel_branco)
            
    #imagem.setPosition(x,y)
    pixel = cria_random_pixel()
    
    for angulo in range(amplitude):
        cordx = (raio * math.cos((math.pi /float(180)) * angulo)) + x
        cordy = (raio * math.sin((math.pi /float(180)) * angulo))  + y
        imagem.setPixel(cordx,cordy,pixel)
    imagem.draw(janela)
    janela.exitOnClick()

# -- Negativo

def negativo_pixel(pixel):
    red = 255 - pixel.getRed()
    green = 255 - pixel.getGreen()
    blue = 255 - pixel.getBlue()
    novo_pixel = cImage.Pixel(red,green,blue)
    return novo_pixel

def negativo_imagem(imagem_ficheiro):

    imagem_velha = cImage.FileImage(imagem_ficheiro)
    largura = imagem_velha.getWidth()
    altura = imagem_velha.getHeight()
    janela = cImage.ImageWin('Negativos',2*largura,altura)
    imagem_velha.draw(janela)
    

    imagem_nova = cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for  linha in range(altura):
            pixel_original = imagem_velha.getPixel(coluna,linha)
            novo_pixel = negativo_pixel(pixel_original)
            imagem_nova.setPixel(coluna,linha,novo_pixel)
    imagem_nova.setPosition(largura+1,0)
    imagem_nova.draw(janela)
    janela.exitOnClick()
    
# ---- Escala de Cinzentos

def pixel_cinzento(pixel):
    """ Converte um pixel para escala de cinzentos."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()
    
    int_media = (vermelho + verde + azul) / 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
    return novo_pixel

def imagem_cinzentos(imagem_fich):
    """ Transforma para escala de cinzentos a imagem."""

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Escala de cinzentos', 2* largura, altura)
    imagem.draw(janela)
    nova_imagem=cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            novo_pixel = pixel_cinzento(pixel)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    nova_imagem.setPosition(largura+1,0)
    nova_imagem.draw(janela)
    janela.exitOnClick()
    
def manipula_imagem(imagem, funcao_cor):
    """ Manipula uma imagem de acordo com uma fun‹o."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            novo_pixel = funcao_cor(pixel)
            nova_imagem.setPixel(coluna,linha, novo_pixel)
    return nova_imagem

def transforma(imagem_fich, funcao_cor):
    """ Transforma uma imagem de acordo com a fun‹o de cor."""
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Transforma‹o de Imagem', 2*largura,altura)
    imagem.draw(janela)
    
    nova_imagem = manipula_imagem(imagem,funcao_cor)
    nova_imagem.setPosition(largura + 1, 0)
    nova_imagem.draw(janela)
    janela.exitOnClick()    

def pixel_sepia(pixel):
    """ Tempo do passado."""
    r = pixel.getRed()
    g = pixel.getGreen()
    b = pixel.getBlue()
    
    novo_r = (r * 0.393 + g * 0.769 + b * 0.189)
    novo_g = (r * 0.349 + g * 0.686 + b * 0.168)
    novo_b = (r * 0.272 + g * 0.534 + b * 0.131)
    if novo_r > 255: novo_r = r 
    if novo_g > 255: novo_g = g 
    if novo_b > 255: novo_b = b

    novo_pixel = cImage.Pixel(novo_r,novo_g,novo_b)
    return novo_pixel      


def altera(imagem,factor_x, factor_y):
    """Altera a imagem de acordo com os factores.
    Estes devem ser inteiros.
    """
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    nova_imagem = cImage.EmptyImage(factor_x * largura, factor_y * altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna, linha)

            for i_x in range(factor_x):
                for i_y in range(factor_y):
                    nova_imagem.setPixel(factor_x * coluna + i_x, factor_y * linha + i_y, pixel)
    return nova_imagem



def espelho_h_e(imagem_fich):
    """Faz o espelho orizontal de uma imagem.
    Usa a parte esquerda."""
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Espelho Horizontal Esquerda', 2*largura,altura)
    imagem.draw(janela)

    nova_imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura/2):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna, linha)
            nova_imagem.setPixel(coluna,linha,pixel)
            nova_imagem.setPixel(largura - coluna - 1,linha,pixel)
    nova_imagem.setPosition(largura + 1, 0)
    nova_imagem.draw(janela)
    janela.exitOnClick()
    
    
if __name__ =='__main__':
    #cria_imagem_cor_4(600,400)
    #desenha_linha(400,400,cImage.Pixel(255,204,102))
    #desenha_quadrado_cheio(50,50,100)
    arco(100,100,50,180)
    #negativo_imagem('/tempo/imagens/duck3.jpg')
    #imagem_cinzentos('/tempo/imagens/duck3.jpg')
    #transforma('/tempo/imagens/duck3.jpg',pixel_sepia)
    janela = cImage.ImageWin('Estica e Encolhe', 3 *375,480)
    imagem = cImage.FileImage('/tempo/imagens/duck3.jpg')
    imagem.draw(janela)
    
    nova_img = altera(imagem, 2,1)
    nova_img.setPosition(375 + 1,0)
    nova_img.draw(janela)
    janela.exitOnClick()
    
