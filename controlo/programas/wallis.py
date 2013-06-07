def wallis_1(num_fact):
    """
    Calcula o valor de pi usando a fórmula de Wallis.
    """
    acum = 1.0
    for i in range(2, num_fact,2):
        esquerda = i / float((i-1))
        direita = i /float((i+1))
        acum = acum * esquerda * direita
    return 2 * acum

def wallis_2(num_fact):
    """
    Calcula o valor de pi usando a fórmula de Wallis.
    """
    acum = 1.0
    for i in range(1, num_fact/2):
        factor = float((2 * i) ** 2) / ((2 * i) ** 2 - 1)
        acum = acum * factor
    return 2 * acum

print(wallis_1(100))
print(wallis_1(1000))
print(wallis_1(10000))


print(wallis_2(100))
print(wallis_2(1000))
print(wallis_2(10000))