#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
strassen.py
 Multiplicações de matrizes pelo método de Strassen.
Created by Ernesto Costa on 2008-11-23.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from random import *
from numpy import *

# Gerador de matrizes quadradas

def gera_mat(dim, val_max):
	return array([randint(1, val_max) for i in range(dim * dim)]).reshape(dim,dim)

# Strassen: caso de base	
def strassen_2(X2,Y2):
	# inicia matriz resultado
	Z2=zeros((2,2), dtype=int)
	# parâmetros
	p1=(X2[0,0] + X2[1,1]) * (Y2[0,0] + Y2[1,1])
	p2= (X2[1,0] + X2[1,1]) * Y2[0,0] 
	p3= X2[0,0] * (Y2[0,1] - Y2[1,1])
	p4=  X2[1,1] * (Y2[1,0] - Y2[0,0])	
	p5=(X2[0,0] + X2[0,1]) * Y2[1,1]
	p6=(X2[1,0] - X2[0,0]) * (Y2[0,0] + Y2[0,1])
	p7=(X2[0,1] - X2[1,1]) * (Y2[1,0] + Y2[1,1])
	# valores actualizados
	Z2[0,0]= p1 + p4 - p5 + p7
	Z2[0,1] = p3 + p5
	Z2[1,0] = p2 + p4
	Z2[1,1] = p1 + p3 + - p2 + p6
	
	return Z2
	
# Strassen: Geral
	
def strassen(X,Y):
	if (X.shape == (2,2)) and (Y.shape == (2,2)):
		return strassen_2(X,Y)
	else:
		n=X.shape[0]
		Z=gera_mat(n,1)
		m= n/2
		X11 = X[:m,:m]
		X12 = X[:m,m:]
		X21 = X[m:,:m]
		X22 = X[m:,m:]
		
		Y11 = Y[:m,:m]
		Y12 = Y[:m,m:]
		Y21 = Y[m:,:m]
		Y22 = Y[m:,m:]		
		
		P1= strassen((X11 + X22),(Y11 + Y22))
		P2= strassen((X21 + X22),Y11)
		P3= strassen(X11,(Y12 - Y22))
		P4= strassen( X22,(Y21 - Y11))
		P5= strassen((X11 + X12),Y22)
		P6= strassen((X21 - X11),(Y11 + Y12))
		P7= strassen((X12 - X22),(Y21 + Y22))
		
		Z11= P1 + P4 - P5 + P7
		Z12= P3 + P5
		Z21= P2 + P4
		Z22= P1 + P3 - P2 + P6
		
		Z[:m,:m] = Z11
		Z[:m,m:] = Z12
		Z[m:,:m] = Z21
		Z[m:,m:] = Z22
		return Z
		
def main():
	"""
	X=array([[1,2], [3,4]])
	Y=array([[5,6],[7,8]])
	print strassen_2(X,Y)
	print X + Y
	print X - Y
	print dot(X,Y)
	print 'Strassen .....'
	print strassen(X,Y)
	XX=array([[1,2,2,1],[3,4,4,3],[5,6,6,5],[7,8,8,7]])
	YY=array([[1,1,2,2], [2,2,1,2],[3,3,3,3],[1,1,1,1]])
	print strassen(XX,YY)
	"""
	#print gera_mat(8,15)
	X=gera_mat(16,5)
	Y=gera_mat(16,5)
	print('X')
	print(X)
	print('Y')
	print(Y)
	print('STRASSEN')
	print(strassen(X,Y))
	print('NORMAL')
	print(dot(X,Y))
	

if __name__ == '__main__':
	main()

