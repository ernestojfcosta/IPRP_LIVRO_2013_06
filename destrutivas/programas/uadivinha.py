import random

def adivinha_meu_numero():
    """
    O utilizador adivinha o número em que estou a pensar.
    """
    meu_numero = 50
    utilizador = input('Em que número estou a pensar? ')
    if utilizador == meu_numero:
        print 'Uau!! Acertaste!'
    else:
        print 'Erraste... Era o 50. Paciência.'
        
def adivinha_meu_numero_b():
    """
    O utilizador adivinha o número em que estou a pensar.
    """
    meu_numero = random.randint(1,100)
    utilizador = input('Em que número estou a pensar? ')
    if utilizador == meu_numero:
        print 'Uau!! Acertaste!'
    else:
        print 'Erraste... Era o %d. Paciência.' % meu_numero

def adivinha_numero_a():
    """
    Adivinha um número inteiro entre 0 e 100.
    """
    numero = random.randint(0,100)
    
    meu_numero = input("Qual é o seu número [0,100]: ")
    
    if meu_numero == numero:
        print 'Uau!!! Acertou.'
    else:
        print 'Lamento. Errou... O número era: %d' % numero
        
 
        

def adivinha_numero_b():
    """
    Adivinha um número entre 0 e 100. N tentativas.
    """
     
    num_tentativas = 3
    numero = random.randint(1,100)
    
    for tentativa in range(num_tentativas):
        meu_numero = input("Qual é o seu número [0,100]: ")
    
        if meu_numero == numero:
            print 'Uau!!! Acertou na tentativa %d!' % (tentativa + 1)
            break # <-- Atenção!
        else: 
            print 'Lamento. Errou...'
        if tentativa == num_tentativas - 1:
            print "Número de tentativas excedido..."
            print 'O número correcto era %d: ' % numero
        else:
            print "Tem mais %d tentativa(s)!" % (num_tentativas - tentativa - 1)

def adivinha_numero_c():
    """
    Adivinha um número entre 0 e 100. N tentativas.
    """
     
    num_tentativas = 3
    numero = random.randint(1,100)
    
    for tentativa in range(num_tentativas):
        meu_numero = input("Qual é o seu número [0,100]: ")
    
        if meu_numero == numero:
            print 'Uau!!! Acertou na tentativa %d!' % (tentativa + 1)
            break # <-- Atenção!
        else: 
            print 'Lamento. Errou...'
            if numero < meu_numero:
                print 'O número correcto é menor...'
            else:
                print 'O número correcto é maior ou igual...'
        if tentativa == num_tentativas - 1:
            print "Número de tentativas excedido..."
            print 'O número correcto era %d: ' % numero
        else:
            print "Tem mais %d tentativa(s)!" % (num_tentativas - tentativa - 1)
            
def entra_dados_aluno():
    """
    Recolhe dados de um aluno.
    """
    nome = raw_input('O seu nome [primeiro último]: ')
    data_nascimento = raw_input('A sua data de nascimento [aaaa/mm/dd]: ')
    numero_aluno = raw_input('O seu número de aluno: ')
    ano_curso = raw_input('Qual o seu ano de curso [1-5]: ')
    return nome,data_nascimento,numero_aluno, ano_curso

def bd_alunos(numero_alunos):
    """
    Armazena informação sobre alunos.
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