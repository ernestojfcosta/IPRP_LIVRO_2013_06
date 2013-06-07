#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
recursividade.py

Created by Ernesto Costa on 2008-10-24.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from random import *
from xturtle import *

lado= 30 # lado do quadrado
pu()
setx(0) # posição inicial x
sety(0) # posição inicial y
pd()

def desenha_pir(nivel):
	for i in range(1,nivel+1):
		stamp()
		# vai para o local certo
		pu()
		setx(xcor() - ((i-1) * lado) - float(lado)/2)
		sety(ycor()- lado)
		pd()
		# desenha um linha de quadrados
		linha(i)
	return True
	
def linha(n):
	for k in range(n):
		# vai para o local certo
		pu()
		setx(xcor() + lado)
		pd()
		# desenha quadrado
		quadrado()
	return True	
	
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
	return True	
	
def quad():
	dot(10,'red')
	for i in range(4):
		fd(lado)
		rt(90)
	return True

def pir_rec(niveis):
	if niveis == 1:
		# desenha
		linha_rec(1)
	else:
		pir_rec(niveis-1)
		# nova posição
		pu()
		setx(xcor() - ((niveis - 2) * lado) - float(lado)/2)
		sety(ycor()- lado)
		pd()
		linha_rec(niveis)


def linha_rec(n):
	if n == 1:
		# desenha quadrado
		quadrado()	
	else:
		linha_rec(n-1)
		# vai para o local certo
		pu()
		setx(xcor() + lado)
		pd()
		quadrado()

			
			
def main():
	pencolor('blue')
	pensize(3)
	#desenha_pir(3)
	colormode(255)
	pir_rec(5)
	#quad()
	ht()
	raw_input()


if __name__ == '__main__':
	main()

