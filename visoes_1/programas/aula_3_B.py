

def prefixos(cadeia):
    """Determina todos os prefixos de uma cadeia de caracteres.
    """
    conta = 0
    while conta < len(cadeia):
        print(cadeia[:conta+1])
        conta = conta + 1
        
def prefixos_b(cadeia):
    conta = 0
    while conta  < len(cadeia):
        print(cadeia[: len(cadeia)-conta])
        conta = conta + 1
    
def pref(cadeia):
    for conta in range(len(cadeia)):
        print(cadeia[:conta+1])
        
def conta_base(base, cadeia_adn):
    conta = 0
    conta_base = 0
    while conta < len(cadeia_adn):
        if base == cadeia_adn[conta]:
            conta_base = conta_base +1
        conta = conta + 1
    return conta_base

def conta_base_b(base, cadeia_adn):
    conta_base = 0
    for conta in range(len(cadeia_adn)):
        if base == cadeia_adn[conta]:
            conta_base = conta_base + 1
    return conta_base
import random 

def gera_adn(num):
    adn= ''
    for conta in range(num):
        base = random.choice('ATCG')
        adn = adn + base
    return adn

def percent_base(base, cadeia_adn):
    conta = conta_base(base, cadeia_adn)
    return float(conta)/len(cadeia_adn)

def tira_vogais(cadeia):
    """Retira as vogais e substitui por um espaço em branco.
    """
    vogais ='aeiou'
    nova_cadeia =''
    for conta in range(len(cadeia)):
        if cadeia[conta] in vogais:
            nova_cadeia = nova_cadeia + ' '
        else:    
            nova_cadeia = nova_cadeia + cadeia[conta]
    return nova_cadeia

def tira_vogais_b(cadeia):
    """Retira as vogais e substitui por um espaÃ§o em branco.
    """
    vogais ='aeiou'
    nova_cadeia =''
    for car in cadeia:
        if car in vogais:
            nova_cadeia = nova_cadeia + ' '
        else:    
            nova_cadeia = nova_cadeia + car
    return nova_cadeia   
    
if __name__ == '__main__':
    #prefixos_b('programming')
    #print conta_base_b('Z','AACTCGCTTATA')
    #print gera_adn(50)
    #print percent_base('A','ATTATCGA')
    print(tira_vogais_b('asldfksdlfeiopip'))
    
    
    