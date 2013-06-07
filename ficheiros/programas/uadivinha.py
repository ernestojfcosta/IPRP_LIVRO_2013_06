import random

def adivinha_meu_numero():
    """
    O utilizador adivinha o n�mero em que estou a pensar.
    """
    meu_numero = 50
    utilizador = input('Em que n�mero estou a pensar? ')
    if utilizador == meu_numero:
        print 'Uau!! Acertaste!'
    else:
        print 'Erraste... Era o 50. Paci�ncia.'
        
def adivinha_meu_numero_b():
    """
    O utilizador adivinha o n�mero em que estou a pensar.
    """
    meu_numero = random.randint(1,100)
    utilizador = input('Em que n�mero estou a pensar? ')
    if utilizador == meu_numero:
        print 'Uau!! Acertaste!'
    else:
        print 'Erraste... Era o %d. Paci�ncia.' % meu_numero

def adivinha_numero_a():
    """
    Adivinha um n�mero inteiro entre 0 e 100.
    """
    numero = random.randint(0,100)
    
    meu_numero = input("Qual � o seu n�mero [0,100]: ")
    
    if meu_numero == numero:
        print 'Uau!!! Acertou.'
    else:
        print 'Lamento. Errou... O n�mero era: %d' % numero
        
 
        

def adivinha_numero_b():
    """
    Adivinha um n�mero entre 0 e 100. N tentativas.
    """
     
    num_tentativas = 3
    numero = random.randint(1,100)
    
    for tentativa in range(num_tentativas):
        meu_numero = input("Qual � o seu n�mero [0,100]: ")
    
        if meu_numero == numero:
            print 'Uau!!! Acertou na tentativa %d!' % (tentativa + 1)
            break # <-- Aten��o!
        else: 
            print 'Lamento. Errou...'
        if tentativa == num_tentativas - 1:
            print "N�mero de tentativas excedido..."
            print 'O n�mero correcto era %d: ' % numero
        else:
            print "Tem mais %d tentativa(s)!" % (num_tentativas - tentativa - 1)

def adivinha_numero_c():
    """
    Adivinha um n�mero entre 0 e 100. N tentativas.
    """
     
    num_tentativas = 3
    numero = random.randint(1,100)
    
    for tentativa in range(num_tentativas):
        meu_numero = input("Qual � o seu n�mero [0,100]: ")
    
        if meu_numero == numero:
            print 'Uau!!! Acertou na tentativa %d!' % (tentativa + 1)
            break # <-- Aten��o!
        else: 
            print 'Lamento. Errou...'
            if numero < meu_numero:
                print 'O n�mero correcto � menor...'
            else:
                print 'O n�mero correcto � maior ou igual...'
        if tentativa == num_tentativas - 1:
            print "N�mero de tentativas excedido..."
            print 'O n�mero correcto era %d: ' % numero
        else:
            print "Tem mais %d tentativa(s)!" % (num_tentativas - tentativa - 1)
            
def entra_dados_aluno():
    """
    Recolhe dados de um aluno.
    """
    nome = raw_input('O seu nome [primeiro �ltimo]: ')
    data_nascimento = raw_input('A sua data de nascimento [aaaa/mm/dd]: ')
    numero_aluno = raw_input('O seu n�mero de aluno: ')
    ano_curso = raw_input('Qual o seu ano de curso [1-5]: ')
    return nome,data_nascimento,numero_aluno, ano_curso

def bd_alunos(numero_alunos):
    """
    Armazena informa��o sobre alunos.
    """
    base_dados = dict()
    for i in range(numero_alunos):
        nome,data_nasc,numero,ano = entra_dados_aluno()
        base_dados[numero] = [nome, data_nasc,ano]
    return base_dados

        
            
if __name__ == '__main__':
    #adivinha_numero_c()
    #adivinha_meu_numero_b()
    #print entra_dados_aluno()
    print bd_alunos(3)