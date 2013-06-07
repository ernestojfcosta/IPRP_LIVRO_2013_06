def perfeito(n):
    return n == sum(divisores(n))

def divisores(n):
    res = ()
    for i in range(1,n//2+1):
        if (n % i) == 0:
            res += (i,)
    return res

def perfeitos(inf,sup):
    for i in range(inf,sup+1):
        if perfeito(i):
            print(i)

if __name__ == '__main__':
    perfeitos(1,1000)
    