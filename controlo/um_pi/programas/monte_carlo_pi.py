import math
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
        d = math.sqrt(x**2 + y**2)
        if d <= 1:
            conta_dardos_in = conta_dardos_in + 1
    res_pi = 4 * (conta_dardos_in/float(num_dardos))
    return res_pi

print monte_carlo_pi(1000)

print monte_carlo_pi(100000)