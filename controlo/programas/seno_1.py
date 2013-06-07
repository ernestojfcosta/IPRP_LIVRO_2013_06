# -*- coding: mac-roman -*-
# ciclos while e for
# cálculo aproximado do seno


def main():
	x=eval(input("Valor de x:\t"))
	n=eval(input("Numero de termos:\t"))
	print(seno1(x,n))
	print("O seno de %4.2f = %5.3f \t" % (x, seno1(x,n)))
	return 0

def seno1(x,n):
	res=0
	for i in range(n):
			res = res + (pow(-1,i) * pow(x,2*i +1)) / float(fact(2*i+1))
	return res


def fact(n):
	"""Calcula o factorial de n.
	"""
	res=1
	for i in range(1,n+1):
		res = res * i
	return res

	
if __name__ == '__main__':
	main()
	



		