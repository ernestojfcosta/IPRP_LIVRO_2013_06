import urllib
import math
import pylab

def media(lista):
    """ 
    Calcula a m�dia.
    """
    med = sum(lista) / float(len(lista))
    return med

def desvio_padrao(lista):
    """
    Calcula o desvio padr�o.
    """
    a_media = media(lista) # <-- Aten��o
    
    soma = 0
    for elem in lista:
        soma = soma + (elem - a_media) ** 2
        
    desvio = math.sqrt(float(soma) / (len(lista) - 1))
    return desvio

def pearson(lista_a, lista_b):
    """ Calcula o coeficiente de correla��o entre duas listas de valores."""
    media_a = media(lista_a)
    media_b = media(lista_b)
    
    desvio_a = desvio_padrao(lista_a)
    desvio_b = desvio_padrao(lista_b)
    
    n = len(lista_a) # n�mero de elementos
    
    soma = 0
    
    for indice in range(n):
        soma = soma + (lista_a[indice] - media_a) * (lista_b[indice] - media_b)
    correlacao = float(soma) / ((n - 1) * desvio_a * desvio_b)   
    return correlacao

if __name__ == '__main__':
    apple = open('/tempo/data/AAPL.txt', 'r')
    dados_apple = apple.readlines()[1:21]
    dados_apple_fecho = [float(linha.split(',')[4]) for linha in dados_apple]
    
    coke = open('/tempo/data/Coke.txt', 'r')
    dados_coke = coke.readlines()[1:21]
    dados_coke_fecho = [float(linha.split(',')[4]) for linha in dados_coke]
    
    corre = pearson(dados_apple_fecho, dados_coke_fecho)
    
    print corre
    
    pylab.plot(dados_apple_fecho,dados_coke_fecho,'ro', label='Apple vs Coke')
    pylab.xlabel('Apple')
    pylab.ylabel('Coke')
    pylab.title('Pearson')
    #pylab.axis([1,15,1,15])
    pylab.legend(loc=1)
    
    pylab.show()
    
    
    