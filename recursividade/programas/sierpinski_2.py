
from turtle import *

def sierpinski(tamanho,nivel): 
    if nivel == 0:
        return True 
    else:
        for i in range(3): 
            sierpinski(tamanho/2,nivel -1) 
            fd(tamanho)
            rt(120)
            
if __name__ == '__main__':
    sierpinski(150,4)