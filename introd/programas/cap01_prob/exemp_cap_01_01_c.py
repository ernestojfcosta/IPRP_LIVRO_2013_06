# -*- coding: mac-roman -*-

# Exemplo simples entradas / saídas / atribuições
#  Ernesto Costa

# Dada a altura calcula o peso ideal para uma pessoa

def main():
	"""" Tem o peso ideal?
	
	"""
	# mensagem
		
	altura = input("A sua altura por favor: ")
	sexo = raw_input("O seu sexo por favor (M / F): ")
	
	if sexo == 'M':
		peso_ideal  = 72.7 * altura - 58
	else:
		peso_ideal = 62.1 * altura - 44.7
	
	print "O seu peso ideal e ", peso_ideal, "kilos"

		
main()


