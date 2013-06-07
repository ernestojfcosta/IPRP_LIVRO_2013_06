# Aula 9 - TP 10

def ler_dados(n,inf,sup):
    lista = []
    while len(lista) < n:
        num = input('Nœmero no intervalo [%d,%d]: ' % (inf, sup))
        if num >= inf and num <= sup:
            lista.append(num)
        else:
            print 'Nœmero fora do intervalo [%d,%d]!!!' % (inf, sup)
    return lista

def ler_dados_rep(n,inf,sup):
    lista = []
    while len(lista) < n:
        num = input('Nœmero no intervalo [%d,%d]: ' % (inf, sup))
        if num in lista:
            print 'Nœmero repetido'
        elif num >= inf and num <= sup:
            lista.append(num)
        else:
            print 'Nœmero fora do intervalo [%d,%d]!!!' % (inf, sup)

    return lista
import random
def pares(n, homens,mulheres):
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
    lista_p = zip(lista_h,lista_m)
    return lista_p

h = ['toto','tata','ohoh']
m = ['titi','tutu','ahah']


def pares_fich(n,fich_h,fich_m):
    f_h = open(fich_h,'r')
    homens = f_h.read().split('\n')
    f_h.close()
    
    f_m = open(fich_m,'r')
    mulheres = f_m.read().split('\n')
    f_m.close()
    
    return pares(n,homens, mulheres)

    
if __name__ =='__main__':
    #print ler_dados(3,10,35)
    print pares_fich(3,'homens.txt','mulheres.txt')
    