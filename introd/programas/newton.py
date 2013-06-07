def raizquad(a):
	"""Cálculo da raiz quadrada de um número positivo pelo método de Newton."""
	print(("Raiz quadrada de: ",a))
	x = eval(input("Valor inicial sff: "))
	for i in range(10):
		x = (1/2.0) * (x + (a/x))
	return x

if __name__ == '__main__':
	print((raizquad(2)))