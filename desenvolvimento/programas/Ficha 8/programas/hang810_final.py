import random


def hang810a(fich_dados):
    # Mensagem inicial
    print 'Bem Vindo ao Jogo do Enforcado!!!'
    print 'Vamos jogar!'
    # recupera informação estatística
    f_in = open(fich_dados,'r')
    dicio_jogadores = fich_to_dict(f_in)
    f_in.close()
    # identificação do jogador
    nome = raw_input('O seu nome por favor: ')
    if nome in dicio_jogadores:
        print 'Olá de novo!'
        print 'O seu desempenho actual é:'
        print 'Jogos efectuados: %d \nVitórias: %d' % (dicio_jogadores[nome][0], dicio_jogadores[nome][1])
    else:
        print 'Bem Vindo!'
        dicio_jogadores[nome]=[0,0]
        
    # jogar
    jogar = True
    while jogar:
        hang810(nome,dicio_jogadores)
        jogar = continuar(jogar,dicio_jogadores, fich_dados)
        
            
def continuar(jogar,dicio_jogadores,fich_dados):
    # Jogar mais??
    mais = raw_input('mais? [S/N]: ')
    while mais not in ['S','N', 's','n','sim','não']:
        mais = raw_input('A resposta tem que ser [S/N]. A sua  resposta: ')
    if mais in ['N','n','não']:
        # Actualiza estatística
        dict_to_fich(dicio_jogadores,fich_dados)
        print 'Adeus, até à vista...'
        jogar = False
    return jogar        
            
def hang810(nome,dicio_jogadores):

    # --- palavra secreta
    palavras = open('/tempo/data/palavras.txt','r').read().split()
    secreta = list(random.choice(palavras))
    dicio = seq_to_dict(secreta)

    # --- parâmetros
    tentativas = len(secreta)
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
        estado = actualiza_estado(estado, estado['palavra'],letra, get_tentativas(estado) - 1)
    # actualiza estatística
    dicio_jogadores[nome][0] = dicio_jogadores[nome][0] + 1
    if acertou:
        dicio_jogadores[nome][1] = dicio_jogadores[nome][1] + 1
    # mensagem final
    mensagem_fim(acertou,secreta)

    
    
# Auxiliares
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

def fich_to_dict(ficheiro):
    """Transforma os dados de um ficheiro para um dicionário."""
    linhas = ficheiro.readlines()
    dicio = {}
    for linha in linhas:
        nome,jogos,vitorias = linha.split()
        dicio.update({nome:[int(jogos),int(vitorias)]})
    return dicio

def dict_to_fich(dicio, ficheiro):
    """Transforma os dados de um dicionário para um ficheiro."""
    f_out= open(ficheiro,'w')
    for chave,valor in dicio.items():
        linha = chave + '\t\t' + str(dicio[chave][0]) + '\t' + str(dicio[chave][1]) + '\n'
        f_out.write(linha)
    f_out.close()
    return dicio 

if __name__ =='__main__':
    hang810a('/tempo/data/enforcado_jogadores.txt')
