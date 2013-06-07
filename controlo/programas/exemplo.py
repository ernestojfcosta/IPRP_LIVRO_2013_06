import random

def gera_cadeia(alfabeto,tamanho):
    cadeia =''
    for i in range(tamanho):
        simbolo = random.choice(alfabeto)
        cadeia += simbolo
    return cadeia
    
def conta_modelo(cadeia, modelo):
    conta = 0
    sobreposicao = len(modelo) - 1
    while len(cadeia) > sobreposicao:
        if cadeia.startswith(modelo):
            conta += 1
        cadeia = cadeia[1:]
    return conta


if __name__ == '__main__':
    cadeia = gera_cadeia('ATCG',10000)
    print((conta_modelo(cadeia,'TATA')))
    
    
    
