"""Quadrado Mágico. 
Programação descendente.
Uso de matrizes
"""

__author__ = 'Ernesto Costa'
__date__ = 'October 2011'



from numpy import *

def quadrado_magico(quadrado):
	num_magico = nm(quadrado)
	# Verifica linhas
	if not linhas(quadrado,num_magico):
		return False, num_magico
	# Verifica colunas
	elif not colunas(quadrado, num_magico):
		return False, num_magico
	# Verifica diagonais
	else:
		return diagonais(quadrado,num_magico), num_magico



# -- Número mágico
def nm(mat):
	lin,col = mat.shape
	return (lin ** 3 + lin) / 2

# -- Linhas
def linhas(quadrado,num_magic):
	res = add.reduce(quadrado, axis = 1)
	for val in res:
		if val != num_magic:
			return False
	return True

# Colunas

def colunas(quadrado,num_magic):
	res = add.reduce(quadrado, axis = 0)
	for val in res:
		if val != num_magic:
			return False
	return True

# Diagonais
def diagonais(quadrado,num_magic):
	aux = array([quadrado.diagonal(),fliplr(quadrado).diagonal()])
	res = add.reduce(aux, axis = 1)
	for val in res:
		if val != num_magic:
			return False
	return True

if __name__ == '__main__':
	quadrado_3 = array([[4,9,2],[3,5,7],[8,1,6]])
	quadrado_4 = array([[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]])
	quadrado_5 = array([[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]])
	print quadrado_5
	print quadrado_magico(quadrado_5)