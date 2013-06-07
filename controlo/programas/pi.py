def leibniz_pi(num_termos):
    """ 
    Calcula valor de pi segundo fórmula de Leibniz.
    """
    acum = 0.0
    den = 1
    for i in range(num_termos):
        acum = acum + (1.0/den) * (-1)**i
        den = den +2
    return 4 * acum


if __name__ == '__main__':
    print((leibniz_pi(1000000)))