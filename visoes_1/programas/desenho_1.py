# -*- coding: mac-roman -*-
# ciclos

from  xturtle import *

def main():
	reset()
	forma(100,90)
	input()
	
def desenho(lado, angulo):
	""" Desenho simples.

	"""
	pendown()
	forward(lado)
	right(angulo)
	forward(angulo)
	right(lado)
	forward(lado/2)
	right(angulo/2)
	forward(lado/2)
	right(angulo/2)
	penup()
	hideturtle()
	
def forma(lado,angulo):
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	
if __name__ == '__main__':
	main()
	
	
	
	