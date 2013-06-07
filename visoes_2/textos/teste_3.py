import cImage
import random

def gera_tuplo():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def gera_imagem(n,m):
    return [[ gera_tuplo() for coluna in range(m)] for linha in range(n)]

def gera_imagem_b(n,m):
    return [[ (0,0,255) for coluna in range(m)] for linha in range(n)]

def cria_imagem_lista(n,m):
    lista_imagem = gera_imagem(n,m)
    imagem = cImage.ListImage(lista_imagem)
    return imagem

def mostra(n,m):
    imagem = cria_imagem_lista(n,m)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('teste',largura, altura)
    imagem.draw(janela)
    janela. exitOnClick()
    
if __name__ == '__main__':
    mostra(320,240)
    