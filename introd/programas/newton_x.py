def raizquad(a):
	 """C�lculo da raiz quadrada de um n�mero positivo pelo m�todo de Newton."""
	x = input("Valor inicial sff: ")
	for i in range(10):
		x = (1/2.0) * (x + (a/x))
	return x

if __name__ == '__main__':
	print raizquad(2)