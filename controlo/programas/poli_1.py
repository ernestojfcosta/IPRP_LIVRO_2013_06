# -*- coding: mac-roman -*-
# condicionais - exemplo raízes de polinómio
# Ernesto costa - 2006

import math

def main():
	""" Calculo das raízes reais de um polinómio.
	"""
	a,b,c = eval(input("Os coeficientes sff (a,b,c):\t"))	
	r1,r2=raizes(a,b,c)
	if r1 == r2 == None:
		print("Não tem raízes reais!")
	elif r1 == r2:
		print("O polinómio de coeficientes\
a=%d b=%d c= %d tem raízes múltiplas r1=%3.2f r2=%3.2f" % (a,b,c,r1,r2))
	else:
		print("As raízes do polinómio de coeficientes\
 a=%d b=%d c= %d são r1=%3.2f r2=%3.2f" % (a,b,c,r1,r2))
	
def raizes(a,b,c):
	""" Calcula raízes.
	"""
	discriminante= pow(b,2) - 4 * a * c
	if discriminante < 0:
		return None,None
	elif discriminante == 0:
		raiz1 = raiz2 = float(-b)/ (2 * a)
		return raiz1, raiz2
	else:
		raiz_discrim = math.sqrt(discriminante)
		raiz1=float((-b + raiz_discrim)) / (2 * a)
		raiz2=float((-b - raiz_discrim)) / (2 * a)
		return raiz1,raiz2
	
if __name__ == '__main__':
	main()