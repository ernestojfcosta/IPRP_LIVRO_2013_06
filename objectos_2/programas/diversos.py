import inspect

def this_list():
    import sys
    d = inspect.currentframe().f_locals
    return d
    
def inverte_dicio(dicio):
    """troca chaves com valores."""
    return dict(list(zip(list(dicio.values()),list(dicio.keys()))))


if __name__ == '__main__':
    #print(this_list())
    d = {'a':1,'b':2}
    print((inverte_dicio(d)))
    
    