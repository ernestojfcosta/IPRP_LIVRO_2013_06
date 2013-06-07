#!/usr/bin/env python
# encoding: utf-8
"""
snowflake.py

Created by ERNESTO COSTA on 2008-03-24.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os
from turtle import *

def snowflake(size,level):
	for i in range(3):
		side(size,level)
		rt(120)
		
def side(size,level):
	if level == 0:
		fd(size)
		return True
	else:
		side(size/3, level-1)
		lt(60)
		side(size/3, level-1)
		rt(120)
		side(size/3,level-1)
		lt(60)
		side(size/3, level-1)

def main():
	#reset()
	#pd()
	size,level=eval(input("Tamanho e Nível: "))
	snowflake(size,level)
	ht()
	exitonclick()


if __name__ == '__main__':
	main()

