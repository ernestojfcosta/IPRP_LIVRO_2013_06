import functools


lista = [1,2,3,4,5]

print(functools.reduce(lambda x,y: x+y, lista))