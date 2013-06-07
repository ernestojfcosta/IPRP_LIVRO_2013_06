# -*- coding: latin1 -*-

# Exemplo 1.1

# Programa para mostrar o comportamento de sistemas simples
# Ernesto Costa - Julho 2006

#--- Início do programa


def main():
	""" Este programa ilustra o comportamento  de um sistema simples.
	
	Este sistems descreve o crescimento de uma população por meio do mapa logístico.
	"""
	print "\nPrograma para ilustrar comportamentos de sistemas simples\n"
	x = input("Valor inicial (entre 0 e 1): ")
	r = input("Valor do coeficiente (entre 0 e 4): ")
	n = input("Numero de valores a calcular: ")
	mapa_logistico(x,r,n)
	return 0

#--- Mapa logístico
def mapa_logistico(x,r,n):
	""" Implementa o mapa logistico.
	     Imprime lista de valores.
	"""
	for cont in range(n):
		x = r * x * (1 -x)
		print x
	return 0

main()

	
	