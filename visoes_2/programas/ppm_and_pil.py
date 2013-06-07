"""
Tratamento de imagens no formato PPM.
Ernesto Costa, May 2013
"""
import cImage


def ppm_to_pil(imagem):
    # carrega ficheiro
    with open(imagem,'r') as ppm_img:
        # extrai cabeçalho (modo e comentário)
        ppm_img.readline()
        ppm_img.readline()
        # extrai dimensão
        dim = ppm_img.readline().split()
        largura = int(dim[0])
        altura = int(dim[1])
        # valor máximo de cor
        max_cor = ppm_img.readline()
        # cria imagem
        pil_img = cImage.EmptyImage(largura,altura)
        # converte
        for lin in range(altura):
            for col in range(largura):
                r = int(ppm_img.readline().rstrip('\n'))
                g = int(ppm_img.readline().rstrip('\n'))
                b = int(ppm_img.readline().rstrip('\n'))
                pixel = cImage.Pixel(r,g,b)
                pil_img.setPixel(col,lin,pixel)
    ppm_img.close()
    return pil_img

def mostra_ppm(imagem):
    """ Procede à diminiuição da pixelização da imagem."""  
    # carrega e Converte
    img = ppm_to_pil(imagem)
    # Cria janela
    largura = img.getWidth()
    altura = img.getHeight()    
    janela = cImage.ImageWin('PPM to PIL', largura, altura )
    # Salva imagem no disco
    nome_ficheiro  = imagem.split('.')[0] + '_to' + '.jpg'    
    img.save(nome_ficheiro)
    # Coloca imagem
    img.draw(janela)
    # Termina
    janela.exitOnClick() 
    
def pil_to_ppm(imagem):
    """Constrói e salva uma imagem em formato PPM, modo ASCII."""
    # carrega ficheiro origem
    pil_img = cImage.FileImage(imagem)
    largura = pil_img.getWidth()
    altura = pil_img.getHeight()
    nome_completo = imagem.split('/')[-1]
    nome  = '/Users/ernestojfcosta/Desktop/' + nome_completo.split('.')[0] + '.ppm'
    ficheiro = open(nome,'w') 
    # constrói cabeçalho (modo, comentário, dimensão, cor máxima
    ficheiro.write('P3\n')
    ficheiro.write('# Criado por Ernesto Costa.\n')
    ficheiro.write(str(largura) + ' ' + str(altura) + '\n')
    ficheiro.write('255\n')
    # Guarda pixeis
    for lin in range(altura):
        for col in range(largura):
            pixel = pil_img.getPixel(col,lin)
            r = str(pixel.getRed()) + '\n'
            ficheiro.write(r)
            g = str(pixel.getGreen()) + '\n'
            ficheiro.write(g)   
            b = str(pixel.getBlue()) + '\n'
            ficheiro.write(b)                                   
    ficheiro.close()
    return ficheiro

if __name__ == '__main__':
    mostra_ppm('/images/lena.ppm')
    #fich = pil_to_ppm('/images/calvin_leia.jpg')

    
