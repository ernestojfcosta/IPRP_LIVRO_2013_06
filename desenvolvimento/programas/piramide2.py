#!/usr/bin/env python
# encoding: utf-8
"""
piramide2.py

Created by ERNESTO COSTA on 2008-11-09.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os

from xturtle import *

lado=30
setx(0)
sety(0)

def pir(niv):
	for i in range(niv,0,-1):
		diagonal(i)
		pu()
		setx(xcor() - (i * float(lado)/2) + lado)
		sety(ycor() - i * lado)
		pd()
		
def diagonal(n):
	for i in range(n):
		quadrado()
		pu()
		setx(xcor() + float(lado)/2)
		sety(ycor() + lado)
		pd() 
		
def quadrado():
	for i in range(4):
		fd(lado)
		rt(90)
		
		
def main():
	pir(5)
	ht()
	raw_input()
	


if __name__ == '__main__':
	main()

