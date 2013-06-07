
# coding: utf-8

"""
Operações sobre ficheiros:
write_image_to_file - Escrita de imagem em ficheiro
read_image_from_file - Leitura de imagem a partir de ficheiro
""" 

# Importação de definições
import defines



def write_image_to_file(dimensao_x,dimensao_y,imagem):
    
    """Escreve imagem em ficheiro no formato PPM
    Argumentos: Dimensão X, dimensão y, lista com a imagem
    Devolve: Indicação de actualização, dimensão X, dimensão Y, lista com a imagem"""
    
    # Abertura de ficheiro para escrita de imagem
    ficheiro_out = raw_input("Indique caminho/nome para ficheiro de imagem a gravar: ")
    f_out = open(ficheiro_out,'w')    
        
    # Escreve a primeira linha (P3)
    f_out.write("P3\n")
    
    # Escreve a segunda linha (comentario de criação)
    f_out.write("# CREATOR: IPRP Image Manipulation Program Version 0.9\n")
    
    # Escreve tamanho da imagem
    f_out.write(str(dimensao_x)+" "+str(dimensao_y)+'\n')
    
    # Escreve o valor maximo de cor
    f_out.write("255\n")
    
    # Escreve no resto do ficheiro os valores RGB dos pixeis
    for y in range (dimensao_y):
        for x in range (dimensao_x):
            f_out.write(str(imagem[y*dimensao_x+x][0])+'\n')
            f_out.write(str(imagem[y*dimensao_x+x][1])+'\n')
            f_out.write(str(imagem[y*dimensao_x+x][2])+'\n')
            
    # Ficheiro com imagem já pode ser fechado
    f_out.close()
        
    return defines.NAO_ACTUALIZA,dimensao_x,dimensao_y,imagem


def read_image_from_file(dimensao_x,dimensao_y,imagem):
    
    """Le imagem no formato PPM a partir de ficheiro
    Argumentos: Dimensão X, dimensão y, lista com a imagem
    Devolve: Indicação de actualização, dimensão X, dimensão Y, lista com a imagem"""
    
    # Abertura de ficheiro para leitura de imagem para memoria
    ficheiro_in = raw_input("Indique nome do ficheiro com a imagem no formato PPM: ")
    f_obj = open(ficheiro_in,'r')    
            
    # Ignora a primeira linha (P3)
    f_obj.readline()
    # Ignora a segunda linha (comentario de criacao)
    f_obj.readline()
    # Le tamanho da imagem
    dimensao = f_obj.readline().split()
    dim_x = int(dimensao[0])
    dim_y = int(dimensao[1])
    # Le o valor maximo de cor (ignorado para ja')
    f_obj.readline()
    # O resto do ficheiro contem os valores RGB dos pixeis
    imagem=[]
    while True:
        one_more_r= f_obj.readline().rstrip('\n')
        one_more_g= f_obj.readline().rstrip('\n')
        one_more_b= f_obj.readline().rstrip('\n')
        if len(one_more_r) == 0:
            break # EOF
        else:
            r=int(one_more_r)
            g=int(one_more_g)
            b=int(one_more_b)
            imagem.append([r,g,b])
    
    # Ficheiro com imagem ja' pode ser fechado
    f_obj.close()
        
    return defines.ACTUALIZA,dim_x,dim_y,imagem



# Devolve informação acerca do módulo se chamado individualmente
def main():
    print ("Informação acerca da utilização deste módulo:")
    print (__doc__)
    
if __name__ == '__main__':
    main()
else:
    print ("file_ops loaded as a module")