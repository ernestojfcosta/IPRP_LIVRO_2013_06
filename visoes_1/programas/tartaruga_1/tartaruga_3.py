"""
sistema_l3.py

Uma vers�o simples de um sistema L.
As regras implementadas como um dicion�rio
Visualiza��o por recurso ao m�dulo cTurtle.
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
# Interpreta��o
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
	hideturtle()
	mainloop()

def interpreta(comandos):
	""" Interpretador dos comandos."""
	for com in comandos:
		exec(dicio_tarta[com])



	

if __name__ == '__main__':
	tam = 10
	ang = 90
	n = 2
	#Sistema -L
	#regras={'F':'F-F++F-F'}
	#axioma ='F'
	#axioma='F--F--F--'
	#axioma='F--F--F'
	axioma = 'F-F-F-F'
	regras= {'F':'F-F+F+FF-F-F+F'}
	# Interpreta��o para a tartaruga
	dicio_tarta={'F':'pd();fd(tam);pu()','+':'rt(ang)','-':'lt(ang)'}
	comandos = main(axioma,regras,n)
	desenho(comandos)
	
	
	