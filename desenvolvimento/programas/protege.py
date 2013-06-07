#!/usr/bin/env python
# -*- encoding: mac-roman -*-
"""
programar.py

Created by Ernesto Costa on 2007-11-17.
Copyright (c) 2007 University of Coimbra. All rights reserved.
"""

import sys
import os

from operator import itemgetter

def consensus(lseq):
	"""Constrói a sequeência de consenso
	a partir de uma lista de sequências de ADN 
	de igual comprimento.
	"""
	assert mesmo_tam(lseq) == True, 'CUIDADO: as sequências têm que ter o mesm o tamanho'
	# 1. inicializa sequência de consenso
	cons = '' # vai ser uma string
	# 2. por cada posição da sequência
	for pos in range(len(lseq[0])): # entrada uma lista
		# 2.1 calcula qual a base mais frequente para a posição corrente
		# inicializa contadores das bases
		dicio_bases={'A':0,'C':0,'T':0,'G':0} # uso um dicionário para contar
		# para cada sequência
		for seq in lseq: 
			# determina a base por cada sequência e actualiza o seu contador
			# ignora o que não interessa
			seq=seq.upper()
			if seq[pos] in ['-','N']:
				continue
			else:
				dicio_bases[seq[pos]]=dicio_bases[seq[pos]] + 1
		# determina a base que ocorre mais vezes
		base=max_ocorre(dicio_bases)
		# 2.2 actualiza a sequência de consenso na posição corrente
		cons = cons + base # a base será um caracter
	# 3. Devolve a sequência de consenso completa
	return cons


def max_ocorre(dicio):
	"""A chave cujo valor associado é o maior.
	A solução depende muito do que se sabe de Python!
	Vamos ver a solução mais 'ignorante'."""
	# Vamos buscar os pares (chave, valor)
	items=dicio.items()
	max_val=items[0][1]
	max_ch=items[0][0]
	for par in items:
		if par[1] > max_val:
			max_val=par[1]
			max_ch=par[0]
	return max_ch

def max_ocorre_1(dicio):
	maior=max(dicio.items,key=itemgetter(1))
	return maior[0]	

# A programção funcional ao seu melhor nível???
def mesmo_tam(lseq):
	return reduce(lambda x,y: x and y, [len(lseq[i])== len(lseq[i+1]) for i in range(len(lseq)-1)])
	
if __name__ == '__main__':
	print consensus(['AT-CG-','AgCTTN','TTccTT'])
	print consensus(['ATtcG','AGC-T','TTnCT'])
	