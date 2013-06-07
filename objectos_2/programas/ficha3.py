def adiciona_a(elem, lista):
    """
    Adiciona o elem ao fim da lista.
    """
    return lista + [elem]


def adiciona_b(elem, lista):
    """
    Adiciona o elem ao fim da lista.
    """
    return lista.append(elem)

def adiciona_c(elem, lista):
    """
    Adiciona o elem ao fim da lista.
    """
    lista.append(elem)
    return lista

if __name__ == '__main__':
    """
    minha_lista = [1,2,3]
    print 'a' * 10
    print adiciona_a(1, minha_lista)
    print minha_lista
    print adiciona_a(adiciona_a(1,minha_lista),adiciona_a(1,minha_lista))
    print minha_lista
    print adiciona_a(1,1)


    print 'b' * 10
    minha_lista = [1,2,3]
    print adiciona_b(1, minha_lista)
    print minha_lista
    print adiciona_b(adiciona_b(1,minha_lista),adiciona_b(1,minha_lista))
    print minha_lista
    print adiciona_b(1,1)
    """
    print('c' * 10)
    minha_lista = [1,2,3]
    print(adiciona_c(1, minha_lista))
    print(minha_lista)
    print(adiciona_c(adiciona_c(1,minha_lista),adiciona_c(1,minha_lista)))
    print(minha_lista)
    print(adiciona_c(1,1))
