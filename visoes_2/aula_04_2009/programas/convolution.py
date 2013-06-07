import cImage


def pixel_cinzento(pixel):
    """ Converte um pixel para escala de cinzentos."""
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()
    
    int_media = (vermelho + verde + azul) / 3
    novo_pixel = cImage.Pixel(int_media,int_media, int_media)
    return novo_pixel

def manipula_imagem(imagem, funcao_cor):
    """ Manipula uma imagem de acordo com uma função."""
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
    """ Transforma uma imagem de acordo com a função de cor."""
    imagem = cImage.FileImage(imagem_fich)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Transformação de Imagem', 2*largura,altura)
    imagem.draw(janela)
    
    nova_imagem = manipula_imagem(imagem,funcao_cor)
    nova_imagem.setPosition(largura + 1, 0)
    nova_imagem.draw(janela)
    janela.exitOnClick()
    
def convolve(anImage,pixelRow,pixelCol,kernel):
    """ Image in gray scale."""
    kernelColumnBase = pixelCol - 1
    kernelRowBase = pixelRow - 1
    
    sum = 0
    for row in range(kernelRowBase,kernelRowBase+3):
        for col in range(kernelColumnBase,kernelColumnBase+3):
            kColIndex = col-kernelColumnBase
            kRowIndex = row-kernelRowBase
            
            apixel = anImage.getPixel(col,row)
            intensity = apixel.getRed()
            
            sum = sum + intensity * kernel[kRowIndex][kColIndex]
    
    return sum


def main():
    kernel_x = [[-1,0,1],[-2,0,2],[-1,0,1]]
    kernel_y = [[1,2,1],[0,0,0],[-1,-2,-1]]
    
    janela = cImage.ImageWin('Convolução', 270,360)
    my_image = cImage.FileImage(270,360)
    