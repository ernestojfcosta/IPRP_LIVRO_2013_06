# -*- coding: mac-roman -*-
# ciclos

from  xturtle import *

def main():
	reset()
	forma(10,2,117,50)
	input()
	

	
def forma(lado,inc,angulo,n):
	reset()
	pendown()
	iterador=list(range(lado,lado +(n * inc), inc))
	for i in iterador:
		forward(i)
		right(angulo)
	penup()
	hideturtle()
	

	
if __name__ == '__main__':
	main()
	
	
	
	