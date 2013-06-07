import cImage
import random
import math


# Da introdução da ficha


def mostra_imagem(imagem,pos,janela):
    """ 
    Mostra imagem numa dada posição da janela.
    """
    imagem.setPosition(pos[0],pos[1])
    imagem.draw(janela)
    
def mostra_imagem_b(imagem):

    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Imagem', largura,altura)
    imagem.draw(janela)

def mostra_imagem_c(imagem,janela):
    imagem.draw(janela)  

def cria_imagem_cor_1(largura,altura):
    janela = cImage.ImageWin('Teste 1',largura,altura)
    imagem = cImage.EmptyImage(largura,altura)
    pixel_branco = cImage.Pixel(255,204,102)
    for coluna in range(largura):
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel_branco)
    imagem.draw(janela)
    janela.exitOnClick()
    
# 7.1    
    
def mosaico(imagem,nx, ny):
    """
    Repete a imagem num matriz nx * ny.
    """
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Mosaico', nx * largura, ny * altura)
    
    for i in range(nx):
        for j in range(ny):
            imagem.setPosition(i*largura, j* altura)
            imagem.draw(janela)
    janela.exitOnClick()
    
def main(imagem_fich, n1,n2):
    imagem = cImage.FileImage(imagem_fich)
    mosaico(imagem,n1,n2)


# 7.2

def ladrilhos(nx,ny,lado,cores):
    """
    Preenche o espaço nx por ny com quadrados coloridos de tamanho lado.
    """
    janela = cImage.ImageWin('Ladrilhos',nx * lado, ny*lado)
    
    for coluna in range(nx):
        for linha in range(ny):
            if (coluna + linha) % 2 == 0:
                quadrado((coluna * lado, linha * lado),lado, cores[0],janela)
            else:
                quadrado((coluna * lado, linha * lado),lado, cores[1],janela)
    janela.exitOnClick()
                
def quadrado(pos,lado,cor,janela):
    """
    Desenha um quadrado colorido na posição pos e lado lado.
    A janela está prédifinida.
    """
    imagem = cImage.EmptyImage(lado,lado)
    imagem.setPosition(pos[0],pos[1])
    pixel = cImage.Pixel(cor[0],cor[1],cor[2])
    for linha in range(lado):  
        for coluna in range(lado):
            imagem.setPixel(coluna,linha,pixel)
    imagem.draw(janela)

def main1(nx,ny,lado,cores):
    ladrilhos(nx,ny,lado,cores)    
    
# 7.3 (Mondrian) Usa a fun��o quadrado

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
    
# -- Variante
def traco_h(pos, espessura, tamanho,cor,janela):
    """
    Desenha um tra�o horizontal.
    """
    imagem = cImage.EmptyImage(tamanho,espessura)
    imagem.setPosition(pos[0],pos[1])
    pixel = cImage.Pixel(cor[0],cor[1],cor[2])
    for coluna in range(tamanho):
        for linha in range(espessura):
            imagem.setPixel(coluna,linha,pixel)
    imagem.draw(janela)
    
def traco_v(pos, espessura, tamanho,cor,janela):
    """
    Desenha um tra�o horizontal.
    """
    imagem = cImage.EmptyImage(espessura,tamanho)
    imagem.setPosition(pos[0],pos[1])
    pixel = cImage.Pixel(cor[0],cor[1],cor[2])
    for coluna in range(espessura):
        for linha in range(tamanho):
            imagem.setPixel(coluna,linha,pixel)
    imagem.draw(janela)
        
def main2():
    janela = cImage.ImageWin('Mondrian', 600, 600)
    traco_h((0,190),20,190, (0,0,0),janela)
    traco_h((0,400),10,600, (0,0,0),janela)
    traco_h((560,500),10,200, (0,0,0),janela)
    traco_v((190,0),10,600, (0,0,0),janela)
    traco_v((560,400),10,200, (0,0,0),janela)
    quadrado((200,0),400,(255,0,0),janela)
    quadrado((0,410),190,(0,0,255),janela)
    quadrado((570,510),90,(255,255,0),janela)
    janela.exitOnClick()
 
