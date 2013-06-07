# Hangman - 

# hang811.py --> N�VEL

# tr�s n�veis: iniciado, normal, perito
# palavras guardadas em ficheiros distintos

# iniciado: # letras <= 4, tentativas = 6 + comprimento
# normal: < # letras <= 8, tentativas = 6 + # letras diferentes
# perito: # letras > 8, tentativas = 6 + 0.75 * # letras diferentes

import random


def hang811():

    while True:
            
        # Defini��o do n�vel
        ficheiro,nivel= escolhe_nivel()
        # --- palavra secreta
        palavras = open(ficheiro).read().split()
        secreta = list(random.choice(palavras))
        dicio = seq_to_dict(secreta)

        # --- par�metros
        tentativas = define_tentativas(dicio,nivel)
        acertou = False
        estado = cria_estado(list('_'* len(secreta)), [],tentativas)

        # Come�a o jogo
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
            estado = actualiza_estado(estado, estado['palavra'],letra, get_tentativas(estado) - 1)
        # mensagem final
        mensagem_fim(acertou,secreta)
    
        """Vamos continuar a jogar?"""
        resposta = raw_input('Continuar a jogar [S/N]?: ')
        if resposta == 'N':
            print 'Foi um prazer jogar consigo!'
            print 'Bye!'
            break
        

# Auxiliares

def escolhe_nivel():
    
    """ Escolhe o n�vel. Implica��es para as palavras e o n�mero de tentativas."""
    print
    print "N�veis poss�veis: Iniciado, Normal, Perito."
    nivel = raw_input('Que n�vel [I/N/P]? ')
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
        print '*** Letra j� usada. Escolha outra sff!***'
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
    return estado

def set_palavra(estado, palavra):
    estado['palavra'] = palavra
    return estado

def set_erradas(estado, usadas):
    estado['usadas'] = usadas
    return estado

def set_tentativas(estado, tentativas):
    estado['tentativas'] = tentativas
    return estado

#--- Visualiza��o

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
        print 'Oops! Esgotaram-se as suas hip�teses...'
        print 'A palavra secreta era: '
        mostra_palavra(secreta)
        print 


def fim(secreta, utilizador):
    return secreta == utilizador


# --- Importante        
def seq_to_dict(palavra):
    """
    Transforma uma palavra num dicion�rio de chave os caracteres e 
    valores a lista dos �ndices.
    """
    dicio = {}
    for indice,letra in enumerate(palavra):
        dicio[letra] = dicio.get(letra,[])+[indice]
    return dicio


    
if __name__ =='__main__':
    hang811()
