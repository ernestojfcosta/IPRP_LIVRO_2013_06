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


def c_curve(size,level):
	if level == 0:
		fd(size)
		return True
	else:
		c_curve(size,level-1)
		rt(90)
		c_curve(size,level-1)
		lt(90)





def main():
	size,level=eval(input("Tamanho e Nível"))
	c_curve(size,level-1)
	ht()
	input()


if __name__ == '__main__':
	main()

