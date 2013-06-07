#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xturtle import *

def figura(lado,angulo):
	"""Desenhar uma sequencia de 4 segmentos
	por recurso ao modulo xturtle."""
	reset()
	pendown()
	# repete 4 vezes
	forward(lado)
	right(angulo)
	forward(lado)
	right(angulo)
	forward(lado)
	right(angulo)
	forward(lado)
	right(angulo)
	penup()
	input("Prima <enter> para terminar")
	return

if __name__ == '__main__':
	figura(100,90)

