def leibniz_pi_1(num_termos):
    """ Calcula valor de pi segundo fórmula de Leibniz.
    """
    conta = 0
    acum = 0.0
    den = 1
    while conta < num_termos:
        acum = acum + (1.0/den) * (-1)**conta
        den = den +2
        conta = conta + 1
    return 4 * acum


def leibniz_pi_2(num_termos):
    """ Calcula valor de pi segundo fórmula de Leibniz.
    """
    acum = 0.0
    den = 1
    for i in range(num_termos):
        acum = acum + (1.0/den) * (-1)**i
        den = den +2
    return 4 * acum

def leibniz_pi_3(num_termos):
    """ Calcula valor de pi segundo fórmula de Leibniz.
    """
    acum = 0.0
    for i in range(num_termos):
        acum = acum + ((-1)**i) * (1.0/(2 * i + 1))  
    return 4 * acum

print leibniz_pi_1(500)

print leibniz_pi_1(1500)

print leibniz_pi_2(500)

print leibniz_pi_2(1500)

print leibniz_pi_3(500)

print leibniz_pi_3(1500)