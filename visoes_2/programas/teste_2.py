import coImage

if __name__ == '__main__':
    l_img = [[(1,2,3), (4,5,6),(7,8,9)],[(1,2,3), (4,5,6),(7,8,9)],[(1,2,3), (4,5,6),(7,8,9)],[(1,2,3), (4,5,6),(7,8,9)]]
    img = coImage.ListImage(l_img)
    larg = img.getWidth()
    alt = img.getHeight()
    
    janela = coImage.ImageWin('teste', larg, alt)
    
    img.draw(janela)
    
    lista = img.toList()
    
    print(lista)
    janela.exitOnClick()
    """
    img = cImage.EmptyImage(10,10)
    pixel = cImage.Pixel(1,2,3)
    """
    
    
    
    