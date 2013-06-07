
# coding: utf-8

# =============================================================
# Introducao 'a Programacao e Resolucao de Problemas 2010-2011
# Resolucao modelo do Trabalho Pratico
# =============================================================


# Modulos do trabalho
import defines
import menu_ops
import image_ops
import file_ops



def main():
    
    # Dimensao da imagem activa1
    dimensao_x = 0
    dimensao_y = 0
    
    # Valores RGB dos pixeis que constituem a imagem
    imagem = None
    
    """ Afixa menu e processa opccao selecionada """
    
    termina = 0
    actualiza_imagem = 0
    
    while (not termina):
            
        if (actualiza_imagem):

            # Apresenta imagem actualizada
            image_ops.output_imagem(dimensao_x,dimensao_y,imagem)
            actualiza_imagem = 0
            
        # Apresenta menu principal e obtem opcao
        opcao=menu_ops.afixa_menu(defines.menu_principal)
        
        if (opcao == defines.MAIN_FIM):
            # Termina execucao do programa
            termina = 1
            
        elif ((opcao != defines.MAIN_CARREGA_FICH) and (not imagem)):
            # Ainda nao existe imagem carregada em memoria
            print ("Nao existe imagem carregada")
            continue
            
        else:
            # Executa operacao correspondente 'a opccao do utilizador
            actualiza_imagem,dimensao_x,dimensao_y,imagem = defines.accoes_menu_principal[opcao](dimensao_x,dimensao_y,imagem)
 
            
            
# Executa ciclo principal do programa                     
if __name__ == '__main__':
    main()

        
    
    