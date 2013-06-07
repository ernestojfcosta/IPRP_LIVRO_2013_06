def nota(exame):
    '''Calcula a nota de um exame num teste de escolha múltipla. '''
    solucao = 'ABBEADDB'
    conta = 0
    for i in range(len(solucao)):
        if exame[i] == solucao[i]:
            conta = conta + 1
    return float(conta)/len(solucao)