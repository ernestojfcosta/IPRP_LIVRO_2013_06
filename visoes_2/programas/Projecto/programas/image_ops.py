
# coding: utf-8

"""
Operações sobre imagens
pixel_negativo - recebe pixel e devolve o seu negativo
pixel_cinza - recebe pixel e devolve pixel na correspondente escala de cinzas
transforma_negativo - transforma imagem no seu negativo
transforma_cinza - transforma imagem em imagem em tons de cinza
cria_moldura - cria moldura em imagem activa
output_imagem - Afixa imagem activa
roda_imagem - roda imagem activa
flip_imagem - inverte horizontalmente ou verticalmente a imagem
corta_imagem - corta a imagem dadas as coordenadas
ajusta_imagem - altera componentes de cor da imagem
encripta_imagem - encripta a imagem activa
oculta_imagem - oculta string em imagem
"""

# Modulos externos
import Image
import random
import sys

# Importação de definições
import defines
import menu_ops


def pixel_negativo(r,g,b):
    
    """Devolve pixel negativo do recebido
    Argumentos: Componente R, componente G, Componente B
    Devolve: Componente R, componente G, componente B"""
    
    return 255-r,255-g,255-g


def pixel_cinza(r,g,b):
    
    """Devolve pixel em escala de cinzas do recebido
    Argumentos: Componente R, componente G, Componente B
    Devolve: Componente R, componente G, componente B"""
    
    media=(r+g+b)/3
    
    return media,media,media


def transforma_negativo(dimensao_x,dimensao_y,imagem):
    
    """Transforma imagem em imagem negativa da original
    Argumentos: Dimensão X, dimensão Y, lista com a imagem
    Devolve: Indicação de actualização, dimensão X, dimensão Y, lista com a imagem"""
    
    # Opera transformação para cada pixel da imagem
    for y in range (dimensao_y):
        for x in range (dimensao_x):
            imagem[dimensao_x*y+x][0],imagem[dimensao_x*y+x][1],imagem[dimensao_x*y+x][2]=pixel_negativo(imagem[dimensao_x*y+x][0],imagem[dimensao_x*y+x][1],imagem[dimensao_x*y+x][2]) 
            
    return defines.ACTUALIZA,dimensao_x,dimensao_y,imagem


def transforma_cinza(dimensao_x,dimensao_y,imagem):
    
    """Transforma imagem em imagem em tons de cinza
    Argumentos: Dimensão X, dimensão Y, lista com a imagem
    Devolve: Indicação de actualização, dimensão X, dimensão Y, lista com a imagem"""
    
    # Opera transformação para cada pixel da imagem
    for y in range (dimensao_y):
        for x in range (dimensao_x):
            imagem[dimensao_x*y+x][0],imagem[dimensao_x*y+x][1],imagem[dimensao_x*y+x][2]=pixel_cinza(imagem[dimensao_x*y+x][0],imagem[dimensao_x*y+x][1],imagem[dimensao_x*y+x][2]) 
            
    return defines.ACTUALIZA,dimensao_x,dimensao_y,imagem

    
def cria_moldura(dimensao_x,dimensao_y,imagem):
    
    """Cria moldura em imagem activa
    Argumentos: Dimensão X, dimensão Y, lista com a imagem
    Devolve: Indicação de actualização, dimensão X, dimensão Y, lista com a imagem"""
    
    #Pede ao utilizador o tamanho da moldura preta a introduzir na imagem
    tam_moldura=menu_ops.afixa_menu(defines.menu_moldura)
    
    if (tam_moldura != defines.MOD_FIM):
        
        tam_moldura *= 5
    
        # Acrescenta moldura horizontal na parte de cima da imagem
        for y in range (tam_moldura):
            for x in range (dimensao_x+2*tam_moldura):
                imagem.insert(0,[0,0,0])
            
        # Acrescenta moldura vertical nos lados esquerdo e direito da imagem
        for y in range (dimensao_y):
            start=((dimensao_x+2*tam_moldura)*tam_moldura)+(y*(dimensao_x+2*tam_moldura))
            for i in range (tam_moldura):
                imagem.insert(start+i,[0,0,0])
            start += (tam_moldura+dimensao_x)
            for i in range (tam_moldura):
                imagem.insert(start+i,[0,0,0])
            
        # Acrescenta moldura horizontal na parte de baixo da imagem
        for y in range (tam_moldura):
            for x in range (dimensao_x+2*tam_moldura):
                imagem.insert(-1,[0,0,0])
    
        dimensao_x += 2*tam_moldura
        dimensao_y += 2*tam_moldura
    
        return defines.ACTUALIZA,dimensao_x,dimensao_y,imagem
    
    else:
        
        return defines.NAO_ACTUALIZA,dimensao_x,dimensao_y,imagem


