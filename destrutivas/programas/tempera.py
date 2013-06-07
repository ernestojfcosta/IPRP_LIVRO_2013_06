# -*- coding: utf-8 -*-

from pylab import *

def ler(fich):
    """lê ficheiro e devolve lista dos valores encontrados
    em cada linha. """
    f_in = open(fich,'r')
    dados = []
    for linha in f_in:
        dados.append(int(linha[:-1]))
    return dados

def main(fich):
    dados = ler(fich)
    plot(dados)
    show()
    
if __name__ == '__main__':
    main('/tempo/temp.txt')
    