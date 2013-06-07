

def mostra_por_linhas(matriz):
	"""Indexação pelo conteúdo."""
	for linha in matriz:
		for coluna in linha:
			print("%5d" % coluna, end=' ')
		print()


def mostra_por_linhas_b(matriz):
	"""Indexação pela posição."""
	for pos_linha in range(len(matriz)):
		for pos_coluna in range(len(matriz[0])):
			print("%5d" % matriz[pos_linha][pos_coluna], end ='')
		print()
		
def mostra_por_colunas(matriz):
	""" AKO transposta. Indexação pelo conteúdo."""
	for pos_coluna in range(len(matriz[0])):
		for pos_linha in range(len(matriz)):
			print("%3d" % matriz[pos_linha][pos_coluna], end='')
		print()


def mostra_tri_sup(matriz):
	"""Matriz triangular superior.Indexação pela posição."""
	for pos_linha in range(len(matriz)):
		print(' '* 4 * pos_linha,end='') 
		for pos_coluna in range(pos_linha,len(matriz[0])):
			print("%4d" % matriz[pos_linha][pos_coluna],end='')
		print()

def mostra_tri_inf(matriz):
	"""Matriz triangular superior.Indexação pela posição."""
	for pos_linha in range(len(matriz)):
		for pos_coluna in range(0,pos_linha+1):
			print("%4d" % matriz[pos_linha][pos_coluna],end='')
		print()
		
def mostra_diag_principal(matriz):
	""" Mostra diagonal principal."""
	for pos_linha in range(len(matriz)):
		print(' '* 3 * pos_linha,end='')
		for pos_coluna in range(0,pos_linha+1):
			if pos_linha == pos_coluna:
				print("%2d" % matriz[pos_linha][pos_coluna])
def cria_mat(n,m,val):
	"""Cria uma matrix nXm sendo que todos os elementos são iguais a val."""
	mat = []
	for j in range(n):
		linha = []
		for i in range(m):
			linha.append(val)
		mat.append(linha)
	return mat

def cria_mat_b(n,m,val):
	"""Cria uma matrix nXm sendo que todos os elementos são iguais a val."""
	linha = [val] * m
	mat = [linha] * n
	return mat

def cria_mat_c(n,m,val):
	"""Cria uma matrix nXm sendo que todos os elementos são iguais a val."""
	return[[val] * m] * n
		
def cria_mat_b(n,m,val):
	"""Cria uma matrix nXm sendo que todos os elementos são iguais a val."""
	mat = [[val for i in range(m)] for j in range(n)]
	return mat

def prod_const_mat(mat,val):
	"""Multiplica os elementos nas colunas ímpares por val."""
	n_linhas = len(mat)
	n_colunas = len(mat[0])
	for linha in range(n_linhas):
		for col in range(1,n_colunas,2):
			mat[linha][col] *= val
	return mat

def soma_matriz(mat_1,mat_2):
	""" Soma duas matrizes da mesma dimensão."""
	n_linhas = len(mat_1)
	n_colunas = len(mat_1[0])
	mat = cria_mat(n_linhas,n_colunas,0)
	# Soma
	for i in range(n_linhas):
		for j in range(n_colunas):
			mat[i][j]= mat_1[i][j]+ mat_2[i][j]
	return mat 

def mult_matriz(mat_1,mat_2):
	"""Multiplica duas matrizes iXk e kXj."""
	n_linhas_1 = len(mat_1)
	n_colunas_1 = len(mat_1[0]) # igual a n_linhas_2
	n_colunas_2 = len(mat_2[0])
	mat_prod = cria_mat(n_linhas_1,n_colunas_2,0)
	# Multiplica
	for i in range(n_linhas_1):
		for j in range(n_colunas_2):
			val=0
			for k in range(n_colunas_1):
				val = val + mat_1[i][k]* mat_2[k][j]
			mat_prod[i][j]=val
	return mat_prod

def transposta(mat):
	"""Calcula a transposta de uma matriz."""
	aux=[]
	for j in range(len(mat[0])):
		linha=[]
		for i in range(len(mat)):
			linha.append(mat[i][j])
		aux.append(linha)
	return aux

# pythoniano

def transposta_b(mat):
	"""Transposta de uma matriz."""
	return [list(linha) for linha in zip(*mat)]

def prod_matriz_vector(mat,vec):
	""" Produto de uma matriz  m x n por um vector 1 x n"""
	res = [prod_escalar(mat[i],vec) for i in range(len(mat))]
	return res

def prod_escalar(vect1, vect2):
	"""Produto escalr de dois vectores representados por listas."""
	prod = [vect1[i] * vect2[i] for i in range(len(vect1))]
	return sum(prod)

def sub_matriz(matriz, linha, coluna, dim_x, dim_y):
	"""Extrai a sub-matriz a partir de (linha, coluna) com dimensão dimX X dimY."""
	sub = cria_mat(dim_x, dim_y,0)
	for x in range(dim_x):
		for y in range(dim_y):
			sub[x][y] = matriz[linha+x][coluna+y]
	return sub
			

if __name__ == '__main__':
	mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
	#mostra_por_linhas_b(mat)
	#mostra_por_colunas(mat)
	#mostra_tri_sup(mat)
	#mostra_tri_inf(mat)
	#mostra_diag_principal(mat)
	#mostra_por_linhas(cria_mat(3,4,0))
	#mostra_por_linhas(cria_mat_b(3,4,0))
	#mostra_por_linhas(cria_mat_c(3,4,0))
	"""
	mostra_por_linhas(prod_const_mat(cria_mat(3,4,1), 3))
	a = cria_mat(3,3,1)
	b = cria_mat(3,3,4)
	mostra_por_linhas(a)
	mostra_por_linhas(b)
	mostra_por_linhas(soma_matriz(a,b))
	
	
	a = cria_mat(3,4,1)
	b = cria_mat(4,3,1)
	vec_1 = [1,2,3]
	mostra_por_linhas(a)
	mostra_por_linhas(b)
	mat_1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
	mostra_por_linhas(mult_matriz(a,b))	
	c = transposta(mat_1)
	e = transposta_b(mat_1)
	mostra_por_linhas(c)
	mostra_por_linhas(e)
	d = transposta([vec_1])
	mostra_por_linhas(d)
	mostra_por_linhas(mult_matriz(mat_1,d))
	"""
	print(sub_matriz(mat,1,1,2,2))
	
