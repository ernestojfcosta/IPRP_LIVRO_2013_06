#import matplotlib
import pylab

#import numpy

def le_uma_temperatura(f_ent):
    """
    Lê os dados da temperatura de uma cidade.
    Devolve -1 se alcançou o fim de ficheiro
    """
    # procura primeira linha significativa 
    linha = f_ent.readline()

    while (linha !='') and (linha == '\n'):
        linha = f_ent.readline()
    
    if linha == '':
        return -1
    else:
        linha = linha[:-1].split()
        #lista_num = [float(dado) for dado in linha]
        lista_num = []
        for indice in range(len(linha)):
            lista_num.append(float(linha[indice]))

        return lista_num

def le_todas_temperaturas(fich):
    """
    Extrai os dados de temperaturas relativos a Portugal.
    """
    f_ent = open(fich,'r')   
    portugal = list()
    
    dados = le_uma_temperatura(f_ent)
    while dados != -1:
        portugal.append(dados)
        dados = le_uma_temperatura(f_ent)
    f_ent.close()
    return portugal

def main1(fich):
    """
    Gráfico das temperaturas médias.
    """
    lista_temp = le_todas_temperaturas(fich)
    lista_temp_mes = transposta_matriz(lista_temp)
    valores_medios = [(sum(mes)/float(len(mes))) for mes in lista_temp_mes]

    pylab.plot(valores_medios)
    pylab.xlabel('Meses do Ano')
    pylab.ylabel('Temp C')
    pylab.title('Temperaturas Medias')
    pylab.show()   

def main3(fich):
    """
    Gráfico das temperaturas médias.
    """
    lista_temp = le_todas_temperaturas(fich)
    valores_medios = medias_colunas(lista_temp)
    t = pylab.arange(1,13,1)
    pylab.plot(t,valores_medios, 'D-')
    pylab.xlabel('Meses do Ano')
    pylab.ylabel('Temp C')
    pylab.title('Temperaturas Medias')
    pylab.show()   

def main1(fich):
    """
    Gráfico das temperaturas individuais.
    """
    lista_temp = le_todas_temperaturas(fich)
    t = pylab.arange(1,13,1)
    for indice in range(len(lista_temp)):
        pylab.plot(t,lista_temp[indice])
    pylab.xlabel('Meses do Ano')
    pylab.ylabel('Temp C')
    pylab.title('Temperaturas')
    pylab.show()
    
    
def transposta_matriz(matriz):
	return [[linha[coluna] for linha in matriz] for coluna in range(len(matriz[0]))]
    
    
def medias_colunas(matriz):
    """
    Medias dos valores por colunas...
    """
    medias = list()
    num_colunas = len(matriz[0])
    
    for coluna in range(num_colunas):
	soma = 0
	for linha in range(len(matriz)):
	    soma = soma + matriz[linha][coluna]
	val = soma / float(num_colunas)
	medias.append(val)
    return medias
    
    
if __name__ == '__main__':
    """
    ficheiro = open('/tempo/data/tempo_portugal.txt','r')
    ficha = le_cidade(ficheiro)
    if ficha != -1:
        cidade, pluviosidade,temperatura = ficha
        print cidade
        print pluviosidade
        print temperatura
    else:
        print 'fim de ficheiro'
    """
    #print dados_portugal('/tempo/data/tempo_portugal.txt')
    #main('/tempo/data/tempo_portugal.txt')
    main3('/tempo/data/temperaturas.txt')
    #lista = [[(1,1),(1,2),(1,3),(1,4)],[(2,1),(2,2),(2,3),(2,4)],[(3,1),(3,2),(3,3),(3,4)]]
    #print transposta_matriz(lista)
    