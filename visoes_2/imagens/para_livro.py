import cImage
import random

# Negativo de imagem
def main_negativo(imagem_ficheiro):
    """Constrói e vizualiza o negativo de uma imagem."""
    # Obtém imagem
    imagem = cImage.FileImage(imagem_ficheiro)
    # Fabrica o negativo
    imagem_nova = negativo_imagem(imagem)
    # Define janela
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Negativo',2*largura, altura)
    # vizualiza
    imagem.draw(janela)
    imagem_nova.setPosition(largura+1,0)
    imagem_nova.draw(janela)
    # Termina
    janela.exitOnClick()
  
def negativo_imagem(imagem):
    """ Negativo de uma imagem."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    imagem_nova = cImage.EmptyImage(largura,altura)
    # percorre pixel a pixel
    for coluna in range(largura):
        for  linha in range(altura):
            # transforma
            pixel_original = imagem.getPixel(coluna,linha)
            novo_pixel = negativo_pixel(pixel_original)
            imagem_nova.setPixel(coluna,linha,novo_pixel)
    return imagem_nova
    
    
def negativo_pixel(pixel):
    red = 255 - pixel.getRed()
    green = 255 - pixel.getGreen()
    blue = 255 - pixel.getBlue()
    novo_pixel = cImage.Pixel(red,green,blue)
    return novo_pixel    

# Cinzentos    

def main_cinzento(imagem_ficheiro):
    """Constrói e vizualiza a escala de cinzentos de uma imagem."""
    # Obtém imagem
    imagem = cImage.FileImage(imagem_ficheiro)
    # Fabrica a escala de cinzentos
    imagem_nova = cinzento_imagem(imagem)
    # Define janela
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Cinzento',2*largura, altura)
    # vizualiza
    imagem.draw(janela)
    imagem_nova.setPosition(largura+1,0)
    imagem_nova.draw(janela)
    # Termina
    janela.exitOnClick()
  
def cinzento_imagem(imagem):
    """ Escala de cinzentos de uma imagem."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    imagem_nova = cImage.EmptyImage(largura,altura)
    # percorre pixel a pixel
    for coluna in range(largura):
        for  linha in range(altura):
            # transforma
            pixel_original = imagem.getPixel(coluna,linha)
            novo_pixel = cinzento_pixel(pixel_original)
            imagem_nova.setPixel(coluna,linha,novo_pixel)
    return imagem_nova

def cinzento_pixel(pixel):
    """ Converte um pixel para escala de cinzentos."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()
    int_media = (vermelho + verde + azul) // 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
    return novo_pixel

# -------------------
    
def mostra_imagem(img_fich):
    # Carrega a imagem do disco
    imagem = cImage.FileImage(img_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    # Cria janela
    janela = cImage.ImageWin('Imagem', largura,altura)
    # Mostra imagem na janela
    imagem.draw(janela)
    # Termina
    janela.exitOnClick()


def cria_janela(nome,largura,altura):
    janela= cImage.ImageWin(nome,largura,altura)
    janela.exitOnClick()
    
def cria_janela_cor(nome,largura,altura,cor):
    janela= cImage.ImageWin(nome,largura,altura)
    janela.setBackground(cor)
    janela.exitOnClick()
    
def desenha_linha(p_1,p_2):
    """Desenha uma linha entre dois pontos."""
    x_1 = p_1[0]
    y_1 = p_1[1]
    x_2 = p_2[0]
    y_2 = p_2[1]
    janela = cImage.ImageWin('Linha', 3* abs(x_2 - x_1), 3*abs(y_2 - y_1))
    janela.setBackground((0,255,0))
    
    imagem = cImage.EmptyImage(abs(x_2 - x_1),abs(y_2 - y_1))
    print(imagem.getWidth(), imagem.getHeight())
    pix = cImage.Pixel(255,0,0)
    for x in range(0, imagem.getWidth()):
        for k in range(0, imagem.getHeight()):
            imagem.setPixel(x,k,cImage.Pixel(0,255,0))
        y = int(x * ((y_2 - y_1)/(x_2 - x_1)) + y_1 - x_1 * ((y_2 - y_1)/ (x_2 - x_1)))
        imagem.setPixel(x,y,pix)
    imagem.setPosition(janela.getWidth()//2 - imagem.getWidth()//2,janela.getHeight()//2 - imagem.getHeight()//2)
    imagem.draw(janela)
    janela.exitOnClick()
        
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
    
def desenha_quad(lado_1, lado_2,cor):
    """ Desenha um quadrilátero colorido."""
    janela = cImage.ImageWin('Quadrilátero', 3 * lado_1,3*lado_2)
    cria_e_mostra(lado_1,lado_2,cor,(20,20),janela)
    janela.exitOnClick()
    
def cria_imagem_vazia(largura,altura):
    imagem = cImage.EmptyImage(largura,altura)
    return imagem

def cria_imagem_vazia_cor(largura, altura, cor):
    imagem = cImage.EmptyImage(largura,altura)
    imagem.setSolidColor(cor)
    return imagem    

def mostra_imagem_simples(imagem):
    # Dimensão
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    # Cria janela
    janela = cImage.ImageWin('Imagem', 2*largura,2*altura)
    # Mostra imagem na janela
    imagem.draw(janela)
    # Termina
    janela.exitOnClick()  
    
def mostra_imagens(lista_imagens):
    janela = cImage.ImageWin('Imagem', 640,480)
    for img in lista_imagens:
        l = random.randint(0, img.getWidth()//3)
        a = random.randint(0, img.getHeight()//3)
        img.setPosition(l,a)
        img.draw(janela)
    janela.exitOnClick()
    
        
def desenha_linha(imagem):
    altura = imagem.getHeight()
    largura = imagem.getWidth()
    janela = cImage.ImageWin('Imagem',largura,altura)
    pix = cImage.Pixel(255,0,0)
    for col in range(largura):
        imagem.setPixel(col, altura//2,pix)
    imagem.draw(janela)
    janela.exitOnClick()
    
def cria_imagem_simples(largura, altura):
    pixel_vermelho = cImage.Pixel(255,0,0)
    pixel_azul = cImage.Pixel(0,0,255) 
    
    imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura):
            if coluna % 10 == 0:
                imagem.setPixel(coluna,linha, pixel_vermelho)
            else:
                imagem.setPixel(coluna,linha, pixel_azul)
    imagem.setPosition(largura,altura) 
    
    janela = cImage.ImageWin('Imagem Simples', 2*largura,2*altura)
    janela.setBackground('green')
    
    imagem.draw(janela)
    
    janela.exitOnClick()

def gera_tuplo():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def gera_imagem(n,m):
    return [[ gera_tuplo() for coluna in range(m)] for linha in range(n)]


def distorcer(imagem, factor_x, factor_y):
    """
    Distorce uma imagem de acordo com os factores indicados.
    Cada pixel vai darorigem a um rectângulo de dimensões
    factor_x X factor_y.
    """  
    # Cria imagens
    img = cImage.FileImage(imagem)
    nova_img = altera(img, factor_x,factor_y)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Distorce', factor_x * (largura+1) , factor_y * (altura+1))
    # Coloca imagens
    img.setPosition(0,0)
    nova_img.setPosition(largura + 1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick()    
    

def altera(imagem,factor_x, factor_y):
    """
    Altera a imagem de acordo com os factores.
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


