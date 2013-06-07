def aplana(lista):
    """Transforma uma lista de lista numa lista simples."""
    res = []
    for lst in lista:
        for elem in lst:
            res.append(elem)
    return res

def aplana_lc(lista):
    """Transforma uma lista de lista numa lista simples."""
    res = [val for elem in lista for val in elem]
    return res


def elimina_dup(lista):
    """Elimina duplicados de uma lista sem respeitar a ordem."""
    lista_ord = lista[:]
    lista_ord.sort()
    return [val for ind,val in enumerate(lista_ord) if not ind or val!= lista_ord[ind - 1]]

if __name__ == '__main__':
    minha_lista = [[1,2,3],[4,5],[6]]
    print(aplana(minha_lista))
    #print(aplana_lc(minha_lista))
    #lista_2 = [1,7,5,2,9,1,5,7,9,9,1]
    #print(elimina_dup(lista_2))
    
    
        