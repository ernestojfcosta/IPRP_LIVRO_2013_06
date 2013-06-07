# Solução Básica
# Ernesto Costa - Novembro 2009
# f87.py
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

def hang88d():
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
            
def hang88b():
    print 'Vamos jogar!'
    while True:
        hang87()
        mais= raw_input('Jogar mais? [S/N]: ')
        if mais == 'N':
            print 'Adeus, até à vista...'
            break

        
        
        
def hang88c():
    print 'Vamos jogar!'
    while True:
        hang87()
        if raw_input('Jogar mais? [S/N]: ') == 'N':
            print 'Adeus, até à vista...'
            break
        
        
def hang87():
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

def mostra_palavra(palavra):
    """ mostra uma plavra formada por caracteres guardados numa lista."""
    pal = ' '.join(palavra)
    print 'Palavra:'
    print pal
    print
    
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

if __name__ == '__main__':
    hang88()
    