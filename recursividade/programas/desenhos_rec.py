#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
desenhos_rec.py

Created by Ernesto Costa on 2008-11-21.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from turtle import *

def arvore(lado, angulo,nivel):
	if nivel:
		pd()
		fd(lado)
		rt(angulo)
		arvore(lado/1.5,angulo,nivel-1)
		lt(2*angulo)
		arvore(lado/1.5,angulo,nivel-1)
		rt(angulo)
		bk(lado)

def arv_desigual(lado, angulo, nivel):
	if nivel:
		lt(angulo)
		arv_esq(lado,angulo, nivel-1)
		rt(2*angulo)
		arv_dir(lado, angulo, nivel -1)
		lt(angulo)
		
def arv_esq(lado, angulo,nivel):
	fd(2*lado)
	arv_desigual(lado, angulo, nivel)
	bk(2*lado)
	
def arv_dir(lado, angulo,nivel):
		fd(lado)
		arv_desigual(lado, angulo, nivel)
		bk(lado)
	
def main():
	setheading(90)
	arv_esq(25,30,7)
	ht()



if __name__ == '__main__':
	main()
	exitonclick()