# 7.4 Desenho livre: para fazerem em casa...

# 7.5 (recta)

def cria_random_pixel():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    p = cImage.Pixel(r,g,b)
    return p

def desenha_recta(janela, x1,y1,x2,y2):
    largura = janela.getWidth()
    altura = janela.getHeight()
    imagem = cImage.EmptyImage(largura,altura)
  
    pixel = cria_random_pixel()
    # desenha recta
    for x in range(x1,x2):
        y = int(((y2 - y1) / (x2 -x1)) * ( x - x1) + y1)
        imagem.setPixel(x,y,pixel)
    imagem.draw(janela)
    
def main3():
    janela = cImage.ImageWin('Recta',400,200)
    desenha_recta(janela,183,105,290,127)
    janela.exitOnClick()

# 7.6. Quadrado a partir de rectas
def desenha_quadrado(janela, posx, posy, lado):
    largura = janela.getWidth()
    altura = janela.getHeight()
    # imagem com fundo branco
    imagem = cImage.EmptyImage(largura,altura)
    pixel_branco = cImage.Pixel(255,255,255)
    for coluna in range(largura):
        for linha in range(altura):
            imagem.setPixel(coluna,linha,pixel_branco)
            
    pixel = cria_random_pixel()
    desenha_recta(janela, posx,posy, posx + lado, posy)
    desenha_recta(janela, posx,posy + lado, posx + lado, posy + lado)
    desenha_recta(janela, posx,posy, posx, posy + lado)
    desenha_recta(janela, posx + lado,posy, posx + lado, posy + lado)
    
# 7.7

def arco(x,y, raio, amplitude):
    """ 
    Desenha (um arco de circunfer�ncia) com centro em (x,y) e raio.
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
        cordx = int((raio * math.cos((math.pi /float(180)) * angulo)) + x)
        cordy = int((raio * math.sin((math.pi /float(180)) * angulo))  + y)
        imagem.setPixel(cordx,cordy,pixel)
    imagem.draw(janela)
    janela.exitOnClick()
    

# 7.8 
def preto_branco(imagem_fich, limiar):
    """ Transforma para imagem a preto e branco."""

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Preto e Branco', 2* largura, altura)
    imagem.draw(janela)
    nova_imagem=cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            pixel_aux = pixel_cinzento(pixel)
            if pixel_aux.getRed() < limiar :
                novo_pixel = cImage.Pixel(0,0,0)
            else:
                novo_pixel = cImage.Pixel(255,255,255)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    nova_imagem.setPosition(largura+1,0)
    nova_imagem.draw(janela)
    janela.exitOnClick()   
    
def pixel_cinzento(pixel):
    """ Converte um pixel para escala de cinzentos."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()
    
    int_media = (vermelho + verde + azul) // 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
    return novo_pixel

# 7.9

def manipula_cor(imagem_fich, val_r,val_g,val_b):
    """ Manipula cores. Altera de modo independente os
    três canais de cor."""

    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    janela = cImage.ImageWin('Manipula cores', 2* largura, altura)
    imagem.draw(janela)
    nova_imagem=cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel= imagem.getPixel(coluna,linha)
            r = pixel.getRed()
            g = pixel.getGreen()
            b = pixel.getBlue()
            novo_r = max(r, r + ((val_r * r) % 255))
            novo_g = max(g, g + ((val_g * g) % 255)) 
            novo_b = max(r, r + ((val_b * b) % 255)) 
            novo_pixel = cImage.Pixel(novo_r,novo_g, novo_b)
            nova_imagem.setPixel(coluna,linha,novo_pixel)
    nova_imagem.setPosition(largura+1,0)
    nova_imagem.draw(janela)
    janela.exitOnClick()      

# 7.10
def espelho_v_s(imagem_fich):
    """Faz o espelho vertical de uma imagem.
    Usa a parte superior."""
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Espelho Vertical Superior', 2*largura,altura)
    imagem.draw(janela)

    nova_imagem = cImage.EmptyImage(largura,altura)
    for coluna in range(largura):
        for linha in range(altura/2):
            pixel = imagem.getPixel(coluna, linha)
            nova_imagem.setPixel(coluna,linha,pixel)
            nova_imagem.setPixel(coluna,altura - linha - 1,pixel)
    nova_imagem.setPosition(largura + 1, 0)
    nova_imagem.draw(janela)
    janela.exitOnClick()
