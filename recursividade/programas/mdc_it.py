#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
mdc_it.py

Created by Ernesto Costa on 2008-11-21.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

def mdc(n,m):
	div_n= divisores(n)
	div_m= divisores(m)
	inter=intersect(div_n,div_m)
	return max(inter)
	
def divisores(num):
	return [i for i in range(1,num+1) if (num % i) == 0]
	
def intersect(l1,l2):
	return [i for i in l1 if i in l2]
	
	
def main():
	print(divisores(32))
	print(divisores(4))
	print(intersect(divisores(32),divisores(4)))
	print(mdc(32,4))
	print(mdc(44,5))
	print(mdc(128,32))


if __name__ == '__main__':
	main()

