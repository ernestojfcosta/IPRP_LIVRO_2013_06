# Aula 9 - TP 9/10

def ler_dados(n,inf,sup):
    lista =[]
    while len(lista) < n:
        num = input('entre [%d,%d]: ' %  (inf,sup))
        if num >= inf and num <= sup:
            lista.append(num)
        else:
            print 'ERRO: nœmero fora do intervalo! '
    return lista


def ler_dados_rep(n,inf,sup):
    lista =[]
    while len(lista) < n:
        num = input('entre [%d,%d]: ' %  (inf,sup))
        
        if num in lista:
            print 'Nœmero j‡ existe!'
        elif num >= inf and num <= sup:
            lista.append(num)
        else:
            print 'ERRO: nœmero fora do intervalo! '
    return lista


import random

def pares(n,homens,mulheres):
    lista_h = []
    lista_m = []
    for i in range(n):
        h = random.choice(homens)
        while h in lista_h:
            h = random.choice(homens)
        lista_h.append(h)
        
        m = random.choice(mulheres)
        while m in lista_m:
            m = random.choice(mulheres)
        lista_m.append(m)
    pares_h_m = zip(lista_h,lista_m)
    return pares_h_m
    
def escolhe_p(pessoas,lista_p):
    p = random.choice(pesoas)
    while p in lista_p:
        p = random.choice(pessoas)
    lista_p.append(p)
    return lista_p

def  pares_fich(n,fich_h, fich_m):
    f_h = open(fich_h,'r')
    homens = f_h.read().split('\n')
    f_h.close()
    
    f_m = open(fich_m,'r')
    mulheres = f_m.read().split('\n')
    f_m.close()
    
    res = pares(n, homens,mulheres)
    return res

def dicio_freq(seq):
    dic ={}
    for i in range(len(seq)):
        if seq[i] in dic.keys():
            dic[seq[i]] = dic[seq[i]] + [i]
        else:
            dic[seq[i]] = [i]
    return dic

def dicio_freq(seq):
    dic ={}
    for i,elem in enumerate(seq):
        if elem in dic.keys():
            dic[elem] = dic[elem] + [i]
        else:
            dic[elem] = [i]
    return dic
    
if __name__=='__main__':
    #print ler_dados_rep(3,8,20)
    #print pares(2,['toto','tata','titi'],['tete','tutu','ahah'])
    #print pares_fich(3,'homens.txt','mulheres.txt')
    print dicio_freq('abacadabracc')