# ficha8.py

# 8.1

#--- lst, join, split

# 8.2

def ler_dados_1(n,inf,sup):
    """ lê e guarda n números inteiros no intervalo inf, sup."""
    res = []
    while len(res) < n:
        num = input('Um número inteiro no intervalo [%d,%d]: ' % (inf,sup))
        if num < inf or num > sup:
            print 'ERRO: o número deve estar no intervalo [%d,%d]!!' % (inf,sup)
        else:
            res.append(num)
    return res

# 8.3

def ler_dados_2(n,inf,sup):
    """ lê e guarda n números inteiros no intervalo inf, sup."""
    res = []
    while len(res) < n:
        num = input('Um número inteiro no intervalo [%d,%d]: ' % (inf,sup))
        if num < inf or num > sup:
            print 'ERRO: o número deve estar no intervalo [%d,%d]!!' % (inf,sup)
        elif num in res:
            print 'ERRO: o número %d já existe!!' % num
        else:
            res.append(num)
    return res

#  8.4: Emparelha
import random

def pares(n,homens, mulheres):
    """ Constrói a lista de n pares (mulher,homem)."""
    lista_h = []
    lista_m = []
    for conta in range(n):
        h = random.choice(homens)
        while h in lista_h:
            h = random.choice(homens)
        lista_h.append(h)
        
        m = random.choice(mulheres)
        while m in lista_m:
            m = random.choice(mulheres)
        lista_m.append(m)
    return zip(lista_m,lista_h)

#  8.5: Emparelha - Ficheiros

def pares_f(n,fich_h,fich_m):
    """ nomes um por linha no ficheiro."""
    f_in_1 = open(fich_h,'r')
    homens= f_in_1.readlines()
    f_in_1.close()
    
    f_in_2 = open(fich_m,'r')
    mulheres= f_in_2.readlines()
    f_in_2.close()
    res = pares(n,homens,mulheres)
    return res

        
# 8.6: Frequências

def dic_freq(sequencia):
    """ Constrói um dicionario com os índices das ocorrências."""
    dicio = {}
    for indice, elem in enumerate(sequencia):
        dicio[elem]= dicio.get(elem,[]) + [indice]
    return dicio

# --- para quem não conhece o enumerate

def dic_freq_b(sequencia):
    """ Constrói um dicionario com os índices das ocorrências."""
    dicio = {}
    indice = 0
    for elem in sequencia:
        dicio[elem]= dicio.get(elem,[]) + [indice]
        indice = indice + 1
    return dicio

# 8.7 - Solução básica

import random


def hang87():
    # inicialização
    # --- palavra secreta
    palavras = open('/tempo/data/palavras.txt').read().split()
    secreta = list(random.choice(palavras))
    dicio = seq_to_dict(secreta)
    # --- parâmetros
    TAMANHO = len(secreta)
    LIMITE = limite(TAMANHO)

    pal_utilizador = list('_'* TAMANHO)
    acertou = False
    letras_usadas = []
    
    # Entra no jogo
    for tentativa in range(LIMITE):
        # estado actual
        mostra_palavra(pal_utilizador)
        # joga
        letra = adivinha(letras_usadas)
        # analisa resposta
        if letra in dicio: 
            # --- Acertou na letra!
            indices = dicio[letra]
            for ind in indices:
                pal_utilizador[ind] = letra
            # --- Acertou na palavra??
            if fim(secreta,pal_utilizador):
                acertou = True
                mensagem_sim(secreta)
                break
        # actualiza estado
        letras_usadas.append(letra)
    # mensagem final
    mensagem_fim(acertou,secreta)
    
        

# Auxiliares

def adivinha(letras_usadas):
    """Tenta mais uma letra."""
    letra = raw_input('Escolha uma letra: ')
    # verifica letra - ciclo
    while letra in letras_usadas:
        print
        print '*** Letra já usada. Escolha outra sff!***'
        print
        letra = raw_input('Escolha uma letra: ')
    return letra
    
def limite(tam_palavra):
    """ para mais tarde se poder generalizar..."""
    return tam_palavra

def mensagem_sim(secreta):
    print
    print 'Uau! Acertou!'
    mostra_palavra(secreta)
    print
    
def mensagem_fim(acertou,secreta):
    if not acertou:
        print 'Oops! Esgotaram-se as suas hipóteses...'
        print 'A palavra secreta era: '
        mostra_palavra(secreta)
        print 'See you!'

def mostra_palavra(palavra):
    """ mostra uma plavra formada por caracteres guardados numa lista."""
    pal = ' '.join(palavra)
    print 'Palavra:'
    print pal
    print

def fim(secreta, utilizador):
    return secreta == utilizador


