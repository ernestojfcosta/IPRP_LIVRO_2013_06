def exec5(seq):
    for i in range(len(seq)):
        print((seq[i]))
        
def padrao_1(n):
    acum = 0
    for val in range(1,n+1):
        acum = acum + val
    return acum

def padrao(objecto):
    acum = func_0()
    for val in func_1(objecto):
        acum = func_2(acum, val)
    return acum

if __name__ == '__main__':
    exec5('abc')
    print((padrao_1(4)))
    
    