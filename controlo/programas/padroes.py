def padrao_1(n):
    """ Imprime linhas de números entre 1 e n."""
    comp = len(str(n))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=comp*' ')
        print()

def padrao_2(n):
    """ Imprime linhas de números entre 1 e n, com n<100."""
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()
 
def padrao_3(n):
    """ Imprime linhas de números entre 1 e n, com n<100."""
    for i in range(1,n+1):
        print(end=(n-i)*'  ')
        for j in range(i,0,-1):
            print(j,end=' ')
        print()        
        
if __name__ == '__main__':
    padrao_1(5)
    print()
    padrao_2(5)
    print()
    padrao_3(5)    
    
    
    