def transforma_imagem(imagem, funcao):
    """ Manipula uma imagem de acordo com uma função."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            novo_pixel = funcao(pixel)
            nova_imagem.setPixel(coluna,linha, novo_pixel)
    return nova_imagem

def main_funcao(imagem_ficheiro, funcao):
    """Transforma uma imagem de acordo com a funcao."""
    # Obtém imagem
    imagem = cImage.FileImage(imagem_ficheiro)
    # Transforma a imagem
    imagem_nova = transforma_imagem(imagem,funcao)
    # Define janela
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin( funcao.__name__,2*largura, altura)
    # vizualiza
    imagem.draw(janela)
    imagem_nova.setPosition(largura+1,0)
    imagem_nova.draw(janela)
    # Termina
    janela.exitOnClick()


def preto_branco_pixel(pixel):
    pixel_aux = cinzento_pixel(pixel)
    if pixel_aux.getRed() < 128 :
        novo_pixel = cImage.Pixel(0,0,0)
    else:
        novo_pixel = cImage.Pixel(255,255,255) 
    return novo_pixel
    
if __name__ =='__main__':
    #mostra_imagem('/images/ants.jpg')  
    #cria_janela('Janela Indiscreta', 320,240)
    #cria_janela_cor('Teste de Cor de Fundo', 320,240,'red')
    #cria_janela_cor('Teste de Cor de Fundo', 320,240,'#ff0000')
    #desenha_linha((50,50),(150,150))
    """
    janela = cImage.ImageWin('Quadrilátero', 320,240)
    cria_e_mostra(50,100,(255,0,0),(20,20),janela)
    janela.exitOnClick()
 
    #desenha_quad(50,100,(255,0,0))
    #imagem = cria_imagem_vazia(320,240)
    largura = 320
    altura = 240
    imagem = cria_imagem_vazia_cor(largura,altura,(0,0,255))
    imagem.setPosition(largura//2,altura//2)
    mostra_imagem_simples(imagem)
    """
    img_1 = cria_imagem_vazia_cor(100,100,(255,0,0))
    img_2 = cria_imagem_vazia_cor(50,50,(0,255,0))
    img_3 = cria_imagem_vazia_cor(150,150,(0,0,255))
    mostra_imagens([img_1, img_2, img_3])
    """
    img = cria_imagem_vazia_cor(150,150,(0,0,255))
    desenha_linha(img)

    cria_imagem_simples(320,240)

    imagem = gera_imagem(2,3)
    
    fich = open('/Users/ernestojfcosta/imagem.txt','w')
    fich.write(str(imagem))
    fich.close()
    """
    #distorcer('/images/calvin_leia_s.jpg', 1,1)
    #main_negativo('/images/calvin_leia_s.jpg')
    #main_cinzento('/images/calvin_leia_s.jpg')
    #main_funcao('/images/calvin_leia_s.jpg',cinzento_pixel)
    #main_funcao('/images/calvin_leia_s.jpg',preto_branco_pixel)
    

    
    
    
    
    