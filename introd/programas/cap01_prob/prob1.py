# -*- coding: latin1 -*-

#--- In�cio do programa

def main():
	print "\nPrograma para ilustrar o comportamento de um sistema simples"
	
	x = input("Valor inicial (entre 0 e 1): ")
	r = input("valor do coeficiente (entre 0 e 4): ")
	n = input("N�mero de valores a calcular: ")
	
	mapa_logistico(x,r,n)
	return 0

#--- Mapa log�stico

def mapa_logistico(x,r,n):
	for cont in range(n):
		x = r * x * (1 - x)
		print x
	return 0

main()
