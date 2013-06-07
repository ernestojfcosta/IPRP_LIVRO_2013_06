#-*- coding: mac-roman -*-
# while

def simples():
	palavra=input("Entre a palavra sff:\t")
	while palavra:
		print(palavra, end=' ')
		palavra=palavra[1:]
	return 0

def impares():
	limite=eval(input("Entre o limite superior sff:\t"))
	while limite:
		if limite % 2 != 0:
			print(limite, end=' ')
		limite = limite -1
	return 0

#impares()

simples()