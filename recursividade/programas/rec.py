#!/usr/bin/env python
# -*- encoding: mac-roman -*-
"""
rec.py

Created by Ernesto Costa on 2007-11-13.
Copyright (c) 2007 University of Coimbra. All rights reserved.
"""

import sys
import os


def prod(m,n):
	try:
		assert(m >= 0)
	except AssertionError:
		print("***ERRO***: m = %s tem que ser positivo ou nulo" % m)
	else:
		if m==0 or n==0:
			return 0
		else:
			return n + prod(m-1,n)
	



if __name__ == '__main__':
	print(prod(5,-3))

