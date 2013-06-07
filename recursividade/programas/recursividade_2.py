#!/usr/bin/env python
# encoding: utf-8
"""
recursividade.py
Exemplos de soluções recursivas

Created by Ernesto Costa on 2006-11-24.
Copyright (c) 2006 Universidade de Coimbra. All rights reserved.
"""

import sys
import os
from random import randint
from copy import copy

# Hanói
def torres_hanoi(n,a,b,c):
	"Implementação das torres de Hanói"
	if n == 1:
		print("Move disco %d de %s para %s" % (n,a,c))
	else:
		torres_hanoi(n-1,a,c,b)
		print("Move disco %d de %s para %s" % (n,a,c))
		torres_hanoi(n-1,b,a,c)

# Factorial

def factorial(n):
	"Calcula o factorial de n"
	if n==0:
		return 1
	else:
		return n * factorial(n-1)
		

# Fibonacci		
def fib_rec(n):
	" Números de fibonacci recursivo"
	if n == 1 or n == 2:
		return 1
	else:
		return fib_rec(n-1) + fib_rec(n-2)
		
# Máximo Divisor Comum
def mdc(m,n):
	"Máximo Divisor Comum: algoritmo de Euclides"
	if n == 0:
		return m
	else:
		return mdc(n, m % n)
		
# Pares e ímpares

def par(n):
	"Número Par"
	if n < 0:
		return False
	elif n == 0:
		return True
	elif impar(n-1):
		return True
	else:
		return False


def impar(n):
	"Número ímpar"
	if n < 1:
		return False
	elif n == 1:
		return True
	elif par(n-1):
		return True
	else:
		return False
		
# Binómio de Newton

def binomio(n,k):
	"Coeficentes do binómio"
	if k ==0 or k == n:
		return 1
	else:
		return binomio(n-1,k) + binomio(n-1,k-1)
		
# Permutações dos elementos de uma lista

def permuta(lista):
	"Permutações de uma lista"
	if lista ==[]:
		return [[]]
	else:
		aux=copy(permuta(lista[1:]))
		for lst in aux:
			[lst.insert(indice,lista[0]) for indice in range(len(lst)+ 1)]
		return aux


		
### Programa Principal
		
def main():
	print("Torres de Hanói")
	torres_hanoi(3,'Inicio','Auxiliar','Fim')
	"""print 'Números de Fibonacci'
	num = input('O número por favor(>0)')
	print "Fibonacci de %d = %d" % (num,fib_rec(num))
	print 'Máximo Divisor Comum'
	m,n= input("Os números por favor")
	print "O Máximo Divisor Comum  de %d e de  %d = %d" % (m,n, mdc(m,n))
	print 'Par e impar'
	num = input('O número por favor')
	if par(num):
		print "%d é par!" % num
	else:
		print "%d é ímpar" % num
	print 'Binómio de Newton'
	n,k = input('Os valores sff')
	for i in range(n,1,-1):
		for j in range(k,0,-1):
			print 'O valor do Binómio para n=%d e k=%d é = %d' % (i,j,binomio(i,j))
	print 'Permutações de uma lista'
	lista =input('A lista por favor')
	print lista
	print 'As permutações da lista %s são %s' % (lista, permuta(lista))"""
	return 0
	

	



if __name__ == '__main__':
    main()

