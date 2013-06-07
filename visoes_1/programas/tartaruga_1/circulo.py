#-*- coding:mac-roman -*-

from xturtle import *

def main():
	reset()
	pendown()
	color('red')
	circulo()
	pen(shown=False)
	input("prima <enter> para terminar. ")

def circulo():
	for i in range(360):
		forward(1)
		right(1)
		
main()






		
