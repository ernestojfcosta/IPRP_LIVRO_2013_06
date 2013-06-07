#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
exempdoc.py

Para ilustrar a importancia de usar cadeias 
de caracteres como documentacao.

Created by Ernesto Costa on 2008-07-13.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os
from math import pi

def volume(raio):
	"""Calculo do Volume de uma esfera."""
	return 4.0/3 * pi * raio
	


if __name__ == '__main__':
	r= eval(input("Valor do raio: "))
	volume(r)


