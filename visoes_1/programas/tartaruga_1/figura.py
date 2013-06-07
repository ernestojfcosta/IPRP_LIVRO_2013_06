

#-*- coding:mac-roman -*-

from xturtle import *

def  figura(lado, angulo):
	reset()
	pendown()
	forward(lado)
	right(angulo)
	forward(lado)
	right(angulo)
	forward(lado)
	right(angulo)
	forward(lado)
	right(angulo)
	penup()
	raw_input("prima <enter> par terminar!")

figura(100,90)

	
	