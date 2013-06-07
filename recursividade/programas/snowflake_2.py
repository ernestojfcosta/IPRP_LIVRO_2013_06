#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
untitled.py

Created by Ernesto Costa on 2008-04-19.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from time import sleep

from xturtle import *

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


if __name__ == '__main__':
	levels=eval(input("Quantos níveis?"))
	reset()
	pu()
	x=-150
	goto((x,0))
	for level in range(levels):
		pd()
		snowflake(100,level)
		pu()
		goto((x+(150*(level + 1)),0))
		ht()
	sleep(50)
	#raw_input()	
	

