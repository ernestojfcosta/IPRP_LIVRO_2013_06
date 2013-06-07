def inter_all(l1,l2): 
    if l1 == []:
        return [l2] 
    elif l2 == []:
        return [l1] 
    else:
        aux1= [[l1[0]] + temp for temp in inter_all(l1[1:], l2)] 
        aux2= [[l2[0]] + temp for temp in inter_all(l1, l2[1:])] 
        return aux1 + aux2
    
if __name__ == '__main__':
    lista_1 = [1,2,3]
    lista_2 = ['a','b','c']
    print(inter_all(lista_1, lista_2))