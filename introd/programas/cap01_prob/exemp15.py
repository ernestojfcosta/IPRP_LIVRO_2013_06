# -*- coding: latin 1 -*-

# Exemplo 1.5

# Mapa logistico: diagrama das órbitas
# Ernesto Costa - Julho 2006



#--- Importar as funções auxiliares de desenho
import matplotlib
from pylab import *

#--- Início do programa
def main():
	""" Este programa ilustra o comportamento caotica do mapa lofgistico.
	
	Faz o diagrama da órbita.
	"""
	print "\nPrograma para ilustrar diferentes comportamentos\n"
	saltar = input("Numero de valores ate  estabilizar: ")
	n = input("Numero de valores a calcular: ")
	rmin = input("Valor minimo do coeficiente (entre 0 e 4): ")
	rmax = input("Valor maximo do coeficiente (entre 0 e 4): ")
	passo = input("Valor do passo: ")
	
	# valores de r a considerar
	
	valores_r = arange(rmin,rmax,passo)
	
	# ciclo principal - varrimento do eixo horizontal
	
	orbita = []    # valores a imprimir
	
	for mu in valores_r:
		
		# estabiliza  valores
		
		x = 0.5
		for cont in range(saltar):
			x = mu * x * (1 - x)
		
		# calcula órbita
		
		lx= []
		for cont in range(n):
			x = mu * x * (1 -x)
			lx = lx+ [x]
		
		# acumula valores numa lista de listas
		
		orbita = orbita + [lx]
	
	
	# parte gráfica
	
	
	valores_verticais = len(valores_r)
	for cont in range(valores_verticais):
		hold(True)
		mu = valores_r[cont]    # valor para eixo vertical
		vertical = orbita[cont]  # valores de uma coluna para um dado mu
		horizontal = len(vertical) * [mu]  # fabrico  número igual de valores iguais a mu
		plot(horizontal,vertical,color= '0.75', linestyle='',markersize=1, marker='o', markerfacecolor='k')
		xlabel('Valor do coeficiente r ')
		ylabel('Valor da orbita')
		title('Diagrama das Orbitas')
	show()
	hold(False)
	return 0

main()

	
	