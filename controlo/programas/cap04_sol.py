#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
cap04_sol.py

Created by Ernesto Costa on 2008-11-27.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

# último teorema de Fermat

def fermat(a,b,c,n):
	# n deve ser maior do que 2!!!
	res= (a**n + b**n) == c**n
	if res:
		print('Oops! Fermat enganou-se!')
		return
	print('Ainda não foi desta!!!')
	
	
def main():
	fermat(3,4,5,2)
	fermat(4,5,8,3)


if __name__ == '__main__':
	main()

