import cImage
import math


def mostra_imagem_b(imagem):

    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Imagem', largura,altura)
    imagem.draw(janela)

def mostra_imagem_c(imagem,janela):
    imagem.draw(janela)    
    
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
    

    
def pixel_cinzento(pixel):
    """ Converte um pixel para escala de cinzentos."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()
    
    int_media = (vermelho + verde + azul) / 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
    return novo_pixel    
    
def convolve(imagem, pix_linha, pix_coluna, kernel):
    """ Calcula a convolu‹o de um pixel."""
    kernel_coluna_base = pix_coluna - 1
    kernel_linha_base = pix_linha - 1
    
    soma = 0
    for linha in range(kernel_linha_base, kernel_linha_base + 3):
        for coluna in range(kernel_coluna_base,kernel_coluna_base + 3):
            k_coluna_indice = coluna - kernel_coluna_base
            k_linha_indice = linha - kernel_linha_base
            
            pixel = imagem.getPixel(coluna, linha)
            intensidade = pixel.getRed()
            
            soma = soma + intensidade * kernel[k_linha_indice][k_coluna_indice]
    return soma

def convolve_todos(imagem, pix_linha, pix_coluna, kernel):
    """ Calcula a convolu‹o de um pixel."""
    kernel_coluna_base = pix_coluna - 1
    kernel_linha_base = pix_linha - 1
    
    soma_r = 0
    soma_g = 0
    soma_b = 0
    for linha in range(kernel_linha_base, kernel_linha_base + 3):
        for coluna in range(kernel_coluna_base,kernel_coluna_base + 3):
            k_coluna_indice = coluna - kernel_coluna_base
            k_linha_indice = linha - kernel_linha_base
            
            pixel = imagem.getPixel(coluna, linha)
            intensidade_r = pixel.getRed()
            intensidade_g = pixel.getGreen()
            intensidade_b = pixel.getBlue()
            
            soma_r = soma_r + intensidade_r * kernel[k_linha_indice][k_coluna_indice]
            soma_g = soma_g + intensidade_g * kernel[k_linha_indice][k_coluna_indice]
            soma_b = soma_b + intensidade_b * kernel[k_linha_indice][k_coluna_indice]
    return soma_r,soma_g,soma_b


def detecta_lados(imagem, limiar):
    """Fabrica uma imagem em que os lados foram detectados. Usa operadores de sobel."""
    imagem_cinza = manipula_imagem(imagem,pixel_cinzento)
    largura = imagem_cinza.getWidth()
    altura = imagem_cinza.getHeight()
    nova_imagem = cImage.EmptyImage(largura, altura)
    preto = cImage.Pixel(0,0,0)
    branco = cImage.Pixel(255,255,255)
    kernel_x = [[-1,-2,-1],[0,0,0],[1,2,1]]
    kernel_y = [[-1,0,1],[-2,0,2],[-1,0,1]]
    
    for linha in range(1, altura - 1):
        for coluna in range(1, largura - 1):
            cx = convolve(imagem_cinza, linha, coluna, kernel_x)
            cy = convolve(imagem_cinza, linha, coluna, kernel_y)
            c = math.sqrt(cx ** 2 + cy ** 2)
            
            if c > limiar:
                nova_imagem.setPixel(coluna, linha, preto)
            else:
                nova_imagem.setPixel(coluna, linha, branco)
    return nova_imagem

def blur(imagem):
    """Tornar uma imagem com contornos vagos."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura, altura)
    kernel = [[1,2,1],[2,1,2],[1,2,1]]

    
    for linha in range(1, altura - 1):
        for coluna in range(1, largura - 1):
            r,g,b = convolve_todos(imagem, linha, coluna, kernel)
            pixel = cImage.Pixel(r,g,b)
            nova_imagem.setPixel(coluna, linha, pixel)
    return nova_imagem

def sharpen(imagem):
    """Tornar uma imagem com contornos vagos."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    nova_imagem = cImage.EmptyImage(largura, altura)
    kernel = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]

    
    for linha in range(1, altura - 1):
        for coluna in range(1, largura - 1):
            r,g,b = convolve_todos(imagem, linha, coluna, kernel)
            pixel = cImage.Pixel(r,g,b)
            nova_imagem.setPixel(coluna, linha, pixel)
    return nova_imagem

def main(imagem_fich,funcao):
    imagem = cImage.FileImage(imagem_fich)
    mostra_imagem_b(imagem)
    
    nova_imagem = funcao(imagem)
    mostra_imagem_b(nova_imagem)
    janela.exitOnClick()
    
def convolve_geral(imagem_fich, kernel):

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela_antiga = cImage.ImageWin('Original',largura,altura)
    mostra_imagem_c(imagem,janela_antiga)
    nova_imagem = cImage.EmptyImage(largura, altura)
    
    for linha in range(1, altura - 1):
        for coluna in range(1, largura - 1):
            r,g,b = convolve_todos(imagem, linha, coluna, kernel)
            pixel_cor = cImage.Pixel(r,g,b)
            pixel_cinza = pixel_cinzento(pixel_cor)
            nova_imagem.setPixel(coluna, linha, pixel_cor)
    janela_nova = cImage.ImageWin('Transformada',largura,altura)
    mostra_imagem_c(nova_imagem,janela_nova)
    janela_antiga.exitOnClick()
    janela_nova.exitOnClick()
    
    
if __name__ == '__main__':
    #main('/tempo/imagens/duck3.jpg',blur)
    #main('/tempo/imagens/duck3.jpg',sharpen)
    convolve_geral('/tempo/imagens/bird1.jpg',[[0,1,10],[1,-4,1],[0,1,0]])


    