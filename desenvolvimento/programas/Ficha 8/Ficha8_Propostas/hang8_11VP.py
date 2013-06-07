import random
def hang8_11():
    # inicializa‹o

    
    jogar = True
    while jogar:
        # --- palavra secreta
        (ficheiro,tentativas)= pedir_dificuldade()
        palavras = open(ficheiro).read().split()
    
        secreta = list(random.choice(palavras))
        dicio = seq_to_dict(secreta)
        # --- par‰metros
        TAMANHO = len(secreta)
        acertou = False
        estado = {'palavra':list('_'* TAMANHO), 'usadas':[],'tentativas':tentativas}

        # Comea o jogo
        while tentativas>0:
            # Estado actual
            mostra_estado(estado)
            # joga
            letra = adivinha(estado)
            # analisa resposta
            if letra in dicio: 
                # --- Acertou na letra!
                indices = dicio[letra]
                pal_utilizador = estado['palavra']
                for ind in indices:
                    pal_utilizador[ind] = letra
                estado['palavra'] = pal_utilizador
                # --- Acertou na palavra??
                if fim(secreta,pal_utilizador):
                    acertou = True
                    mensagem_sim(secreta)
                    break
            else:
                tentativas=tentativas-1
            # Actualiza estado
            actualiza_estado(estado, estado['palavra'],letra,tentativas)
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
        print '*** Letra jà usada. Escolha outra sff!***'
        print
        letra = raw_input('Escolha uma letra: ')
    return letra
    
def limite(tam_palavra):
    """ para mais tarde se poder generalizar..."""
    return tam_palavra

def mostra_estado(estado):
    print '**Estado Actual**:'
    palavra = ' '.join(estado['palavra'])
    erradas = ' '.join(estado['usadas'])
    tentativas = estado['tentativas']
    print 'Palavra: ', palavra
    print ' Letras Usadas: ', erradas
    print ' Tentativas Restantes: ', tentativas
    
    
def actualiza_estado(estado, palavra, letra, tentativas):
    estado['palavra'] = palavra
    estado['usadas'] = estado['usadas'] + [letra]
    estado['tentativas'] = tentativas


    
def mensagem_sim(secreta):
    print
    print 'Uau! Acertou!'
    mostra_palavra(secreta)
    print
    
def mensagem_fim(acertou,secreta):
    if not acertou:
        print 'Oops! Esgotaram-se as suas hip—teses...'
        print 'A palavra secreta era: '
        mostra_palavra(secreta)
        print 

def mostra_palavra(palavra):
    """ mostra uma plavra formada por caracteres guardados numa lista."""
    pal = ' '.join(palavra)
    print 'Palavra:'
    print pal
    print

def fim(secreta, utilizador):
    return secreta == utilizador

def pedir_dificuldade():
    nivel=input('Qual o n’vel de dificuldade (1:F‡cil,2:MŽdio,3:Dificil)?')
    if nivel==1:
        fich='palavras_faceis.txt'
        tentativas=4
    elif nivel ==2:
        fich='palavras_medias.txt'
        tentativas=6
    else:
        fich='palavras_dificeis.txt'
        tentativas=8
    return fich,tentativas


# --- Importante        
def seq_to_dict(palavra):
    """
    Transforma uma palavra num dicionàrio de chave os caracteres e 
    valores a lista dos Õndices.
    """
    dicio = {}
    for indice,letra in enumerate(palavra):
        dicio[letra] = dicio.get(letra,[])+[indice]
    return dicio

if __name__ =='__main__':
    hang8_11()