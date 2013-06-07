# -*- coding: mac-roman -*-
# exepções - exemplo raízes de polinómio
# Ernesto costa - 2006

import math

def main():
	""" Calculo das raizes reais de um poinomio.
	"""
	try:
		a,b,c = eval(input("Os coeficientes sff (a,b,c):\t"))	
		discriminante=pow(b,2)- 4 * a * c
		raiz_discrim = math.sqrt(discriminante)
		raiz1=float((-b + raiz_discrim)) / (2 * a)
		raiz2=float((-b - raiz_discrim)) / (2 * a)
		if raiz1 == raiz2:
			print("O polinomio de coeficientes\
a=%d b=%d c= %d tem raizes multiplas raiz1= raiz2=%3.2f " % (a,b,c,raiz1))
		else:
			print("As raizes do polinomio de coeficientes\
a=%d b=%d c= %d sao raiz1=%3.2f raiz2=%3.2f" % (a,b,c,raiz1,raiz2))
	except ValueError:
		print("\n Nao tem raizes reais!")



	
if __name__ == '__main__':
	main()
