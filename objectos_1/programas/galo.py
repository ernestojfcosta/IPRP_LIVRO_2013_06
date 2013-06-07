#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
untitled.py

Created by Ernesto Costa on 2008-07-07.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os
from xturtle import *

a=-1
b=-1
c=-1
d=-1
e=-1
f=-1
g=-1
h=-1
i=-1
num_jogada=0
	
def circulo(x,y):
	color('red')
	penup()
	setpos(x*100,y*100-40)
	pendown()
	width(5)
	circle(40)
	penup()

def cruz(x,y):
	color('green')
	width(5)
	penup()
	setpos(x*100-40,y*100-40)
	pendown()
	setpos(x*100+40,y*100+40)
	penup()
	setpos(x*100-40,y*100+40)
	pendown()
	setpos(x*100+40,y*100-40)
	penup()

def linha(x1,y1,x2,y2,peso,cor):
	color(cor)
	width(peso)
	penup()
	setpos(x1,y1)
	pendown()
	setpos(x2,y2)
	penup()

def jogada(x,y):
	global a,b,c,d,e,f,g,h,i,num_jogada
	# determina quadricula
	if x>50:
		xpos=1
	elif x<-50:
		xpos=-1
	else:
		xpos=0

	if y>50:
		ypos=1
	elif y<-50:
		ypos=-1
	else:
		ypos=0
	
	# valida jogada
	jogada_valida=0
	
	if xpos==-1:
		if ypos==1 and a==-1:
			jogada_valida=1
			a=(num_jogada+1)%2
		if ypos==0 and d==-1:
			jogada_valida=1
			d=(num_jogada+1)%2
		if ypos==-1 and g==-1:
			jogada_valida=1
			g=(num_jogada+1)%2

	if xpos==0:
		if ypos==1 and b==-1:
			jogada_valida=1
			b=(num_jogada+1)%2
		if ypos==0 and e==-1:
			jogada_valida=1
			e=(num_jogada+1)%2
		if ypos==-1 and h==-1:
			jogada_valida=1
			h=(num_jogada+1)%2

	if xpos==1:
		if ypos==1 and c==-1:
			jogada_valida=1
			c=(num_jogada+1)%2
		if ypos==0 and f==-1:
			jogada_valida=1
			f=(num_jogada+1)%2
		if ypos==-1 and i==-1:
			jogada_valida=1
			i=(num_jogada+1)%2


	if jogada_valida==1:
		num_jogada=num_jogada+1
		if (num_jogada%2==0):
			cruz(xpos,ypos)
		else:
			circulo(xpos,ypos)
	
def desenhaGrelha():
	linha(-150,50,150,50,5,'blue')
	linha(-150,-50,150,-50,5,'blue')
	linha(-50,-150,-50,150,5,'blue')
	linha(50,-150,50,150,5,'blue')

def main():
	hideturtle()
	delay(0)
	desenhaGrelha()
	onscreenclick(jogada,1)


main()
mainloop()