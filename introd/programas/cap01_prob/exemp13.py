# -*- coding: mac-roman -*-

# Exemplo 1.3

# Programa para mostrar o comportmento ca�tico baseado no mapa log�stico
# Ernesto Costa - Julho 2006



#--- Importar as fun��es auxiliares de desenho
import matplotlib
from pylab import *

#--- In�cio do programa
def main():
	""" Este programa ilustra o comportamento caotico do mapa logistico.
	
	
	"""
	print "\nPrograma para ilustrar o comportamento caotico\n"
	x1,x2 = input("Valores iniciais (entre 0 e 1): ")
	graf1 = mapa_logistico(x1)
	graf2 = mapa_logistico(x2)
# parte gr�fica
	plot(graf1,'r',graf2,'g')
	xlabel('Iteracoes n ')
	ylabel('Valores x(n)')
	title('Mapa Logistico')
	show()
	return 0

#--- Mapa log�stico

def mapa_logistico(x):
	""" Implementa o mapa logistico.
	
	"""
	lista =[]
	for cont in range(100):
		x = 3.95 * x * (1 -x)
		lista = lista + [x]
	return lista

main()

	
	