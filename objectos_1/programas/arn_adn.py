#-*- coding: utf-8 -*-

from string import *

def cadeia_dupla(arn):
	"""A partir da cadeia de ARN construir a dupla cadeia
	de ADN correspondente"""
	bases_adn='ATCG'
	bases_arn='AUCG'
	bases_comp='TAGC'
	adn=''
	adn2=''
	for base in arn:
		indice_arn= find(bases_arn,base)
		adn= adn + bases_adn[indice_arn]
		adn2= adn2 + bases_comp[indice_arn]
	return arn,(adn,adn2)

print(cadeia_dupla('AUUGCUUAA'))
