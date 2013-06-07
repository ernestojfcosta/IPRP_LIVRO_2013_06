#! -*- coding: utf-8 -*-

## Exercícios sobre input e output

def acesso_a():
    """
    Simula a entrada num sistema por nome de utilizador
    e palavra de código.
    """
    codigos = {'ernesto':'toto','ana':'gato','patricia':'gandhi'}
    
    utilizador = raw_input("O seu nome de utilizador: ")
    if codigos.has_key(utilizador):
        codigo = raw_input("O seu código de acesso: ")
        if codigo == codigos[utilizador]:
            print 'Bem Vindo %s!!' % utilizador
        else:
            print 'Código errado'
    else:
        print "Utilizador desconhecido"
 
# n tentativas       
        
def acesso_b():
    """
    Simula a entrada num sistema por nome de utilizador
    e palavra de código. n tentativas.
    """
    codigos = {'ernesto':'toto','ana':'gato','patricia':'gandhi'}
    
    num_tentativas = 3
    
    for tentativa in range(num_tentativas):
        utilizador = raw_input("O seu nome de utilizador: ")
        if codigos.has_key(utilizador):
            codigo = raw_input("O seu código de acesso: ")
            if codigo == codigos[utilizador]:
                print 'Bem Vindo %s!!' % utilizador.capitalize()
                break # Atenção!
            else:
                print 'Código errado'
        else:
            print "Utilizador desconhecido"    
        if tentativa == num_tentativas - 1:
            print "Número de tentativas excedido..."
        else:
            print "Tem mais %d tentativa(s)!" % (num_tentativas - tentativa - 1)



acesso_b()
