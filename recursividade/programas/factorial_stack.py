#!/usr/bin/env python
#  -*- coding: iso-8859-1 -*-
#  This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#  This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# author: Marlon Petry
# Date: 2008/07/06
# Function: Remove Recursion with one Stack in python
#
class Stack:

     def __init__(self):
         self.stack = []

     def push(self,object):
         self.stack.append(object)

     def pop(self):
         if len(self.stack) == 0:
            raise “Error”, “stack is empty”
         obj = self.stack[-1]
         del self.stack[-1]
         return obj

     def isempty(self):
         if len(self.stack) == 0:
            return False
         else:
            return True

class CalculusFatorial:
    stack = Stack()
    def fatorialRecursive(self, x):
        if x == 0:
            return 1
        else:
            return (x * self.fatorialRecursive(x - 1))

    def fatorialSimulateRecursive(self, x):
        factorial = 1;
        while x > 0:
            self.stack.push(x)
            x -= 1

        while self.stack.isempty():
            factorial *= self.stack.pop()

        return factorial

calc = CalculusFatorial()
print calc.fatorialRecursive(950)
print “Não recursivo”
print calc.fatorialSimulateRecursive(950)
calc.show()