def output_imagem(dimensao_x,dimensao_y,imagem):
    
    """Afixa imagem activa em memoria
    Argumentos: Dimensão X, dimensão Y, lista com a imagem"""

    print '>>> Output imagem com dimensoes:',dimensao_x,'x',dimensao_y
    print '>>> Dimensao da lista com a imagem em memoria:',len(imagem)
    
    # Cria janela com as dimensões correspondentes à imagem
    image = Image.new('RGB',(dimensao_x,dimensao_y))
    
    # Constroi imagem
    for y in range (dimensao_y):
        for x in range (dimensao_x):
            image.putpixel((x,y),(imagem[y*dimensao_x+x][0],imagem[y*dimensao_x+x][1],imagem[y*dimensao_x+x][2]))
    image.show(title="sample output")
    
    return None


def roda_imagem(dimensao_x,dimensao_y,imagem):
    
    """Roda a imagem activa em memoria
    Argumentos: Dimensão X, dimensão Y, lista com a imagem
    Devolve: Indicação de actualização, dimensão X, dimensão Y, lista com a imagem"""
    
    rotacao = menu_ops.afixa_menu(defines.menu_rotacao)
    
    if (rotacao != defines.ROT_FIM):
    
        if (rotacao == defines.ROT_90):
            
            imagem2=[]
     
            # Rotação de 90 graus clockwise
            for x in range(dimensao_x):
                for y in range(dimensao_y):
                    imagem2.append(imagem[dimensao_x*(dimensao_y-(y+1))+x])
            dimensao_x,dimensao_y=dimensao_y,dimensao_x
    
        elif (rotacao == defines.ROT_180):
            
            imagem2=[]
        
            # Rotação de 180 graus clockwise
            for y in range(dimensao_y-1,-1,-1):
                for x in range(dimensao_x-1,-1,-1):
                    imagem2.append(imagem[dimensao_x*y+x])
                
        return defines.ACTUALIZA,dimensao_x,dimensao_y,imagem2

    else:
        
        return defines.NAO_ACTUALIZA,dimensao_x,dimensao_y,imagem
    
    
def flip_imagem(dimensao_x,dimensao_y,imagem):
    
    """Flip horizontal ou vertical da imagem activa em memoria
    Argumentos: Dimensão X, dimensão Y, lista com a imagem
    Devolve: Indicação de actualização, dimensão X, dimensão Y, lista com a imagem"""
    
    flip = menu_ops.afixa_menu(defines.menu_flip)
    
    if (flip != defines.FLIP_FIM):
    
        if (flip == defines.FLIP_HOR):
            
            # Flip horizontal da imagem
            for y in range(dimensao_y):
                for x in range(dimensao_x/2):
                    imagem[y*dimensao_x+x],imagem[y*dimensao_x+dimensao_x-x-1] = imagem[y*dimensao_x+dimensao_x-x-1],imagem[y*dimensao_x+x]
        
        elif (flip == defines.FLIP_VER):
            
            # Flip vertical da imagem
            for x in range(dimensao_x):
                for y in range(dimensao_y/2):
                    imagem[y*dimensao_x+x],imagem[(dimensao_y-y-1)*dimensao_x+x] = imagem[(dimensao_y-y-1)*dimensao_x+x],imagem[y*dimensao_x+x]
       
        return defines.ACTUALIZA,dimensao_x,dimensao_y,imagem
    
    else:
        
        return defines.NAO_ACTUALIZA,dimensao_x,dimensao_y,imagem

    
