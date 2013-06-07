# -*- coding:mac-roman -*-
# ciclos while

def main():
	numero=eval(input("numero por favor:\t"))
	while numero <0:
		print("\nO numero tem que ser positivo!")
		numero=eval(input("numero por favor:\t"))
	print(" Numero e igual a %d" % numero)

if __name__ =='__main__':
	main()

