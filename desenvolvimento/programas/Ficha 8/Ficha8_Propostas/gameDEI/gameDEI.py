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

# Base de dados que descreve a estrutura interna do edificio do DEI
dei = {"fora":[foraDesc, {"leste":"corredor", "sul":"lab", "oeste":"cafe"}], "corredor":[corredorDesc,{"oeste":"fora"}],"cafe":[cafeDesc, {"leste":"fora"}],"lab":[labDesc, {"norte":"fora","leste":"biblioteca"}],"biblioteca":[bibliotecaDesc, {"oeste":"lab"}]}

# os comandos validos
validCommands = ["go","quit","help"]

currentRoom = "fora"

def play():
    """
    Funcao principal do programa. Fica em loop ate encerrar o jogo.
    """
    
    printWelcome();
    
    finished = False
    while finished == False:
        command = getCommand()
        finished = processCommand(command)
        
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
    inputSplit= inputLine.split()
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
        goRoom(command)
        
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
    
def goRoom(command):
    """
    Tenta seguir a direcao estabelicida. Caso exista uma saida entra no ambiente,
    caso contrario imprime uma mensagem de erro.
    """
    
    if command[1] == None:
        print "Para onde ir?"
        return
    
    direction = command[1]
    
    global currentRoom
    nextRoom = getExit(currentRoom, direction)
    
    if nextRoom == None:
        print "Nao existe uma porta!"
    else:
        currentRoom = nextRoom
        print getLongDescription(currentRoom)
    
def getExit(currentRoom, direction): 
    """
    Retorna o ambiente pode ser alcancado a partir da direcao estabelicida. 
    Se nao existe nenhum ambiente retorna None
    """
    
    if direction in dei[currentRoom][1].keys():
        return dei[currentRoom][1][direction]
    else:
        return None

def getLongDescription(currentRoom):
    """
    Retorna a descricao estendida do ambiente
    """
    
    return "Estas " + dei[currentRoom][0] + "\n" + getExitString(currentRoom)

def getExitString(currentRoom):
    """
    Retorna um string que enumera as possiveis saidas de um ambiente
    """
    
    returnString = "Saidas:"
    keys = dei[currentRoom][1].keys()
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
           
if __name__ == '__main__':
    play()
