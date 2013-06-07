#! -*- coding: utf-8 -*-

# 1

def nota(exame):
    '''Calcula a nota de um exame num teste de escolha múltipla. '''
    solucao = 'ABBEADDB'
    conta = 0
    for i in range(len(solucao)):
        if exame[i] == solucao[i]:
            conta = conta + 1
    return float(conta)/len(solucao)


#print "Nota: "
#print nota('ABEEADEC')

# 2

baleias = [5,4,7,3,2,3,2,6,4,2,1,7,1,3]

def amplitude(lista):
    """Diferença entre valores máximo e mínimo numa lista."""
    return max(lista) - min(lista)

def maximo_a(lista):
    """
    Devolve valor máximo numa lista.
    """
    max_actual = lista[0]
    for indice in range(len(lista)):
        if lista[indice] > max_actual:
            max_actual = lista[indice]
    return max_actual

def maximo_b(lista):
    """
    Devolve valor máximo numa lista.
    """
    max_actual = lista[0]
    for elem in lista[1:]:
        if elem > max_actual:
            max_actual = elem
    return max_actual

# 3 tendência central

def media(lista):
    """ 
    Calcula a média.
    """
    med = sum(lista) / float(len(lista))
    return med

#print "média: "
#print media([1,2,3,4,5])
#print media(baleias)

def media_b(lista):
    """Calcula a média."""
    soma = 0
    for num in lista:
        soma = soma + num
        
    med = soma / float(len(lista))
    return med

#print media_b(baleias)

def mediana(lista):
    """
    Calcula a mediana: metade dos valores são inferiores, metade é superior.
    """
    lista_aux = lista[:] # <-- Atenção!
    lista_aux.sort()
    meio = len(lista_aux) / 2
    if len(lista) % 2 == 0:
        res = (lista_aux[meio-1] + lista_aux[meio]) / 2.0
    else:
        res = lista_aux[meio]
    return res

lista_1 = [1,8,3,20,4,7]
lista_2 = [1,8,3,20,4,7,15]

#print "Mediana: "
#print mediana(lista_1)
#print mediana(lista_2)
#print lista_1
#print lista_2

# 4 Dispersão

import math

def desvio_padrao(lista):
    """Calcula o desvio padrão."""
    a_media = media(lista) # <-- Atenção
    soma = 0
    for elem in lista:
        soma = soma + (elem - a_media) ** 2     
    desvio = math.sqrt(float(soma) / (len(lista) - 1))
    return desvio

#print "Desvio Padrão"
#print desvio_padrao(lista_1)
#print desvio_padrao(baleias)


import matplotlib
import pylab

def mostra(lista):
    """Gráfico simples de uma lista de valores."""
    pylab.xlabel('Dias')
    pylab.ylabel('Quantidade')
    pylab.title('Baleias')
    pylab.plot(lista)
    pylab.show()
    
mostra(baleias)


# --- DICIONÁRIOS


def exp_genes(adn):
    """ A partir da sequência de ADN determina as proteínas."""
    arn = transcreve(adn)
    prot = traduz(arn)
    return prot

def transcreve(adn):
    """ substitui T por U no adn."""
    adn = adn.upper()
    arn = adn.replace('T','U')
    return arn
                    
def traduz(arn):
    """A partir do arn devolve a lista de proteínas."""
    l_cod = codoes(arn)
    prot = proteinas(l_cod)
    return prot


# 
def codoes(arn):
	""" 
	Devolve a lista de codões a partir de uma sequência.
	A sequência é percorrida em grupos de três
	enquanto é possível.
	"""
	cod = []
	for i in range(0,len(arn) - 2,3):
	    cod = cod + [arn[i:i+3]]
	return cod

    

def codoes_b(arn):
    """ 
    Devolve a lista de codões a partir de uma sequência.
    A sequência é percorrida em grupos de três
    enquanto é possível.
    """
    cod = []
    for i in range(0,len(arn) - 2,3):
	cod.append(arn[i:i+3])
    return cod
    
#print codoes('ATTCGGTAA')
#print codoes_b('ATTCGGTAA')

# ---

def frequencia(valores):
    """
    Cria com dicionário com a frequência da occorrência dos valores.
    """
    freq = dict()
    for item in valores:
	freq[item] = freq.get(item,0) + 1
    return freq

#print frequencia(baleias)

def moda(valores):
    """
    Calcula a moda de um conjunto de valores.
    """
    dicio_freq = frequencia(valores)
    # -- porque pode haver mais do que uma moda...
    lista_valores = dicio_freq.values()
    maxima_freq = max(lista_valores)
    # -- contrói resultado
    lista_modas = list()
    for chave in dicio_freq:
	if dicio_freq[chave] == maxima_freq:
	    lista_modas.append(chave)
    return lista_modas

#print moda(baleias)

def tabela_frequencia_a(valores):
    """
    Imprime uma tabela de frequências.
    """
    dicio_freq = frequencia(valores)
    
    lista_elementos = dicio_freq.keys()
    lista_elementos.sort()
    
    print "Item", "\t\t", "Frequencia"
    for elemento in lista_elementos:
	print elemento,"\t\t", dicio_freq[elemento]
	
#tabela_frequencia_a(baleias)

def tabela_frequencia_b(valores):
    """
    Imprime uma tabela de frequências.
    """
    dicio_freq = frequencia(valores)
    
    lista_elementos = dicio_freq.keys()
    lista_elementos.sort()
    
    print "Item", "\t\t", "Frequencia"
    for elemento in lista_elementos:
	print elemento,"\t\t", dicio_freq[elemento] * '*'
	
#tabela_frequencia_b(baleias)

import matplotlib
import pylab

def tabela_frequencia_c(valores):
    """
    Imprime uma tabela de frequências.
    """
    dicio_freq = frequencia(valores)
    
    lista_elementos = dicio_freq.keys()
    lista_elementos.sort()
    
    lista_freq_ord = list()
    for elem in lista_elementos:
	lista_freq_ord.append(dicio_freq[elem])®
    
    pylab.xlabel('Elementos')
    pylab.ylabel('Frequencia')
    pylab.title('Baleias')
    
    pylab.plot(lista_freq_ord)
    pylab.show()
    
#tabela_frequencia_c(baleias)

def palavra_chave(nome_utilizador, segredo):
    """
    Verifica a palavra chave de um utilizador.
    """
    codigos = {'ernesto':'toto','patricia':'hello31','ana':'gato56'}
    if not codigos.has_key(nome_utilizador):
	return 'Não o conheço!'
    
    codigo_correcto = codigos[nome_utilizador]
    if segredo == codigo_correcto:
	return 'Bem vindo!'
    else:
	return 'Enganou-se'
    
print palavra_chave('ernesto', 'toto')
print palavra_chave('ana', 'oops')
print palavra_chave('xico_esperto','abacadabra')

