#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
ficha 4.py

Created by Ernesto Costa on 2008-10-08.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os
from random import *

# Exercício 4.1

def par_impar(num):
	if (num % 2) == 0 :
		print('Par')
	else: 
		print('Ímpar')
		
		
# Exercicio 4.2

def duplica_car(cadeia):
	cad = ''
	for car in cadeia:
		cad = cad + 2 * car
	return cad
	
	
# Exercicio 4.3

def jogo():
	dado1=randint(1,6)
	dado2=randint(1,6)
	if dado1 == dado2:
		return True
	else:
		return False

# Exercicio	 4.4 
	
def jogo2(n):
	for i in range(n):
		print("Jogada %d deu %s." % (i+1, jogo()))
	return 'Fim'

# Exercicio 4.5 

def jogo3(n):
	joga='A'
	contaA=0
	contaB=0
	for i in range(n):
		if jogo():
			if joga=='A':
				contaA=contaA + 1
				joga='B'
			else:
				contaB=contaB + 1
				joga='A'
	if contaA > contaB:
		venc='A'
	elif contaB > contaA:
		venc='B'
	else:
		venc='Ninguém'
		
	print('O jogador A ganhou %d jogos \nO jogador B ganhou %d jogos.' % (contaA,contaB))
	print('O vencedor foi %s' % venc)
	return 0

	
# Exercicio 4.6

def fact(n):
	if n == 0:
		return 1
	else:
		res = 1
		for i in range(1,n+1):
			res = res * i
		return res
		
# Exercício 4.7

def euler(aprox):
	res=1
	conta=0
	while True:
		conta = conta + 1
		aux= res + (1.0 / fact(conta))
		if (aux - res) < aprox:
			break
		else:
			res = aux
	return aux

# Exercicio 4.8 

def mistura(nomes, numeros):
	res=[]
	for i in range(len(nomes)):	
		res.append([nomes[i],numeros[i]])
	return res	

# Exercicio 4.9

def assoc(lista,nome):
	for i in range(len(lista)):
		if lista[i][0] == nome:
			return lista[i][1]
	return 'nome inexistente'

# Exercício 4.10

def codoes(s):
	""" Devolve a lista de codões a partir
	de uma sequência. A sequência é percorrida em grupos de três
	enquanto é possível"""
	cod = [s[i:i+3] for i in range(0,len(s),3)]
	return cod
	
	
# Exercício 4.11 

def troca(lista, ind1, ind2):
    if ind1==0:
        return lista[ind2::-1] + lista[ind2+1:]
    else:
        return lista[:ind1] + lista[ind2:ind1-1:-1] + lista[ind2+1:]


# Exercicio 4.12

def euro(chave_num,chave_est):
	# Gera 5 numeros
	num_sol=[]
	for i in range(5):
		num=randint(1,50)
		while num in num_sol:
			num=randint(1,50)
		num_sol.append(num)
	# Gera 2 estrelas
	est_sol=[]
	for i in range(2):
		num=randint(1,9)
		while num in est_sol:
			num=randint(1,9)
		est_sol.append(num)
	# Conta numeros certos
	conta_num=0
	for i in range(5):
		if chave_num[i] in num_sol:
			conta_num= conta_num +1
	conta_est=0
	for i in range(2):
		if chave_est[i] in est_sol:
			conta_est=conta_est +1
	return (conta_num, conta_est)


# Exercício 4.13

def chave(l1):
	return l1[1]
	

def ordena_lista1(lista):
	lista.sort(key=chave)
	return lista

# Exercício 4.14

def lista_tel(fich):
	fin=open(fich,'r')
	dicio={}
	for linha in fin:
		c,v=linha.replace('\n','').split()
		dicio[c]=int(v)
	return dicio
	

# Exercício 4.15

def complementa(bp):
	"""Encontra o complemento de uma sequência"""
	complemento_bases= {'A':'T','G':'C','T':'A','C':'G'}
	temp = [complemento_bases[base] for base in bp]
	return ''.join(temp)

# --- Variante

def complementa2(bp):
	complemento_bases= {'A':'T','G':'C','T':'A','C':'G'}
	aux=''
	for i in range(len(bp)):
		aux = aux + complemento_bases[bp[i]]
	return aux			

# Exercício 4.16
	
def converte(l_codoes):
	"""Converte uma lista de codões
	na sequência de aminoácidos"""
	amino={
		'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
		'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
		'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
		'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',

		'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
	    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
		'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
		'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',

		'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
		'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
		'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
		'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',

		'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
		'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
		'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
		'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
		    }
	return ''.join([amino[codao] for codao in l_codoes])

# Exercício 4.17

