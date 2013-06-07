# -*- coding: mac-roman -*-
# break

def main():
	""" Exemplo de uso de break.
	"""
	while True:
		nome=input("O seu nome:\t")
		if nome =='stop':
			break
		idade=eval(input(" A sua idade:\t"))
		print("\nViva %s!\t %d e uma linda idade..." % (nome,idade))
	print("Finito!")
	return 0

if __name__ == '__main__':
	main()
