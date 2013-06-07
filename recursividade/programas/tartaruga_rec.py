#!/usr/bin/env python
# encoding: utf-8
"""
tartaruga_rec.py

Created by Ernesto Costa on 2006-11-25.
Copyright (c) 2006 Universidade de Coimbra. All rights reserved.
"""

import sys
import os
from xturtle import *

def figura2(lado,angulo,vezes):
	pd()
	for i in range(vezes):
		fd(lado)
		rt(angulo)
	ht()
	return 0

		
def figura(lado,angulo):
	"""Desenha figuras recursivamente a partir de um padrão de base simples.
	Admite que a tartaruga tem a caneta levantada.
	"""
	pd()
	if lado:
		forward(lado)
		right(angulo)
		figura(lado-1,angulo)
	ht()
	return 0
	
def figura_inc_lado(lado,angulo,inc):
	"Desenha recursivamente com o incremento como parâmetro"
	pd()
	if lado > 0:
		forward(lado)
		right(angulo)
		figura_inc_lado(lado-inc,angulo,inc)
	ht()
	return 0
	
def figura_inc_ang(lado,angulo,inc):
	"Desenha recursivamente com o incremento como parâmetro"
	pd()
	if angulo > 0:
		forward(lado)
		right(angulo)
		figura_inc_ang(lado,angulo-inc,inc)
	ht()
	return 0	
	
def figura_inc_lado_ang(lado,angulo,incl,inca):
	"Desenha recursivamente com o incremento como parâmetro"
	pd()
	if lado > 0:
		forward(lado)
		right(angulo)
		figura_inc_lado_ang(lado-incl,angulo-inca,incl,inca)
	ht()
	return 0

def figura_inc_lado_ang_var(lado,angulo,incl,inca):
	"Desenha recursivamente com o incremento como parâmetro"
	pd()
	if lado > 0:
		forward(lado)
		right(angulo)
		figura_inc_lado_ang(lado-incl,angulo-inca,0.8*incl,0.7*inca)
	ht()
	return 0
	
def main():
	print("Vamos desenhar recursivamente!")
	figura_inc_lado_ang_var(100,120,5,3)
	input()
## Árvores

def base_arv(comp,decremento,espessura):
	" Desenha o elemento de base"
	pendown()
	pensize(espessura)
	forward(comp)
	left(30)
	forward(comp - decremento)
	backward(comp - decremento)
	right(60)
	forward(comp - decremento)
	backward(comp - decremento)
	left(30)
	backward(comp)
	hideturtle()
	penup()
	
def arv_rec(comp,decremento,altura):
	" Desenha a árvore"
	if altura:
		pensize(altura)
		forward(comp)
		left(30)
		arv_rec(comp-decremento,decremento,altura-1)
		right(60)
		arv_rec(comp-decremento,decremento,altura-1)
		left(30)
		backward(comp)


def arvore(comp,decremento,altura):
	"""Desenha recursivamente uma árvore.
	A altura controla a profundidade da árvore."""
	pendown()
	arv_rec(comp,decremento,altura)
	hideturtle()
	penup()

	
			

if __name__ == '__main__':
	main()
	

