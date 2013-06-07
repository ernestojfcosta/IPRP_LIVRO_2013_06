# -*- coding: mac-roman -*-
#  continue

def main():
	""" Exemplo de uso de continue.
	"""
	x=10
	while x:
		x=x-1
		if x % 2 == 0:
			continue
		print(x, end=' ')
	print("\nFinito!")
	return 0

if __name__ == '__main__':
	main()
