#!/usr/bin/env python
# encoding: utf-8
"""
prucura.py

Created by Ernesto Costa on 2006-11-18.
Copyright (c) 2006 __DEI__. All rights reserved.
"""

import sys
import os
from time import clock
from random import *
import matplotlib
from pylab import *
from copy import copy,deepcopy

	
def main_tempo():
	"""Teste dos algoritmos  de ordenamento.
	Análise temporal no pior caso 
	"""
	"Gera listas e elementos"
	minimo,maximo,passo = eval(input("Valor minimo, maximo e passo das listas"))
	lista_listas = []
	for i in range(minimo, maximo,passo):
		lista= gera_lista(i)
		#lista.sort(reverse=True)  # para caso mais desfavorável
		lista_listas.append(lista)
	comp = len(lista_listas)
	tempos_1 = []
	tempos_2 = []
	tempos_3 = []
	tempos_4 = []
	tempos_5 = []
	for i in range(comp):
		## linear 1
		inicio_1=clock()
		selec_dir(lista_listas[i])
		fim_1 = clock()
		tempo_1 = fim_1 - inicio_1
		## bubblesort
		inicio_2=clock()
		bubblesort_3(lista_listas[i])
		fim_2 = clock()
		tempo_2 = fim_2 - inicio_2
		## fusao
		inicio_3=clock()
		ordena_fusao(lista_listas[i],0,len(lista_listas[i])-1)
		fim_3 = clock()
		tempo_3 = fim_3 - inicio_3
		## linear 4
		inicio_4=clock()
		quicksort(lista_listas[i],0,len(lista_listas[i])-1)
		fim_4 = clock()
		tempo_4 = fim_4 - inicio_4
		## binario 1
		lista_inser=lista_listas[i]
		lista_inser.sort()
		inicio_b_1=clock()
		insertion_1(lista_inser)
		fim_b_1 = clock()
		tempo_b_1 = fim_b_1 - inicio_b_1
		### Acumula tempos
		tempos_1.append(tempo_1)
		tempos_2.append(tempo_2)
		tempos_3.append(tempo_3)
		tempos_4.append(tempo_4)
		tempos_5.append(tempo_b_1)
	### desenhar
	clf()
	title(r'$An\acute{a}lise \hspace{0.5} Temporal \hspace{0.5} - \hspace{0.5} Algoritmos \hspace{0.5} de \hspace{0.5} Ordenamento$')
	xlabel(r'$Dimens\tilde{a}o$')
	ylabel('Tempo')
	t=arange(minimo,maximo,passo)
	plot(t,tempos_1,'g',t,tempos_2,'y',t,tempos_3,'b',t,tempos_4,'c',t,tempos_5,'r')
	legend(('Selecção','Bolhas','Fusão','Quicksort','Inserção'))
	show()
	return 0

def gera_lista(comp):
	"""Gera lista com valores inteiros aleatórios.
	O comprimento da lista é comp
	"""
	lista=[]
	for j in range (comp):
		lista.append(randint(1,20 * comp))
	return lista

##### ALGORITMOS

### Selecção directa
def selec_dir(seq):
	"""Ordenamento por selecção directa"""
	seq=seq[:]
	for cont in range(len(seq)-1,0,-1):
		indice=seq.index(max(seq[:cont+1]))
		seq[cont],seq[indice]=seq[indice],seq[cont]
	return seq

### Fusão

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


### Quicksort		

def quicksort(seq,inicio,fim):
	"""Quick Sort. O pivpt é o primeiro elemento"""
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

### Bolhas
def bubblesort_3(seq):
	"""Ordenamento por bolhas.
	Apenas ordena o subvector esquerdo onde houve trocas!
	"""
	seq = seq[:]
	indice= len(seq)-1
	while indice > 0:
		cont = indice - 1
		indice = 0
		for i in range(cont+1):
			if seq[i] > seq[i+1]:
				seq[i],seq[i+1] = seq[i+1],seq[i]
				indice=i
	return seq	


### Por inserção
def insertion_1(seq):
	""" Como um jogador de cartas"""
	seq=[0]+seq[:] 
	for cont in range(2,len(seq)):
		elem=seq[cont]
		indice=cont - 1
		while elem < seq[indice]:
			seq[indice + 1] = seq[indice]
			indice = indice - 1
		seq[indice + 1] = elem
	return seq[1:]

	


			
if __name__ == '__main__':
	main_tempo()

