#-*- coding:mac-roman -*-

from xturtle import *

def main():
	reset()
	pendown()
	color('red')
	figura_curva(1,1,360)
	figura_curva(1,2,180)
	pen(shown=False)
	input("prima <enter> para terminar. ")

def figura_curva(avanca,roda,repete):
	for i in range(repete):
		forward(avanca)
		right(roda)
		
main()
