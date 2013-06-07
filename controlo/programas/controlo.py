"""Controlo."""

def ordena_3(x,y,z):
    """Ordena os três números por ordem crescente."""
    if (x <= y) and (x <= z):
        if y <= z:
            return (x,y,z)
        else:
            return (x,z,y)
    if (y <= x) and (y <= z):
        if x <= z:
            return (y,x,z)
        else:
            return (y,z,x)    
    if (z <= x) and (z <= y):
        if x <= y:
            return (z,x,y)
        else:
            return (z,y,x)  

def nota(e,t1,t2,t3,t4):
    """Calcula nota final."""
    nota = 0.075 * (t1 + t2 + t3 + t4) + 0.7 * e
    print(nota)
    if nota >= 14 :
        return "Aprovado"
    elif nota < 7:
        return "Reprovado"
    else:
        return "Oral"
        
# pergunta 3
import random 

def dados(tentativas):
    """Determina a percentagem de lançamentos que deram um número par."""
    conta = 0
    for i in range(tentativas):
        numero = random.randint(0,6)
        if numero % 2 == 0:
            conta = conta + 1
    return conta/tentativas        
        

# Divisor / primo

def menor_divisor(n):
    """Calcula 0 menor divisor do inteiro n > 1."""
    for i in range(2,n+1):
        if n%i == 0:
            return i
        
def primo(n):
    """Um número > 1 é primo?"""
    return menor_divisor(n) == n


# Fibonacci

def fib(n):
    """Calcula o número de Fibonacci de ordem n."""
    if n <= 2:
        return 1
    f_1 = 1
    f_2 = 1
    for i in range(3,n+1):
        f_1, f_2 = f_2,f_1 + f_2
    return f_2

def is_fib(n):
    """Determina se n é um número da sequência de fibonacci."""
    fib_ant = 0
    fib = 1
    while fib < n: 
        # next fib
        fib_ant, fib = fib, fib_ant + fib
    return fib == n

# Golomb self-describing sequence

def golomb(n):
    """Calcula o valor do enésimo elemewnto da sequência de Golomg."""
    # caso simples
    if n <= 2:
        return n
    num = 2
    val = 2
    while True:
        # Calcula seguinte
        if num >= n:
            return val
        num += (val - 1)
        val += 1
        
        
       
if __name__ == '__main__':
    #print(primo(100))
    #print(is_fib(8))
    for i in range(1,20):
        print(i,'\t',golomb(i))
    

    
        