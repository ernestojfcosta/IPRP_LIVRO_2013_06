#! /usr/bin/env python
# -*- coding: utf-8 -*-

from cmath import *

def main():
	""" Calcula as raizes de um polinomio do
	segundo grau."""
	
	a,b,c = eval(input("Os coeficientes a,b e c: "))
	
	comum = sqrt(b**2 - 4 * a * c)

	raiz1 = (- b + comum)/ (2 * a)
	raiz2 = (- b - comum) / (2 * a)
	
	print("As raizes: ", raiz1, " e  ", raiz2)
	
	return 0

if __name__ == '__main__':
	main()