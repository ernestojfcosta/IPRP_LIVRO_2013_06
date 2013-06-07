from turtle import *

def exec1(lado,angulo):
	pd()
	fd(lado)
	rt(angulo)
	fd(lado)
	rt(angulo)
	fd(lado)
	rt(angulo)
	fd(lado)
	rt(angulo)
	ht()
	
def exec2(lado,angulo):
	pd()
	fd(lado)
	lado*= 1.5
	rt(angulo)
	angulo += 30
	fd(lado)
	lado*= 1.5
	rt(angulo)
	angulo += 30
	fd(lado)
	lado*= 1.5
	rt(angulo)
	angulo += 30
	fd(lado)
	lado*= 1.5
	rt(angulo)
	angulo += 30	
	ht()
	
if __name__ == '__main__':
	exec2(50,75)
	exitonclick()