# --- Importante        
def seq_to_dict(palavra):
    """
    Transforma uma palavra num dicionário de chave os caracteres e 
    valores a lista dos índices.
    """
    dicio = {}
    for indice,letra in enumerate(palavra):
        dicio[letra] = dicio.get(letra,[])+[indice]
    return dicio
    
# 8.8: vários jogos

# só se altera o essencial...
import random

def hang88():
    print 'Vamos jogar!'
    jogar = True
    while jogar:
        hang87()
        mais= raw_input('Jogar mais? [S/N]: ')
        if mais == 'N':
            print 'Adeus, até à vista...'
            jogar = False
            
# para os mais puristas...
def hang88b():
    print 'Vamos jogar!'
    jogar = True
    while jogar:
        jogar = continuar(jogar)
            
def continuar(jogar):
    mais == raw_input('mais? [S/N]: ')
    while mais not in ['S','N', 's','n','sim','não']:
        mais == raw_input('A resposta tem que ser [S/N]. A sua  resposta: ')
    if mais in ['N','n','não']:
            print 'Adeus, até à vista...'
            jogar = False
            

# 8.9: Estado

import random

def hang89b():
    print 'Vamos jogar!'
    while True:
        hang89()
        if raw_input('Jogar mais? [S/N]: ') == 'N':
            print 'Adeus, até à vista...'
            break
        
        
def hang89():
    # inicialização
    # --- palavra secreta
    palavras = open('/tempo/data/palavras.txt').read().split()
    secreta = list(random.choice(palavras))
    dicio = seq_to_dict(secreta)
    # --- parâmetros
    TAMANHO = len(secreta)
    LIMITE = limite(TAMANHO)

    estado = {'palavra':list('_'* TAMANHO),'usadas':[],'tentativas':LIMITE}
    acertou = False
    # Entra no jogo
    for tentativa in range(LIMITE):
        # estado actual
        mostra_estado(estado)
        # joga
        letra = adivinha(estado['usadas'])
        # analisa resposta
        if letra in dicio: 
            # --- Acertou na letra!
            indices = dicio[letra]
            for ind in indices:
                estado['palavra'][ind] = letra
            # --- Acertou na palavra??
            if fim(secreta,estado['palavra']):
                acertou = True
                mensagem_sim(secreta)
                break
        # actualiza estado
        estado['usadas'] = estado['usadas'] + [letra]
        estado['tentativas'] = estado['tentativas'] - 1
    # mensagem final
    mensagem_fim(acertou,secreta)
    
        

# Auxiliares

def adivinha(letras_usadas):
    """Tenta mais uma letra."""
    letra = raw_input('Escolha uma letra: ')
    # verifica letra - ciclo
    while letra in letras_usadas:
        print
        print '*** Letra já usada. Escolha outra sff!***'
        print
        letra = raw_input('Escolha uma letra: ')
    return letra
    
def limite(tam_palavra):
    """ para mais tarde se poder generalizar..."""
    return tam_palavra

def mensagem_sim(secreta):
    print
    print 'Uau! Acertou!'
    mostra_palavra(secreta)
    print
    
def mensagem_fim(acertou,secreta):
    if not acertou:
        print 'Oops! Esgotaram-se as suas hipóteses...'
        print 'A palavra secreta era: '
        mostra_palavra(secreta)
        print 'See you!'

  
def mostra_estado(estado):
    # mostra palavra
    print 'Palavra Actual: ',' '.join(estado['palavra'])
    print
    # mostra Letras usadas
    print 'Letras já usadas: ',', '.join(estado['usadas'])
    print
    # mostra tentativas restantes
    print 'Ainda tem as tentativas: ', estado['tentativas']
    print
    
def fim(secreta, utilizador):
    return secreta == utilizador


# --- Importante        
def seq_to_dict(palavra):
    """
    Transforma uma palavra num dicionário de chave os caracteres e 
    valores a lista dos índices.
    """
    dicio = {}
    for indice,letra in enumerate(palavra):
        dicio[letra] = dicio.get(letra,[])+[indice]
    return dicio

# 812: Nível

