# -*- coding: mac_roman -*-

# Exemplo simples entradas / saídas / atribuições
#  Ernesto Costa


def main():
	"""" 
	Dado o peso, a altura e o sexo determina o peso ideal e o desvio
	"""
	# dados
	peso = eval(input("O seu peso por favor: "))
	altura = eval(input("A sua altura por favor: "))
	sexo = input("O seu sexo por favor ( M / F): ")
	
	# análise dos casos
	if sexo == 'M':
		peso_ideal = (72.7 * altura) - 58
	else:
		peso_ideal = (62.1 * altura) - 44.7
	
	# decisão
	desvio = round(peso - peso_ideal)
	if desvio < 0:
		desvio = str(-desvio)
		print("Voce precisa de engordar! " + desvio + " kilos")
	elif desvio > 0:
		print("Voce precisa de emagrecer! " + str (desvio) + " kilos")
	else:
		print("Parabens! Tem o peso ideal!!!")
		
if __name__ == '__main__':		
	main()

	
	
		
		
		