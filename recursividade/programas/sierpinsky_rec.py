#!/usr/bin/env python
# encoding: utf-8
"""
snowflake.py

Created by ERNESTO COSTA on 2008-03-24.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os
from time import sleep

from turtle import *

def spierpinsky(size,level):
	for i in range(3):
		tri(size,level)
		rt(120)
		
def tri(size,level):
	pd()
	st()
	if level == 0:
		fd(size)
		return True
	else:
		tri(size/2, level-1)
		lt(120)
		tri(size/2, level-1)
		lt(120)
		tri(size/2,level-1)
		lt(120)
		ht()
		pu()
		fd(size)

if __name__ == '__main__':
	levels=eval(input("Quantos níveis?"))
	reset()
	pu()
	x=-150
	goto((x,0))
	for level in range(1,levels+1):
		pd()
		tri(200,level)
		pu()
		goto((x+(110*(level)),0))
	ht()
	sleep(50)
	input()
"""	
def main():
	reset()
	pd()
	size,level=input(u"Tamanho e nível")
	tri(size,level)
	ht()
	sleep(50)
	#raw_input()


if __name__ == '__main__':
	main()
"""