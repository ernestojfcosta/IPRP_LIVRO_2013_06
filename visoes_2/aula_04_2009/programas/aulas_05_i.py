import cImage

def mostra_imagem(imagem1,imagem2):
    largura1 = imagem1.getWidth()
    altura1 = imagem1.getHeight()
    
    largura2 = imagem2.getWidth()
    altura2 = imagem2.getHeight() 
    
    janela1 = cImage.ImageWin('Imagem 1', largura1,altura1)
    janela2 = cImage.ImageWin('Imagem 2', largura2,altura2)
    
    imagem1.draw(janela1)
    imagem2.draw(janela2)
    
    janela1.exitOnClick()
    janela2.exitOnClick()

    
def converte_imagem(imagem):
    largura = imagem.getWidth()
    altura = imagem.getHeight()

    
    #janela = cImage.ImageWin('Imagem', largura,altura)
    
    lista = imagem.toList()
    
    #imagem.draw(janela)
    #janela.exitOnClick()
    return lista
    
    
def main(img1_fich, img2_fich):
    imagem_1 = cImage.FileImage(img1_fich)
    imagem_2 = cImage.FileImage(img2_fich)
    mostra_imagem(imagem_1,imagem_2)
    
def main1(img_fich):
    imagem = cImage.FileImage(img_fich)
    nova_imagem = converte_imagem(imagem)
    print nova_imagem
    
if __name__ == '__main__':
    #main('/tempo/imagens/duck3.jpg','/tempo/imagens/bird1.jpg')
    main1('/tempo/imagens/duck3.jpg')
    