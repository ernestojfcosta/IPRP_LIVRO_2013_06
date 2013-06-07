

# repete impressão
def mensagem(texto):
    """ Imprime o texto cinco vezes."""
    for i in range(5):
        print(texto)


# tabela de números

def imprime_tabela(numero):
    """ Tabela com os valores de numero, numero ^ 2."""
    print('Número\t\tQuadrado')
    for i in range(1,numero+1):
        print('%6d\t\t%8d' % (i, i**2))
    
# Desenhar IPRP

# take-off

def comprimento():
    """Calcula o tamanho da pista necessário para a descolagem."""
    vel = eval(input('Velocidade de descolagem (m/s): '))
    ace = eval(input('Aceleração para descolagem (m/s²): '))    
    comp = (vel**2) / (2*ace)
    print('Para a velocidade %3.2f e aceleração %3.2f o comprimento mínimo da pista é: %5.2f.' % (vel,ace,comp))
               
# temperatura                
def temperatura():
    """Calcula o valor da temperatura exterior em função do vento."""
    vel = eval(input('Velocidade do vento (milhas/hora): '))
    temp = eval(input('Temperatura (Fashrenheit [-58, 41]): '))    
    
    res = 35.74 + 0.6215 * temp - 35.75 * (vel**0.16) + 0.4275 * temp * (vel ** 0.16)
    
    print('Para a velocidade do vento %3.2f e temperatura exterior %3.2f a temperatura é sentida conmo: %5.2f.' % (vel,temp,res))  


# energia               
def energia():
    """Calcula o valor da energia necessária para variar a temperatura da água."""
    t_i = eval(input('Temperatura inicial  (Celcius): '))
    t_f = eval(input('Temperatura final (Celcius): '))  
    m = eval(input('Quantidade de água (Quilogramas): ')) 
    
    e = m * (t_f - t_i) * 4184
    
    print('Para a massa de água %3.2f, temperatura inicial %3.2f e temperatura final %3.2f a energia necessária é: %10.2f Joules.' % (m,t_i,t_f,e))  

# constrói acrónimo
def acronimo(cadeia):
    """Constrói o acrónimo a partir de uma frase representada por uma cadeia de caracteres."""
    acro = ''
    inicio = True
    for car in cadeia:
        if inicio == True:
            acro = acro + car.upper()
            inicio = False
        elif car == ' ':
            inicio = True
    return acro

# Tabuada
def tabuada(n):
    """Imprime a tabela da tabuada do númeron."""
    print('Tabuada do número  %d' % n)
    print('-'*30)
    for i in range(1,11):
        print('7\tx\t%4d\t=%4d' % (i,i*n))


# Imprime
"""
print(format('Bem vindo a IPRP', '20s'))
print(format('Bem vindo a IPRP', '<20s'))
print(format('Bem vindo a IPRP', '>20s'))
print(format('Bem vindo a IPRP e ao DEIUC', '>20s'))
"""
# mostra matriz

def mostra_matriz(matriz):
    """imprime os elementos de uma matriz de modo organizado."""
    print()
    for j,linha in enumerate(matriz):
        for i,coluna in enumerate(linha):
            print('(%d,%d): %d\t' % (j,i,coluna), end='')
        print()

# Estimar a população
def estima(pop):
    """Ao fim de um ano qual o novo valor da população."""
    nasce = eval(input('Frequência de nascimentos (minutos): '))
    morre = eval(input('Frequência de falecimentos (minutos): '))
    emigra = eval(input('Frequência de emigração (minutos): '))
    
    total_minutos = 365 * 24 * 60
    
    nascimentos_ano = total_minutos // nasce
    mortes_ano = total_minutos // morre
    emigrantes_ano = total_minutos // emigra
    
    final_ano = pop + nascimentos_ano - mortes_ano - emigrantes_ano
    print('Resumo dos dados:')
    print('-----------------')
    print('Frequência de nascimentos: %d\nFrequência de mortes: %d\n\
    Frequência de emigrantes:%d\nPopulação Inicial:%d'%(nasce,morre, emigra, pop))
    print('Estimativa:')  
    print('-----------')
    print('A população ao fim de um ano: %d' %final_ano)
    
    
                          
    
    
    
    
    
    
if __name__ == '__main__':
    pass
    #print(acronimo('Random Acess Memory'))
    #imprime_tabela(5)
    #comprimento()
    #temperatura()
    #energia()
    #tabuada(7)
    #mat = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    #mostra_matriz(mat)
    estima(10e6)