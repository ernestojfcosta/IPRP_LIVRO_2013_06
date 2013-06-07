

def matriz_t(matriz):
    res = list(zip(*matriz))
    res = [list(elem) for elem in res]
    return res


if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(matriz_t(mat))