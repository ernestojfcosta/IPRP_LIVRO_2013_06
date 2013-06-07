# -*- coding: mac-roman -*-
# ciclos

from  xturtle import *

def main():
	reset()
	forma(30,20)
	input()
	
def desenho(lado):
	""" Desenho simples.	"""
	pendown()
	forward(lado)
	right(90)
	forward(lado-10)
	right(90)
	penup()
	hideturtle()
	
def forma(lado,n):
	tamanho = lado
	for i in range(n):
		desenho(tamanho)
		tamanho = tamanho / 0.9
	"""desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)
	desenho(lado,angulo)"""
	
if __name__ == '__main__':
	main()
	
	
	
