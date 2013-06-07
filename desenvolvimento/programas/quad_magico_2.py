#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
quad_mágico_2.py

Created by Ernesto Costa on 2008-11-30.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

#--- Constante mágica
def constante_mag(quad):
	'Admitimos que é um quadrado mágico'
	dim=dimensao(quad)
	return (dim ** 3 + dim)/2

def dimensao(quad):
	"""Quadrado mágico representado como uma
	lista de listas"""
	return len(quad)


def quad_mag(quad):
	cm= constante_mag(quad)
	# soma por linhas: todas iguais à constante mágica?
	for linha in linhas(quad):
		if soma(linha) != cm:
			return False
	# soma por colunas: todas iguais à constante mágica?
	for coluna in colunas(quad):
		if soma(coluna) != cm:
			return False
	# soma por diagonais: todas iguais à constante mágica?
	for diag in diagonais(quad):
		if soma(diag) != cm:
			return False
	return True
	
# -- representado por uma lista de listas. Cada lista é uma linha
# -- exemplo 3*3: quad=[[1,2,3],[4,5,6],[7,8,9]]
def linhas(quad):
	return quad
	
def colunas(quad):
	# quad(l,c) --> quad(c,l)
	dim=len(quad)
	return [[ quad[c][l] for c in range(dim)] for l in range(dim)]

def diagonais(quad):
	dim=len(quad)
	diag1= [quad[i][i] for i in range(dim) ]
	diag2= [quad[l][c] for l in range(dim) for c in range(dim) if l + c == dim - 1]
	return [diag1,diag2]	


def soma(lista):
	return sum(lista)	
	
			
def main():
	print colunas([[1,2,3],[4,5,6],[7,8,9]])
	print diagonais([[1,2,3],[4,5,6],[7,8,9]])
	print quad_mag([[2,7,8],[9,5,1],[4,3,6]])
	print quad_mag([[2,7,6],[9,5,1],[4,3,8]])
	
if __name__ == '__main__':
	main()

