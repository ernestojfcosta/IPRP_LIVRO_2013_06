
# coding: utf-8

"""
Definição de valores e menus
"""


from file_ops import *
from image_ops import *


# Controlo de actualização da imagem afixada
NAO_ACTUALIZA = 0
ACTUALIZA = 1

# Tamanho máximo de mensagem ocultada em imagem
MAX_MSG = 100


# Definições para opcções do menu principal
MAIN_FIM = 0
MAIN_CARREGA_FICH = 1
MAIN_GUARDA_FICH = 2
MAIN_MOLDURA = 3
MAIN_NEGATIVO = 4
MAIN_CINZA = 5
MAIN_RODA = 6
MAIN_MIRRORING = 7
MAIN_CORTE = 8
MAIN_AJUSTES = 9
MAIN_ENCRIPTA = 10
MAIN_ESTEGANO = 11


# Definições para opcções do menu de rotações
ROT_FIM = 0
ROT_90 = 1
ROT_180 = 2


# Definições para opcções do menu de moldura
MOD_FIM = 0
MOD_5 = 1
MOD_10 = 2
MOD_15 = 3
MOD_20 = 4


# Definições para opcções do menu de flip
FLIP_FIM = 0
FLIP_HOR = 1
FLIP_VER = 2


# Definições para opcções do menu de ajustes RGB
AJU_FIM = 0
AJU_RED = 1
AJU_GREEN = 2
AJU_BLUE = 3


# Definições para opcções do menu de encriptação
ENC_FIM = 0
ENC_ENC = 1
ENC_DEC = 2


# Definições para opcções do menu de ocultação
OCU_FIM = 0
OCU_LER = 1
OCU_ESC = 2


# Opcções do menu principal
menu_principal = { MAIN_CARREGA_FICH : "Carregar imagem de ficheiro", \
                   MAIN_GUARDA_FICH : "Guardar imagem em ficheiro", \
                   MAIN_MOLDURA : "Criacao de moldura em imagem", \
                   MAIN_NEGATIVO : "Passagem a negativo de imagem",
                   MAIN_CINZA: "Passagem de imagem a tons de cinza",\
                   MAIN_RODA : "Rotacao da imagem", \
                   MAIN_MIRRORING : "Mirroring horizontal ou vertical da imagem", \
                   MAIN_CORTE : "Corte da imagem",\
                   MAIN_AJUSTES : "Alteracao de vermelhos, verdes e azuis", \
                   MAIN_ENCRIPTA : "Encriptacao de imagem", \
                   MAIN_ESTEGANO : "Ocultacao de mensagem em imagem", \
                   MAIN_FIM : "*Terminar programa*", \
                 }


# Funções correspondentes às opcções do menu principal
accoes_menu_principal = { MAIN_CARREGA_FICH : read_image_from_file, \
                          MAIN_GUARDA_FICH : write_image_to_file, \
                          MAIN_MOLDURA : cria_moldura, \
                          MAIN_NEGATIVO : transforma_negativo, \
                          MAIN_CINZA : transforma_cinza, \
                          MAIN_RODA : roda_imagem, \
                          MAIN_MIRRORING : flip_imagem, \
                          MAIN_CORTE : corta_imagem, \
                          MAIN_AJUSTES : ajusta_imagem, \
                          MAIN_ENCRIPTA : encripta_imagem, \
                          MAIN_ESTEGANO : oculta_mensagem
                        }


# Opcções do menu rotação
menu_rotacao =  {  ROT_90 : "Rotacao (clockwise) de 90 graus", \
                   ROT_180 : "Rotacao (clockwise) de 180 graus", \
                   ROT_FIM : "*Regressar ao menu principal", \
                }


# Opcções do menu moldura
menu_moldura =  {  MOD_5  : "Cria moldura com 5 pixes", \
                   MOD_10 : "Cria moldura com 10 pixeis", \
                   MOD_15 : "Cria moldura com 15 pixeis", \
                   MOD_20 : "Cria moldura com 20 pixeis", \
                   MOD_FIM : "*Regressa ao menu principal", \
                }
 


# Opcções do menu flip
menu_flip =     {  FLIP_HOR : "Flip horizontal da imagem", \
                   FLIP_VER : "Flip vertical da imagem", \
                   FLIP_FIM : "*Regressa ao menu principal", \
                }


# Opcções do menu flip
menu_ajustes =  {  AJU_RED   : "Ajuste do componente RED", \
                   AJU_GREEN : "Ajuste do componente GREEN", \
                   AJU_BLUE  : "Ajuste do componente BLUE", \
                   AJU_FIM   : "*Regressa ao menu principal", \
                }


# Opcções do menu encriptação
menu_encriptacao = {   ENC_ENC : "Cifrar imagem activa em memoria", \
                    ENC_DEC : "Decifrar imagem activa em memoria", \
                    ENC_FIM : "*Regressa ao menu principal", \
                }


# Opcções do menu ocultar
menu_ocultar = {   OCU_LER : "Ler mensagem oculta em imagem", \
                       OCU_ESC : "Escrever mensagem oculta em imagem", \
                       OCU_FIM : "*Regressa ao menu principal", \
                   }



# Devolve informação acerca do módulo se chamado individualmente
def main():
    print ("Informação acerca da utilização deste módulo:")
    print (__doc__)
    
if __name__ == '__main__':
    main()
else:
    print ("defines loaded as a module")
    
    