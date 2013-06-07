def transposta(matriz):
	""" Transposta de uma matriz quadrada."""
	return [[matriz[j][i] for j in range(len(matriz[0]))] for i in range(len(matriz))]

def transposta_b(matriz):
	copia = [[None for j in range(len(matriz))] for i in range(len(matriz[0]))]
	for linha in range(len(matriz)):
		for coluna in range(len(matriz[0])):
			copia[coluna][linha] = matriz[linha][coluna]
	return copia

def transposta_c(matriz):
	""" Transposta de uma matriz."""
	return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

if __name__ == '__main__':
	matriz_1 = [[1,2,3],[5,6,7],[9,10,11]]
	matriz_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
	matriz_3 = [[1,2],[3,4],[5,6]]
	print((transposta(matriz_1)))
	print((transposta_b(matriz_2)))
	print((transposta_c(matriz_3)))