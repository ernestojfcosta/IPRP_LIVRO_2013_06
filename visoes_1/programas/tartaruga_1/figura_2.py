#-*- coding:mac-roman -*-

from xturtle import *

def  figura(lado, angulo, repete):
	reset()
	pendown()
	for i in range(repete):
		forward(lado)
		right(angulo)
	penup()
	raw_input("prima <enter> par terminar!")

def quadrado():
	figura(100,90,4)
	
quadrado()
