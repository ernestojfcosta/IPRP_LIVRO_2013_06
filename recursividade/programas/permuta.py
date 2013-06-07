#!/usr/bin/env python
# encoding: utf-8
"""
permuta.py

Created by Ernesto Costa on 2006-11-25.
Copyright (c) 2006 Universidade de Coimbra. All rights reserved.
"""

import sys
import os
from copy import copy

def permuta(lista):
	"Permutações de uma lista"
	if lista ==[]:
		return [[]]
	else:
		aux=permuta(lista[1:])
		resultado=[]
		for lst in aux:
			resultado.extend(insere_mult(lst,lista[0]))
		return resultado

def permuta_2(lst):
	if lst == []:
		return [[]]
	else:
		resp= []
		for perm in permuta_2(lst[1:]):
			for pos in range(len(perm) +1):
				resp.append(perm[:pos] + [lst[0]] + perm[pos:])
		return resp

def anagrama(cad):
	if cad == '':
		return [cad]
	else:
		resp= []
		for perm in anagrama(cad[1:]):
			for pos in range(len(perm) + 1):
				resp.append(perm[:pos] + cad[0] + perm[pos:])
		return resp

# -- Variante

def anag(cad):
	if cad == '':
		return [cad]
	else:
		return [perm[:pos] + cad[0] + perm[pos:] for perm in anag(cad[1:]) for pos in range(len(perm)+1)]

def insere_mult(seq,objecto):
	"""Devolve uma lista de sequências com o objecto inserido nas várias posições da
	sequência"""
	return [insere(seq,objecto,i) for i in range(len(seq)+1) ]
	
	
def insere(seq,objecto,indice):
	" Insere na posição indice da sequência seq o objecto "
	seq=copy(seq)
	seq.insert(indice,objecto)
	return seq
	
def main():
	"""Teste da função permuta"""
	#print 'Início'
	#seq=input('Sequencia')
	#print 'Permutações de %s' % seq
	#print permuta(seq)
	#return 0
	#print anagrama('amor')
	print(anag('amor'))


if __name__ == '__main__':
    main()

