# -*- coding: mac_roman -*-

# Exemplo simples entradas / saídas / atribuições
#  Ernesto Costa

# Dado o peso, a altura e o sexo detrmina o peso ideal e o afastamento

def main():
	"""" Tem o peso ideal?
	
	"""
	# mensagem
	
	peso = input("O seu peso por favor: ")
	altura = input("A sua altura por favor: ")
	sexo = raw_input("O seu sexo por favor ( M / F): ")
	
	# análise dos casos
	
	if sexo == 'M':
		peso_ideal = (72.7 * altura) - 58
	else:
		peso_ideal = (62.1 * altura) - 44.7
	
	# decisão
	
	desvio = round(peso - peso_ideal)
	
	if desvio < 0:
		desvio = str(-desvio)
		print "Voce precisa de engordar! " + desvio + " kilos"
	elif desvio > 0:
		print "Voce precisa de emagrecer! " + str (desvio) + " kilos"
	else:
		print "Parabens! Tem o peso ideal!!!"
		
# fazer gráfico sobre isso
		
main()

	
	
		
		
		