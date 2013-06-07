# Hangman - Versão inicial

# hang0.py
import random


def hang88():
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
    
        pal_utilizador = list('_'* TAMANHO)
        acertou = False
        letras_usadas = []
 
        # Começa o jogo
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
        print 

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


    
if __name__ =='__main__':
    hang88()
