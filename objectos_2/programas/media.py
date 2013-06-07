def media(lista):
    """ Calcula a média dos valores contidos na lista."""
    soma = 0
    for num in lista:
        soma += num
    med = soma / len(lista)
    return med

def media(lista):
    """ Calcula a média dos valores contidos na lista."""
    return sum(lista)/len(lista)

if __name__ == '__main__':
    lst = [1,2,3,4,5,6]
    print(media(lst))
    