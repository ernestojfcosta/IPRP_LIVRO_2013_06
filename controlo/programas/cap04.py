#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
cap04.py

Created by Ernesto Costa on 2008-11-27.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os
from random import *

def gera_adn(tam):
	adn='ATGC'
	return ''.join([choice(adn) for conta in range(tam)])

def exe1():
	t= eval(input('temperatura sff:'))
	if t > 38.5:
		print('ATENÇÃO: febre!')

def exe2():
	nome=input('Qual é o seu nome?')
	if nome.endswith('Costa'):
		print('Olá Senhor Costa')

def exe3(n):
	if (n % 2) == 0:
		print("O número %d é par" % n)
		
def exe4():
	seq='ATGAnnTAG'
	if 'n' in seq:
		conta= seq.count('n')
		print('A sequência %s tem %d bases não definidas' % (seq,conta))	

def exe5(n):
	if (n % 2) == 0:
		print("O número %d é par" % n)
	else:
		print("O número %d é impar" % n)	
		
def exe6():
	nome=input('Qual é o seu nome?')
	if nome.endswith('Costa'):
		print('Olá Senhor Costa')
	else:
		print('Olá desconhecido')		
def exe7():
	primer='AACTAACCACTTCGGAATCTAGGACGGGGGAG\
	CGTTTACATGACGCCGTGGACCAAAGATTAGGCAATCGTCA\
	GTCGCTGCGCCAAGAACACGGAGAGTACCTCATGCGTGAT\
	CTTTTCATAGAGCTTGAGAACTGCTGACCTAGGGTTT'
	comp_primer=len(primer)
	percent_GC= float(primer.count('G') + primer.count('C'))/comp_primer
	if percent_GC > 0.50:
		if comp_primer > 20:
			programaPCR=1
	else:
		programa_PCR=2


def exe8():
	seq='vATGCAnATG'
	base=seq[0]
	if base in 'ATGC':
		print('Nucleótido exacto')
	elif base in 'dbhkmnrsuvwxy':
		print('Nucleótido ambíguo')
	else:
		print('Não é um nucleótido')

def exe_ass(n):
	assert 7 < n < 77, 'Valores fora dos limites'
	print(n)
	
# ----- Ciclos	
from xturtle import *

def exec1(lado,angulo):
	pd()
	fd(lado)
	rt(angulo)
	fd(lado)
	rt(angulo)
	fd(lado)
	rt(angulo)
	fd(lado)
	rt(angulo)
	ht()

def exec2(lado,angulo):
	pd()
	for i in range(4):
		fd(lado)
		rt(angulo)
	ht()


def exec3(lado, angulo, vezes):
	pd()
	for i in range(vezes):
		fd(lado)
		rt(angulo)
	ht()

def exec4(seq):
	for ch in seq:
		print(ch)
					
def main():
	#print gera_adn(150)
	#exe_ass(100)
	#exec3(75,45,6)
	#raw_input()
	exec4('abc')


if __name__ == '__main__':
	main()



