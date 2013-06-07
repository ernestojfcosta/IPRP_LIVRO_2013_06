#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
peano.py

Created by Ernesto Costa on 2008-03-23.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from time import sleep

from xturtle import *

def fill_curve(size,level):
	"Recursive space filling"
	if level == 0:
		fd(size)
		return None
	else:
		fill_curve(size/3,level-1)
		lt(90)
		fill_curve(size/3,level-1)
		rt(90)
		fill_curve(size/3,level-1)
		rt(90)
		fill_curve(size/3,level-1)
		rt(90)
		fill_curve(size/3,level-1)
		lt(90)
		fill_curve(size/3,level-1)
		lt(90)
		fill_curve(size/3,level-1)
		lt(90)
		fill_curve(size/3,level-1)
		rt(90)
		fill_curve(size/3,level-1)

if __name__ == '__main__':
	levels=eval(input("Quantos níveis?"))
	reset()
	pu()
	x=-150
	goto((x,0))
	for level in range(levels):
		pd()
		fill_curve(100,level)
		pu()
		goto((x+(150*(level + 1)),0))
	ht()
	sleep(50)
	#raw_input()	

	

