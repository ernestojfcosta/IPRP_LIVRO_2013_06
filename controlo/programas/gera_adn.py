#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
gera_adn.py

Created by Ernesto Costa on 2008-09-28.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from string import *
from random import *

def gera_adn(tamanho):
	bases='ATCG'
	adn=''
	for i in range(tamanho):
		adn=adn + choice(bases)
	return adn

def main():
	print(gera_adn(25))


if __name__ == '__main__':
	main()

