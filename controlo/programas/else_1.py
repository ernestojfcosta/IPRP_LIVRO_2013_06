# -*- coding: mac-roman -*-
#  else

def main():
	""" Exemplo de uso de else.
	"""
	y=eval(input("Numero sff (>1):\t"))
	factor_max(y)
	return 0

def factor_max(y):
	x= y /2
	while x>1:
		if y % x == 0:
			print(y, "Tem factor ",x)
			break
		x = x-1
	else:
		print(y, " e um numero primo")
		

	
if __name__ == '__main__':
	main()