#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
piramide.py

Created by Ernesto Costa on 2008-11-02.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from random import randint
from xturtle import *

lado = 40
# posição inicial
pu()
setx(0)
sety(0)
pd()

def piramide(niveis):
	# desenha pirâmide
	for i in range(1, niveis + 1):
		desenha_linha(i)
		# actualiza posição
		pu()
		sety(ycor() - lado)
		setx(xcor() - i * lado - float(lado)/2)
		pd()
	return 'Fim'

def desenha_linha(linha):
	# desenha linha
	for i in range(linha):
		#desenha_quadrado() # preto e branco
		quadrado() # a cores
		# nova posição
		pu()
		setx(xcor() + lado)
		pd()
	return 'Fim'

def desenha_quadrado():
	for i in range(4):
		fd(lado)
		rt(90)
	return 'Fim'
	
def quadrado():
	# desenha
	r=randint(0,255)
	g=randint(0,255)
	b=randint(0,255)
	fillcolor(r,g,b)
	fill(True)
	for i in range(4):
		fd(lado)
		rt(90)
	fill(False)
	return 'Fim'
	
def main():
	pencolor('blue')
	pensize(3)
	colormode(255)
	piramide(5)
	ht()
	raw_input()

if __name__ == '__main__':
	main()

