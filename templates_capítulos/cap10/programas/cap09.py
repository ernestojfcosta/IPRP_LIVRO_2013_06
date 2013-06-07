#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
cap09.py

Created by Ernesto Costa on 2008-12-01.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from random import *

# --- Exemplo 1
#--  Gera palindromes: Skiena pg 120
# Partir de um número. Se não for palíndrome somar ao seu inverso e continuar

def rev_add(n,maximo):
	numeros=[randint(1,maximo) for i in range(n)]
	for num in numeros:
		print 'Número inicial: %d, número de iterações: %d, palíndrome %d' % pal(num)
	return
	
def pal(num):
	"""Se não for possível entra em ciclo..."""
	aux = num
	conta=0
	while not palindrome(aux):
		conta = conta +1
		aux = aux + inverso_num(aux)
	return (num,conta, aux)

def inverso_num(num):
	return int(str(num)[::-1])
	
# -- variantes 

def rev_add(n,maximo):
	# Gera números
	numeros=[]
	for i in range(n):
		numeros.append(randint(1,maximo))
	# Calcula
	for num in numeros:
		print 'Número inicial: %d, número de iterações: %d, palíndrome %d' % pal(num)
	return
		
def inverte(num):
	"""Números na bese 10. Uso das posições"""
	aux=0
	while num > 0:
		digit= num % 10
		num = num / 10
		aux = aux * 10 + digit
	return aux
	


	
def palindrome(num):
	return (str(num) == str(num)[::-1])	
	
	
#-----------------------------------------------------	
def main():
	#print palindrome(122)
	#print pal(195)
	rev_add(10,10000)
	#print inverte(123456789)


if __name__ == '__main__':
	main()

