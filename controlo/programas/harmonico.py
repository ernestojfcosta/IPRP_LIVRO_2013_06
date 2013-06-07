import matplotlib.pyplot as plt
import math

def harmonico_0(n):
    h_n = 0
    for k in range(n,0,-1):
        h_n += (1/k)
    return h_n

def harmonico(n):
    h_n = 0
    for k in range(1,n+1):
        h_n += (1/k)
    return h_n

def harmonia(n):
    serie = ()
    for i in range(1,n+1):
        serie += (harmonico(i),)
    return serie

def harmonia_b(n):
    serie = ()
    for i in range(1,n+1):
        serie += (harmonico_b(i),)
    return serie

def harmonico_c(n):
    """Melhora a precisão."""
    return math.fsum([1/k for k in range(1,n+1)])

def harmonico_b(n):
    return math.log(n) + 0.5772156649


if __name__ == '__main__':
    print((harmonico(100000)))
    print((harmonico_b(100000)))
    print((harmonico_c(100000)))
    print((harmonico_0(100000)))
    """
    valores_a = harmonia(30)
    valores_b = harmonia_b(30)
    #----
    plt.xlabel('n')
    plt.ylabel('$H_n$')
    plt.title('Números Harmónicos')
    plt.plot(valores_a, label='Fórmula')
    plt.plot(valores_b, label='Aproximado')
    plt.legend(loc=0)
    plt.show()
    """
    