# 7.11
def roda_90(imagem):
    """ Roda uma imagem 90 graus para a direita."""
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    
    nova_imagem = cImage.EmptyImage(altura,largura) # troca por causa da rotação
    
    for coluna in range(largura):
        for linha in range(altura):
            pixel = imagem.getPixel(coluna,linha)
            nova_imagem.setPixel(linha,coluna,pixel)
    return nova_imagem


# 7.12
def combina_pixel(pixel1, pixel2,function):
    """ Combina dois pixeis de acordo com a fun��o."""
    r1 = pixel1.getRed()
    g1 = pixel1.getGreen()
    b1 = pixel1.getBlue()
    
    r2 = pixel2.getRed()
    g2 = pixel2.getGreen()
    b2 = pixel2.getBlue()
    
    r,g,b = function(r1,r2,g1,g2,b1,b2)
    return cImage.Pixel(r,g,b)

def funde(imagem1, imagem2,  funcao):
    
    largura_1 = imagem1.getWidth()
    altura_1 = imagem1.getHeight()
    largura_2 = imagem2.getWidth()
    altura_2 = imagem2.getHeight()
    largura = min(largura_1,largura_2)
    altura = min(altura_1,altura_2)
    

    
    nova_imagem = cImage.EmptyImage(largura,altura)
    
    for coluna in range(largura):
        for linha in range(altura):
            pix1= imagem1.getPixel(coluna, linha)
            pix2 = imagem2.getPixel(coluna,linha)
            
            novo_pixel = combina_pixel(pix1,pix2, funcao)
            
            nova_imagem.setPixel(coluna,linha,novo_pixel)
            
    return nova_imagem

def media(r1,g1,b1, r2,g2,b2):
    """ Devolve tuplo formado pela média."""
    r = (r1 + r2) // 2
    g = (g1 + g2) //2
    b = (b1 + b2) // 2
    return r,g,b

def maior(r1,g1,b1, r2,g2,b2):
    """ Devolve tuplo formado pela pelo maior dos dois."""
    r = max(r1 , r2)
    g = max(g1 , g2)
    b = max(b1 , b2)
    return r,g,b

def menor(r1,g1,b1, r2,g2,b2):
    """ Devolve tuplo formado pela pelo maior dos dois."""
    r = min(r1 , r2)
    g = min(g1 , g2)
    b = min(b1 , b2)
    return r,g,b


def main4(imagem_fich_1, imagem_fich_2,funcao):
    imagem_1 = cImage.FileImage(imagem_fich_1)
    imagem_2 = cImage.FileImage(imagem_fich_2)
    
    largura_1 = imagem_1.getWidth()
    altura_1 = imagem_1.getHeight()
    largura_2 = imagem_2.getWidth()
    altura_2 = imagem_2.getHeight()
    largura = min(largura_1,largura_2)
    altura = min(altura_1,altura_2)
    
    janela = cImage.ImageWin('Fusão', largura, altura)
    
    nova_imagem = funde(imagem_1,imagem_2,funcao)
    
    nova_imagem.draw(janela)
    janela.exitOnClick()

# 7.13 - Apresenta-se o algoritmo de convolu��o
# o resultado depende do kernel

def convolve_cinza(imagem, pix_linha, pix_coluna, kernel):
    """ Calcula a convolu��o de UM pixel.Imagem em escala de cinzentos."""
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

def convolve_cor(imagem, pix_linha, pix_coluna, kernel):
    """ Calcula a convolu��o de um pixel.A cores."""
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
            
            soma_r = soma_r + int(intensidade_r * kernel[k_linha_indice][k_coluna_indice])
            soma_g = soma_g + int(intensidade_g * kernel[k_linha_indice][k_coluna_indice])
            soma_b = soma_b + int(intensidade_b * kernel[k_linha_indice][k_coluna_indice])
    return soma_r,soma_g,soma_b

