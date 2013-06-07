import cImage
import math

# --- Abordagem A -----------------------
def transforma_convol_pb(imagem,mascara,limiar):
    """Imagem em escala de cinzentos."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura, altura)
    index = len(mascara)//2   
    for coluna in range(index,largura-index):
        for linha in range(index,altura-index):
            novo_pixel = convolucao_pb(coluna,linha,imagem, mascara,limiar)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    return nova_imagem


def convolucao_pb(x,y, imagem, filtro,limiar):
    """Imagem em escala de cinzentos."""
    index = len(filtro) // 2
    r = 0
    for i in range(-index, index+1):
        for j in range(-index,index+1):
            pixel = imagem.getPixel(x+j,y+i)
            r += pixel.getRed() * filtro[j+index][i+index]
    r = restringe(int(r),0,255)
    if r < limiar:
        novo_pixel = cImage.Pixel(255, 255,255) 
    else:
        novo_pixel = cImage.Pixel(0,0,0) 
    return novo_pixel


def extrai(imagem, mascara, limiar):
    """ Convolução de uma  imagem."""  
    # Cria imagens
    img_cor = cImage.FileImage(imagem)
    img = imagem_cinzentos(img_cor)
    nova_img = transforma_convol_pb(img,mascara,limiar)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Extrai Características',2 * largura, altura )
    # Coloca imagens
    nova_img.setPosition(largura+1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 


# ---- Abordagem B -------------------------------------------------- 
def extrai_caract(imagem, mascara_1, mascara_2,limiar):
    """ Convolução de uma  imagem."""  
    # Cria imagens
    img_cor = cImage.FileImage(imagem)
    img = imagem_cinzentos(img_cor)
    nova_img = transforma_convol(img,mascara_1, mascara_2,limiar)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('Extrai Características',2 * largura, altura )
    # Coloca imagens
    nova_img.setPosition(largura+1,0)
    img.draw(janela)
    nova_img.draw(janela)
    # Termina
    janela.exitOnClick() 
    
def transforma_convol(imagem,mascara_1, mascara_2,limiar):
    """Imagem em escala de cinzentos."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura, altura)
    index = len(mascara_1)//2   
    for coluna in range(index,largura-index):
        for linha in range(index,altura-index):
            val_x = convolve(coluna,linha,imagem, mascara_1)
            val_y = convolve(coluna,linha,imagem, mascara_2)
            val = restringe(math.sqrt(val_x**2 + val_y**2), 0, 255)
            novo_pixel = preto_branco_pixel(cImage.Pixel(val, val, val), limiar)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    return nova_imagem

def convolve(x,y, imagem, filtro):
    """Imagem em escala de cinzentos."""
    index = len(filtro) // 2
    r = 0
    for i in range(-index, index+1):
        for j in range(-index,index+1):
            pixel = imagem.getPixel(x+j,y+i)
            r += pixel.getRed() * filtro[j+index][i+index]
    r = restringe(int(r),0,255)
    return r
    
def pixel_cinzento(pixel):
    """ Converte um pixel para escala de cinzentos tendo em atenção a diferença dos canais."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()    
    int_media = (vermelho + verde + azul) // 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
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

def preto_branco_pixel(pixel,limiar):
    """Admite pixel na escala de cinzentos."""
    preto = cImage.Pixel(0,0,0)
    branco = cImage.Pixel(255,255,255)
    if pixel.getRed() < limiar :
        novo_pixel = preto
    else:
        novo_pixel = branco
    return novo_pixel


def restringe(canal, inf,sup):
    if canal > sup:
        canal = sup
    elif canal < inf:
        canal = inf
    return canal

if __name__ == '__main__':
    sobel_v = [[-1,0,1],[-2,0,2],[-1,0,1]]
    sobel_h = [[1,2,1],[0,0,0],[-1,-2,-1]]
    gauss_1 = [[1/16,2/16,1/16],[2/16,4/16,2/16],[1/16,2/16,1/16]]   
    
    #extrai('/images/d_duck.jpeg',sobel_v, 25)    
    #extrai('/images/calvin_leia_s.jpg',sobel_v, 150)
    #extrai_caract('/images/calvin_leia_s.jpg',sobel_v,sobel_h, 150)
    #extrai_caract('/images/calvin_leia_s.jpg',sobel_v,sobel_h, 100)
    #extrai_caract('/images/calvin_leia_s.jpg',sobel_v,sobel_h, 50)
    #extrai_caract('/images/d_duck.jpeg',sobel_v,sobel_h, 150)
    #extrai_caract('/images/d_duck.jpeg',sobel_v,sobel_h, 100)
    #extrai_caract('/images/d_duck.jpeg',sobel_v,sobel_h, 150)   
    extrai_caract('/images/engine.png',sobel_v,sobel_h, 150)  