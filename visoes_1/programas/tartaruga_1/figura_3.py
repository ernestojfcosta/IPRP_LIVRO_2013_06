#-*- coding:mac-roman -*-

from xturtle import *

def  coisa():
	# arranca
	forward(30)
	left(60)
	forward(30)
	right(120)
	forward(30)
	left(60)
	forward(30)
	

def figura(repete):
	# e agora?
	reset()
	pendown()
	color('green')
	right(90)
	for i in range(repete):
		coisa()
		right(60)
	penup()
	raw_input("prima <enter> par terminar!")

figura(6)
