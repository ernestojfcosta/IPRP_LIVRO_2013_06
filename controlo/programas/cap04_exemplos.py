#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
cap04_exemplos.py

Created by Ernesto Costa on 2008-12-03.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

# -- break

def factor_max(y):
	x= y /2
	while x>1:
		if y % x == 0:
			print(y, "Tem factor ",x)
			break
		x = x-1
	else:
		print(y, " e um numero primo")


def ent_dados():
	""" Exemplo de uso de break."""
	while True:
		nome=input("O seu nome:\t")
		if nome =='stop':
			break
		idade=eval(input(" A sua idade:\t"))
		print("\nViva %s!\t %d e uma linda idade..." % (nome,idade))
	print("Finito!")
	return 0


from math import sqrt

def quad_perfeito(n):
	"O maior quadrado perfeito menor do que n"
	for num in range(n,0,-1):
		raiz=sqrt(num)
		if raiz == int(raiz):
			print("Maior quadrado perfeito menor do que %d é %d" % (n,num))
			break
	
# -- continue

def codigo():
	"Pedir um código com exactamente quatro caracteres"
	while True:
		cod = input('Código sff: ')
		if len(cod) != 4:
			print('O código tem que ter 4 caracteres')
			continue
		else:
			print('Bem-vindo')
			break

def impares(x):
	""" Exemplo de uso de continue."""
	while x:
		x=x-1
		if x % 2 == 0:
			continue
		print("%d é ímpar." % x)
	print("\nFinito!")
	return 0
	
#-- else

def primo(y):
	x= y /2
	while x>1:
		if y % x == 0:
			print(y, "Tem factor ",x)
			break
		x = x-1
	else:
		print(y, " é um número primo")
		
def password(lista_passw):
	" Três chances para introduzir correctamente uma password"
	flag=False
	conta=3
	while conta:
		codigo=input("Entre o seu código sff:")
		for passw in lista_passw:
			if codigo==	passw:
				flag=True
				print("Bem-vindo")
				break
		if not flag:
			print("Código errado. Tente novamente.")
			conta= conta - 1
			continue
		else:
			break
	else:
		print("Código errado. Acabaram as suas tentativas!!!")

def password2(lista_passw):
	" Três chances para introduzir correctamente uma password"
	conta=3
	while conta:
		codigo=input("Entre o seu código sff:")
		if codigo in lista_passw:
			print("Bem-vindo")
			break
		print("Código errado.")
		conta= conta - 1
		continue
	else:
		print("Acabaram as suas tentativas!!!")	
# -- pass

def verfica(nome):
	if nome =='Ernesto Costa':
		print('Bem-vindo')
	elif nome == 'Bill Gates':
		print('Acesso Negado!')
	else:
		# depois decido...
		pass
	
# -- try

def try_1(x):
	try:
		y=eval(input("\nDenominador: "))
		print(float(x) / y)
	except ZeroDivisionError:
		print("\nCuidado: y nao pode ser zero!")



def try_2():
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
	
	
def try_3():
	""" Calculo das raizes reais de um poinomio.
	"""
	try:
		a,b,c = eval(input("Os coeficientes sff (a,b,c):\t"))	
		discriminante=pow(b,2)- 4 * a * c
		raiz_discrim = math.sqrt(discriminante)
		raiz1=float((-b + raiz_discrim)) / (2 * a)
		raiz2=float((-b - raiz_discrim)) / (2 * a)
		if raiz1 == raiz2:
			print("O polinomio de coeficientes\
			a=%d b=%d c= %d tem raizes multiplas raiz1= raiz2=%3.2f " % (a,b,c,raiz1))
		else:
			print("As raizes do polinomio de coeficientes\
			a=%d b=%d c= %d sao raiz1=%3.2f raiz2=%3.2f" % (a,b,c,raiz1,raiz2))
	except ValueError:
		print("\n Nao tem raizes reais!")

def try_4(mensagem):
	try:
		print(mensagem)
	except:
		print('Algo correu mal')
	else:
		print('Boa. Tudo correu como previsto!')
		
def try_5():
	while True:
		try:
			x=eval(input('o numerador:'))
			y=eval(input('o denominador:'))
			res= x/y
			print('%d a dividir por %d = %d' % (x,y,res))
		except:
			print('Entrada inválida. Tente novamente.')
		else:
			break
		
		
def main():
	#quad_perfeito(99)
	# password2(password2(['ernesto','antunes','maria', 'anabela'])
	#try_4('olá')
	try_5()


if __name__ == '__main__':
	main()

