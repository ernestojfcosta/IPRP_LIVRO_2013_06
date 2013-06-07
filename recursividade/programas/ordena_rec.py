#!/usr/bin/env python
# encoding: utf-8
"""
ordena_rec.py

Created by Ernesto Costa on 2006-11-25.
Copyright (c) 2006 Universidade de Coimbra. All rights reserved.
"""

import sys
import os
from random import randint
from copy import copy,deepcopy
from bisect import *

""" coisas para testar

from sys import argv
import random
random.seed (1234321)
l = range(int (argv [1]))
random.shuffle(l)
quicksort (l)


"""
# Abordagens triviais de custo proporcional ao comprimento da sequência
def procura_trivial_1(x,seq):
	"Sim ou não?"
	return x in seq
	
def procura_trivial_2(x,seq):
	"O índice?"
	try:
		return seq.index(x)
	except ValueError:
		return -1
		
def procura_expert_1(x,seq):
	"Usa o módulo bisect. A lista tem que estar ordenada!"
	ponto_inser_x=bisect_right(seq,x)
	return seq and seq[ponto_inser_x - 1] == x
	
def procura_expert_2(x,seq):
	"Usa o módulo bisect. A lista tem que estar ordenada!"
	ponto_inser_x=bisect_right(seq,x)
	if seq and seq[ponto_inser_x - 1] == x:
		return ponto_inser_x-1
	else:
		return -1
	
# procura binária: complexidade log(n)	
def procura_bin_rec(x,seq, inicio,fim):
	""" Procura com base no facto dos elementos estarem ordenados
	"""
	if inicio == fim:
		if seq[inicio] == x:
			return inicio
		else:
			return -1
	else:
		meio =(inicio + fim)/2
		if x == seq[meio]:
			return meio
		elif x < seq[meio]:
			return procura_bin_rec(x,seq,inicio,meio-1)
		else:
			return procura_bin_rec(x,seq,meio+1,fim)

### Ordenamento


def ordena_fusao(seq,esquerda,direita):
	"""Dividir a sequência ao meio. Ordenar cada uma das partes separadamente.
	Depois fundir as duas partes"""
	if esquerda == direita:
		return [seq[esquerda]]
	else:
		seq=deepcopy(seq)		
		meio = (esquerda + direita)/2
		seq_esq=ordena_fusao(seq,esquerda,meio)
		seq_dir=ordena_fusao(seq,meio+1,direita)
		return fusao(seq_esq,seq_dir)

def fusao(seq1,seq2):
	seq=[]
	p_1=0
	p_2=0
	while (p_1 < len(seq1)) and (p_2 < len(seq2)):
		if seq1[p_1] < seq2[p_2]:
			seq.append(seq1[p_1])
			p_1 = p_1 + 1
		else:
			seq.append(seq2[p_2])
			p_2 = p_2 + 1
	if p_1 == len(seq1):
		seq.extend(seq2[p_2:])
	else:
		seq.extend(seq1[p_1:])
	return seq

	
# quicksort		
	
def quicksort(seq,inicio,fim):
	"""Quick Sort"""
	if inicio < fim:
		divisor= particao(seq, inicio, fim)
		quicksort(seq, inicio, divisor)
		quicksort(seq, divisor+1, fim)
	return seq


def particao(lista, esquerda, direita):
	"""Divide a lista em duas metades em torno de um elemento (pivot).
	no final todos os elementos menores (maiores) ou iguais ao pivot estão à
	esquerda (direita) da lista. Devolve o índice que separa a parte esquerda da direita"""
	pivot=lista[esquerda]
	p_esq=esquerda
	p_dir=direita
	while True:
		while lista[p_dir] > pivot:
			p_dir = p_dir - 1
		while lista[p_esq] < pivot:
			p_esq = p_esq + 1
		if p_esq < p_dir:
			lista[p_esq],lista[p_dir] = lista[p_dir],lista[p_esq]
			p_esq=p_esq + 1
			p_dir=p_dir - 1
		else:
			return p_dir
	
	
def main():
	num, limite = eval(input('Número de elementos e  valor máximo (num, limite)?'))
	lista= []
	for i in range(num):
		lista.append(randint(1,limite))
	objecto = randint(1,2*limite)
	print('Lista inicial e objecto')
	print(lista,objecto)
	lst_1=copy(lista)
	lst_2=copy(lista)
	lista.sort()
	print("sim ou não?")
	print(procura_trivial_1(objecto,lst_1))
	print("indice")
	print(procura_trivial_2(objecto,lst_1))
	print("expert 1")
	print(procura_expert_1(objecto,lista))
	print("expert 2")
	print(procura_expert_2(objecto,lista))
	print('Procura Binária - Rec')
	print(procura_bin_rec(objecto,lista,0,len(lista)-1))
	print('Ordenamento Fusão')
	print("Com ordenamento fusão lista ANTES =\n%s" % lst_2)
	nova_lst_f= ordena_fusao(lst_2,0,len(lst_2)-1)
	print("Com ordenamento fusão lista DEPOIS =\n%s" % nova_lst_f)
	print('Quicksort: ordena no lugar!')
	print("Com ordenamento rápido lista ANTES =\n%s" % lst_2)
	nova_lst_q=quicksort(lst_2,0,len(lst_2)-1)
	print("Com ordenamento rápido lista DEPOIS =\n%s" % nova_lst_q)
	return 0
	
	
if __name__ == '__main__':
    main()

