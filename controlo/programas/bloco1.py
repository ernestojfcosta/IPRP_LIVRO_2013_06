#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
bloco1.py

Created by Ernesto Costa on 2008-11-27.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os


def main():
	pass


if __name__ == '__main__':
	x=1
	if x:
		y=2
		if y:
			print('Bloco 2: x= %d, y= %d' % (x,y))
		print('Bloco 1: x= %d, y= %d' % (x,y))
	print('Bloco 0: x= %d, y= %d' % (x,y))

