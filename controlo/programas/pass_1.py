# -*- coding: mac-roman -*-
#  pass

def main():
	""" Exemplo de uso de pass.
	Espera interupcao pelo keyboard.
	"""
	while True:
		try:
			x=int(input("Um numero sff:\t"))
			break
		except ValueError:
			pass
	print("\nFinito!")

	
if __name__ == '__main__':
	main()
	
