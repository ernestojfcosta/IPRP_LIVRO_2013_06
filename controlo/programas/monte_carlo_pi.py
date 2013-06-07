import random

def monte_carlo_pi(num_dardos):
    """
    Calcula o valor de pi pelo método de monte Carlo.
    """
    # define e inicializa acumulador
    conta_dardos_in = 0.0
    for i in range(num_dardos):
        # gera posição dardo i
        x= random.random()
        y= random.random()
        # calcula distância à origem
        d = (x**2 + y**2)**0.5
        if d <= 1:
            conta_dardos_in = conta_dardos_in + 1
    res_pi = 4 * (conta_dardos_in/num_dardos)
    return res_pi

if __name__ == '__main__':
    print((monte_carlo_pi(1000)))
    print((monte_carlo_pi(10000000)))