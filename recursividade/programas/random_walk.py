#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
random_walk.py

Created by Ernesto Costa on 2008-04-19.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from time import sleep
from random import *
from xturtle import *

def random_walk(size, steps, xi=0,yi=0):
	reset()
	pu()
	x=xi
	y=yi
	goto((x,y))
	pd()
	for step in range(steps):
		delta_x=choice([-size,0,size])
		delta_y=choice([-size,0,size])
		x=x + delta_x
		y=y + delta_y
		goto(x,y)
	ht()
		


if __name__ == '__main__':
	size,steps,x,y=eval(input("tamanho, passos,x e y: "))
	random_walk(size,steps,x,y)
	sleep(10)