def corta_imagem(dimensao_x,dimensao_y,imagem):
    
    """Corte da imagem activa em memoria
    Argumentos: Dimensão X, dimensão Y, lista com a imagem
    Devolve: Indicação de actualização, dimensão X, dimensão Y, lista com a imagem"""
    
    # Obtem coordenadas para operacao de corte
    xs,ys,xi,yi = menu_ops.get_corte(dimensao_x,dimensao_y)
    
    imagem2 = []
    
    # Copia pixeis na area selecionada para a nova lista
    base_y = dimensao_x * (dimensao_y-ys)
    for i in range (ys-yi+2):
        for j in range (xi-xs+2):
            indice = base_y + i*(dimensao_x) + xs + j
            imagem2.append(imagem[indice])
     
    # Actualiza coordenadas
    dimensao_x = xi - xs + 2
    dimensao_y = ys - yi + 2
    
    return defines.ACTUALIZA,dimensao_x,dimensao_y,imagem2


def ajusta_imagem(dimensao_x,dimensao_y,imagem):
    
    """Ajustes a componentes RGB na imagem
    Argumentos: Dimensão X, dimensão Y, lista com a imagem
    Devolve: Indicação de actualização, dimensão X, dimensão Y, lista com a imagem"""
    
    componente = menu_ops.afixa_menu(defines.menu_ajustes)
    
    if (componente != defines.AJU_FIM):
        
        valor_ajuste = menu_ops.get_ajuste()
        
        for i in range(len(imagem)):
            if (componente == defines.AJU_RED):
                imagem[i][0] = valor_ajuste
            elif (componente == defines.AJU_GREEN):
                imagem[i][1] = valor_ajuste
            elif (componente == defines.AJU_BLUE):
                imagem[i][2] = valor_ajuste
                
        return defines.ACTUALIZA,dimensao_x,dimensao_y,imagem
    
    else:
            
        return defines.NAO_ACTUALIZA,dimensao_x,dimensao_y,imagem


def encripta_imagem(dimensao_x,dimensao_y,imagem):
    
    """Encripta imagem em ficheiro
    Argumentos: Dimensão X, dimensão Y, lista com a imagem
    Devolve: Indicação de actualização, dimensão X, dimensão Y, lista com a imagem"""
    
    operacao = menu_ops.afixa_menu(defines.menu_encriptacao)
    
    if (operacao != defines.ENC_FIM):
        
        # Obtem password a utilizar como semente na geracao da cifra
        password = menu_ops.get_password()
        
        # Calcula valor para a semente
        seed = 0
        for i in range( len(password) ):
            seed += ord(password[i])
        
        
        # Gera sequencia aleatoria a utilizar como password
        password = []
        
        repetidos=0

        # Gera sequencia de dimensao_x numeros unicos, a utilizar como password
        random.seed(seed)
        
        for i in range (dimensao_x):
            novo = 0
            while ( not novo ):
                novo_numero=random.randint(1,dimensao_x)
                if ( novo_numero not in password ):
                    novo = 1
                    password.append(novo_numero)
                                        
        # Lista de imagem auxiliar
        imagem2 = []
        for i in range( dimensao_x * dimensao_y ):
            imagem2.append([0,0,0])
        
        if ( operacao == defines.ENC_ENC ):
            
            # Encripta imagem activa em memória, trocando a ordem 'as colunas
            # de acordo com a password gerada anteriormente
                        
            for i in range ( dimensao_x ):
                
                # Copia para a nova imagem a coluna cuja posicao e' dada pelo numero armazenado na password
                for j in range (dimensao_y ):
                    imagem2.pop(j*dimensao_x+i)
                    imagem2.insert(j*dimensao_x+i,imagem[j*dimensao_x+password[i]-1])

                                   
        else:
            
            # Percorre password de modo a reconstruir imagem original
            for i in range ( dimensao_x ):
                
                for j in range ( dimensao_y) :
                    imagem2.pop(password[i]-1+j*dimensao_x)
                    imagem2.insert(password[i]-1+j*dimensao_x,imagem[i+j*dimensao_x])
    
        
        return defines.ACTUALIZA,dimensao_x,dimensao_y,imagem2
    
    else:
        
        return defines.NAO_ACTUALIZA,dimensao_x,dimensao_y,imagem


