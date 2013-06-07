def prefixos(cadeia):
    
    conta = 0
    while conta < len(cadeia):
        print(cadeia[:conta+1])
        conta = conta + 1
        
def prefixos_b(cadeia):
    conta = len(cadeia)
    while conta > 0:
        print(cadeia[:conta])
        conta = conta -1



def sufixos(cadeia):
    conta = 0
    while conta < len(cadeia):
        print(cadeia[- (conta + 1):])
        conta = conta + 1

def em(primeira,segunda):
    indice = 0
    comp_p = len(primeira)
    comp_s = len(segunda)
    while indice < comp_s - comp_p + 1:
        if encontra(primeira, segunda[indice:indice + comp_p]) :
            return indice
        indice = indice + 1
    return -1

def encontra(cad_1,cad_2):
    return cad_1 == cad_2


        
if __name__ == '__main__':
    #prefixos('programming')
    #prefixos_b('programming')
    sufixos('programming')
    #print em('mong', 'programming')
    
        
        
