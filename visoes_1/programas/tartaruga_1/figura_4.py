#-*- coding:mac-roman -*-

from xturtle import *

def main(n):
	reset()
	pendown()
	color('blue')
	for i in range(n):
		desenha(100,90)
		right(10)
	pen(shown=False)
	raw_input("prima <enter> para terminar. ")
	
def desenha(lado,angulo):
	for i in range(4):
		forward(lado)
		right(angulo)

main(36)
