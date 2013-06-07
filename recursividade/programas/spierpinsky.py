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

from xturtle import *

def sierpinski(size,level):
	if level == 0:
		return True
	else:
		for i in range(3):
			sierpinski(size/2,level -1)
			fd(size)
			rt(120)
		
def sier(size,level):
	pd()
	st()
	if level == 0:
		fd(size)
		return True
	else:
		sier(size/2, level-1)
		lt(120)
		sier(size/2, level-1)
		lt(120)
		sier(size/2,level-1)
		lt(120)
		ht()
		pu()
		fd(size)

def main():
	sierpinski(200,4)
	ht()
	input()
	
if __name__ == '__main__':
	main()
"""	
#if __name__ == '__main__':
	levels=input(u"Quantos níveis?")
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
	raw_input()
	
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