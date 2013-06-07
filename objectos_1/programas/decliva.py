#-*- coding: mac-roman -*-
# Calcula o declive de um segmento de recta
# Zelle 3.6

def main():
	x1,y1=eval(input("\nCoordenadas do primeiro ponto (x,y):\t"))
	x2,y2=eval(input("\nCoordenadas do segundo ponto (x,y):\t"))
	
	res = declive(x1,y1,x2,y2)
	print("\nO declive para os pontos (%d,%d) e (%d,%d) =\t %2.3f." % (x1,y1,x2,y2,res))
	return 0

def declive(x1,y1,x2,y2):
	""" Usa a forma habitual para calcular o declive.
	Cuidado: nao podem ter a mesma abcissa!
	"""
	if x1 != x2:
		dec =float((y2 - y1))/(x2 - x1)
	else:
		return "Erro: mesma abcissa!"
	return dec

main()
