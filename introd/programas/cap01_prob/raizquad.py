#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
raizquad.py

Created by Ernesto Costa on 2008-07-06.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os
def raizquad(n):
	# Calculo da raiz quadrada de um número positivo pelo método de Newton
	x = input("Valor inicial sff: ")
	for i in range(10):
		x = (1/2.0) * (x + (n/x))
	print x


