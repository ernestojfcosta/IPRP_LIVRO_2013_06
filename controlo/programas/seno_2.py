# -*- coding: mac-roman -*-
# ciclos while e for
# cálculo aproximado do seno


def main():
	x=eval(input("Valor de x:\t"))
	prec=eval(input("Valor da precisao:\t"))
	print(seno2(x,prec))
	print("O seno de %4.2f = %5.3f com precisao %15.14f \t" % (x, seno2(x,prec),prec))
	return 0


def seno2(x,prec):
	ordem=0
	res=0
	dif=x
	while dif> prec:
		termo= (pow(-1,ordem) * pow(x,2*ordem +1)) / float(fact(2*ordem+1))
		res,ant = res + termo,res
		dif = abs(res-ant)
		ordem = ordem +1
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
	



		