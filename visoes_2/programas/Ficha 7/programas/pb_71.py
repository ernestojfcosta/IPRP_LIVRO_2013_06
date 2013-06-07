import cImage
import random

def cozinha_mono(nx,ny,lado, cor, janela):
    """ Desenha os azulejos todos da mesma cor."""
    for coluna in range(nx):
        for linha in range(ny):
            imagem = quadrado(lado, cor)
            imagem.setPosition(coluna * lado,linha * lado)
            imagem.draw(janela)

def cozinha_poli(nx,ny,lado, cores, janela):
    """ Desenha os azulejos com duas cores alternadas."""
    for coluna in range(nx):
        for linha in range(ny):
            if (coluna + linha)%2 == 0:
                # par
                imagem = quadrado(lado, cores[0])
            else:
                # ’mpar
                imagem = quadrado(lado, cores[1])
                
            imagem.setPosition(coluna * lado,linha * lado)
            imagem.draw(janela)
                
def quadrado(lado,cor):
    """
    Cria um quadrado colorido de lado.
    """
    imagem = cImage.EmptyImage(lado,lado)
    pixel = cImage.Pixel(cor[0],cor[1],cor[2])
    for linha in range(lado):  
        for coluna in range(lado):
            imagem.setPixel(coluna,linha,pixel)       
    return imagem

def main1(nx,ny,lado,cores):
    janela = cImage.ImageWin('Ladrilhos',nx * lado, ny*lado)
    cozinha_poli(nx,ny,lado,cores, janela) 
    janela.exitOnClick()
    
def main2(nx,ny,lado):
    janela = cImage.ImageWin('Ladrilhos',nx * lado, ny*lado)
    # escolhe cores aleatoriamente
    cores= []
    for i in range(2):
        r = random.randint(0,255)
        g= random.randint(0,255)
        b = random.randint(0,255)
        while (r,g,b) in cores:
            r = random.randint(0,255)
            g= random.randint(0,255)
            b = random.randint(0,255)
        cores.append((r,g,b))
            
    cozinha_poli(nx,ny,lado,cores, janela) 
    janela.exitOnClick()
    
if __name__=='__main__':
    main2(4,3,50)
    
