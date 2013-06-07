from numpy import *


class Matriz(object):
    
    # construtor
    def __init__(self,dim):
        self.dim = dim
        self.valor = zeros(dim*dim,int).reshape(dim,dim)
        
    # Acessores
    def get_dim(self):
        return self.dim
    
    def get_valor(self):
        return self.valor
    
    def get_linhas(self):
        return self.valor[:]
    
    def get_linha(self,i):
        return self.valor[i]
    
    def get_colunas(self):
        return self.valor[:,arange(self.dim)]
    
    def get_coluna(self,j):
        return self.valor[:,j]
    
    def get_diagonais(self):
        return list((self.valor.diagonal(), fliplr(self.valor).diagonal()))
    
    # Modificadores
    def set_valores(self,valor):
	self.valor = array(valor).astype(int)
	
    # Utilidades
    def soma(self,valor):
        return add.reduce(valor,1)


# Quadrado Mágico
def main(matriz):
	num_magico = nm(matriz)
	# Verifica linhas
	soma_linhas = matriz.soma(matriz.get_linhas())
	if not all_equal_nm(soma_linhas,num_magico):
		return False, num_magico
	# Verifica colunas
	soma_colunas = matriz.soma(matriz.get_colunas())
	if not all_equal_nm(soma_colunas, num_magico):
		return False, num_magico
	# Verifica diagonais
	soma_diagonais = matriz.soma(matriz.get_diagonais())
	return all_equal_nm(soma_diagonais,num_magico), num_magico

# -- Número mágico
def nm(mat):
	lin,col = mat.dim,mat.dim
	return (lin ** 3 + lin) / 2
    
def all_equal_nm(mat,num_magic):
    return alltrue(mat == num_magic)


if __name__ == '__main__':
    """
    mat = QMatriz(5)
    print mat.get_valor()
    print '*' * 30
    print mat.get_linhas()
    print '*' * 30
    print mat.get_linha(2)
    print '*' * 30
    print mat.get_coluna(2)
    print '*' * 30
    print mat.get_diagonais()
    """
    quadrado_3 = [[4,9,2],[3,5,7],[8,1,6]]
    quadrado_4 = [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]
    quadrado_5 = [[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]]
    matriz_3 = Matriz(3)
    matriz_3.set_valores(quadrado_3)
    matriz_4 = Matriz(4)
    matriz_4.set_valores(quadrado_4)
    matriz_5 = Matriz(5)
    matriz_5.set_valores(quadrado_5)
    print matriz_3.valor

    print '*' * 30
    print matriz_4.valor
    print main(matriz_4)
    print '*' * 30
    print matriz_5.valor
    print main(matriz_5)
    print '*' * 30
    