def oculta_mensagem(dimensao_x,dimensao_y,imagem):
    
    """Oculta mensagem em ficheiro de imagem
    Argumentos: Dimensão X, dimensão Y, lista com a imagem
    Devolve: Indicação de actualização, dimensão X, dimensão Y, lista com a imagem"""
    
    operacao = menu_ops.afixa_menu(defines.menu_ocultar)
    
    if ( operacao != defines.OCU_FIM):
        
        if ( operacao == defines.OCU_ESC):
            
            # Obtem a mensagem a ocultar na imagem
            mensagem = menu_ops.get_mensagem(imagem)
            mensagem += '\n'
        
            indice_imagem = 0
            indice_rgb = 0
            
            # Percorre todos os caracteres da mensagem a ocultar
            for i in range( len(mensagem) ): 
                # Para cada um dos 8 bits de cada caracter
                for j in range( 8 ):
                    # Obtem o bit correspondente
                    novo_bit = (ord(mensagem[i])>>j) & 1
                    # Armazena o bit no bit menos significativo da componente de cor
                    novo_valor = imagem[indice_imagem][indice_rgb]
                    if (novo_bit == 1):
                        novo_valor = novo_valor | novo_bit
                    else:
                        novo_valor = novo_valor & 254
                    imagem[indice_imagem][indice_rgb] = novo_valor
                    
                    # Avanca indices
                    indice_rgb += 1
                    if ( indice_rgb == 3 ):
                        indice_rgb = 0
                        indice_imagem += 1

        
                        
            return defines.ACTUALIZA,dimensao_x,dimensao_y,imagem
        
                    
        elif ( operacao == defines.OCU_LER):

            # Obtem mensagem oculta na imagem activa em memoria
            indice_caracter = 0
            novo_caracter = 0
            indice_imagem = 0
            termina = 0
            mensagem = ""
            indice_sai = 0
    
            
            # Percorre todos os valores rgb da imagem, ate' encontrar o newline
            while ( (not termina) and (indice_imagem<len(imagem)) and (indice_imagem<defines.MAX_MSG) ):
                
                # Para cada um dos 3 componentes de cor
                for j in range( 3 ):
                    
                    # Obtem o bit armazenado na componente de cor
                    novo_bit = ( imagem[indice_imagem][j] & 1 )
                    
                    # Armazena o bit no novo caracter
                    novo_caracter = ( novo_caracter | (novo_bit<<indice_caracter) )
                    # Avanca indices
                    indice_caracter += 1
                    
                    if ( indice_caracter == 8 ):
                        indice_caracter = 0
                        mensagem = mensagem + chr(novo_caracter)
                        if ( novo_caracter == ord('\n')):
                            termina = 1
                        novo_caracter = 0
                            
                indice_imagem += 1

                
            if (termina):
                print "A mensagem oculta na imagem e' a seguinte: ", mensagem
            else:
                print "A imagem não tem mensagem armazenada"
                
            return defines.NAO_ACTUALIZA,dimensao_x,dimensao_y,imagem

    else:
        
        return defines.NAO_ACTUALIZA,dimensao_x,dimensao_y,imagem

    
    
# Devolve informação acerca do módulo se chamado individualmente
def main():
    print ("Informação acerca da utilizacao deste módulo:")
    print (__doc__)
    
if __name__ == '__main__':
    main()
else:
    print ("image_ops loaded as a module")