# Hangman - 

# hang89.py

import random


def hang89():
    # inicialização
    # --- palavra secreta
    palavras = open('/tempo/data/palavras.txt').read().split()
    
    jogar = True
    while jogar:
        secreta = list(random.choice(palavras))
        dicio = seq_to_dict(secreta)
        # --- parâmetros
        TAMANHO = len(secreta)
        LIMITE = limite(TAMANHO)
        acertou = False
        estado = cria_estado(list('_'* TAMANHO), [],LIMITE)

        # Começa o jogo
        for tentativa in range(LIMITE):
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
    
        jogar=jogar_mais()
        

# Auxiliares

def jogar_mais():
    """Vamos continuar a jogar?"""
    resposta = raw_input('Continuar a jogar [S/N]?: ')
    if resposta == 'N':
        jogar = False
        print 'Foi um prazer jogar consigo!'
        print 'Bye!'
    else:
        jogar = True
    return jogar

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
    hang89()
