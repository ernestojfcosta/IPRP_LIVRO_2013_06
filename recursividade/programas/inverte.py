def inverte3(seq): 
    if len(seq) == 1:
        return seq 
    meio= len(seq)//2
    return inverte3(seq[meio:]) + inverte3(seq[:meio])


if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8,9]
    print(inverte3(lista))