def convolve_geral(imagem_fich, kernel):
    """ Convolve imagem a cores dado o kernel. """
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela_antiga = cImage.ImageWin('Original',largura,altura)
    mostra_imagem_c(imagem,janela_antiga)
    nova_imagem = cImage.EmptyImage(largura, altura)
    
    for linha in range(1, altura - 1):
        for coluna in range(1, largura - 1):
            r,g,b = convolve_cor(imagem, linha, coluna, kernel)
            pixel_cor = cImage.Pixel(r,g,b)
            # se for em escala de cinzentos incluir e alterar setPixel
            #pixel_cinza = pixel_cinzento(pixel_cor)
            nova_imagem.setPixel(coluna, linha, pixel_cor)
    janela_nova = cImage.ImageWin('Transformada',largura,altura)
    mostra_imagem_c(nova_imagem,janela_nova)
    janela_antiga.exitOnClick()
    janela_nova.exitOnClick()
    
def pixel_cinzento(pixel):
    """ Converte um pixel para escala de cinzentos."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()
    
    int_media = (vermelho + verde + azul) // 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
    return novo_pixel
    
   

# 7.14
def prod_escalar(vect1, vect2):
    """
    Produto escalr de dois vectores representados por listas.
    """
    prod = [vect1[i] * vect2[i] for i in range(len(vect1))]
    return sum(prod)

def prod_matriz_vector(mat,vec):
    """
    Produto de uma matriz  m x n por um vector 1 x n
    """
    res = [prod_escalar(mat[i],vec) for i in range(len(mat))]
    return res

def roda_imagem(imagem, angulo):
    """
    Roda a imagem um valor igual a angulo. Com amputa��o.
    """
    ang_rad= math.radians(angulo)
    val1 = math.cos(ang_rad)
    val2 = math.sin(ang_rad)
    mat=[[val1, -val2],[val2, val1]]
    
    largura = imagem.getWidth()
    altura = imagem.getHeight()

    
    # cria background branco
    pixel_branco = cImage.Pixel(255,255,255)
    
    nova_imagem = cImage.EmptyImage(largura, altura)
    for coluna in range(largura):
        for linha in range(altura):
            nova_imagem.setPixel(coluna,linha,pixel_branco)
            
    # roda num novo sistema de eixos
    
    for coluna in range((-largura/2)+1 , largura/2):
        for linha in range((-altura/2)+1 , altura/2):
            
            nova_coluna, nova_linha = [int(valor) for valor in prod_matriz_vector(mat,[coluna, linha])]

            nova_coluna = converte_x(nova_coluna, largura//2)
            nova_linha =  converte_y(nova_linha,altura//2)
            
            if dentro(nova_coluna,nova_linha, largura, altura):
                col = converte_x(coluna,largura//2)
                lin = converte_y(linha,altura//2)
                pixel = imagem.getPixel(col, lin)
                nova_imagem.setPixel(nova_coluna,nova_linha, pixel)
    return nova_imagem

def converte_x(px, referencia):
    return referencia + px


def converte_y(py, referencia):
    return referencia - py

def dentro(px1,py1,px2,py2):
    """
    Estou a considerar o canto superior esquerdo
    como tendo coordenadas (0,0).
    """
    res = (px1 > 0) and (py1 > 0) and (px1 < px2) and (py1 < py2)
    return res
            
    
def main14(imagem_fich, angulo):
    imagem = cImage.FileImage(imagem_fich)
    
    largura = imagem.getWidth()
    altura =  imagem.getHeight()
    
    janela = cImage.ImageWin('Roda', largura,altura)
    
    nova_imagem = roda_imagem(imagem, angulo)
    
    nova_imagem.draw(janela)
    
    janela.exitOnClick()


    
if __name__ =='__main__':
    main('/images/duck0.jpg',3,2)
    #main1(4,3,50,[(255,0,0),(0,0,255)])
    #main2()
    #main3()
    #main4('/images/duck.gif', '/images/two.gif', maior)
    #convolve_geral('/images/duck.gif',[[0,0.5,0],[0.5,2,0.5],[0,0.5,0]])
        