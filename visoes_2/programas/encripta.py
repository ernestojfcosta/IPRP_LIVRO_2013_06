import cImage
import random

def encripta(imagem):
    """Encripta uma imagem mudando a ordem das linhas."""
    # Converte em lista de listas

    imagem_lista = imagem.toList()
    # Define permutação
    tamanho = len(imagem_lista)
    original = list(range(tamanho))
    permuta = original[:]
    random.shuffle(permuta)
    # Encripta
    nova_imagem_lista = mistura_imagem(imagem_lista, permuta)
    # Converte de volta
    nova_imagem = cImage.ListImage(nova_imagem_lista)
    return nova_imagem

def mistura_imagem(imagem, permuta):
    nova_imagem = []
    for i in range(len(imagem)):
        nova_imagem.append(imagem[permuta[i]])
    return nova_imagem

def mostra_encripta(imagem):
    img = cImage.FileImage(imagem)
    largura = img.getWidth()
    altura = img.getHeight()
    
    nova_imagem = encripta(img)
    
    janela = cImage.ImageWin('Encripta', 2*largura, altura)
    nova_imagem.setPosition(largura+1,0)
    
    img.draw(janela)
    nova_imagem.draw(janela)
    
    janela.exitOnClick()
    
    
    


if __name__ == '__main__':
    """
    imagem = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    original = list(range(len(imagem)))
    random.shuffle(original)
    print(original)
    nova_imagem = mistura_imagem(imagem, original)
    print(nova_imagem)
    """
    mostra_encripta('/images/calvin_leia.jpg')