def hang12():

    while True:
            
        # Definição do nível
        ficheiro,nivel= escolhe_nivel()
        # --- palavra secreta
        palavras = open(ficheiro).read().split()
        secreta = list(random.choice(palavras))
        dicio = seq_to_dict(secreta)

        # --- parâmetros
        tentativas = define_tentativas(dicio,nivel)
        acertou = False
        estado = cria_estado(list('_'* len(secreta)), [],tentativas)

        # Começa o jogo
        for tentativa in range(tentativas):
            # Estado actual
            mostra_estado(estado)
            # joga
            letra = adivinha(estado)
            # analisa resposta
            if letra in dicio: 
                # --- Acertou na letra!
                indices = dicio[letra]
                pal_utilizador = get_palavra(estado)
                for ind in indices:
                    pal_utilizador[ind] = letra
                estado= set_palavra(estado,pal_utilizador)
                # --- Acertou na palavra??
                if fim(secreta,pal_utilizador):
                    acertou = True
                    mensagem_sim(secreta)
                    break
            # Actualiza estado
            actualiza_estado(estado, estado['palavra'],letra, get_tentativas(estado) - 1)
        # mensagem final
        mensagem_fim(acertou,secreta)
    
        """Vamos continuar a jogar?"""
        resposta = raw_input('Continuar a jogar [S/N]?: ')
        if resposta == 'N':
            jogar = False
            print 'Foi um prazer jogar consigo!'
            print 'Bye!'
            break
        

# Auxiliares

def escolhe_nivel():
    
    """ Escolhe o nível. Implicações para as palavras e o número de tentativas."""
    print
    print "Níveis possíveis: Iniciado, Normal, Perito."
    nivel = raw_input('Que nível [I/N/P]? ')
    if nivel == 'I':
        return '/tempo/data/pal_iniciado.txt', 'I'
    elif nivel == 'N':
        return '/tempo/data/pal_normal.txt', 'N' 
    else:
        return '/tempo/data/pal_perito.txt', 'P'
    
def define_tentativas(dicio_pal, nivel):
    diferentes = len(dicio_pal)
    comprimento = sum([ len(indices) for indices in dicio_pal.values()])
    
    if nivel == 'I':
        return 6 + comprimento
    elif nivel == 'N':
        return 6 + diferentes
    else:
        return int(6 + 0.8 * diferentes)
    





def adivinha(estado):
    """Tenta mais uma letra."""
    letra = raw_input('Escolha uma letra: ')
    # verifica letra - ciclo
    while letra in estado['usadas']:
        print
        print '*** Letra já usada. Escolha outra sff!***'
        print
        letra = raw_input('Escolha uma letra: ')
    return letra
    
def limite(tam_palavra):
    """ para mais tarde se poder generalizar..."""
    return tam_palavra


# ESTADO

#---- Construtor
def cria_estado(palavra,usadas,tentativas):
    estado={'palavra':palavra,'usadas':usadas,'tentativas':tentativas}
    return estado


#--- Acessores

def get_palavra(estado):
    return estado['palavra']

def get_usadas(estado):
    return estado['usadas']

def get_tentativas(estado):
    return estado['tentativas']

#--- Modificadores

def actualiza_estado(estado, palavra, letra,tentativas):
    estado['palavra'] = palavra
    estado['usadas'] = estado['usadas'] + [letra]
    estado['tentativas'] = tentativas

def set_palavra(estado, palavra):
    estado['palavra'] = palavra
    return estado

def set_erradas(estado, usadas):
    estado['usadas'] = usadas
    return estado

def set_tentativas(estado, tentativas):
    estado['tentativas'] = tentativas
    return estado

#--- Visualização

def mostra_estado(estado):
    print 'Estado Actual:'
    palavra = ' '.join(estado['palavra'])
    usadas = ', '.join(estado['usadas'])
    tentativas = estado['tentativas']
    print 'Palavra: ', palavra
    print 'Letras Usadas: ', usadas
    print 'Tentativas Restantes: ', tentativas
    
def mostra_palavra(palavra):
    """ mostra uma plavra formada por caracteres guardados numa lista."""
    pal = ' '.join(palavra)
    print 'Palavra:'
    print pal
    print
    
def mensagem_sim(secreta):
    print
    print 'Uau! Acertou!'
    mostra_palavra(secreta)
    print
    
def mensagem_fim(acertou,secreta):
    if not acertou:
        print 'Oops! Esgotaram-se as suas hipóteses...'
        print 'A palavra secreta era: '
        mostra_palavra(secreta)
        print 


def fim(secreta, utilizador):
    return secreta == utilizador


# --- Importante        
def seq_to_dict(palavra):
    """
    Transforma uma palavra num dicionário de chave os caracteres e 
    valores a lista dos índices.
    """
    dicio = {}
    for indice,letra in enumerate(palavra):
        dicio[letra] = dicio.get(letra,[])+[indice]
    return dicio


if __name__ =='__main__':
    """
    print ler_dados_2(3,-30,30)
    hom =['ernesto', 'luis', 'carlos', 'pedro','alberto']
    mul =['ana','luisa','joana', 'isabel','daniela', 'carla']
    print pares(5,hom,mul)
    print dic_freq_b('abaabcba')
    """
    hang89b()
    
    
    