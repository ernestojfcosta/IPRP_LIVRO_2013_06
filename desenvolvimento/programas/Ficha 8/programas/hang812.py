# Hangman - 

# hang812.py --> Tentativas?

# o estado tem 4 campos: palavra, letras certas, letras erradas, tentativas restantes


import random


def hang812():

    while True:
            
        # Defini‹o do n’vel
        ficheiro,nivel= escolhe_nivel()
        # --- palavra secreta
        palavras = open(ficheiro).read().split()
        secreta = list(random.choice(palavras))
        dicio = seq_to_dict(secreta)

        # --- par‰metros
        tentativas = define_tentativas(dicio,nivel)
 
        estado = cria_estado(list('_'* len(secreta)),[], [],tentativas, 0)

        # Comea o jogo
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
                estado = set_palavra(estado,pal_utilizador)
                estado = set_certas(estado, get_certas(estado) + [letra])
                # --- Acertou na palavra??
                if fim(secreta,pal_utilizador):
                    estado = set_acertou(estado,1)
                    break
            else:
                estado = set_erradas(estado, get_erradas(estado)+ [letra])
            estado = set_tentativas(estado, get_tentativas(estado) - 1)
            if vai_errar(dicio, estado):
                estado = set_acertou(estado,2)
                break
        # mensagem final
        mensagem_fim(estado,secreta)
    
        """Vamos continuar a jogar?"""
        resposta = raw_input('Continuar a jogar [S/N]?: ')
        if resposta == 'N':
            jogar = False
            print 'Foi um prazer jogar consigo!'
            print 'Bye!'
            break
        

# Auxiliares

def escolhe_nivel():
    
    """ Escolhe o n’vel. Implica›es para as palavras e o nœmero de tentativas."""
    print
    print "N’veis poss’veis: Iniciado, Normal, Perito."
    nivel = raw_input('Que n’vel [I/N/P]? ')
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
    letras = estado['certas'] + estado['erradas']
    while letra in letras:
        print
        print '*** Letra j‡ usada. Escolha outra sff!***'
        print
        letra = raw_input('Escolha uma letra: ')
    return letra
    
def limite(tam_palavra):
    """ para mais tarde se poder generalizar..."""
    return tam_palavra


# ESTADO

#---- Construtor
def cria_estado(palavra,certas,erradas,tentativas, acertou):
    estado={'palavra':palavra,'certas':certas,'erradas':erradas,'tentativas':tentativas, 'acertou': acertou}
    return estado


#--- Acessores

def get_palavra(estado):
    return estado['palavra']

def get_certas(estado):
    return estado['certas']

def get_erradas(estado):
    return estado['erradas']

def get_tentativas(estado):
    return estado['tentativas']

def get_acertou(estado):
    return estado['acertou']

#--- Modificadores
 
def actualiza_estado(estado, palavra, certa,errada,tentativas,acertou):
    estado['palavra'] = palavra
    estado['certas'] = estado['certas'] + [certa]
    estado['erradas'] = estado['erradas'] + [errada]
    estado['tentativas'] = tentativas
    estado['acertou'] = acertou
    return estado

def set_palavra(estado, palavra):
    estado['palavra'] = palavra
    return estado

def set_certas(estado, certas):
    estado['certas'] = certas
    return estado

def set_erradas(estado, erradas):
    estado['erradas'] = erradas
    return estado

def set_tentativas(estado, tentativas):
    estado['tentativas'] = tentativas
    return estado
def set_acertou(estado,acertou):
    estado['acertou'] = acertou
    return estado

#--- Visualiza‹o

def mostra_estado(estado):
    print 'Estado Actual:'
    palavra = ' '.join(estado['palavra'])
    certas = ', '.join(estado['certas'])
    erradas = ', '.join(estado['erradas'])
    tentativas = estado['tentativas']
    print 'Palavra: ', palavra
    print 'Letras certas: ', certas
    print 'Letras erradas: ', erradas
    print 'Tentativas Restantes: ', tentativas
    
def mostra_palavra(palavra):
    """ mostra uma palavra formada por caracteres guardados numa lista."""
    pal = ' '.join(palavra)
    print 'Palavra:'
    print pal
    print
    


def mensagem_fim(estado,secreta):
    acertou = get_acertou(estado)
    if acertou == 0:
        print 'Oops! Esgotaram-se as suas hip—teses...'
    elif acertou == 1:
        print 'Uau! Acertou!'
    else:
        print 'Lamento. J‡ n‹o tem hip—teses de acertar!' 
        
    print 'A palavra secreta era: '
    mostra_palavra(secreta)
        
        
def fim(secreta, utilizador):
    return secreta == utilizador


def vai_errar(dicio,estado):
    """ J‡ n‹o tem hip—teses de acertar."""
    if (len(dicio) - len(get_certas(estado))) > get_tentativas(estado):
        return True
    else:
        return False
    
# --- Importante        
def seq_to_dict(palavra):
    """
    Transforma uma palavra num dicion‡rio de chave os caracteres e 
    valores a lista dos ’ndices.
    """
    dicio = {}
    for indice,letra in enumerate(palavra):
        dicio[letra] = dicio.get(letra,[])+[indice]
    return dicio


    
if __name__ =='__main__':
    hang812()
