import math

def area_tri(base, altura):
    """Calcula a área de um triângulo conhecida a sua base e a altura."""
    return 1/2 * base * altura

def area_tri_b(lado_1, lado_2,angulo):
    """Calcula a área de um triângulo conhecido dois dos seus lados e o respectivo ângulo."""
    return 1/2 * lado_1 * lado_2 * math.sin(angulo)



if __name__ == '__main__':
    print(area_tri(5,7))