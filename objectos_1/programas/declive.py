"""Capítulo 3."""

def declive(x1,y1,x2,y2):
	""" Usa a forma habitual para calcular o declive, dados dois pontos.
	Cuidado: não podem ter a mesma abcissa!
	"""
	if x1 != x2:
		return (y2 - y1)/(x2 - x1)
	else:
		return float('Inf')


def declive(x1,y1,x2,y2):
	""" Usa a forma habitual para calcular o declive, dados dois pontos.
	Cuidado: não podem ter a mesma abcissa!
	"""
	return (y2 - y1)/(x2 - x1)

if __name__ == '__main__':
	print((declive(5,4,8,10)))
	print((declive(5,4,5,10)))	