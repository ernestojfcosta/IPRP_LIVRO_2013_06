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
	if not somas(quadrado,num_magico,1):
		return False, num_magico
	# Verifica colunas
	elif not somas(quadrado, num_magico,0):
		return False, num_magico
	# Verifica diagonais
	else:
		diagonais = array([quadrado.diagonal(),fliplr(quadrado).diagonal()])
		return somas(quadrado,num_magico,1), num_magico



# -- Número mágico
def nm(mat):
	lin,col = mat.shape
	return (lin ** 3 + lin) / 2

# -- Somas
def somas(quadrado,num_magic, eixo):
	res = add.reduce(quadrado, axis = eixo)
	return alltrue(res == num_magic)

def somas_b(quadrado, num_magic, eixo):
	res = add.reduce(quadrado, axis = eixo)
	return all([val == num_magic for val in res])


if __name__ == '__main__':
	quadrado_3 = array([[4,9,2],[3,5,7],[8,1,6]])
	quadrado_4 = array([[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]])
	quadrado_5 = array([[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]])
	print quadrado_5
	print quadrado_magico(quadrado_5)