"""Capítulo 3."""
import random
import math

# matemáticos....

def bate_cardiaco(idade):
    """O batimento cardíaco aproximado em função da idade."""
    return 208 - 0.7 * idade

def bate_card_max(idade):
    """O batimento cardíaco aproximado em função da idade."""
    return 163 + 1.16 * idade - 0.018 * (idade **2)    


def ganhos(inicial, taxa_juro, tempo):
    """
    Calcula o valor obtido ao fim de um nºúmero de anos tempo
    partindo do valor inicial e de uma taxa de juro.
    """
    return inicial * (1 + taxa_juro)** tempo


def max_elem_1(elementos,funcao):
    """Qual o elemento de maior valor de acordo com a função."""
    # Inicializa
    melhor_valor = None
    melhor_elem = None
    # Testa e actualiza
    for elem in elementos:
        valor = funcao(elem)
        if melhor_valor == None or valor > melhor_valor:
            # actualiza
            melhor_valor = valor
            melhor_elem = elem
    return melhor_elem
            

def max_elem_2(elementos,funcao):
    """Qual o elemento de maior valor de acordo com a função."""
    # Inicializa
    melhor_elem = elementos[0]
    melhor_valor = funcao(melhor_elem)
    # Testa e actualiza
    for elem in elementos[1:]:
        valor = funcao(elem)
        if valor > melhor_valor:
            # actualiza
            melhor_valor = valor
            melhor_elem = elem
    return melhor_elem    
    
    
def max_elem_3(elementos,funcao):
    """Qual o elemento de maior valor de acordo com a função."""
    return max(elementos,key=funcao)


def max_elem_4(elementos,funcao):
    """Qual o elemento de maior valor de acordo com a função."""
    valores = (funcao(elem) for elem in elementos)
    return max(elementos,key=funcao)
       
    
def max_elem_valor_1(elementos,funcao):
    """Devolve o elemento de valor máximo e o rspectivo valor."""
    # Inicializa
    melhor_elem = elementos[0]
    melhor_valor = funcao(melhor_elem)
    # Testa e actualiza
    for elem in elementos[1:]:
        valor = funcao(elem)
        if valor > melhor_valor:
            # actualiza
            melhor_valor = valor
            melhor_elem = elem
    return melhor_elem, melhor_valor     


def max_elem_valor_2(elementos,funcao):   
    """Qual o elemento de maior valor de acordo com a função."""
    melhor_elem = max(elementos,key=funcao) 
    melhor_valor = funcao(melhor_elem)
    return melhor_elem, melhor_valor

def quadrado(x):
    return x ** 2


    
# Biologia

def gera_adn(tam):
    """Gera uma cadeia de ADN de tamnho tam."""
    return ''.join([random.choice('TACG') for i in range(tam)])

def gera_adn_b(tam):
    """Gera uma cadeia de ADN de tamnho tam."""
    arn =''
    for i in range(tam):
        base = random.choice('TACG')
        arn = arn + base
    return arn

def transcreve(adn):
    """Tranforma o ADN em ARN."""
    return adn.replace('T','U')

def transcreve_b(adn):
    """Tranforma o ADN em ARN."""
    adn = adn.upper()
    return adn.replace('T','U')

def gene_pos(arn):
    """Indica a posição do início do primeiro gene na cadeia de ARN."""
    return arn.find('AUG')

def gene_pos(arn, pos):
    """Indica a posição do início do primeiro gene na cadeia de ARN,
    a partir da posição pos."""
    return arn.find('AUG',pos)

def gene_todos(arn):
    """Imprime a posição do início de todos os genes da cadeia de ARN."""
    pos = arn.find('AUG',0)
    while pos != -1:
        print(pos)
        pos = arn.find('AUG',pos+1)
        

def complemento(adn):
    """Fabrica o comolemento da cadeia de ADN."""
    bases = 'TACG'
    par = 'ATGC'
    comp = ''
    for base in adn:
        indice = bases.index(base)
        comp = comp + par[indice]
    return comp
    
    

# Criptografia

def encripta(texto_normal):
    """Encriptação por separação dos caracteres nas posições pares
    e nas posições ímpares."""
    comp = len(texto_normal)
    # caracteres nas posições pares
    car_pares = ""
    for i in range(0,comp,2):
        car_pares = car_pares + texto_normal[i] 
    # caracteres nas posições ímpares
    car_impares = ""
    for i in range(1,comp,2):
        car_impares = car_impares + texto_normal[i]   
    # junta tudo
    texto_encriptado = car_impares + car_pares
    return texto_encriptado

def encripta(texto_normal):
    """Encriptação por separação dos caracteres nas posições pares
    e nas posições ímpares."""
    car_pares = ""
    car_impares = ""
    car_conta = 0
    for car in texto_normal:            
        if car_conta % 2 == 0: # par ou ímpar?         
            car_pares = car_pares + car
        else:
            car_impares = car_impares + car
        car_conta = car_conta + 1
    texto_encriptado = car_impares + car_pares
    return texto_encriptado

