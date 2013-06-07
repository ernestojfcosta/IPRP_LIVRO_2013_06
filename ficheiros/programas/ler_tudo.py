def le_todas_temperaturas(fich):
    """
    Extrai os dados de temperaturas relativos a Portugal.
    """
    with open(fich,'r')  as f_ent:
        portugal = list()
        dados = le_uma_temperatura(f_ent)
        while dados != -1:
            portugal.append(dados)
            dados = le_uma_temperatura(f_ent)
    f_ent.close()
    return portugal

def le_uma_temperatura(f_ent):
    """
    Ler dados da temperatura de uma cidade.
    Devolve -1 se  fim de ficheiro
    """
    linha = f_ent.readline()
    while (linha !='') and (linha == '\n'):
        linha = f_ent.readline()
    if linha == '':
        return -1
    else:
        linha = linha[:-1].split()
        return [float(dado) for dado in linha]
    
if __name__ == '__main__':
    dados = ler_todas_temperaturas('/data/temperaturas.txt')  
    print(dados)