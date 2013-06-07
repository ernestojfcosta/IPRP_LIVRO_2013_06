#-*- coding:utf-8 -*-

from turtle import *

def laco(n,arco):
    for i in range(n):
        rt(360.0/n)
        fd(arco)

def multiplos_lacos(n,arco):
    for i in range(n):
        rt(360.0/n)
        laco(n,arco)
        
def main(n, arco):
    bgcolor('black')
    pencolor('red')
    pensize(3)
    multiplos_lacos(n,arco)
    hideturtle()
    exitonclick()
    
main(100,10)