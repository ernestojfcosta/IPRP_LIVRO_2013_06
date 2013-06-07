#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
hanoi_stack.py

Created by Ernesto Costa on 2008-11-22.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

import pdb


class Stack:
   
   def __init__(self):
       self.stack = []
   
   def push(self,object):
       self.stack.append(object)
   
   def pop(self):
       if len(self.stack) == 0:
          raise 'Erro', 'Pilha Vazia'
       obj = self.stack[-1]
       del self.stack[-1]
       return obj
   
   def isempty(self):
       if len(self.stack) == 0:
          return False
       else:
          return True

class Hanoi:
    stack = Stack()
    def hanoi(self,disco,esquerda,direita,meio):
        if(disco == 1):
            print 'Disco %s desloca-se da vara %s para a vara %s' % (disco,esquerda,direita)
        else:
            self.hanoi(disco - 1 , esquerda, direita, meio)
            print 'Disco %s desloca-se da vara %s para a vara %s' % (disco,esquerda,meio)
		self.hanoi(disco - 1, direita, meio, esquerda)
    
    def hanoiNotRecursive(self,disco,esquerda,direita,meio):
        flag = -1;
        
        while disco > 0:
 	    self.stack.push((disco, esquerda, direita, meio))
	    disco = disco -1
	    flag = flag + 1
	while flag >= 0:
	    
	    disco,esquerda,direita,meio = self.stack.pop()
	    flag = flag -1;
	    if disco == 1:
	    	print 'Disco %s desloca-se da vara %s para a vara %s' % (disco,esquerda,direita)
        else:
		print 'Disco %s desloca-se da vara %s para a vara %s' % (disco,esquerda,meio)
	    disco = disco - 1
	    while disco > 0:
	      self.stack.push((disco, direita, meio, esquerda))
              disco = disco - 1
	      flag = flag + 1

testeHanoi = Hanoi()
testeHanoi.hanoi(3,'E','D','M')
print 'Hanoi not recursive'
testeHanoi.hanoiNotRecursive(3,'E','D','M')
