#!/usr/bin/env python
# -*- encoding: mac-roman -*-
"""
ficha2bio.py

Resolução dos exercícios da ficha 2

Created by Ernesto Costa on 2007-10-23.
Copyright (c) 2007 University of Coimbra. All rights reserved.
"""

import sys
import os

# Problema 2.1.1

def salario():
	horas_mes = input("Quantas horas trabalhou este mes: ")
	salario_hora = input("Quanto ganha por hora: ")
	
	vencimento_bruto = horas_mes * salario_hora
	print "Vencimento bruto=",vencimento_bruto," euros"
	
	desconto_seg_social = vencimento_bruto*0.11
	print "Desconto para a Segurança Social=", desconto_seg_social," euros"
	
	retido_irs = vencimento_bruto*0.135
	print "Valor retido para efeitos de IRS=",retido_irs," euros"
	
	vencimento_liquido = vencimento_bruto - desconto_seg_social-retido_irs
	print "Vencimento líquido=",vencimento_liquido," euros"
	
	return 0

# Problema 2.1.2

def prefixo():
	pal= raw_input("A primeira palavra sff: ")
	pre = raw_input("A segunda palavra sff: ")
	indice = pal.find(pre)
	return indice == 0
	
def prefixo_1():
	pal= raw_input("A primeira palavra sff: ")
	pre = raw_input("A segunda palavra sff: ")
	return pal.startswith(pre)
	


# Problema 2.2.2

def multiplos(inf,sup):
	corr=inf
	while corr < sup:
		print corr
		corr = corr + inf
	return 0
	
def multiplos_1(inf,sup):
	# Outro modo de calcular
	return [i for i in range(inf,sup,inf)]
	
# Problema 2.2.4

def tri(cadeia):
	for i in range(len(cadeia) - 2):
		print cadeia[i:i+3]	
	return 0
	
	
# Problema 2.2.6

def alfabetica(cadeia):
	i=0
	comp= len(cadeia) - 1
	alpha= True
	while (alpha and comp):
		if cadeia[i] > cadeia[i+1]:
			alpha=False
			break
		i = i + 1
		comp = comp - 1
	return alpha


# Problema 2.2.7

def hamming(seq1, seq2):
	seq1.lower()
	seq2.lower()
	dist = 0
	for i in range(min(len(seq1),len(seq2))):
		if seq1[i] != seq2[i]:
			dist = dist +1
	dist = dist + abs(len(seq1) - len(seq2))
	return dist

# Problema 2.2.8

def restrict(adn, enz):
	adn.lower()
	indice = adn.find(enz)
	while indice != -1:
		print "Enzima %s na posição %d" % (enz, indice)
		indice = adn.find(enz, indice+1)
	return 0

from random import choice
	
def gerador(n):
	alpha='ATCG'
	res=''
	for i in range(n):
		res = res + choice(alpha)
	return res

# Problema 2.2.9

def procura_inicio(cds):
	cds=cds.lower()
	indice = -1
	while 1:
		indice = cds.find('atg',indice + 1)
		if indice == -1:
			break
		if indice % 3:
			continue
		print "Posição possível de início: %d" % indice
	return 0

			
(# Problema 2.3.1

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
)arn)
# Problema 2.3.2

def desenha_fig(ficheiro):
	f= open(ficheiro,'r')
	x1,y1= f.readline().replace('\n','').split()
	setpos(int(x1),int(y1))
	pendown()
	for linha in f:
		x2,y2 = linha.replace('\n','').split()
		goto(int(x2),int(y2))
	f.close()
	return 0
	
		
if __name__ == '__main__':
	salario()
	print prefixo()
	print prefixo_1()
	print alfabetica('aB')
	multiplos(3, 28)
	tri('Biologia')
	print hamming('ATGGGCA','ATAAG')
	restrict(gerador(100000),'GAATTC')
	procura_inicio('ATGATGGGTTATGTT')
	problema 2.3.1
	figura(70,20)
	hideturtle()
	raw_input()
	# Problema 2.3.2
	desenha_fig('/opt/local/tmp/figura.txt')
	raw_input()
	print multiplos_1(15, 153)
	print 'fim'
	

