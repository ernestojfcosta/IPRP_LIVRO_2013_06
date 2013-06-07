import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return math.exp((-x**2)/2)

def mostra_func(f, min_x,max_x):
    x = np.arange(min_x, max_x,0.01)
    plt.plot(x,[f(elem) for elem in x])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(r'$e^{-x^{2}}$')
    plt.show()
    
if __name__ == '__main__':
    mostra_func(f,-2,2)