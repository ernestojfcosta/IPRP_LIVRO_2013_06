"""Quadrado Mágico. 
Programação descendente.
"""

__author__ = 'Ernesto Costa'
__date__ = 'October 2011'

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
	#return resposta, num_magico
	
def nm(quadrado):
	linhas = len(quadrado)
	colunas = len(quadrado[0])
	return (linhas ** 3 + colunas) / 2

# -- Linhas
def linhas(quadrado,num_magic):
	for linha in lin(quadrado):
		if soma(linha) != num_magic:
			return False
	return True

def lin(quadrado):
	return quadrado
# -- Colunas
def colunas(quadrado, num_magic):
	for coluna in col(quadrado):
		if soma(coluna) != num_magic:
			return False
	return True

def col(quadrado):
	mat = []
	for i in range(len(quadrado)):
		linha_i = []
		for j in range(len(quadrado[0])):
			linha_i.append(quadrado[j][i])
		mat.append(linha_i)
	return mat


def col_b(quadrado):
	return [[quadrado[j][i] for j in range(len(quadrado[0]))] for i in range(len(quadrado))]


def col_c(quadrado):
	return [list(elem) for elem in zip(*quadrado)]


import copy

def col_d(quadrado):
	mat = copy.deepcopy(quadrado)
	#mat = quadrado[:]
	for i in range(len(quadrado)):
		for j in range(i+1,len(quadrado[0])):
			mat[i][j] = quadrado[j][i]
			mat[j][i] = quadrado[i][j]
	return mat

# -- Diagonais
def diagonais(quadrado,num_magic):
	for diagonal in diag(quadrado):
		if soma(diagonal) != num_magic:
			return False
	return True

def diag(quadrado):
	diag_1 = []
	diag_2 = []
	for i in range(len(quadrado)):
		for j in range(len(quadrado[0])):
			if i == j:
				diag_1.append(quadrado[i][j])
			if (i+j) == (len(quadrado) - 1):
				diag_2.append(quadrado[i][j])
	return [diag_1, diag_2]


def soma(lista):
	return sum(lista)

def soma_b(lista):
	total = 0
	for elem in lista:
		total = total + elem
	return total

def soma_c(lista):
	return reduce(lambda x,y: x+y, lista)
	
	
if __name__ == '__main__':
	quadrado_3 = [[4,9,2],[3,5,7],[8,1,6]]
	quadrado_4 = [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]
	quadrado_5 = [[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]]
	#quadrado = []
	print quadrado_magico(quadrado_5)
	#print quadrado,'\n', col_d(quadrado)
	#print quadrado,'\n', diag(quadrado)