#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
recursivos.py

Created by Ernesto Costa on 2008-11-22.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from random import *

# divisão inteira

def mod(n,m):
	if n < m:
		return n
	else:
		return mod(n-m,m)

# busca padrão

def pat_match(pad,texto):
	if len(texto) < len(pad):
		return False
	elif pad == texto[:len(pad)]:
		return True
	else: 
		return pat_match(pad,texto[1:])
		
# - Variante: indica o índice do começo do padrão no texto
def pat_match_ind(pad,texto,indice):
	if len(texto) < len(pad):
		return False,-1
	elif pad == texto[:len(pad)]:
		return True, indice
	else: 
		return pat_match_ind(pad,texto[1:], indice +1)		
# aplanar uma lista = retirar parêntesis

def aplana(L):
	if L==[]:
		return L
	elif isinstance(L[0],list):
		return aplana(L[0]) + aplana(L[1:])
	else:
		return [L[0]] + aplana(L[1:])
	
# produto de vectores	
def prod_vectores(LV):
	if not LV:
		return [LV]
	else:
		res=[]
		for elem in LV[0]:
			for aux in prod_vectores(LV[1:]):
				res.append([elem] + aux)
		return res
# -- Variante		
def prod_vect_2(LV):
	if not LV:
		return [LV]
	else:
		return [[elem] + aux for elem in LV[0] for aux in prod_vect_2(LV[1:])]	
				
def main():
	#print mod(18,14)
	texto = ''.join([choice(['a','b','c','d','e']) for i in range(20)])
	print(texto)
	print(pat_match('abc',texto))
	print(pat_match_ind('abc',texto,0))
	#print aplana([[1,2],[[3]],4, [5,[6],7]])
	#print aplana([])
	#print prod_vectores([[1,2,3],['a','b','c']])
	#print prod_vect_2([[1,2,3],[4,5,6],['a','b','c']])


if __name__ == '__main__':
	main()

