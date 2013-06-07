#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by ERNESTO COSTA on 2008-09-27.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os

from xturtle import  *

def quad1(lado):
    pd()
    fd(lado)
    rt(90)
    fd(lado)
    rt(90)
    fd(lado)
    rt(90)
    fd(lado)
    ht()
    
if __name__ == '__main__':
    quad1(50)
    input()



