"""
O Mundo do DEI e' um jogo de aventura muito simples
basead em texto. Os utilizadores podem perambular 
num ambiente, e e' tudo. Este jogo deve ser estendido
para se tornar mais interessante.

Este jogo esta' baseado no "Zuul Game" de M. Kolling e 
D. Barnes.

Autor: R. de Lemos 
Versao: 15 Novembro 2009
"""

# Descricao dos ambientes
foraDesc = "fora do DEI na entrada principal."
corredorDesc = "no corredor."
cafeDesc = "no cafe."
labDesc = "no laboatorio."
bibliotecaDesc = "na biblioteca."
jogoDesc = "na sala de jogos"

# Base de dados que descreve a estrutura interna do edificio do DEI
dei = {"fora":[foraDesc, {"leste":"corredor", "sul":"lab", "oeste":"cafe","sudoeste":"biblioteca"}, None], "corredor":[corredorDesc,{"oeste":"fora"},None],"cafe":[cafeDesc, {"leste":"fora"}, None],"lab":[labDesc, {"norte":"fora","leste":"biblioteca"},None],"biblioteca":[bibliotecaDesc, {"oeste":"lab"}, None], "jogo":[jogoDesc,{"norte":"corredor","sul":"cafe","oeste":"biblioteca"}, None]}

# os comandos validos
validCommands = ["go","get","quit","help"]

# as chaves existentes
keys = ["ouro","prata","bronze"]

currentRoom = "fora"
wallet = []

import time
import random

def play():
    """
    Funcao principal do programa. Fica em loop ate encerrar o jogo.
    """
    
    distributeKeys()
    printWelcome();
    start = time.time()
    
    finished = False
    while finished == False:
        command = getCommand()
        finished = processCommand(command)
    
    stop = time.time()
    totalTime = round((stop-start)/60,2)
    if currentRoom == "fora" and allKeys() and totalTime <= 2:
        print "Ganhou o jogo!"
    print "O jogo durou:", totalTime, "minutos"
    print "Obrigado por ter jogado!"
    
def printWelcome():
    """
    Imprime a mensagem de boas vindas do programa
    """
    
    print
    print "Bem vindos ao Mundo do DEI!"
    print "O Mundo do DEI e' um novo jogo de aventura, terrivelmente chato."
    print "Escreva 'help' caso precise de ajuda."
    print 
    print getLongDescription(currentRoom)
        
def getCommand():
    word1 = None
    word2 = None
    
    inputLine = raw_input("> ")
    inputSplit= inputLine.lower().split()
    if len(inputSplit)==2:
        word1 = inputSplit[0]
        word2 = inputSplit[1]
    elif len(inputSplit)==1:
        word1 = inputSplit[0]
    if word1 in validCommands:
        command = [word1,word2]
        return command
    else:
        command = [None,word2]
        return command
        
def processCommand(command):
    """
    Dado um comando, executa o comando
    """
    
    wantToQuit = False
    
    if command[0] == None:
        print "Eu nao sei o que esta' a dizer..."
        return False
    
    if (command[0] == "help"):
        printHelp()
        
    elif(command[0] == "go"):
        goRoom(command,currentRoom)
    elif(command[0] == "get"):
        getKey(currentRoom)
        
    elif(command[0] == "quit"):
        wantToQuit = quit(command)
    
    return wantToQuit


def printHelp():
    """
    Imprime a lista de comandos disponivel
    """
    
    print "Estas perdido. Estas sozinho. Perambulas pelo desconhecido."
    print
    print "Os teus comandos sao:"
    showAll()
    
def quit(command):
    """
    O comando para sair do programa, entretanto verifica se quer realmente sair
    do programa
    """
    
    if command[1] != None:
        print "Sai de que?" 
        return False
    else:
        return True
    
def goRoom(command,room):
    """
    Tenta seguir a direcao estabelicida. Caso exista uma saida entra no ambiente,
    caso contrario imprime uma mensagem de erro.
    """
    global currentRoom
    if command[1] == None:
        print "Para onde ir?"
        return
    
    direction = command[1]
    
    nextRoom = getExit(room, direction)
    
    if nextRoom == None:
        print "Nao existe uma porta!"
    else:
        currentRoom = nextRoom
        print getLongDescription(currentRoom)
        
def getKey(room):
    """
    Verifica se uma sala tem chave, caso tenha retira a chave
    e da para o jogador.
    """
    if  dei[room][2]== None:
        print "Nao existe chave"
    else:
        wallet.append(dei[room][2])
        dei[room][2]= None
        

def getExit(room, direction): 
    """
    Retorna o ambiente pode ser alcancado a partir da direcao estabelicida. 
    Se nao existe nenhum ambiente retorna None
    """
    
    if direction in dei[room][1].keys():
        return dei[room][1][direction]
    else:
        return None

def getLongDescription(room):
    """
    Retorna a descricao estendida do ambiente
    """
    print "Estas " + dei[room][0] 
    if dei[room][2] != None:
        print "Contem a chave: " + dei[room][2]
    return getExitString(room)
    
def getExitString(room):
    """
    Retorna um string que enumera as possiveis saidas de um ambiente
    """
    
    returnString = "Saidas:"
    keys = dei[room][1].keys()
    for i in range(len(keys)):
        returnString = returnString + " " + keys[i]   
    return returnString

    
def isCommand(aString):
    """
    Verifica se o String fornecido e' um comando valido
    """
    
    for i in range (len(validCommands)):
        if validCommands[i] == aString:
            return True 
    return False

def showAll():
    """
    Imprime todos os comandos validos.
    """
    
    for i in range (len(validCommands)):
        print validCommands[i] + " ",
    print
    
def allKeys():
    """"
    Verifica se o jogador tem tres chaves e se elas sao diferentes
    """
    
    if len(wallet) == 3:
        if (wallet[0] != wallet[1]) and (wallet[0] != wallet[2]) and (wallet[1] != wallet[2]):
            return True
    return False

def distributeKeys():
    """
    Distribui as chaves pelas salas de uma forma aleatoria.
    """
    
    deiKeys = dei.keys()
    for i in range(len(keys)):
        valKey = random.choice(deiKeys)
        while dei[valKey][2]!=None or valKey == "fora":
            valKey = random.choice(deiKeys)
        dei[valKey][2]= keys[i]
                
           
if __name__ == '__main__':
    play()
