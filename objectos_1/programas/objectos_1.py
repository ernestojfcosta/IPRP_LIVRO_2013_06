"""Objectos_1."""

# max de acordo com função
import random 

def meu_max(elementos,funcao):
    """qual o maior elemento de acordo com a funcao."""
    valores = (funcao(elem) for elem in elementos)
    return max(valores)

if __name__ == '__main__':
    lista = [random.randint(1,100) for i in range(10)]
    print(lista)
    funcao = lambda x: x
    print(meu_max(lista,funcao))
    