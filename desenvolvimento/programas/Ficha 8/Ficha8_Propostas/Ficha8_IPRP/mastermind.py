#Mastermind
#Adivinhe o número e a posição de uma sequência de X elementos escolhidos 
#de um grupo de Y possíveis. X e Y podem variar entre 1 e 9 sendo que Y>=X.
#Comece por pedir o número de elementos diferentes existentes (Y) e depois o 
#número de elementos da sequência (X). De seguida crie uma sequência ordenada
#de X elementos distintos, dos Y permitidos, e dê ao utilizador 10 oportunidades 
#para a adivinhar. Por cada palpite do utilizador terá de lhe dizer quantos números
#ele pôs no sítio correcto, e quantos existem na chave embora não nas posições
#assinaladas.Guarde o histórico das jogadas e resultados para apresentar no ecrâ.
#Veja o exemplo seguinte que mostra um jogo após 3 jogadas:
from random import randint

def mastermind_apresenta_tabuleiro(jogadas,xx):
    """
    Apresenta o tabuleiro do jogo
    jogadas: lista com jogadas realizadas até ao momento (lista de listas)
    xx: quantidade de números a descobrir
    """
    print '*'*20
    print 'Tabuleiro'
    print '*'*20
    print '? '*xx
    print '--'*xx
    for jogada in jogadas:
        for nums in range(xx):
            print str(jogada[nums]),
        print ' pos.certa:'+str(jogada[nums+1])+' pos.errada:'+str(jogada[nums+2])
    print ''

    
def mastermind_gera_chave(xx,yy):
    """
    Gera chave automaticamente
    xx: quantidade de números a descobrir
    yy: quantidade de valores possíveis para cada posição
    """
    chave_nova=[]
    for i in range(xx):
        a=randint(1,yy)
        while(a in chave_nova):
            a=randint(1,yy)
        chave_nova.append(a)
    return chave_nova


def mastermind_pede_jogada(tamanho_chave):
    valido=0
    while not valido:
        nova_jogada=list(raw_input('Jogada (separe os n.os por vírgulas) : ').split(','))
        try:
            if len(nova_jogada)!=tamanho_chave:
                print str(tamanho_chave)+' n.os separados por vírgulas' 
            else:
                for ii in range(len(nova_jogada)):
                    nova_jogada[ii]=int(nova_jogada[ii])
                valido=1
        except:
            valido=0
            print 'Erro! Deve introduzir '+str(tamanho_chave)+' n.os separados por vírgulas'
    return nova_jogada


def mastermind():
    """
    Jogo do Mastermind
    """
    print '\n*** JOGO DO MASTERMIND ***\n'
    jogar=1
    while jogar==1:
        chave=[]
        jogadas=[]
        #cada jogada é guardada como uma lista de x elementos + elementos na posição certa+ elementos existentes na posição errada
        x=y=0      # x vai ter o n.o de elementos a descobrir, y vai ter o número de elementos diferentes de onde escolher
        valido=0
        while not valido:
            try:
                x=input('Quantidade de números a descobrir : ')
                y=input('Quantidade de números possíveis para cada posição: ')
                if x<1 or x>9 or y<1 or y>9 or x>y:
                    valido=0
                    print 'Erro! Deve introduzir n.o elementos entre 1 e 9 e elem.possiveis>=elem.na seq.'
                else:
                    valido=1
            except:
                print 'Erro! Deve introduzir n.o elementos entre 1 e 9 e elem.possiveis>=elem.na seq.'
                valido=0
                
        #gerar chave
        chave=mastermind_gera_chave(x,y)
        
        #Jogo
        for i in range(10): # no máximo 10 tentativas
            #apresentar tabuleiro
            mastermind_apresenta_tabuleiro(jogadas,x)

            if i!=0 and jogadas[len(jogadas)-1][x]==x: # verificar se acertou e se não estamos no inicio
                break #acertou
            
            #pedir jogada
            nova_jogada=mastermind_pede_jogada(x)
            
            #avaliar jogada
            pos_certa=0  #conta números que existem na chave e que estão na posição certa
            pos_errada=0 #conta números que existem na chave mas que estão na posição errada
            
            for n in range(x):
                if nova_jogada[n]==chave[n]:
                    pos_certa=pos_certa+1
                else:
                    if nova_jogada[n] in chave:
                        pos_errada=pos_errada+1
            nova_jogada.append(pos_certa)
            nova_jogada.append(pos_errada)           
            jogadas.append(nova_jogada)
            
        if jogadas[len(jogadas)-1][x]==x:
            print '!!! *** ACERTOU *** !!!'
        else:
            print '!!! *** EXCEDEU O N.O DE TENTATIVAS *** !!!'
        # Jogar outra vez?
        resposta=raw_input('Quer jogar outra vez (S/N)? ')
        if resposta.upper()!='S':
            jogar=0
            print 'Bye bye'
        
if __name__ == '__main__':
    mastermind()
            
                
        
        