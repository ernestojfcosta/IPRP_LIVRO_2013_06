# -*- coding: mac-roman -*-
# condicionais - exemplo raízes de polinómio
# Vários caminhos
# Ernesto costa - 2006

import math

def main():
	""" Calculo das raizes reais de um polinomio.
	"""
	try:
		a,b,c = input("Os coeficientes sff (a,b,c):\t")	
		discriminante=pow(b,2)- 4 * a * c
		raiz_discrim = math.sqrt(discriminante)
		raiz1=float((-b + raiz_discrim)) / (2 * a)
		raiz2=float((-b - raiz_discrim)) / (2 * a)		
		if r1 == r2:
		print "O polinomio de coeficientes\
a=%d b=%d c= %d tem raizes multiplas r1= r2=%3.2f " % (a,b,c,r1)
		else:
			print "As raizes do polinomio de coeficientes\
a=%d b=%d c= %d sao r1=%3.2f r2=%3.2f" % (a,b,c,r1,r2)
		return raiz1,raiz2
	except:
		pass
	
if __name__ == '__main__':
	main()
