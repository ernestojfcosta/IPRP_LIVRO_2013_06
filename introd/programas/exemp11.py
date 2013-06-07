# -*- coding: mac-roman -*-

# Exemplo 1.1

# Programa para mostrar o comportamento de sistemas simples
# Ernesto Costa - Julho 2006

#--- InÌcio do programa


def main():
	""" Este programa ilustra o comportamento  de um sistema simples.
	
	Este sistems descreve o crescimento de uma populaÁ„o por meio do mapa logÌstico.
	"""
	print("\nComportamento do mapa logistico\n")
	x = eval(input("Valor inicial (entre 0 e 1): "))
	mu = eval(input("Valor do coeficiente (entre 0 e 4): "))
	n = eval(input("Numero de valores a calcular: "))
	mapa_logistico(x,mu,n)
	return 0

#--- Mapa logÌstico
def mapa_logistico(x,mu,n):
	""" Implementa o mapa logistico.
	     Imprime lista de valores.
	"""
	for cont in range(n):
		x = mu * x * (1 -x)
		print(x)
	return 0

main()

	
	