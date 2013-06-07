#-*- coding: mac-roman -*-
# turtle while

from xturtle import *

def main():
	lado,angulo_inicial,angulo_viragem,repete=eval(input("Lado e angulos (inicial e de viragem) e repeticoes sff:\t"))
	reset()
	for i in range(repete):
		poligono(lado,angulo_inicial)
		right(angulo_viragem)
	input()
	return 0


def main1():
	lado,angulo=eval(input("Lado e angulo sff:\t"))
	reset()
	poligono(lado,angulo)
	input()
	return 0


def poligono(lado,angulo):
	pendown()
	volta=0
	while (volta % 360 != 0) or (volta ==0):
		forward(lado)
		right(angulo)
		volta = volta + angulo
	penup()
	hideturtle()
	
if __name__ =='__main__':
	main()