def encripta_a(texto_normal):
    """Encriptação por separação dos caracteres nas posições pares
    e nas posições ímpares."""
    comp = len(texto_normal)
    car_pares = ""
    car_impares = ""
    for indice in range(comp):            
        if indice % 2 == 0: # par ou ímpar?         
            car_pares = car_pares + texto_normal[indice]
        else:
            car_impares = car_impares + texto_normal[indice]
    texto_encriptado = car_impares + car_pares
    return texto_encriptado

def encripta(texto_normal):
    """Encriptação por separação dos caracteres nas posições pares
    e nas posições ímpares."""
    comp = len(texto_normal)
    # pares
    car_pares = texto_normal[0:comp:2]
    # impares
    car_impares = texto_normal[1:comp:2]
    # junta
    texto_encriptado = car_impares + car_pares
    return texto_encriptado

def desencripta(texto_encriptado):
    """ Descodifica um texto codificado por transposição."""
    # Onde está o meio?
    meio = len(texto_encriptado) // 2
    # ímpares
    car_impares = texto_encriptado[:meio] 
    # pares
    car_pares = texto_encriptado[meio:] 
    # alterna pares e ímpares
    texto_normal = ""
    for i in range(meio):             
        texto_normal = texto_normal + car_pares[i] + car_impares[i]
    # mais pares do que ímpares?
    if len(texto_encriptado) % 2 != 0: 
        texto_normal = texto_normal + car_pares[-1]
    return texto_normal

def codifica_2(texto_normal,chave):
    """Codifica um texto pelo método de substituição. A chave é a distância
    para codificar. Exemplo: 'a' passa a 'c' se chave for 2. Supõe que
    os caracteres são as 26 letras (minúsculas) do alfabeto """
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    texto_encriptado = ''
    for car in texto_normal:
        novo_codigo = (alfabeto.index(car) + chave) % len(alfabeto)
        novo_car = alfabeto[novo_codigo]
        texto_encriptado = texto_encriptado + novo_car
    return texto_encriptado

def codifica(texto_normal,chave):
    """Codifica um texto pelo método de substituição. A chave é 
    dada por uma correspondência um a um entre caracteres. Supõe que
    os caracteres são as 26 letras (minúsculas) do alfabeto mais o espaço em branco"""   
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    texto_encriptado = ''
    for car in texto_normal:
        indice = alfabeto.find(car) 
        texto_encriptado = texto_encriptado + chave[indice]
    return texto_encriptado

def descodifica_1(texto_encriptado,chave):
    """Descodifica um texto pelo método de substituição. A chave é 
    dada por uma correspondência um a um entre caracteres. Supõe que
    os caracteres são as 26 letras (minúsculas) do alfabeto mais o espaço em branco"""   
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    texto_normal = ''
    for car in texto_encriptado:
        indice = chave.find(car) 
        texto_normal = texto_normal + alfabeto[indice]
    return texto_normal


# Tuplos

def dist(x_1,y_1, x_2,y_2):
    """Cálculo da distância euclidiana entre os pontos 1 e 2."""
    return math.sqrt((x_2 - x_1)** 2 + (y_2 - y_1)** 2)

def distancia(ponto_1, ponto_2):
    """Cálculo da distância euclidiana entre os pontos 1 e 2."""
    return math.sqrt((ponto_2[0] - ponto_1[0])** 2 + (ponto_2[1] - ponto_1[1])** 2)
    
if __name__ == '__main__':
    #texto = 'Ernesto Jorge Fernandes Costa'
    #print(encripta(texto))
    #print(encripta_a(texto))
    #print(desencripta("ret og enne otEnsoJreFradsCsa"))
    #adn = gera_adn(10)
    #print(adn)
    #arn = transcreve(adn)
    #arn = 'CAUGCCGCGCAUGUUCC'
    #print(gene_pos(arn,3))
    #gene_todos(arn)
    #print(complemento(adn))
    """
    print(dist(3,5, 10, 6))
    print(distancia((3,5),(10,6)))
    print(bate_cardiaco(59))
    print(bate_card_max(59))
    print(ganhos(1000,0.05,14))
    """
    elementos = ((1,2),(1,2,3,4,5),(1,2,3,4))
    elementos_2 = (4,8,3,2,1,9,7,5,6)
    print((max_elem_1(elementos,len)))
    print((max_elem_2(elementos,len)))
    print((max_elem_3(elementos,len)))
    print((max_elem_4(elementos,len)))
    print((max_elem_valor_1(elementos,len)))
    print((max_elem_valor_2(elementos,len)))
    
    print((max_elem_1(elementos_2,quadrado)))
    print((max_elem_2(elementos_2,quadrado)))
    print((max_elem_3(elementos_2,quadrado)))
    print((max_elem_4(elementos_2,quadrado)))
    print((max_elem_valor_1(elementos_2,quadrado)))
    print((max_elem_valor_2(elementos_2,quadrado)))    
    
    
    
    
    
    