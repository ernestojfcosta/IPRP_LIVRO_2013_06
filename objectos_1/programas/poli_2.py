"""Capítulo 3"""
import cmath 

def poli_2(a,b,c):
	""" Calcula as raizes de um polinomio do segundo grau."""
	delta = cmath.sqrt(b**2 - 4 * a * c)
	raiz_1 = (- b + delta)/ (2 * a)
	raiz_2 = (- b - delta) / (2 * a)
	return raiz_1, raiz_2

if __name__ == '__main__':
	print((poli_2(2,3,4)))
	