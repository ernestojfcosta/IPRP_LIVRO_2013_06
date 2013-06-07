"""
sistema_l2.py

Uma versão simples de um sistema L.
As regras implementadas como um dicionário
Visualização por recurso ao módulo cTurtle.
"""
from cTurtle import *

# Reescrita
def main(axioma,regras,passos):
	resultado=reescreve(axioma,regras,passos)
	return resultado
	

def reescreve(exp,regras,passos):
	forma = exp
	for i in range(passos):
		forma = aplica(regras,forma)
	return forma

def aplica(regras,exp):
	forma=''
	for ch in exp:
		forma = forma + regras.get(ch,ch)
	return forma


# ---------------------------------------------------------------
# Interpretação
# Simular um sistema L simples por recurso a xturtle
# ---------------------------------------------------------------
def inic():
	"""Inicializa o sistema."""
	reset()
	up()
	shape('turtle')
	color('red')
	setheading(0)
	goto(0,0)


def desenho(seq):
	inic()
	interpreta(seq)
	mainloop()

def interpreta(comandos):
	""" Interpretador dos comandos."""
	for com in comandos:
		exec(dicio_tarta[com])


if __name__ == '__main__':
	#Sistema -L
	#regras={'B':'A','A':'AB'}
	#axioma='B'
	#regras={'B':'A','A':'AB'}
	#axioma='A'
	# cantor dust
	regras={'B':'BBB','A':'ABA'}
	axioma='A'
	# Interpretação para a tartaruga
	dicio_tarta={'A':'pd();fd(10);pu()','B':'rt(45)'}
	comandos = main(axioma,regras,6)
	desenho(comandos)