#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by ERNESTO COSTA on 2008-03-24.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os
from xturtle import *


def lHilbert(size,level):
	if level == 0 :
		return
	else:
		lt(90)
		rHilbert(size,level-1)
		fd(size)
		rt(90)
		lHilbert(size, level-1)
		fd(size)
		lHilbert(size, level-1)
		rt(90)
		fd(size)
		rHilbert(size,level-1)
		lt(90)
		
def rHilbert(size,level):
	if level == 0 :
		return
	else:
		rt(90)
		lHilbert(size,level-1)
		fd(size)
		lt(90)
		rHilbert(size, level-1)
		fd(size)
		rHilbert(size, level-1)
		lt(90)
		fd(size)
		lHilbert(size,level-1)
		rt(90)		
	



def main():
	size,level=eval(input("Tamanho e Nível"))
	lHilbert(size,level)
	input()


if __name__ == '__main__':
	main()

