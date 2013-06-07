import math
import pylab

def media(lista):
    """ 
    Calcula a média.
    """
    med = sum(lista) / float(len(lista))
    return med

def desvio_padrao(lista):
    """
    Calcula o desvio padrão.
    """
    a_media = media(lista) # <-- Atenção
    
    soma = 0
    for elem in lista:
        soma = soma + (elem - a_media) ** 2
        
    desvio = math.sqrt(float(soma) / (len(lista) - 1))
    return desvio

def pearson(lista_a, lista_b):
    """ Calcula o coeficiente de correlação entre duas listas de valores."""
    media_a = media(lista_a)
    media_b = media(lista_b)
    
    desvio_a = desvio_padrao(lista_a)
    desvio_b = desvio_padrao(lista_b)
    
    n = len(lista_a) # número de elementos
    
    soma = 0
    
    for indice in range(n):
        soma = soma + (lista_a[indice] - media_a) * (lista_b[indice] - media_b)
    correlacao = float(soma) / ((n - 1) * desvio_a * desvio_b)   
    return correlacao

def mostra(dados_1, dados_2, legenda):
    pylab.plot(dados_1,dados_2,'ro', label=legenda)
    pylab.xlabel('Chuva')
    pylab.ylabel('Temperatura')
    pylab.title('Pearson')
    pylab.axis([0,100,10,25])
    pylab.legend(loc=1)    

if __name__ == '__main__':
    chuva_lisboa =[95.2, 86.7,	84.7,59.5,44.4,	17.9,4.3,5.2,33.0,74.7,	99.6,96.7]
    temperatura_lisboa = [10.5,11.3,12.8,14.5,	16.7,19.4,21.5,	21.9,20.4,17.4,	13.7,11.1]
    chuva_faro =[ 80.2,	64.7,42.4,39.9,21.7,11.4,1.2,1.1,12.0,59.7,98.0,88.8]
    temperatura_faro = [12.0,12.5,13.7,15.2,17.8,20.7,23.3,23.6,22.0,18.8,15.1,12.7]
    
    """
    pylab.figure()
    
    pylab.subplot(211)
    pylab.plot(chuva_lisboa,temperatura_lisboa,'ro', label='Lisboa')
    #pylab.xlabel('Chuva')
    pylab.ylabel('Temperatura')
    pylab.title('Pearson')
    pylab.axis([0,100,10,25])
    pylab.legend(loc=1)
    
    pylab.subplot(212)    
    pylab.plot(chuva_faro,temperatura_faro,'bs',label='Faro')
    pylab.xlabel('Chuva')
    pylab.ylabel('Temperatura')
    #pylab.title('Pearson')
    pylab.axis([0,100,10,25])
    pylab.legend(loc=1)
    """
    print((pearson(chuva_lisboa, temperatura_lisboa)))
    print((pearson(chuva_faro, temperatura_faro)))
    mostra(chuva_lisboa, temperatura_lisboa, 'Lisboa')
    pylab.show()   

    