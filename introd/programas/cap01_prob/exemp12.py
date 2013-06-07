# -*- coding: latin 1 -*-

# Exemplo 1.2

# Programa para mostrar o comportmento de sistemas simples
# Ernesto Costa - Julho 2006



#--- Importar as fun��es auxiliares de desenho
import matplotlib
from pylab import *

#--- In�cio do programa
def main():
	""" Este programa ilustra os diferentes comportamentos de um sistema simples.
	
	O sistema descreve o crescimento de uma popula��o por meio do mapa log�stico.
	"""
	print "\nPrograma para ilustrar diferentes comportamentos\n"
	x = input("Valor inicial (entre 0 e 1): ")
	r = input("Valor do coeficiente (entre 0 e 4): ")
	n = input("Numero de valores a calcular: ")
	mapa_logistico(x,r,n)
	return 0

#--- Mapa log�stico
#  Testar com valores de r=2.5, 3.3, 3.5 e 3.9
# Com estes valores verificam-se as quatro situa��es t�picas
def mapa_logistico(x,r,n):
	""" Implementa o mapa logistico.
	
	"""
	lista =[]
	for cont in range(n):
		x = r * x * (1 -x)
		lista = lista + [x]
	# a parte gr�fica
	plot(lista)
	xlabel('Iteracoes n ')
	ylabel('Valores x(n)')
	title('Mapa Logistico')
	show()
	return 0

main()

	
	