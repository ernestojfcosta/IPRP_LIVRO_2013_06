def arv_bin_proc(lista): 
    if lista == []:
        return lista 
    else:
        pivot=lista[0]
        esq= [elem for elem in lista if elem < pivot]
        dir= [elem for elem in lista if elem > pivot]
        return [pivot,[arv_bin_proc(esq)],[arv_bin_proc(dir)]]
    
if __name__ == '__main__':
    lista = [6,3,10,2,6,5,4,1,7,8,9]
    print(arv_bin_proc(lista))