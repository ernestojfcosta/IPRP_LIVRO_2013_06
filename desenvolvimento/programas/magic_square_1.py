#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
magic_square_.py

Created by Ernesto Costa on 2008-11-28.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from random import randint

# vamos usar Numpy
from numpy import *


# gera matrizes

def gera_mat(lin, col, val_max):
	return array([randint(1, val_max) for i in range(lin * col)]).reshape(lin,col)
	
# verificar se pode ser um quadrado mágico

def pos_qm(mat):
	""" Verifica se a matriz M pode representar um
	quadrado mágico"""
	# dimensão da matriz
	lin,col=shape(mat)
	assert lin == col, "ERRO: Tem que ser uma matriz quadrada!"
	lmat=mat.reshape(size(mat)).tolist()
	lmat.sort()
	return lmat == range(1,size(mat) + 1)
	
	
# verificar

def isquadmagic(mat):
	assert pos_qm(mat),"ERRO: Impossível ser um quadrado mágico!"
	dim=shape(mat)[0]
	mconst=magic_const(mat)
	# Linhas
	mat_lista_l=mat.tolist()
	linhas=True
	for i in range(dim):
		if not (sum(mat_lista_l[i]) == mconst):
			linhas = False
			break
	# Colunas
	mat_lista_c=mat.transpose().tolist()
	colunas=True
	for i in range(dim):
		if not (sum(mat_lista_c[i]) == mconst):
			colunas = False
			break
	# Diagonais
	mat_lista_d1=mat.diagonal().tolist()
	mat_lista_d2=[mat[l,c] for l in range(dim) for c in range(dim) if l + c == dim - 1]
	diagonais = (sum(mat_lista_d1) == mconst) and (sum(mat_lista_d2) == mconst) 
	return linhas and colunas and diagonais
	

# calcular constante mágica

def magic_const(mat):
	assert pos_qm(mat),"ERRO: Impossível ser um quadrado mágico!"
	lin,col=shape(mat)
	return (lin ** 3 + lin) / 2


# transposta
def transposta(mat_lista):
	linhas= len(mat_lista)
	colunas= len(mat_lista[0])
	return [[ mat_lista[c][l] for c in range(colunas)] for l in range(linhas)]		


# gerar quadrado mágico   

def magic(n):
	if n > 2 and n % 2 == 0:
		print "You need an odd number."
	elif n <=2:
		print "You need a number greater or equal to 3."
	else:
		print "Magic Square: ", n, 'x', n
		grid = [ [ 0 for c in xrange(n) ] for r in xrange(n) ]
		row, col = 0, n/2
		n2, v = n*n, 1;
		r, c = 0, 0
		grid[row][col] = v
		while v != n2:
			v += 1
			if (row-1) >= 0:
			    r = row-1
			else:
			    r = n-1
			if (col+1) < n:
			    c = col+1
			else: c = 0
			if grid[r][c]:
				if (row+1) < n:
					r = row+1
					if grid[r][col]:
					    break
					c = col
			grid[r][c] = v
			row = r
			col = c
		for r in xrange(n):
			for c in xrange(n):
				print "%2d" % grid[r][c],
			print
def main():
	a=gera_mat(3,3,9)
	#a=gera_mat(5,9)
	#print pos_qm(array([[1,2,3],[9,8,7],[5,6,4]]))
	#print magic_const(array([[1,2,3],[9,8,7],[5,6,4]]))
	#print transpose(array([[1,2,3],[9,8,7],[5,6,4]]))
	#print isquadmagic(array([[2,7,8],[9,5,1],[4,3,6]]))
	print transposta([[1,2,3],[4,5,6],[7,8,9]])


if __name__ == '__main__':
	main()

