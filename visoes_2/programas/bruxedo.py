import cImage


lista_pix = [(171, 166, 160), (172, 165, 157), (173, 164, 155), (173, 166, 158), (174, 165, 160), (174, 165, 160), (173, 166, 156), (173, 164, 155), (173, 164, 155)]

pix_tuplo_rgb = list(zip(*lista_pix))
print(pix_tuplo_rgb)
novo_pixel = tuple([sum(elem)//9 for elem in pix_tuplo_rgb])
print(novo_pixel)

nova_imagem = cImage.EmptyImage(20,10)
nova_imagem.setPixel(15, 6 , cImage.Pixel(*novo_pixel))
"""
janela = cImage.ImageWin('Imagem', 20,10)
nova_imagem.draw(janela)
janela.exitOnClick()
"""