def amino_3_to_1(l_amino):
	"""converte uma sequência de amino de três letras
	para uma letra.
	"""	
	tres_um={"GLY" : "G", "ALA" : "A", "LEU" : "L", "ILE" : "I",
	        "ARG" : "R", "LYS" : "K", "MET" : "M", "CYS" : "C",
	        "TYR" : "Y", "THR" : "T", "PRO" : "P", "SER" : "S",
	        "TRP" : "W", "ASP" : "D", "GLU" : "E", "ASN" : "N",
	        "GLN" : "Q", "PHE" : "F", "HIS" : "H", "VAL" : "V"}
	amino_1=''
	for amino_acid in l_amino:
			amino_1 = amino_1 + tres_um[amino_acid]
	return amino_1

# Exercício 4.18

# inverte papel chaves e valores

def converte_1_3(dicio):
	chaves=list(dicio.keys())
	valores= list(dicio.values())
	d=dict(list(zip(valores,chaves)))
	return d
	

def amino_1_to_3(l_amino):
		"""converte uma sequência de amino de três letras
		para uma letra.
		"""	
		tres_um={"GLY" : "G", "ALA" : "A", "LEU" : "L", "ILE" : "I",
		        "ARG" : "R", "LYS" : "K", "MET" : "M", "CYS" : "C",
		        "TYR" : "Y", "THR" : "T", "PRO" : "P", "SER" : "S",
		        "TRP" : "W", "ASP" : "D", "GLU" : "E", "ASN" : "N",
		        "GLN" : "Q", "PHE" : "F", "HIS" : "H", "VAL" : "V"}
		um_tres=converte_1_3(tres_um)
		amino_1=''
		for amino_acid in l_amino:
				amino_1 = amino_1 + '-' + um_tres[amino_acid]
		return amino_1[1:]
			
# Exercício 4.19

def converte2(l_codoes):
	"""Converte uma lista de codões na sequência de aminoácidos"""
	amino={
	'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
	'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
	'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
	'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
	
	'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
	'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
	'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
	'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
	
	'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
	'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
	'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
	'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
	
	'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
	'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
	'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
	'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
	}
	start='AUG'
	stop = ['UAA','UAG','UGA']
	res=''
	indice=l_codoes.index(start) # procura start
	for ind in range(indice+1,len(l_codoes)+1):
		if l_codoes[ind] in stop:
			break
		else:
			res = res + amino[l_codoes[ind]]
	return res

# Exercício 4.20

def troca(dicio):
	"""Troca o papel das chaves e dos valores num dicionário."""
	novo=[(val,ch) for ch,val in list(dicio.items()) ]
	novo_dicio={}
	for i in range(len(novo)):
		novo_dicio[novo[i][0]]=novo[i][1]
	return novo_dicio
	
def troca1(dicio):
	chaves=list(dicio.keys())
	valores= list(dicio.values())
	d=dict(list(zip(valores,chaves)))
	return d
	
def troca2(dicio):
	novo_dicio={}
	for c,v in dicio.items():
		novo_dicio[v]=c
	return novo_dicio	
	
	
# Exercício 4.21

from xturtle import *

def tri(tamanho,angulo,cor):
	pd()
	color(cor)
	for i in range(3):
		forward(tamanho)
		left(angulo)
	hideturtle()

def tri_tri():
	tri(60,120,'red')
	fd(60)
	tri(60,-120,'green')
	fd(60)
	tri(60,120,'blue')
	input('enter para terminar')
	
# Exercício 4.22

def move_objecto(raio, cor,pos,dist):
	pu()
	posx=pos[0]
	posy=pos[1]
	goto(posx,posy)
	pd()
	ht()
	speed(1)
	for i in range(dist):
		# desenha
		dot(raio,cor)
		# espera
		delay(250)
		delay(0)
		# apaga
		clear()
		# muda posição
		pu()
		posx= posx + 5
		#posy= posy+1
		goto(posx,posy)
		pd()
		pass
	input('Prima uma tecla para terminar')


			
			
		
def main():
	#jogo3(500)
	#print ordena_lista1([['ernesto', 60],['anabela', 36],['patricia', 44],['jp', 3],['daniela', 40]])
	#print lista_tel('/tempo/telefones.txt')
	"""print converte_1_3({"GLY" : "G", "ALA" : "A", "LEU" : "L", "ILE" : "I",
	        "ARG" : "R", "LYS" : "K", "MET" : "M", "CYS" : "C",
	        "TYR" : "Y", "THR" : "T", "PRO" : "P", "SER" : "S",
	        "TRP" : "W", "ASP" : "D", "GLU" : "E", "ASN" : "N",
	        "GLN" : "Q", "PHE" : "F", "HIS" : "H", "VAL" : "V"})"""

	#print amino_1_to_3('GRTDV')
	#print converte2(['AAG','AUG','GAC','UCG','UAA','AUU'])
	"""print '0 -----'
	print troca({1:'um',2:'dois',3:'tres'})
	print '1 -----'
	print troca1({1:'um',2:'dois',3:'tres'})
	print '2 -----'	
	print troca2({1:'um',2:'dois',3:'tres'})"""
	move_objecto(20,'red',(0,0),50)




if __name__ == '__main__':
	main()

