#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
bio_f2_sol.py

Created by Ernesto Costa on 2008-10-14.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os
# from string import * # caso use funções e não métodos

# Exercício 2.1

def conv_k_m(kilo):
	return 0.62 * kilo
	
# Exercício 2.2

def somat():
	res=1
	print(res)
	res = res  + 1.0/2
	print(res)
	res = res + 1.0/3
	print(res)
	res = res + 1.0/4
	print(res) 
	res = res + 1.0/5
	print(res)
	res = res + 1.0/6
	print(res)
	res = res + 1.0/7
	print(res)
	res = res + 1.0/8
	print(res)


# Exercicio 2.3
from math import pi

def area_esfera(raio):
	res = 4 * pi * raio ** 2
	return res

# Exercício 2.4

def volume_esfera(raio):
	area = area_esfera(raio)
	res = (area * raio)/3
	return res

# Exercício 2.5	

def exp_e_x(x):
	res=1
	print(res)
	res = res  + x
	print(res)
	res = res + (x ** 2)/2.0
	print(res)
	res = res + (x ** 3) / 3.0
	print(res) 
	res = res + (x ** 4) / 4.0
	print(res)
	res = res + (x ** 5) / 5.0
	print(res)

# Exercício 2.6

def codao_start(cod):
	cod = cod.lower()
	return cod[0] == 'a' and cod[1] == 'u' and cod[2] == 'g'
	
# Exercício 2.7

def poli_A(adn):
	poli ='AAAAA'
	return adn.find(poli)  # alternativa find(arn,poli) - necessário importar módulo

# Exercício 2.8

def dupla(arn):
	arn=arn.lower()
	adn=arn.replace('u','t')
	# somos obrigados a usar algo ainda não dado nesta aula :-(!
	# mesmo assim pode-se ainda fazer melhor...
	bases_adn='atcg'
	bases_adn_comp='tagc'
	adn_comp = ''
	for b in adn:
		adn_comp= adn_comp + bases_adn_comp[bases_adn.find(b)]
	print(adn)
	print(adn_comp)


# Exercício 2.9

def codao_start_f(fich):
	fin= open(fich,'r')
	cod = fin.read().replace('\n','').lower()
	fin.close()
	return cod[0] == 'a' and cod[1] == 'u' and cod[2] == 'g'
	

def poli_A_f(fich):
	poli='AAAAA'
	fin=open(fich,'r')
	res=fin.read().upper().find(poli)
	fin.close()
	return res
	

# Exercício 2.10

def dupla_f(fich_in,fich_out):
	# Lê
	fin=open(fich_in,'r')
	adn=fin.read().lower().replace('u','t')
	fin.close()
	# somos obrigados a usar algo ainda não dado nesta aula :-(!
	# mesmo assim pode-se ainda fazer melhor...
	# Calcula
	bases_adn='atcg'
	bases_adn_comp='tagc'
	adn_comp = ''
	for b in adn:
		adn_comp= adn_comp + bases_adn_comp[bases_adn.find(b)]
	# Escreve
	fout=open(fich_out,'w')
	fout.write(adn)
	fout.write('\n')
 	fout.write(adn_comp)
	fout.close()

# Exercício 2.11

from xturtle import *
from random import *

def circulo(x,y,raio,cor):
	penup()
	setpos(x,y-raio)
	pendown()
	color(cor)
	circle(raio)
	penup()

def figura(raio,delta):
	width(5)
	colormode(255)
	circulo(0,0,raio,'black')
	circulo(2*raio+delta,0,raio,'red')
	circulo(-2*raio-delta,0,raio,'blue')
	circulo(raio+delta/2,-raio,raio,'green')
	circulo(-raio-delta/2,-raio,raio,'orange')
	
# Exercício 2.12

def existe_cod(cod,adn):
	adn=adn.lower()
	cod=cod.lower()
	x = adn.find(cod) # alternativa find(adn,cod) -- importar módulo
	if x != -1:
		print('Existe')
	else:
		print('Não Existe')


# Exercício 2.13

def conta(base,adn):
	base=base.lower()
	adn=adn.lower()
	res=0
	for b in adn:
		if b == base:
			res = res + 1
	return res
	
# Exercicio 2.14

def pos_base(base, adn):
	enc = -1
	pos=0
	while pos <= len(adn):
		if adn[pos] == base:
			enc = pos
			return enc
		pos = pos +1
	return enc
	
# Exercício 2.15

def conta_bases(fich):
	fin=open(fich)
	adn=fin.read().lower().replace('\n','')
	fin.close()
	conta_A=0
	conta_T=0
	conta_C=0
	conta_G=0
	for b in adn:
		if b == 'a':
			conta_A = conta_A + 1
		elif b == 't':
			conta_T = conta_T + 1
		elif b == 'c':
			conta_C = conta_C + 1
		else:
			conta_G = conta_G + 1
	print('Adeninas= ', conta_A)	
	print('Timinas= ', conta_T)		
	print('Citosinas= ', conta_C)		
	print('Guaninas= ', conta_G)		
		
def main():
	print('area')
	print(area_esfera(20))
	print('volume')
	print(volume_esfera(30))
	print('exponencial')
	exp_e_x(2.1)
	print('Poli tail A')
	print(poli_A('ATTCATAAAAAG'))
	print('Poli tail A - Ficheiro')
	print(poli_A_f('/tempo/bases.txt'))	# este foi criado por mim...
	print('Existe codão?')
	existe_cod('aug','attcggaugt')
	print('Conta ocorrências')
	print(conta('c', 'attcgctctca'))
	print('Posição da base na sequência')
	print(pos_base('c', 'attcgctctca'))
	print('conta bases ficheiro')
	conta_bases('/tempo/bases.txt') # este foi criado por mim ...
	print('figura JO')
	figura(50,20)
	input()


if __name__ == '__main__':
	main()

