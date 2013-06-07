# -*- coding: mac-roman -*-

# Exemplo 1.4

# Programa para mostrar os 4 comportmentos de um sistema simples baseado no mapa logístico
# Ernesto Costa - Julho 2006



#--- Importar as funções auxiliares de desenho
import matplotlib
from pylab import *

#--- Início do programa
def main():
	""" Este programa ilustra os diferentes comportamentos  do mapa logistico.
	
	
	"""
	print("\nPrograma para ilustrar o comportamento do mapa logistico\n")
	x = eval(input("Valor inicial (entre 0 e 1): "))
	r1,r2,r3,r4 = eval(input("Os quatro valores de teste: "))
	graf1 = mapa_logistico(x,r1)
	graf2 = mapa_logistico(x,r2)
	graf3 = mapa_logistico(x,r3)
	graf4 = mapa_logistico(x,r4)
# parte gráfica
	subplot(221)
	plot(graf1,'r')
	xlabel('Iteracoes n ')
	ylabel('Valores x(n)')
	title('Mapa Logistico')
	
	subplot(222)
	plot(graf2,'b')
	xlabel('Iteracoes n ')
	ylabel('Valores x(n)')
	title('Mapa Logistico')
	
	subplot(223)
	plot(graf3,'y')
	xlabel('Iteracoes n ')
	ylabel('Valores x(n)')
	title('Mapa Logistico')
	
	subplot(224)
	plot(graf4,'g')
	xlabel('Iteracoes n ')
	ylabel('Valores x(n)')
	title('Mapa Logistico')
	
	show()
	return 0

#--- Mapa logístico

def mapa_logistico(x,r):
	""" Implementa o mapa logistico.
	
	"""
	lista =[]
	for cont in range(100):
		x = r * x * (1 -x)
		lista = lista + [x]
	return lista

main()

	
	