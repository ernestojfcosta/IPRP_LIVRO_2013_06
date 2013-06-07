# -*- coding: utf-8 -*-

from random import *

def main():
	""" Fabrica nomes de utilizadores
	a partir do nome proprio e do nome de familia"""
	# entrada de dados
	proprio = input("O seu primeiro nome sff: ").lower()
	familia = input("O seu ultimo nome sff: ").lower()
	
	# processamento
	nome = proprio[0] + familia[:7]
	nome_util = nome + str(randint(1,50))
	
	# saida do resultado
	print("O seu nome de utilizador e = %s" % nome_util)
	return



if __name__ == '__main__':
	main()

